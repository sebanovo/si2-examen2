from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.jobs.repository import JobsRepository
from app.services.jobs.schemas import DemoJobEnqueueRequest
from app.services.jobs.service import JobsService

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/demo/enqueue")
def enqueue_demo_job(
    payload: DemoJobEnqueueRequest,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_demo_job(current_user, payload)

    return success_response(
        message="Demo background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/evidences/{evidence_id}/audio-transcription/enqueue")
def enqueue_audio_transcription_job(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_audio_transcription_job(current_user, evidence_id)

    return success_response(
        message="Audio transcription background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/evidences/{evidence_id}/image-analysis/enqueue")
def enqueue_image_analysis_job(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_image_analysis_job(current_user, evidence_id)

    return success_response(
        message="Image analysis background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/incidents/{incident_id}/summary/enqueue")
def enqueue_incident_summary_job(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_incident_summary_job(current_user, incident_id)

    return success_response(
        message="Incident summary background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_jobs(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.list_jobs(limit=limit, offset=offset)

    return success_response(
        message="Background jobs loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{job_id}")
def get_job_by_id(
    job_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.get_job_by_id(job_id)

    return success_response(
        message="Background job loaded successfully.",
        data=result.model_dump(mode="json"),
    )