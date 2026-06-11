from datetime import datetime

from pydantic import BaseModel, Field


class BackgroundJobRequestedByUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class BackgroundJobResponse(BaseModel):
    id: str
    requested_by_user_id: str | None = None
    job_type: str
    status: str
    provider_name: str | None = None
    queue_name: str
    celery_task_id: str | None = None
    entity_type: str | None = None
    entity_id: str | None = None
    payload_json: dict | None = None
    result_json: dict | None = None
    error_message: str | None = None
    attempts_count: int
    started_at: datetime | None = None
    finished_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
    requested_by_user: BackgroundJobRequestedByUserResponse | None = None


class DemoJobEnqueueRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    countdown_seconds: int = Field(default=0, ge=0, le=30)