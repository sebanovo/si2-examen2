from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_TECHNICIAN
from app.common.responses import success_response
from app.core.dependencies import get_db_session, get_routing_provider
from app.core.security import require_roles
from app.integrations.routing.base import RoutingProvider
from app.services.auth.models import User
from app.services.technician_mobile.repository import TechnicianMobileRepository
from app.services.technician_mobile.schemas import (
    TechnicianAvailabilityUpdateRequest,
    TechnicianCompleteIncidentRequest,
    TechnicianLocationPingRequest,
    TechnicianOperationNoteRequest,
)
from app.services.technician_mobile.service import TechnicianMobileService

router = APIRouter(prefix="/technician", tags=["Technician Mobile"])


@router.get("/me")
def get_my_technician_profile(
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.get_my_profile(current_user)

    return success_response(
        message="Technician profile loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/availability")
def update_my_technician_availability(
    payload: TechnicianAvailabilityUpdateRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.update_my_availability(current_user, payload)

    return success_response(
        message="Technician availability updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/incidents")
def list_my_assigned_incidents(
    active_only: bool = Query(default=True),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.list_my_incidents(
        current_user=current_user,
        active_only=active_only,
        limit=limit,
        offset=offset,
    )

    return success_response(
        message="Technician assigned incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "active_only": active_only,
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/me/incidents/{incident_id}")
def get_my_assigned_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.get_my_incident(current_user, incident_id)

    return success_response(
        message="Technician assigned incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/incidents/{incident_id}/en-route")
def mark_my_incident_en_route(
    incident_id: str,
    payload: TechnicianOperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.mark_en_route(current_user, incident_id, payload)

    return success_response(
        message="Incident marked as en route by technician successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/incidents/{incident_id}/location")
def report_my_technician_location(
    incident_id: str,
    payload: TechnicianLocationPingRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.report_my_location(current_user, incident_id, payload)

    return success_response(
        message="Technician location reported successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/incidents/{incident_id}/arrive")
def mark_my_arrival(
    incident_id: str,
    payload: TechnicianOperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.mark_arrived(current_user, incident_id, payload)

    return success_response(
        message="Incident marked as arrived by technician successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/incidents/{incident_id}/start")
def start_my_service(
    incident_id: str,
    payload: TechnicianOperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.start_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service started by technician successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/incidents/{incident_id}/complete")
def complete_my_service(
    incident_id: str,
    payload: TechnicianCompleteIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_TECHNICIAN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TechnicianMobileService(TechnicianMobileRepository(db), routing_provider)
    result = service.complete_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service completed by technician successfully.",
        data=result.model_dump(mode="json"),
    )