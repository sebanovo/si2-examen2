from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class IncidentVehicleSummaryResponse(BaseModel):
    id: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    year: int | None = None
    color: str | None = None


class IncidentProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    contact_phone: str | None = None
    city: str | None = None
    is_available: bool
    average_rating: float


class IncidentTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class IncidentClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentResponse(BaseModel):
    id: str
    client_user_id: str
    vehicle_id: str
    provider_id: str | None = None
    assigned_technician_id: str | None = None
    dispatch_mode: str | None = None

    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    client_contact_phone_snapshot: str | None = None
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = None
    estimated_price_min: float | None = None
    estimated_price_max: float | None = None

    ai_summary_status: str
    summary_provider_name: str | None = None
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool
    summary_processed_at: datetime | None = None
    summary_error_message: str | None = None

    responder_last_latitude: float | None = None
    responder_last_longitude: float | None = None
    responder_last_source_type: str | None = None
    responder_last_recorded_at: datetime | None = None

    route_provider_name: str | None = None
    route_distance_meters: float | None = None
    route_distance_km: float | None = None
    route_duration_seconds: int | None = None
    route_eta_seconds: int | None = None
    route_eta_minutes: int | None = None
    route_polyline: str | None = None
    route_last_calculated_at: datetime | None = None
    route_error_message: str | None = None

    requested_at: datetime
    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    vehicle: IncidentVehicleSummaryResponse
    client_user: IncidentClientSummaryResponse
    provider: IncidentProviderSummaryResponse | None = None
    assigned_technician: IncidentTechnicianSummaryResponse | None = None


class CreateIncidentRequest(BaseModel):
    vehicle_id: str
    reported_category: Literal[
        "BATTERY",
        "TIRE",
        "ACCIDENT",
        "ENGINE",
        "LOCKOUT",
        "OVERHEATING",
        "OTHER",
        "UNCERTAIN",
    ] = "OTHER"
    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = "MEDIUM"
    title: str = Field(min_length=3, max_length=150)
    description: str = Field(min_length=5)
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = Field(default=None, max_length=255)


class UpdateOwnPendingIncidentRequest(BaseModel):
    reported_category: Literal[
        "BATTERY",
        "TIRE",
        "ACCIDENT",
        "ENGINE",
        "LOCKOUT",
        "OVERHEATING",
        "OTHER",
        "UNCERTAIN",
    ] | None = None
    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] | None = None
    title: str | None = Field(default=None, min_length=3, max_length=150)
    description: str | None = Field(default=None, min_length=5)
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = Field(default=None, max_length=255)
