from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ProviderEstimateIncidentPricingRequest(BaseModel):
    estimated_price_min: float | None = Field(default=None, ge=0)
    estimated_price_max: float | None = Field(default=None, ge=0)
    note: str | None = Field(default=None, max_length=1000)


class ProviderFinalizeIncidentPricingRequest(BaseModel):
    final_price_amount: float = Field(gt=0)
    payment_method: Literal["CASH", "QR", "GATEWAY", "TRANSFER", "CARD"] | None = None
    mark_as_paid: bool = False
    payment_reference: str | None = Field(default=None, max_length=255)
    note: str | None = Field(default=None, max_length=1000)


class ClientCheckoutPreviewRequest(BaseModel):
    payment_method: Literal["QR", "GATEWAY", "TRANSFER", "CARD"]
    payment_provider_name: str | None = Field(default="mock_checkout", max_length=50)
    return_url: str | None = Field(default=None, max_length=500)


class ClientMarkIncidentPaidRequest(BaseModel):
    payment_method: Literal["QR", "GATEWAY", "TRANSFER", "CARD", "CASH"]
    payment_provider_name: str | None = Field(default="manual", max_length=50)
    payment_reference: str | None = Field(default=None, max_length=255)


class BillingUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class BillingProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    owner_user: BillingUserSummaryResponse | None = None


class IncidentBillingResponse(BaseModel):
    id: str
    incident_id: str
    client_user_id: str | None = None
    provider_id: str | None = None

    currency_code: str

    estimated_price_min: float | None = None
    estimated_price_max: float | None = None
    final_price_amount: float | None = None

    platform_commission_rate: float
    platform_commission_amount: float | None = None
    provider_gross_amount: float | None = None
    provider_net_amount: float | None = None

    client_plan_subscription_id: str | None = None
    plan_coverage_id: str | None = None
    coverage_applied_amount: float | None = None
    client_payable_amount: float | None = None

    payment_status: str
    payment_method: str | None = None
    payment_provider_name: str | None = None
    payment_reference: str | None = None

    checkout_reference: str | None = None
    checkout_payload_json: dict | None = None

    pricing_note: str | None = None
    pricing_finalized_at: datetime | None = None
    payment_completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    created_at: datetime
    updated_at: datetime

    provider: BillingProviderSummaryResponse | None = None
    client_user: BillingUserSummaryResponse | None = None


class BillingCheckoutPreviewResponse(BaseModel):
    incident_id: str
    checkout_reference: str
    payment_method: str
    payment_provider_name: str
    amount: float
    currency_code: str
    payment_status: str
    checkout_payload_json: dict | None = None
