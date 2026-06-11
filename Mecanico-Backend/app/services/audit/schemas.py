from datetime import datetime

from pydantic import BaseModel


class AuditActorUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class AuditLogResponse(BaseModel):
    id: str
    actor_user_id: str | None = None
    incident_id: str | None = None
    provider_id: str | None = None
    request_id: str | None = None
    event_scope: str
    event_type: str
    entity_type: str | None = None
    entity_id: str | None = None
    http_method: str | None = None
    route_path: str | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    status_code: int | None = None
    outcome: str
    payload_json: dict | None = None
    created_at: datetime
    actor_user: AuditActorUserResponse | None = None


class MetricSnapshotCapturedByUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class MetricSnapshotResponse(BaseModel):
    id: str
    captured_by_user_id: str | None = None
    snapshot_type: str
    payload_json: dict
    created_at: datetime
    captured_by_user: MetricSnapshotCapturedByUserResponse | None = None
