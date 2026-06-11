from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from app.common.constants import (
    AUDIT_EVENT_PAYMENT_MARKED_PAID,
    PAYMENT_STATUS_CANCELLED,
    PAYMENT_STATUS_PAID,
    PAYMENT_STATUS_PENDING_PAYMENT,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.integrations.payments.factory import get_payment_provider
from app.integrations.payments.base import PaymentCheckoutRequest
from app.services.audit.dispatcher import AuditEventDispatcher
from app.services.auth.models import User
from app.services.billing.models import IncidentBilling
from app.services.billing.repository import BillingRepository
from app.services.billing.schemas import (
    BillingCheckoutPreviewResponse,
    IncidentBillingResponse,
)
from app.services.billing.payment_schemas import (
    ClientCreateCheckoutRequest,
    ClientSimulatePaymentFailureRequest,
    ClientSimulatePaymentSuccessRequest,
)
from app.services.billing.service import BillingService

MONEY_QUANTIZER = Decimal("0.01")


class PaymentSimulationService:
    """
    Servicio de checkout y simulación de pagos.

    Este servicio no reemplaza BillingService.
    Solo agrega una capa formal de proveedor de pago simulado para defensa,
    pruebas con Postman e integración con Angular/Flutter.
    """

    def __init__(self, repository: BillingRepository) -> None:
        self.repository = repository
        self.payment_provider = get_payment_provider()

    def create_client_checkout(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientCreateCheckoutRequest,
    ) -> BillingCheckoutPreviewResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not have billing information yet.")

            payable_amount = self._resolve_payable_amount(billing)

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot create a checkout.")

            if billing.payment_status == PAYMENT_STATUS_PAID:
                raise ConflictException("This incident is already paid.")

            checkout = self.payment_provider.create_checkout(
                PaymentCheckoutRequest(
                    incident_id=incident_id,
                    client_user_id=str(current_user.id),
                    provider_id=str(billing.provider_id) if billing.provider_id is not None else None,
                    amount=payable_amount,
                    currency_code=billing.currency_code,
                    payment_method=payload.payment_method,
                    return_url=self._normalize_optional_text(payload.return_url),
                )
            )

            billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT
            billing.payment_method = payload.payment_method
            billing.payment_provider_name = checkout.provider_name
            billing.checkout_reference = checkout.checkout_reference
            billing.checkout_payload_json = checkout.payload_json
            billing.payment_reference = None
            billing.payment_completed_at = None

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after checkout creation.")

        payable_amount = self._resolve_payable_amount(billing)

        return BillingCheckoutPreviewResponse(
            incident_id=incident_id,
            checkout_reference=billing.checkout_reference or "",
            payment_method=billing.payment_method or payload.payment_method,
            payment_provider_name=billing.payment_provider_name or self.payment_provider.provider_name,
            amount=float(payable_amount),
            currency_code=billing.currency_code,
            payment_status=billing.payment_status,
            checkout_payload_json=billing.checkout_payload_json,
        )

    def simulate_client_payment_success(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientSimulatePaymentSuccessRequest,
    ) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not have billing information yet.")

            payable_amount = self._resolve_payable_amount(billing)

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot be paid.")

            if billing.payment_status == PAYMENT_STATUS_PAID:
                self.repository.commit()
                refreshed = self.repository.get_billing_by_incident_id(incident_id)
                if refreshed is None:
                    raise NotFoundException("Incident billing not found after payment simulation.")
                return self._build_response(refreshed)

            if not billing.checkout_reference:
                raise ConflictException("A checkout must be created before simulating payment success.")

            provider_result = self.payment_provider.simulate_success(
                checkout_reference=billing.checkout_reference,
                amount=payable_amount,
                currency_code=billing.currency_code,
            )

            billing.payment_status = PAYMENT_STATUS_PAID
            billing.payment_provider_name = provider_result.provider_name
            billing.payment_reference = (
                self._normalize_optional_text(payload.payment_reference)
                or provider_result.provider_payment_reference
            )
            billing.payment_completed_at = datetime.now(timezone.utc)
            billing.checkout_payload_json = self._merge_checkout_payload(
                current_payload=billing.checkout_payload_json,
                update_payload={
                    "status": "PAID",
                    "last_payment_attempt": provider_result.payload_json,
                    "payment_message": provider_result.message,
                },
            )

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after payment simulation.")

        self._emit_audit_safely(
            actor_user_id=str(current_user.id),
            incident_id=incident_id,
            provider_id=str(billing.provider_id) if billing.provider_id is not None else None,
            event_type=AUDIT_EVENT_PAYMENT_MARKED_PAID,
            payload_json={
                "payment_status": billing.payment_status,
                "payment_method": billing.payment_method,
                "payment_provider_name": billing.payment_provider_name,
                "payment_reference": billing.payment_reference,
                "checkout_reference": billing.checkout_reference,
                "simulated": True,
            },
        )

        return self._build_response(billing)

    def simulate_client_payment_failure(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientSimulatePaymentFailureRequest,
    ) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not have billing information yet.")

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot simulate payment failure.")

            if billing.payment_status == PAYMENT_STATUS_PAID:
                raise ConflictException("Paid billings cannot simulate payment failure.")

            if not billing.checkout_reference:
                raise ConflictException("A checkout must be created before simulating payment failure.")

            provider_result = self.payment_provider.simulate_failure(
                checkout_reference=billing.checkout_reference,
                failure_reason=payload.failure_reason,
            )

            billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT
            billing.payment_provider_name = provider_result.provider_name
            billing.payment_completed_at = None
            billing.checkout_payload_json = self._merge_checkout_payload(
                current_payload=billing.checkout_payload_json,
                update_payload={
                    "status": "FAILED",
                    "last_payment_attempt": provider_result.payload_json,
                    "payment_message": provider_result.message,
                },
            )

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after payment failure simulation.")

        self._emit_audit_safely(
            actor_user_id=str(current_user.id),
            incident_id=incident_id,
            provider_id=str(billing.provider_id) if billing.provider_id is not None else None,
            event_type="PAYMENT_SIMULATION_FAILED",
            payload_json={
                "payment_status": billing.payment_status,
                "payment_method": billing.payment_method,
                "payment_provider_name": billing.payment_provider_name,
                "checkout_reference": billing.checkout_reference,
                "failure_reason": payload.failure_reason,
                "simulated": True,
            },
        )

        return self._build_response(billing)

    def _resolve_payable_amount(self, billing: IncidentBilling) -> Decimal:
        amount = billing.client_payable_amount

        if amount is None:
            amount = billing.final_price_amount

        if amount is None:
            raise ConflictException("Final pricing has not been defined yet.")

        resolved_amount = Decimal(str(amount)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

        if resolved_amount <= Decimal("0.00"):
            raise ConflictException("The payable amount must be greater than zero.")

        return resolved_amount

    def _merge_checkout_payload(
        self,
        *,
        current_payload: dict[str, Any] | None,
        update_payload: dict[str, Any],
    ) -> dict[str, Any]:
        merged_payload = dict(current_payload or {})
        merged_payload.update(update_payload)
        return merged_payload

    def _build_response(self, billing: IncidentBilling) -> IncidentBillingResponse:
        return BillingService(self.repository)._build_billing_response(billing)

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None

    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type="INCIDENT_BILLING",
                entity_id=incident_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return