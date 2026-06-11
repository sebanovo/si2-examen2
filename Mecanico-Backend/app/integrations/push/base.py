from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class PushNotificationRequest:
    recipient_token: str
    title: str
    body: str
    data: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class PushNotificationResult:
    accepted: bool
    provider_message_id: str | None = None
    raw_response: dict[str, Any] = field(default_factory=dict)


class PushNotificationProvider(Protocol):
    provider_name: str

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        ...