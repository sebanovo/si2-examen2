from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from uuid import uuid4

from app.common.constants import (
    DEFAULT_CURRENCY_CODE,
    DEFAULT_PLATFORM_COMMISSION_RATE,
    INCIDENT_STATUS_CANCELLED,
    PAYMENT_STATUS_CANCELLED,
    PAYMENT_STATUS_ESTIMATED,
    PAYMENT_STATUS_PAID,
    PAYMENT_STATUS_PENDING_PAYMENT,
    PAYMENT_STATUS_PENDING_PRICING,
    AUDIT_EVENT_BILLING_ESTIMATED,
    AUDIT_EVENT_BILLING_FINALIZED,
    AUDIT_EVENT_PAYMENT_MARKED_PAID,

    
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.billing.models import IncidentBilling
from app.services.billing.repository import BillingRepository
from app.services.billing.schemas import (
    BillingCheckoutPreviewResponse,
    BillingProviderSummaryResponse,
    BillingUserSummaryResponse,
    ClientCheckoutPreviewRequest,
    ClientMarkIncidentPaidRequest,
    IncidentBillingResponse,
    ProviderEstimateIncidentPricingRequest,
    ProviderFinalizeIncidentPricingRequest,
)
from app.services.audit.dispatcher import AuditEventDispatcher

MONEY_QUANTIZER = Decimal("0.01")
RATE_QUANTIZER = Decimal("0.0001")


class BillingService:
    def __init__(self, repository: BillingRepository) -> None:
        self.repository = repository

    def get_my_client_incident_billing(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def get_my_provider_incident_billing(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def get_platform_incident_billing(self, incident_id: str) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def upsert_provider_incident_estimate(
        self,
        current_user: User,
        incident_id: str,
        payload: ProviderEstimateIncidentPricingRequest,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if incident.status == INCIDENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled incidents cannot be estimated.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)

            estimated_min, estimated_max = self._resolve_estimate_range(
                provider=provider,
                incident=incident,
                explicit_min=payload.estimated_price_min,
                explicit_max=payload.estimated_price_max,
            )

            incident.estimated_price_min = estimated_min
            incident.estimated_price_max = estimated_max

            billing.client_user_id = incident.client_user_id
            billing.provider_id = incident.provider_id
            billing.estimated_price_min = estimated_min
            billing.estimated_price_max = estimated_max
            billing.pricing_note = self._normalize_optional_text(payload.note)

            if billing.payment_status in (PAYMENT_STATUS_PENDING_PRICING, PAYMENT_STATUS_CANCELLED):
                billing.payment_status = PAYMENT_STATUS_ESTIMATED
                billing.cancelled_at = None

            self.repository.save(incident)
            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after estimate update.")


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_BILLING_ESTIMATED,
        payload_json={
            "estimated_price_min": float(billing.estimated_price_min) if billing.estimated_price_min is not None else None,
            "estimated_price_max": float(billing.estimated_price_max) if billing.estimated_price_max is not None else None,
            "payment_status": billing.payment_status,
        },
    )

        return self._build_billing_response(billing)

    def finalize_provider_incident_pricing(
        self,
        current_user: User,
        incident_id: str,
        payload: ProviderFinalizeIncidentPricingRequest,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        if payload.mark_as_paid and payload.payment_method is None:
            raise ConflictException("payment_method is required when mark_as_paid=true.")

        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if incident.status == INCIDENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled incidents cannot be finalized economically.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("This incident billing is cancelled and cannot be finalized.")

            final_price = self._to_money_decimal(payload.final_price_amount)
            commission_rate = self._to_rate_decimal(DEFAULT_PLATFORM_COMMISSION_RATE)
            commission_amount = (final_price * commission_rate).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)
            provider_gross = final_price
            provider_net = (provider_gross - commission_amount).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

            billing.client_user_id = incident.client_user_id
            billing.provider_id = incident.provider_id
            billing.currency_code = DEFAULT_CURRENCY_CODE

            if incident.estimated_price_min is not None:
                billing.estimated_price_min = incident.estimated_price_min
            if incident.estimated_price_max is not None:
                billing.estimated_price_max = incident.estimated_price_max

            billing.final_price_amount = final_price
            billing.platform_commission_rate = commission_rate
            billing.platform_commission_amount = commission_amount
            billing.provider_gross_amount = provider_gross
            billing.provider_net_amount = provider_net
            billing.client_plan_subscription_id = None
            billing.plan_coverage_id = None
            billing.coverage_applied_amount = None
            billing.client_payable_amount = None
            billing.payment_method = payload.payment_method
            billing.payment_reference = self._normalize_optional_text(payload.payment_reference)
            billing.pricing_note = self._normalize_optional_text(payload.note)
            billing.pricing_finalized_at = datetime.now(timezone.utc)
            billing.cancelled_at = None

            if payload.mark_as_paid:
                billing.payment_status = PAYMENT_STATUS_PAID
                billing.payment_completed_at = datetime.now(timezone.utc)
            else:
                billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT
                billing.payment_completed_at = None

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after pricing finalization.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_BILLING_FINALIZED,
        payload_json={
            "final_price_amount": float(billing.final_price_amount) if billing.final_price_amount is not None else None,
            "platform_commission_amount": float(billing.platform_commission_amount) if billing.platform_commission_amount is not None else None,
            "provider_net_amount": float(billing.provider_net_amount) if billing.provider_net_amount is not None else None,
            "payment_status": billing.payment_status,
        },
    )

        return self._build_billing_response(billing)

    def create_client_checkout_preview(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientCheckoutPreviewRequest,
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

            payable_amount = billing.client_payable_amount or billing.final_price_amount
            if payable_amount is None:
                raise ConflictException("Final pricing has not been defined yet.")

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot create a checkout preview.")

            if billing.payment_status == PAYMENT_STATUS_PAID:
                raise ConflictException("This incident is already paid.")

            checkout_reference = f"CHK-{uuid4().hex[:12].upper()}"
            checkout_payload_json = {
                "checkout_reference": checkout_reference,
                "incident_id": incident_id,
                "client_user_id": str(current_user.id),
                "provider_id": str(billing.provider_id) if billing.provider_id is not None else None,
                "amount": float(payable_amount),
                "currency_code": billing.currency_code,
                "payment_method": payload.payment_method,
                "payment_provider_name": payload.payment_provider_name,
                "return_url": self._normalize_optional_text(payload.return_url),
                "status": "PREVIEW_CREATED",
            }

            billing.payment_method = payload.payment_method
            billing.payment_provider_name = payload.payment_provider_name
            billing.checkout_reference = checkout_reference
            billing.checkout_payload_json = checkout_payload_json

            if billing.payment_status == PAYMENT_STATUS_ESTIMATED:
                billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after checkout preview.")

        payable_amount = billing.client_payable_amount or billing.final_price_amount
        if payable_amount is None:
            raise NotFoundException("Incident billing not found after checkout preview.")

        return BillingCheckoutPreviewResponse(
            incident_id=incident_id,
            checkout_reference=billing.checkout_reference or "",
            payment_method=billing.payment_method or payload.payment_method,
            payment_provider_name=billing.payment_provider_name or (payload.payment_provider_name or "mock_checkout"),
            amount=float(payable_amount),
            currency_code=billing.currency_code,
            payment_status=billing.payment_status,
            checkout_payload_json=billing.checkout_payload_json,
        )

    def mark_client_incident_as_paid(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientMarkIncidentPaidRequest,
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

            if billing.final_price_amount is None:
                raise ConflictException("Final pricing has not been defined yet.")

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot be paid.")

            billing.payment_status = PAYMENT_STATUS_PAID
            billing.payment_method = payload.payment_method
            billing.payment_provider_name = payload.payment_provider_name
            billing.payment_reference = self._normalize_optional_text(payload.payment_reference)
            billing.payment_completed_at = datetime.now(timezone.utc)

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after payment update.")

        return self._build_billing_response(billing)

    def cancel_billing_due_to_incident_cancellation(self, incident_id: str) -> None:
        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                return

            if billing.payment_status == PAYMENT_STATUS_PAID:
                return

            billing.payment_status = PAYMENT_STATUS_CANCELLED
            billing.cancelled_at = datetime.now(timezone.utc)

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

    def _get_or_create_billing_snapshot(self, incident_id: str) -> IncidentBilling:
        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)
                self.repository.save(billing)
                self.repository.commit()
                self.repository.refresh(billing)
                return billing

            self._sync_snapshot_fields_from_incident(billing, incident)
            self.repository.save(billing)
            self.repository.commit()
            self.repository.refresh(billing)
            return billing
        except Exception:
            self.repository.rollback()
            raise

    def _create_empty_billing_for_incident(self, incident) -> IncidentBilling:
        billing = IncidentBilling(
            incident_id=incident.id,
            client_user_id=incident.client_user_id,
            provider_id=incident.provider_id,
            currency_code=DEFAULT_CURRENCY_CODE,
            estimated_price_min=incident.estimated_price_min,
            estimated_price_max=incident.estimated_price_max,
            final_price_amount=None,
            platform_commission_rate=self._to_rate_decimal(DEFAULT_PLATFORM_COMMISSION_RATE),
            platform_commission_amount=None,
            provider_gross_amount=None,
            provider_net_amount=None,
            payment_status=PAYMENT_STATUS_ESTIMATED if (
                incident.estimated_price_min is not None or incident.estimated_price_max is not None
            ) else PAYMENT_STATUS_PENDING_PRICING,
            payment_method=None,
            payment_provider_name=None,
            payment_reference=None,
            checkout_reference=None,
            checkout_payload_json=None,
            pricing_note=None,
            pricing_finalized_at=None,
            payment_completed_at=None,
            cancelled_at=None,
        )
        return billing

    def _sync_snapshot_fields_from_incident(self, billing: IncidentBilling, incident) -> None:
        billing.client_user_id = incident.client_user_id
        billing.provider_id = incident.provider_id
        if billing.final_price_amount is None:
            billing.estimated_price_min = incident.estimated_price_min
            billing.estimated_price_max = incident.estimated_price_max

        if incident.status == INCIDENT_STATUS_CANCELLED and billing.payment_status != PAYMENT_STATUS_PAID:
            billing.payment_status = PAYMENT_STATUS_CANCELLED
            if billing.cancelled_at is None:
                billing.cancelled_at = datetime.now(timezone.utc)

    def _resolve_estimate_range(
        self,
        *,
        provider,
        incident,
        explicit_min: float | None,
        explicit_max: float | None,
    ) -> tuple[Decimal | None, Decimal | None]:
        if explicit_min is not None or explicit_max is not None:
            normalized_min = self._to_money_decimal(explicit_min) if explicit_min is not None else None
            normalized_max = self._to_money_decimal(explicit_max) if explicit_max is not None else None
            return self._normalize_estimate_range(normalized_min, normalized_max)

        used_category = (
            incident.suggested_category.strip().upper()
            if incident.suggested_category
            else incident.reported_category.strip().upper()
        )

        candidate_services = []
        for provider_service in provider.provider_services:
            if not provider_service.is_active:
                continue
            if not provider_service.is_mobile_service_enabled:
                continue
            if not provider_service.is_emergency_service_enabled:
                continue
            catalog_item = provider_service.service_catalog_item
            if catalog_item is None or not catalog_item.is_active:
                continue

            if used_category in ("OTHER", "UNCERTAIN") or catalog_item.category == used_category:
                candidate_services.append(provider_service)

        derived_min_values: list[Decimal] = []
        derived_max_values: list[Decimal] = []

        for item in candidate_services:
            if item.price_estimate_min is not None:
                derived_min_values.append(self._to_money_decimal(item.price_estimate_min))
            if item.price_estimate_max is not None:
                derived_max_values.append(self._to_money_decimal(item.price_estimate_max))

        if not derived_min_values and not derived_max_values:
            raise ConflictException(
                "No estimate values were provided and no provider service estimates could be derived."
            )

        derived_min = min(derived_min_values) if derived_min_values else None
        derived_max = max(derived_max_values) if derived_max_values else None

        return self._normalize_estimate_range(derived_min, derived_max)

    def _normalize_estimate_range(
        self,
        estimated_min: Decimal | None,
        estimated_max: Decimal | None,
    ) -> tuple[Decimal, Decimal]:
        if estimated_min is None and estimated_max is None:
            raise ConflictException("At least one estimate value is required.")

        if estimated_min is None and estimated_max is not None:
            estimated_min = estimated_max

        if estimated_max is None and estimated_min is not None:
            estimated_max = estimated_min

        if estimated_min is None or estimated_max is None:
            raise ConflictException("Invalid estimate range.")

        if estimated_min > estimated_max:
            raise ConflictException("estimated_price_min cannot be greater than estimated_price_max.")

        return estimated_min, estimated_max

    def _build_billing_response(self, billing: IncidentBilling) -> IncidentBillingResponse:
        client_payload = None
        if billing.client_user is not None:
            client = billing.client_user
            client_payload = BillingUserSummaryResponse(
                id=str(client.id),
                email=client.email,
                first_name=client.first_name,
                last_name=client.last_name,
                full_name=client.full_name,
                phone_number=client.phone_number,
            )

        provider_payload = None
        if billing.provider is not None:
            provider = billing.provider
            owner_payload = None
            if provider.owner_user is not None:
                owner = provider.owner_user
                owner_payload = BillingUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = BillingProviderSummaryResponse(
                id=str(provider.id),
                provider_type=provider.provider_type,
                business_name=provider.business_name,
                owner_user=owner_payload,
            )

        return IncidentBillingResponse(
            id=str(billing.id),
            incident_id=str(billing.incident_id),
            client_user_id=str(billing.client_user_id) if billing.client_user_id is not None else None,
            provider_id=str(billing.provider_id) if billing.provider_id is not None else None,
            client_plan_subscription_id=(
                str(billing.client_plan_subscription_id)
                if billing.client_plan_subscription_id is not None
                else None
            ),
            plan_coverage_id=(
                str(billing.plan_coverage_id)
                if billing.plan_coverage_id is not None
                else None
            ),
            currency_code=billing.currency_code,
            estimated_price_min=float(billing.estimated_price_min) if billing.estimated_price_min is not None else None,
            estimated_price_max=float(billing.estimated_price_max) if billing.estimated_price_max is not None else None,
            final_price_amount=float(billing.final_price_amount) if billing.final_price_amount is not None else None,
            platform_commission_rate=float(billing.platform_commission_rate),
            platform_commission_amount=(
                float(billing.platform_commission_amount)
                if billing.platform_commission_amount is not None
                else None
            ),
            provider_gross_amount=(
                float(billing.provider_gross_amount) if billing.provider_gross_amount is not None else None
            ),
            provider_net_amount=(
                float(billing.provider_net_amount) if billing.provider_net_amount is not None else None
            ),
            coverage_applied_amount=(
                float(billing.coverage_applied_amount)
                if billing.coverage_applied_amount is not None
                else None
            ),
            client_payable_amount=(
                float(billing.client_payable_amount)
                if billing.client_payable_amount is not None
                else None
            ),
            payment_status=billing.payment_status,
            payment_method=billing.payment_method,
            payment_provider_name=billing.payment_provider_name,
            payment_reference=billing.payment_reference,
            checkout_reference=billing.checkout_reference,
            checkout_payload_json=billing.checkout_payload_json,
            pricing_note=billing.pricing_note,
            pricing_finalized_at=billing.pricing_finalized_at,
            payment_completed_at=billing.payment_completed_at,
            cancelled_at=billing.cancelled_at,
            created_at=billing.created_at,
            updated_at=billing.updated_at,
            provider=provider_payload,
            client_user=client_payload,
        )

    def _to_money_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _to_rate_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(RATE_QUANTIZER, rounding=ROUND_HALF_UP)

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
