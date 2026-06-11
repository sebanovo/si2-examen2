from datetime import datetime

from pydantic import BaseModel, Field


class TechnicianAvailabilityUpdateRequest(BaseModel):
    is_available: bool
    current_latitude: float | None = Field(default=None, ge=-90, le=90)
    current_longitude: float | None = Field(default=None, ge=-180, le=180)


class TechnicianLocationPingRequest(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    accuracy_meters: float | None = Field(default=None, ge=0)


class TechnicianOperationNoteRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)


class TechnicianCompleteIncidentRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)
    completion_summary: str | None = Field(default=None, max_length=3000)


class TechnicianUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None


class TechnicianProviderSummaryResponse(BaseModel):
    id: str
    business_name: str
    provider_type: str
    contact_phone: str | None
    average_rating: float


class TechnicianProfileResponse(BaseModel):
    id: str
    user_id: str | None
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None
    specialty: str | None
    is_active: bool
    is_available: bool
    current_latitude: float | None
    current_longitude: float | None
    created_at: datetime
    updated_at: datetime
    user: TechnicianUserSummaryResponse | None = None
    provider: TechnicianProviderSummaryResponse | None = None


class TechnicianClientSummaryResponse(BaseModel):
    id: str
    full_name: str
    phone_number: str | None


class TechnicianVehicleSummaryResponse(BaseModel):
    id: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    color: str | None


class TechnicianIncidentResponse(BaseModel):
    id: str
    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    client_contact_phone_snapshot: str | None
    incident_latitude: float | None
    incident_longitude: float | None
    address_reference: str | None
    requested_at: datetime
    assigned_at: datetime | None
    en_route_at: datetime | None
    arrived_at: datetime | None
    started_at: datetime | None
    completed_at: datetime | None
    cancelled_at: datetime | None
    structured_summary: str | None
    suggested_category: str | None
    suggested_priority: str | None
    route_provider_name: str | None
    route_distance_meters: float | None
    route_duration_seconds: int | None
    route_eta_seconds: int | None
    route_polyline: str | None
    route_last_calculated_at: datetime | None
    client: TechnicianClientSummaryResponse | None = None
    vehicle: TechnicianVehicleSummaryResponse | None = None
    provider: TechnicianProviderSummaryResponse | None = None
    technician: TechnicianProfileResponse | None = None


class TechnicianLocationPingResponse(BaseModel):
    incident_id: str
    technician_id: str
    provider_id: str
    latitude: float
    longitude: float
    accuracy_meters: float | None
    recorded_at: datetime
    route_provider_name: str | None
    route_distance_meters: float | None
    route_duration_seconds: int | None
    route_eta_seconds: int | None
    route_polyline: str | None