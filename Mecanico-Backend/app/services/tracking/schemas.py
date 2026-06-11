from datetime import datetime

from pydantic import BaseModel, Field


class IncidentTrackingProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    contact_phone: str | None = None
    city: str | None = None
    average_rating: float


class IncidentTrackingTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class IncidentTrackingClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentTrackingRouteResponse(BaseModel):
    provider_name: str | None = None
    distance_meters: float | None = None
    distance_km: float | None = None
    duration_seconds: int | None = None
    eta_seconds: int | None = None
    eta_minutes: int | None = None
    polyline: str | None = None
    last_calculated_at: datetime | None = None
    error_message: str | None = None


class IncidentTrackingResponderPositionResponse(BaseModel):
    latitude: float | None = None
    longitude: float | None = None
    source_type: str | None = None
    recorded_at: datetime | None = None


class IncidentLiveTrackingResponse(BaseModel):
    incident_id: str
    status: str
    priority: str
    title: str
    description: str
    address_reference: str | None = None
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    provider: IncidentTrackingProviderSummaryResponse | None = None
    assigned_technician: IncidentTrackingTechnicianSummaryResponse | None = None
    client_user: IncidentTrackingClientSummaryResponse

    responder_position: IncidentTrackingResponderPositionResponse
    route: IncidentTrackingRouteResponse


class LocationPingRequest(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    accuracy_meters: float | None = Field(default=None, ge=0)
    technician_id: str | None = None


class TrackingHistoryItemResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str | None = None
    technician_id: str | None = None
    source_type: str
    latitude: float
    longitude: float
    accuracy_meters: float | None = None
    recorded_at: datetime
    provider_business_name: str | None = None
    technician_full_name: str | None = None
