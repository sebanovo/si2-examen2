from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.common.constants import (
    PUSH_DELIVERY_STATUS_FAILED,
    PUSH_DELIVERY_STATUS_RUNNING,
    PUSH_DELIVERY_STATUS_SUCCEEDED,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.core.database import SessionLocal
from app.services.notifications.models import PushNotificationDelivery


def build_push_notification_delivery_context(delivery_id: str) -> dict:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery)
            .options(selectinload(PushNotificationDelivery.user_device_token))
            .where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            raise NotFoundException("Push notification delivery not found.")

        device_token = delivery.user_device_token
        if device_token is None:
            raise ConflictException("Push notification delivery does not have a device token.")

        if not device_token.is_active:
            raise ConflictException("The target device token is inactive.")

        return {
            "delivery_id": str(delivery.id),
            "recipient_token": device_token.device_token,
            "title": delivery.title,
            "body": delivery.body,
            "data": delivery.data_json or {},
        }
    finally:
        db.close()


def mark_delivery_running(delivery_id: str) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery).where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_RUNNING
        delivery.error_message = None

        db.add(delivery)
        db.commit()
    finally:
        db.close()


def mark_delivery_succeeded(
    delivery_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery).where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_SUCCEEDED
        delivery.provider_name = provider_name
        delivery.provider_message_id = result_payload.get("provider_message_id")
        delivery.error_message = None
        delivery.sent_at = datetime.now(timezone.utc)

        db.add(delivery)
        db.commit()
    finally:
        db.close()


def mark_delivery_failed(
    delivery_id: str,
    provider_name: str | None,
    error_message: str,
    deactivate_device: bool = False,
) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery)
            .options(selectinload(PushNotificationDelivery.user_device_token))
            .where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_FAILED
        delivery.provider_name = provider_name
        delivery.error_message = error_message
        delivery.sent_at = datetime.now(timezone.utc)

        if deactivate_device and delivery.user_device_token is not None:
            delivery.user_device_token.is_active = False
            delivery.user_device_token.last_seen_at = datetime.now(timezone.utc)
            db.add(delivery.user_device_token)

        db.add(delivery)
        db.commit()
    finally:
        db.close()
