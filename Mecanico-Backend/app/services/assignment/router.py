from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.assignment.repository import AssignmentRepository
from app.services.assignment.service import AssignmentService
from app.services.auth.models import User

router = APIRouter(prefix="/assignment", tags=["Assignment"])


@router.post("/platform/incidents/{incident_id}/publish")
def publish_incident_for_assignment(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.publish_incident_for_assignment(incident_id)

    return success_response(
        message="Incident published for assignment successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/candidates")
def list_platform_candidates_for_incident(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.list_platform_candidates_for_incident(incident_id)

    return success_response(
        message="Incident assignment candidates loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/available")
def list_my_available_candidates(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.list_my_available_candidates(current_user)

    return success_response(
        message="Available assignment candidates loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/available/{candidate_id}")
def get_my_available_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.get_my_available_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/available/{candidate_id}/accept")
def accept_my_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.accept_my_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate accepted successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/available/{candidate_id}/reject")
def reject_my_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.reject_my_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate rejected successfully.",
        data=result.model_dump(mode="json"),
    )
