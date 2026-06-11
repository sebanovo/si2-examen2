from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from app.common.constants import (
    DEVICE_PLATFORM_ANDROID,
    DEVICE_PLATFORM_IOS,
    DEVICE_PLATFORM_WEB,
)


class RegisterDeviceTokenRequest(BaseModel):
    device_token: str = Field(min_length=20, max_length=512)
    device_platform: Literal[
        DEVICE_PLATFORM_ANDROID,
        DEVICE_PLATFORM_IOS,
        DEVICE_PLATFORM_WEB,
    ]
    device_label: str | None = Field(default=None, max_length=120)
    app_role: str | None = Field(default=None, max_length=30)


class UserDeviceTokenResponse(BaseModel):
    id: str
    user_id: str
    device_platform: str
    device_label: str | None = None
    app_role: str | None = None
    push_provider_name: str | None = None
    is_active: bool
    last_seen_at: datetime
    created_at: datetime
    updated_at: datetime


class PlatformSendTestPushRequest(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    body: str = Field(min_length=2, max_length=1000)
    data: dict[str, str] = Field(default_factory=dict)
    incident_id: str | None = None


class NotificationDispatchSummaryResponse(BaseModel):
    event_code: str
    incident_id: str | None = None
    target_user_id: str
    active_device_tokens_count: int
    enqueued_jobs_count: int


class NotificationRecipientUserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str


class NotificationDeliveryResponse(BaseModel):
    id: str
    background_job_id: str | None = None
    incident_id: str | None = None
    recipient_user_id: str | None = None
    user_device_token_id: str | None = None
    provider_name: str | None = None
    event_code: str
    title: str
    body: str
    data_json: dict | None = None
    status: str
    provider_message_id: str | None = None
    error_message: str | None = None
    sent_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
    recipient_user: NotificationRecipientUserResponse | None = None
