from datetime import datetime

from pydantic import BaseModel, Field


class CreateOrUpdateProviderRatingRequest(BaseModel):
    rating_score: int = Field(ge=1, le=5)
    punctuality_score: int | None = Field(default=None, ge=1, le=5)
    service_quality_score: int | None = Field(default=None, ge=1, le=5)
    communication_score: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = Field(default=None, max_length=1000)
    would_recommend: bool | None = None


class ProviderRatingUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str


class ProviderRatingProviderSummaryResponse(BaseModel):
    id: str
    business_name: str
    provider_type: str
    average_rating: float


class ProviderRatingTechnicianSummaryResponse(BaseModel):
    id: str
    full_name: str
    phone_number: str | None


class ProviderRatingIncidentSummaryResponse(BaseModel):
    id: str
    title: str
    status: str
    completed_at: datetime | None


class ProviderRatingResponse(BaseModel):
    id: str
    incident_id: str
    client_user_id: str
    provider_id: str
    technician_id: str | None

    rating_score: int
    punctuality_score: int | None
    service_quality_score: int | None
    communication_score: int | None
    comment: str | None
    would_recommend: bool | None
    provider_average_after_rating: float | None

    created_at: datetime
    updated_at: datetime

    client_user: ProviderRatingUserSummaryResponse | None = None
    provider: ProviderRatingProviderSummaryResponse | None = None
    technician: ProviderRatingTechnicianSummaryResponse | None = None
    incident: ProviderRatingIncidentSummaryResponse | None = None


class ProviderRatingStatsResponse(BaseModel):
    provider_id: str
    provider_name: str
    average_rating: float
    ratings_count: int
    five_star_count: int
    four_star_count: int
    three_star_count: int
    two_star_count: int
    one_star_count: int
    would_recommend_count: int