from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.incidents.repository import IncidentsRepository
from app.services.incidents.schemas import CreateIncidentRequest, UpdateOwnPendingIncidentRequest
from app.services.incidents.service import IncidentsService

router = APIRouter(prefix="/incidents", tags=["Incidents"])


@router.post("")
def create_own_incident(
    payload: CreateIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.create_own_incident(current_user, payload)

    return success_response(
        message="Incident created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me")
def list_own_incidents(
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_own_incidents(current_user)

    return success_response(
        message="Own incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/me/{incident_id}")
def get_own_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_own_incident(current_user, incident_id)

    return success_response(
        message="Own incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/{incident_id}")
def update_own_pending_incident(
    incident_id: str,
    payload: UpdateOwnPendingIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.update_own_pending_incident(current_user, incident_id, payload)

    return success_response(
        message="Own incident updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/{incident_id}/cancel")
def cancel_own_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.cancel_own_incident(current_user, incident_id)

    return success_response(
        message="Own incident cancelled successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_all_incidents(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_all_incidents(limit=limit, offset=offset)

    return success_response(
        message="Incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{incident_id}")
def get_incident_by_id_for_platform(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_incident_by_id_for_platform(incident_id)

    return success_response(
        message="Incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/me")
def list_provider_incidents(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_provider_incidents(current_user)

    return success_response(
        message="Provider incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/{incident_id}")
def get_provider_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_provider_incident(current_user, incident_id)

    return success_response(
        message="Provider incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )