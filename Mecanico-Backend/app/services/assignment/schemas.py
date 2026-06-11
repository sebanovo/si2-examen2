from datetime import datetime

from pydantic import BaseModel


class AssignmentCandidateMatchedServiceResponse(BaseModel):
    code: str
    category: str
    title: str


class AssignmentCandidateProviderOwnerResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class AssignmentCandidateProviderResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    city: str | None = None
    contact_phone: str | None = None
    average_rating: float
    available_capacity: int
    available_technicians_count: int
    base_latitude: float | None = None
    base_longitude: float | None = None
    owner_user: AssignmentCandidateProviderOwnerResponse
    matched_services: list[AssignmentCandidateMatchedServiceResponse]


class AssignmentCandidateIncidentResponse(BaseModel):
    id: str
    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = None
    ai_summary_status: str
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool


class AssignmentCandidateResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str
    status: str
    recommendation_rank: int
    score: float
    distance_km: float | None = None
    required_service_codes: list[str]
    matched_service_codes: list[str]
    rationale: dict | None = None
    provider_average_rating_snapshot: float
    provider_available_capacity_snapshot: int
    available_technicians_count_snapshot: int
    published_at: datetime
    responded_at: datetime | None = None
    expires_at: datetime | None = None
    provider: AssignmentCandidateProviderResponse
    incident: AssignmentCandidateIncidentResponse


class AssignmentPublishResponse(BaseModel):
    incident_id: str
    incident_status: str
    used_category: str
    used_priority: str
    required_service_codes: list[str]
    published_candidates_count: int
    recommended_candidate_id: str | None = None
    recommended_provider_id: str | None = None


class AssignmentActionResponse(BaseModel):
    candidate_id: str
    candidate_status: str
    incident_id: str
    incident_status: str
    assigned_provider_id: str | None = None
    assigned_at: datetime | None = None
