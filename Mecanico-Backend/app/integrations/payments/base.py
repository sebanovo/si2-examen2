from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Protocol


@dataclass(frozen=True)
class PaymentCheckoutRequest:
    incident_id: str
    client_user_id: str
    provider_id: str | None
    amount: Decimal
    currency_code: str
    payment_method: str
    return_url: str | None = None


@dataclass(frozen=True)
class PaymentCheckoutResult:
    checkout_reference: str
    provider_name: str
    provider_transaction_id: str
    payment_status: str
    amount: Decimal
    currency_code: str
    payment_method: str
    payment_url: str | None
    qr_payload: str | None
    expires_at_iso: str
    payload_json: dict[str, Any]


@dataclass(frozen=True)
class PaymentSimulationResult:
    checkout_reference: str
    provider_name: str
    provider_transaction_id: str
    provider_payment_reference: str
    payment_status: str
    message: str
    payload_json: dict[str, Any]


class PaymentProvider(Protocol):
    provider_name: str

    def create_checkout(self, request: PaymentCheckoutRequest) -> PaymentCheckoutResult:
        raise NotImplementedError

    def simulate_success(
        self,
        *,
        checkout_reference: str,
        amount: Decimal,
        currency_code: str,
    ) -> PaymentSimulationResult:
        raise NotImplementedError

    def simulate_failure(
        self,
        *,
        checkout_reference: str,
        failure_reason: str,
    ) -> PaymentSimulationResult:
        raise NotImplementedError