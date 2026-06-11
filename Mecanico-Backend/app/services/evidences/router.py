from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session, get_storage_service
from app.core.security import require_roles
from app.integrations.storage.base import StorageService
from app.services.auth.models import User
from app.services.evidences.repository import EvidencesRepository
from app.services.evidences.schemas import CreateTextEvidenceRequest
from app.services.evidences.service import EvidencesService

router = APIRouter(prefix="/evidences", tags=["Evidences"])


@router.post("/client/incidents/{incident_id}/files")
async def upload_incident_file_evidence_as_client(
    incident_id: str,
    evidence_type: str = Form(...),
    description: str | None = Form(default=None),
    file: UploadFile = File(...),
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = await service.upload_incident_file_evidence_as_client(
        current_user=current_user,
        incident_id=incident_id,
        evidence_type=evidence_type,
        description=description,
        upload_file=file,
    )

    return success_response(
        message="Incident file evidence uploaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/text")
def create_incident_text_evidence_as_client(
    incident_id: str,
    payload: CreateTextEvidenceRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.create_incident_text_evidence_as_client(
        current_user=current_user,
        incident_id=incident_id,
        payload=payload,
    )

    return success_response(
        message="Incident text evidence created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/incidents/{incident_id}")
def list_client_incident_evidences(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_client_incident_evidences(current_user, incident_id)

    return success_response(
        message="Client incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/incidents/{incident_id}")
def list_provider_incident_evidences(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_provider_incident_evidences(current_user, incident_id)

    return success_response(
        message="Provider incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/platform/incidents/{incident_id}")
def list_platform_incident_evidences(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_platform_incident_evidences(incident_id)

    return success_response(
        message="Platform incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/{evidence_id}/download")
def download_evidence(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT, ROLE_PROVIDER_ADMIN, ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
):
    service = EvidencesService(EvidencesRepository(db), storage_service)

    user_role_codes = {role.code for role in current_user.roles}

    if ROLE_PLATFORM_ADMIN in user_role_codes:
        return service.download_evidence_as_platform(evidence_id)

    if ROLE_PROVIDER_ADMIN in user_role_codes:
        return service.download_evidence_as_provider(current_user, evidence_id)

    return service.download_evidence_as_client(current_user, evidence_id)
