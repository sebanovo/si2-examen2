from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.notifications.repository import NotificationsRepository
from app.services.notifications.schemas import (
    PlatformSendTestPushRequest,
    RegisterDeviceTokenRequest,
)
from app.services.notifications.service import NotificationsService

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/me/devices/register")
def register_my_device_token(
    payload: RegisterDeviceTokenRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.register_my_device_token(current_user, payload)

    return success_response(
        message="Device token registered successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/devices")
def list_my_device_tokens(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.list_my_device_tokens(current_user)

    return success_response(
        message="Device tokens loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )

@router.delete("/me/devices/{device_token_id}")
def deactivate_my_device_token(
    device_token_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.deactivate_my_device_token(current_user, device_token_id)

    return success_response(
        message="Device token deactivated successfully.",
        data=result.model_dump(mode="json"),
    )

@router.post("/platform/users/{user_id}/test")
def send_platform_test_push(
    user_id: str,
    payload: PlatformSendTestPushRequest,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.send_platform_test_push(current_user, user_id, payload)

    return success_response(
        message="Platform test push notification enqueued successfully.",
        data=result.model_dump(mode="json"),
    )

@router.get("/platform/incidents/{incident_id}/deliveries")
def list_platform_incident_deliveries(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.list_platform_incident_deliveries(incident_id)

    return success_response(
        message="Incident notification deliveries loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
