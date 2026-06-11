from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.operations.repository import OperationsRepository
from app.services.operations.schemas import (
    CompleteIncidentRequest,
    DispatchIncidentRequest,
    OperationNoteRequest,
)
from app.services.operations.service import OperationsService

router = APIRouter(prefix="/operations", tags=["Operations"])


@router.get("/provider/me/active")
def list_my_active_operations(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_my_active_operations(current_user)

    return success_response(
        message="Active provider operations loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/provider/incidents/{incident_id}/state")
def get_my_operation_state(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.get_my_operation_state(current_user, incident_id)

    return success_response(
        message="Provider operation state loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/dispatch")
def dispatch_my_incident(
    incident_id: str,
    payload: DispatchIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.dispatch_my_incident(current_user, incident_id, payload)

    return success_response(
        message="Incident dispatched successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/arrive")
def mark_my_arrival(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.mark_my_arrival(current_user, incident_id, payload)

    return success_response(
        message="Incident marked as arrived successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/start")
def start_my_service(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.start_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service started successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/complete")
def complete_my_service(
    incident_id: str,
    payload: CompleteIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.complete_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service completed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/cancel")
def cancel_my_service(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.cancel_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service cancelled successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/history")
def list_my_operation_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_my_operation_history(current_user, incident_id)

    return success_response(
        message="Provider operation history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/platform/incidents/{incident_id}/history")
def list_platform_operation_history(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_platform_operation_history(incident_id)

    return success_response(
        message="Platform operation history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
