from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class RoleResponse(BaseModel):
    id: str
    code: str
    name: str
    description: str | None = None


class AuthenticatedUserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool
    is_superuser: bool
    role_codes: list[str]
    roles: list[RoleResponse]
    created_at: datetime
    updated_at: datetime


class RegisterProviderProfileRequest(BaseModel):
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


class RegisterRequest(BaseModel):
    account_type: Literal["CLIENT", "INDEPENDENT_MECHANIC", "WORKSHOP"] = "CLIENT"
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    provider_profile: RegisterProviderProfileRequest | None = None


class LoginRequest(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in_minutes: int
    user: AuthenticatedUserResponse
