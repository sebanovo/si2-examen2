from datetime import datetime

from pydantic import BaseModel, Field


class OperationTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class OperationClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentOperationStateResponse(BaseModel):
    incident_id: str
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

    ai_summary_status: str
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool

    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    client_user: OperationClientSummaryResponse
    assigned_technician: OperationTechnicianSummaryResponse | None = None


class DispatchIncidentRequest(BaseModel):
    technician_id: str | None = None
    note: str | None = Field(default=None, max_length=1000)


class OperationNoteRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)


class CompleteIncidentRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)
    completion_summary: str | None = Field(default=None, max_length=3000)


class OperationEventActorResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class IncidentOperationEventResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str | None = None
    technician_id: str | None = None
    actor_user_id: str | None = None
    event_type: str
    from_status: str | None = None
    to_status: str | None = None
    note: str | None = None
    payload_json: dict | None = None
    created_at: datetime
    actor_user: OperationEventActorResponse | None = None
    technician: OperationTechnicianSummaryResponse | None = None
