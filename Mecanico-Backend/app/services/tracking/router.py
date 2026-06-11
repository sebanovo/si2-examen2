from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session, get_routing_provider
from app.core.security import require_roles
from app.integrations.routing.base import RoutingProvider
from app.services.auth.models import User
from app.services.tracking.repository import TrackingRepository
from app.services.tracking.schemas import LocationPingRequest
from app.services.tracking.service import TrackingService

router = APIRouter(prefix="/tracking", tags=["Tracking"])


@router.post("/provider/incidents/{incident_id}/location")
def report_my_location(
    incident_id: str,
    payload: LocationPingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.report_my_location(current_user, incident_id, payload)

    return success_response(
        message="Responder location reported successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/refresh-route")
def refresh_my_route(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.refresh_my_route(current_user, incident_id)

    return success_response(
        message="Route refreshed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/live")
def get_provider_live_tracking(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_provider_live_tracking(current_user, incident_id)

    return success_response(
        message="Provider live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/history")
def list_provider_tracking_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_provider_tracking_history(current_user, incident_id)

    return success_response(
        message="Provider tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/client/incidents/{incident_id}/live")
def get_client_live_tracking(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_client_live_tracking(current_user, incident_id)

    return success_response(
        message="Client live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/incidents/{incident_id}/history")
def list_client_tracking_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_client_tracking_history(current_user, incident_id)

    return success_response(
        message="Client tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/platform/incidents/{incident_id}/live")
def get_platform_live_tracking(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_platform_live_tracking(incident_id)

    return success_response(
        message="Platform live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/history")
def list_platform_tracking_history(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_platform_tracking_history(incident_id)

    return success_response(
        message="Platform tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
