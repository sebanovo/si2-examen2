from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal
from uuid import uuid4

from app.integrations.payments.base import (
    PaymentCheckoutRequest,
    PaymentCheckoutResult,
    PaymentSimulationResult,
)


class MockPaymentProvider:
    """
    Proveedor de pago simulado para defensa, pruebas y desarrollo.

    No procesa dinero real.
    Su objetivo es representar una pasarela reemplazable por Stripe, QR bancario,
    transferencia u otro proveedor real sin cambiar el flujo principal del backend.
    """

    provider_name = "mock_payment"

    def create_checkout(self, request: PaymentCheckoutRequest) -> PaymentCheckoutResult:
        checkout_reference = f"CHK-MOCK-{uuid4().hex[:12].upper()}"
        provider_transaction_id = f"MOCK-TXN-{uuid4().hex[:12].upper()}"
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=30)

        payment_url = self._build_payment_url(checkout_reference)
        qr_payload = self._build_qr_payload(
            checkout_reference=checkout_reference,
            amount=request.amount,
            currency_code=request.currency_code,
            incident_id=request.incident_id,
        )

        payload_json = {
            "provider_name": self.provider_name,
            "provider_transaction_id": provider_transaction_id,
            "checkout_reference": checkout_reference,
            "incident_id": request.incident_id,
            "client_user_id": request.client_user_id,
            "provider_id": request.provider_id,
            "amount": float(request.amount),
            "currency_code": request.currency_code,
            "payment_method": request.payment_method,
            "payment_url": payment_url,
            "qr_payload": qr_payload,
            "expires_at": expires_at.isoformat(),
            "return_url": request.return_url,
            "status": "PENDING",
            "is_demo_payment": True,
            "instructions": (
                "Pago simulado para defensa. No procesa dinero real. "
                "Usa simulate-success o simulate-failure para completar el flujo."
            ),
        }

        return PaymentCheckoutResult(
            checkout_reference=checkout_reference,
            provider_name=self.provider_name,
            provider_transaction_id=provider_transaction_id,
            payment_status="PENDING",
            amount=request.amount,
            currency_code=request.currency_code,
            payment_method=request.payment_method,
            payment_url=payment_url,
            qr_payload=qr_payload,
            expires_at_iso=expires_at.isoformat(),
            payload_json=payload_json,
        )

    def simulate_success(
        self,
        *,
        checkout_reference: str,
        amount: Decimal,
        currency_code: str,
    ) -> PaymentSimulationResult:
        provider_transaction_id = f"MOCK-TXN-{uuid4().hex[:12].upper()}"
        provider_payment_reference = f"MOCK-PAID-{uuid4().hex[:12].upper()}"

        payload_json = {
            "provider_name": self.provider_name,
            "checkout_reference": checkout_reference,
            "provider_transaction_id": provider_transaction_id,
            "provider_payment_reference": provider_payment_reference,
            "amount": float(amount),
            "currency_code": currency_code,
            "status": "PAID",
            "is_demo_payment": True,
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }

        return PaymentSimulationResult(
            checkout_reference=checkout_reference,
            provider_name=self.provider_name,
            provider_transaction_id=provider_transaction_id,
            provider_payment_reference=provider_payment_reference,
            payment_status="PAID",
            message="Mock payment approved successfully.",
            payload_json=payload_json,
        )

    def simulate_failure(
        self,
        *,
        checkout_reference: str,
        failure_reason: str,
    ) -> PaymentSimulationResult:
        provider_transaction_id = f"MOCK-TXN-{uuid4().hex[:12].upper()}"
        provider_payment_reference = f"MOCK-FAILED-{uuid4().hex[:12].upper()}"

        payload_json = {
            "provider_name": self.provider_name,
            "checkout_reference": checkout_reference,
            "provider_transaction_id": provider_transaction_id,
            "provider_payment_reference": provider_payment_reference,
            "status": "FAILED",
            "failure_reason": failure_reason,
            "is_demo_payment": True,
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }

        return PaymentSimulationResult(
            checkout_reference=checkout_reference,
            provider_name=self.provider_name,
            provider_transaction_id=provider_transaction_id,
            provider_payment_reference=provider_payment_reference,
            payment_status="FAILED",
            message="Mock payment failed.",
            payload_json=payload_json,
        )

    def _build_payment_url(self, checkout_reference: str) -> str:
        return f"https://mock-payments.local/checkout/{checkout_reference}"

    def _build_qr_payload(
        self,
        *,
        checkout_reference: str,
        amount: Decimal,
        currency_code: str,
        incident_id: str,
    ) -> str:
        return (
            f"MOCK_PAYMENT|"
            f"checkout={checkout_reference}|"
            f"incident={incident_id}|"
            f"amount={amount}|"
            f"currency={currency_code}"
        )