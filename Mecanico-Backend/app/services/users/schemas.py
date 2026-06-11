from datetime import datetime
from pydantic import BaseModel, Field


class UserRoleItemResponse(BaseModel):
    id: str
    code: str
    name: str
    description: str | None = None


class UserProfileResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool
    is_superuser: bool
    role_codes: list[str]
    roles: list[UserRoleItemResponse]
    created_at: datetime
    updated_at: datetime


class UpdateOwnProfileRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=2, max_length=120)
    last_name: str | None = Field(default=None, min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)