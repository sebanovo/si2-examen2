from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ProviderOwnerResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool


class ProviderConfiguredServiceSummaryResponse(BaseModel):
    id: str
    service_catalog_item_id: str
    code: str
    category: str
    title: str
    price_estimate_min: float | None = None
    price_estimate_max: float | None = None
    estimated_duration_minutes: int | None = None
    is_mobile_service_enabled: bool
    is_emergency_service_enabled: bool
    is_active: bool


class TechnicianResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool
    current_latitude: float | None = None
    current_longitude: float | None = None
    created_at: datetime
    updated_at: datetime


class ProviderResponse(BaseModel):
    id: str
    owner_user_id: str
    provider_type: str
    business_name: str
    legal_name: str | None = None
    description: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None
    city: str | None = None
    address: str | None = None
    base_latitude: float | None = None
    base_longitude: float | None = None
    is_active: bool
    is_available: bool
    max_concurrent_services: int
    current_active_services: int
    available_capacity: int
    average_rating: float
    owner_user: ProviderOwnerResponse
    technicians_count: int
    available_technicians_count: int
    configured_services_count: int
    active_services_count: int
    active_services: list[ProviderConfiguredServiceSummaryResponse]
    created_at: datetime
    updated_at: datetime


class CreateProviderAdminUserRequest(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)


class CreateProviderProfileRequest(BaseModel):
    provider_type: Literal["INDEPENDENT_MECHANIC", "WORKSHOP"]
    business_name: str = Field(min_length=2, max_length=150)
    legal_name: str | None = Field(default=None, max_length=180)
    description: str | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=30)
    city: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=255)
    base_latitude: float | None = None
    base_longitude: float | None = None
    max_concurrent_services: int = Field(default=1, ge=1, le=100)


class ProviderOnboardingRequest(BaseModel):
    admin_user: CreateProviderAdminUserRequest
    provider: CreateProviderProfileRequest


class UpdateOwnProviderRequest(BaseModel):
    business_name: str | None = Field(default=None, min_length=2, max_length=150)
    legal_name: str | None = Field(default=None, max_length=180)
    description: str | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=30)
    city: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=255)
    base_latitude: float | None = None
    base_longitude: float | None = None
    is_available: bool | None = None
    max_concurrent_services: int | None = Field(default=None, ge=1, le=100)


class UpdateProviderOperationsRequest(BaseModel):
    is_active: bool | None = None
    is_available: bool | None = None
    max_concurrent_services: int | None = Field(default=None, ge=1, le=100)
    current_active_services: int | None = Field(default=None, ge=0, le=100)


class CreateTechnicianRequest(BaseModel):
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    specialty: str | None = Field(default=None, max_length=120)
    is_available: bool = True
    current_latitude: float | None = None
    current_longitude: float | None = None


class UpdateTechnicianRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=2, max_length=120)
    last_name: str | None = Field(default=None, min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    specialty: str | None = Field(default=None, max_length=120)
    is_active: bool | None = None
    is_available: bool | None = None
    current_latitude: float | None = None
    current_longitude: float | None = None
