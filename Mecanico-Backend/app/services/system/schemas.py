from datetime import datetime

from pydantic import BaseModel


class HealthPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    status: str
    timestamp: datetime


class ReadinessComponentPayload(BaseModel):
    name: str
    status: str
    detail: str


class ReadinessPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    status: str
    components: list[ReadinessComponentPayload]
    timestamp: datetime


class AppInfoPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    api_prefix: str
    docs_enabled: bool
    docs_url: str | None = None
    ai_provider: str
    storage_provider: str
    speech_to_text_provider: str
    vision_provider: str
    llm_provider: str
    routing_provider: str
    push_provider: str
    trusted_hosts: list[str]
    security_headers_enabled: bool
    https_redirect_enabled: bool
    audit_http_enabled: bool
    timestamp: datetime


class SystemMetricsPayload(BaseModel):
    incidents_by_status: dict[str, int]
    background_jobs_by_status: dict[str, int]
    push_deliveries_by_status: dict[str, int]
    providers: dict
    technicians: dict
    financial: dict
    subscriptions_by_status: dict[str, int]
    average_assignment_seconds: float | None = None
    average_completion_seconds: float | None = None
    audit_events_last_24h: int
    timestamp: datetime
