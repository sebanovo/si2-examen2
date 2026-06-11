from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator


class ServiceCatalogItemResponse(BaseModel):
    id: str
    code: str
    category: str
    title: str
    description: str | None = None
    supports_mobile_service: bool
    supports_emergency_service: bool
    is_active: bool
    sort_order: int
    created_at: datetime
    updated_at: datetime


class CreateServiceCatalogItemRequest(BaseModel):
    code: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=2, max_length=50)
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    supports_mobile_service: bool = True
    supports_emergency_service: bool = True
    is_active: bool = True
    sort_order: int = Field(default=0, ge=0, le=1000)

    @field_validator("code")
    @classmethod
    def normalize_code(cls, value: str) -> str:
        return value.strip().upper().replace(" ", "_")

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str) -> str:
        return value.strip().upper()


class UpdateServiceCatalogItemRequest(BaseModel):
    category: str | None = Field(default=None, min_length=2, max_length=50)
    title: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = None
    supports_mobile_service: bool | None = None
    supports_emergency_service: bool | None = None
    is_active: bool | None = None
    sort_order: int | None = Field(default=None, ge=0, le=1000)

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return value.strip().upper()


class ProviderServiceResponse(BaseModel):
    id: str
    provider_id: str
    service_catalog_item_id: str
    service_code: str
    service_category: str
    catalog_title: str
    catalog_description: str | None = None
    custom_title: str | None = None
    custom_description: str | None = None
    effective_title: str
    effective_description: str | None = None
    price_estimate_min: float | None = None
    price_estimate_max: float | None = None
    estimated_duration_minutes: int | None = None
    supports_mobile_service: bool
    supports_emergency_service: bool
    is_mobile_service_enabled: bool
    is_emergency_service_enabled: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime


class ProviderCatalogAvailabilityResponse(BaseModel):
    catalog_item: ServiceCatalogItemResponse
    provider_service: ProviderServiceResponse | None = None
    is_configured: bool


class UpsertProviderServiceRequest(BaseModel):
    service_catalog_item_id: str
    custom_title: str | None = Field(default=None, max_length=150)
    custom_description: str | None = None
    price_estimate_min: float | None = Field(default=None, ge=0)
    price_estimate_max: float | None = Field(default=None, ge=0)
    estimated_duration_minutes: int | None = Field(default=None, ge=1, le=1440)
    is_mobile_service_enabled: bool = True
    is_emergency_service_enabled: bool = True
    is_active: bool = True

    @model_validator(mode="after")
    def validate_price_range(self):
        if (
            self.price_estimate_min is not None
            and self.price_estimate_max is not None
            and self.price_estimate_max < self.price_estimate_min
        ):
            raise ValueError("price_estimate_max cannot be lower than price_estimate_min.")
        return self


class UpdateProviderServiceRequest(BaseModel):
    custom_title: str | None = Field(default=None, max_length=150)
    custom_description: str | None = None
    price_estimate_min: float | None = Field(default=None, ge=0)
    price_estimate_max: float | None = Field(default=None, ge=0)
    estimated_duration_minutes: int | None = Field(default=None, ge=1, le=1440)
    is_mobile_service_enabled: bool | None = None
    is_emergency_service_enabled: bool | None = None
    is_active: bool | None = None

    @model_validator(mode="after")
    def validate_price_range(self):
        if (
            self.price_estimate_min is not None
            and self.price_estimate_max is not None
            and self.price_estimate_max < self.price_estimate_min
        ):
            raise ValueError("price_estimate_max cannot be lower than price_estimate_min.")
        return self
