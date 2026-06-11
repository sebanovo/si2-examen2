from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class VehicleResponse(BaseModel):
    id: str
    owner_user_id: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    year: int | None = None
    color: str | None = None
    notes: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class CreateVehicleRequest(BaseModel):
    plate_number: str = Field(min_length=3, max_length=20)
    vehicle_type: Literal["CAR", "MOTORCYCLE", "TRUCK", "VAN", "OTHER"]
    brand: str = Field(min_length=2, max_length=80)
    model: str = Field(min_length=1, max_length=80)
    year: int | None = Field(default=None, ge=1950, le=2100)
    color: str | None = Field(default=None, max_length=50)
    notes: str | None = None


class UpdateOwnVehicleRequest(BaseModel):
    vehicle_type: Literal["CAR", "MOTORCYCLE", "TRUCK", "VAN", "OTHER"] | None = None
    brand: str | None = Field(default=None, min_length=2, max_length=80)
    model: str | None = Field(default=None, min_length=1, max_length=80)
    year: int | None = Field(default=None, ge=1950, le=2100)
    color: str | None = Field(default=None, max_length=50)
    notes: str | None = None
    is_active: bool | None = None