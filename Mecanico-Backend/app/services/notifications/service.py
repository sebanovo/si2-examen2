from datetime import datetime, timezone

from app.common.constants import (
    PUSH_EVENT_TEST,
)
from app.common.exceptions import ForbiddenException, NotFoundException
from app.core.config import settings
from app.services.auth.models import User
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.services.notifications.models import PushNotificationDelivery, UserDeviceToken
from app.services.notifications.repository import NotificationsRepository
from app.services.notifications.schemas import (
    NotificationDeliveryResponse,
    NotificationDispatchSummaryResponse,
    NotificationRecipientUserResponse,
    PlatformSendTestPushRequest,
    RegisterDeviceTokenRequest,
    UserDeviceTokenResponse,
)


class NotificationsService:
    def __init__(self, repository: NotificationsRepository) -> None:
        self.repository = repository
        self.dispatcher = PushNotificationDispatcher(repository.db)

    def register_my_device_token(
        self,
        current_user: User,
        payload: RegisterDeviceTokenRequest,
    ) -> UserDeviceTokenResponse:
        existing_token = self.repository.get_user_device_token_by_token(payload.device_token)
        now = datetime.now(timezone.utc)

        if existing_token is None:
            token = UserDeviceToken(
                user_id=current_user.id,
                device_token=payload.device_token,
                device_platform=payload.device_platform,
                device_label=self._normalize_optional_text(payload.device_label),
                app_role=self._normalize_optional_text(payload.app_role),
                push_provider_name=settings.push_provider.lower(),
                is_active=True,
                last_seen_at=now,
            )
        else:
            token = existing_token
            token.user_id = current_user.id
            token.device_platform = payload.device_platform
            token.device_label = self._normalize_optional_text(payload.device_label)
            token.app_role = self._normalize_optional_text(payload.app_role)
            token.push_provider_name = settings.push_provider.lower()
            token.is_active = True
            token.last_seen_at = now

        try:
            self.repository.save(token)
            self.repository.commit()
            self.repository.refresh(token)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_device_token_response(token)

    def list_my_device_tokens(self, current_user: User) -> list[UserDeviceTokenResponse]:
        tokens = self.repository.list_active_user_device_tokens_by_user_id(str(current_user.id))
        return [self._build_device_token_response(item) for item in tokens]

    def deactivate_my_device_token(
        self,
        current_user: User,
        device_token_id: str,
    ) -> UserDeviceTokenResponse:
        token = self.repository.get_user_device_token_by_id(device_token_id)
        if token is None:
            raise NotFoundException("Device token not found.")

        if str(token.user_id) != str(current_user.id):
            raise ForbiddenException("This device token does not belong to the authenticated user.")

        token.is_active = False
        token.last_seen_at = datetime.now(timezone.utc)

        try:
            self.repository.save(token)
            self.repository.commit()
            self.repository.refresh(token)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_device_token_response(token)

    def send_platform_test_push(
        self,
        current_user: User,
        user_id: str,
        payload: PlatformSendTestPushRequest,
    ) -> NotificationDispatchSummaryResponse:
        target_user = self.repository.get_user_by_id(user_id)
        if target_user is None:
            raise NotFoundException("Target user not found.")

        active_tokens = self.repository.list_active_user_device_tokens_by_user_id(user_id)
        created_jobs = self.dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=str(current_user.id),
            incident_id=payload.incident_id,
            event_code=PUSH_EVENT_TEST,
            recipient_user_ids=[user_id],
            title=payload.title.strip(),
            body=payload.body.strip(),
            data=payload.data,
        )

        return NotificationDispatchSummaryResponse(
            event_code=PUSH_EVENT_TEST,
            incident_id=payload.incident_id,
            target_user_id=str(target_user.id),
            active_device_tokens_count=len(active_tokens),
            enqueued_jobs_count=len(created_jobs),
        )

    def list_platform_incident_deliveries(
        self,
        incident_id: str,
    ) -> list[NotificationDeliveryResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        deliveries = self.repository.list_deliveries_by_incident_id(incident_id)
        return [self._build_delivery_response(item) for item in deliveries]

    def _build_device_token_response(self, token: UserDeviceToken) -> UserDeviceTokenResponse:
        return UserDeviceTokenResponse(
            id=str(token.id),
            user_id=str(token.user_id),
            device_platform=token.device_platform,
            device_label=token.device_label,
            app_role=token.app_role,
            push_provider_name=token.push_provider_name,
            is_active=token.is_active,
            last_seen_at=token.last_seen_at,
            created_at=token.created_at,
            updated_at=token.updated_at,
        )

    def _build_delivery_response(
        self,
        delivery: PushNotificationDelivery,
    ) -> NotificationDeliveryResponse:
        recipient_user_payload = None
        if delivery.recipient_user is not None:
            recipient_user = delivery.recipient_user
            recipient_user_payload = NotificationRecipientUserResponse(
                id=str(recipient_user.id),
                email=recipient_user.email,
                first_name=recipient_user.first_name,
                last_name=recipient_user.last_name,
                full_name=recipient_user.full_name,
            )

        return NotificationDeliveryResponse(
            id=str(delivery.id),
            background_job_id=(
                str(delivery.background_job_id) if delivery.background_job_id is not None else None
            ),
            incident_id=str(delivery.incident_id) if delivery.incident_id is not None else None,
            recipient_user_id=(
                str(delivery.recipient_user_id) if delivery.recipient_user_id is not None else None
            ),
            user_device_token_id=(
                str(delivery.user_device_token_id)
                if delivery.user_device_token_id is not None
                else None
            ),
            provider_name=delivery.provider_name,
            event_code=delivery.event_code,
            title=delivery.title,
            body=delivery.body,
            data_json=delivery.data_json,
            status=delivery.status,
            provider_message_id=delivery.provider_message_id,
            error_message=delivery.error_message,
            sent_at=delivery.sent_at,
            created_at=delivery.created_at,
            updated_at=delivery.updated_at,
            recipient_user=recipient_user_payload,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None
