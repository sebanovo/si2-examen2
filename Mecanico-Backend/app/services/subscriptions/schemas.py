from datetime import datetime
from pydantic import BaseModel, Field


class ProviderPlanUpsertRequest(BaseModel):
    code: str = Field(min_length=2, max_length=60)
    name: str = Field(min_length=2, max_length=150)
    description: str | None = Field(default=None, max_length=2000)
    billing_period: str
    price_amount: float = Field(gt=0)
    currency_code: str = Field(default="BOB", min_length=3, max_length=10)
    is_active: bool = True
    auto_renews: bool = False


class ProviderPlanCoverageUpsertRequest(BaseModel):
    coverage_id: str | None = None
    service_catalog_item_id: str | None = None
    incident_category: str | None = None
    coverage_type: str
    coverage_value: float = Field(gt=0)
    max_coverage_amount: float | None = Field(default=None, gt=0)
    waiting_period_days: int = Field(default=0, ge=0)
    max_applications_per_subscription: int | None = Field(default=None, ge=1)
    is_active: bool = True


class ClientSubscribeToPlanRequest(BaseModel):
    external_reference: str | None = Field(default=None, max_length=120)
    note: str | None = Field(default=None, max_length=1000)


class SubscriptionUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class SubscriptionProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    owner_user: SubscriptionUserSummaryResponse | None = None


class ProviderPlanCoverageResponse(BaseModel):
    id: str
    plan_id: str
    service_catalog_item_id: str | None = None
    service_catalog_item_code: str | None = None
    service_catalog_item_title: str | None = None
    incident_category: str | None = None
    coverage_type: str
    coverage_value: float
    max_coverage_amount: float | None = None
    waiting_period_days: int
    max_applications_per_subscription: int | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class ProviderPlanResponse(BaseModel):
    id: str
    provider_id: str
    code: str
    name: str
    description: str | None = None
    billing_period: str
    price_amount: float
    currency_code: str
    is_active: bool
    auto_renews: bool
    created_at: datetime
    updated_at: datetime
    provider: SubscriptionProviderSummaryResponse | None = None
    coverages: list[ProviderPlanCoverageResponse]


class ClientPlanSubscriptionResponse(BaseModel):
    id: str
    client_user_id: str
    provider_id: str
    plan_id: str
    status: str
    started_at: datetime
    expires_at: datetime
    cancelled_at: datetime | None = None
    external_reference: str | None = None
    note: str | None = None
    created_at: datetime
    updated_at: datetime
    provider: SubscriptionProviderSummaryResponse | None = None
    plan: ProviderPlanResponse


class IncidentCoveragePreviewResponse(BaseModel):
    incident_id: str
    billing_amount_basis: float
    matched_incident_category: str
    has_applicable_coverage: bool
    client_plan_subscription_id: str | None = None
    plan_id: str | None = None
    plan_name: str | None = None
    plan_coverage_id: str | None = None
    coverage_type: str | None = None
    coverage_value: float | None = None
    coverage_applied_amount: float | None = None
    client_payable_amount: float | None = None
    rationale: dict | None = None


class IncidentSubscriptionApplicationResponse(BaseModel):
    id: str
    incident_id: str
    incident_billing_id: str | None = None
    client_plan_subscription_id: str
    plan_coverage_id: str
    matched_service_catalog_item_id: str | None = None
    matched_incident_category: str | None = None
    coverage_type: str
    coverage_value: float
    original_amount: float
    coverage_applied_amount: float
    client_payable_amount: float
    status: str
    snapshot_json: dict | None = None
    applied_at: datetime
    updated_at: datetime
