from pathlib import Path

from fastapi import UploadFile
from fastapi.responses import FileResponse, RedirectResponse, Response

from app.common.constants import (
    EVIDENCE_TYPE_AUDIO,
    EVIDENCE_TYPE_IMAGE,
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_NOT_REQUESTED,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.core.config import settings
from app.integrations.factory import build_storage_service_by_name
from app.integrations.storage.base import StorageService
from app.services.auth.models import User
from app.services.evidences.models import IncidentEvidence
from app.services.evidences.repository import EvidencesRepository
from app.services.evidences.schemas import (
    CreateTextEvidenceRequest,
    EvidenceUploaderResponse,
    IncidentEvidenceResponse,
)
from app.services.jobs.dispatcher import PipelineDispatcher


class EvidencesService:
    def __init__(
        self,
        repository: EvidencesRepository,
        storage_service: StorageService,
    ) -> None:
        self.repository = repository
        self.storage_service = storage_service
        self.dispatcher = PipelineDispatcher(repository.db)

    async def upload_incident_file_evidence_as_client(
        self,
        current_user: User,
        incident_id: str,
        evidence_type: str,
        description: str | None,
        upload_file: UploadFile,
    ) -> IncidentEvidenceResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        return await self._create_file_evidence(
            incident_id=incident_id,
            uploaded_by_user=current_user,
            evidence_type=evidence_type,
            description=description,
            upload_file=upload_file,
        )

    def create_incident_text_evidence_as_client(
        self,
        current_user: User,
        incident_id: str,
        payload: CreateTextEvidenceRequest,
    ) -> IncidentEvidenceResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        storage_result = self.storage_service.save_text_content(
            incident_id=incident_id,
            text_content=payload.text_content,
        )

        file_extension = self._extract_file_extension(
            original_filename="text_evidence.txt",
            stored_filename=storage_result.stored_filename,
        )

        evidence = IncidentEvidence(
            incident_id=incident.id,
            uploaded_by_user_id=current_user.id,
            evidence_type=EVIDENCE_TYPE_TEXT,
            original_filename="text_evidence.txt",
            stored_filename=storage_result.stored_filename,
            file_extension=file_extension,
            mime_type=storage_result.mime_type,
            file_size_bytes=storage_result.file_size_bytes,
            description=payload.description.strip() if payload.description else None,
            text_content_snapshot=payload.text_content.strip(),
            storage_provider=storage_result.storage_provider,
            storage_bucket=storage_result.storage_bucket,
            storage_object_key=storage_result.storage_object_key,
            public_url=storage_result.public_url,
            absolute_file_path=storage_result.absolute_file_path,
            audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
            image_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        )

        created_evidence = self.repository.create_evidence(evidence)

        self.dispatcher.dispatch_for_new_evidence(
            evidence=created_evidence,
            requested_by_user_id=str(current_user.id),
        )

        return self._build_evidence_response(created_evidence)

    def list_client_incident_evidences(self, current_user: User, incident_id: str) -> list[IncidentEvidenceResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def list_provider_incident_evidences(self, current_user: User, incident_id: str) -> list[IncidentEvidenceResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def list_platform_incident_evidences(self, incident_id: str) -> list[IncidentEvidenceResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def download_evidence_as_client(self, current_user: User, evidence_id: str) -> Response:
        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        incident = self.repository.get_incident_by_id(str(evidence.incident_id))
        if incident is None:
            raise NotFoundException("Incident not found for this evidence.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This evidence does not belong to the authenticated client.")

        return self._build_download_response(evidence)

    def download_evidence_as_provider(self, current_user: User, evidence_id: str) -> Response:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        incident = self.repository.get_incident_by_id(str(evidence.incident_id))
        if incident is None:
            raise NotFoundException("Incident not found for this evidence.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This evidence does not belong to your provider.")

        return self._build_download_response(evidence)

    def download_evidence_as_platform(self, evidence_id: str) -> Response:
        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        return self._build_download_response(evidence)

    async def _create_file_evidence(
        self,
        incident_id: str,
        uploaded_by_user: User,
        evidence_type: str,
        description: str | None,
        upload_file: UploadFile,
    ) -> IncidentEvidenceResponse:
        normalized_type = evidence_type.strip().upper()

        if normalized_type not in (EVIDENCE_TYPE_IMAGE, EVIDENCE_TYPE_AUDIO):
            raise ConflictException("Only IMAGE or AUDIO file evidences are allowed in this endpoint.")

        storage_result = await self.storage_service.save_uploaded_file(
            incident_id=incident_id,
            upload_file=upload_file,
        )

        file_extension = self._extract_file_extension(
            original_filename=upload_file.filename,
            stored_filename=storage_result.stored_filename,
        )

        evidence = IncidentEvidence(
            incident_id=incident_id,
            uploaded_by_user_id=uploaded_by_user.id,
            evidence_type=normalized_type,
            original_filename=upload_file.filename,
            stored_filename=storage_result.stored_filename,
            file_extension=file_extension,
            mime_type=storage_result.mime_type,
            file_size_bytes=storage_result.file_size_bytes,
            description=description.strip() if description else None,
            text_content_snapshot=None,
            storage_provider=storage_result.storage_provider,
            storage_bucket=storage_result.storage_bucket,
            storage_object_key=storage_result.storage_object_key,
            public_url=storage_result.public_url,
            absolute_file_path=storage_result.absolute_file_path,
            audio_processing_status=(
                PROCESSING_STATUS_NOT_REQUESTED if normalized_type != EVIDENCE_TYPE_AUDIO else PROCESSING_STATUS_NOT_REQUESTED
            ),
            image_processing_status=(
                PROCESSING_STATUS_NOT_REQUESTED if normalized_type != EVIDENCE_TYPE_IMAGE else PROCESSING_STATUS_NOT_REQUESTED
            ),
        )

        created_evidence = self.repository.create_evidence(evidence)

        self.dispatcher.dispatch_for_new_evidence(
            evidence=created_evidence,
            requested_by_user_id=str(uploaded_by_user.id),
        )

        return self._build_evidence_response(created_evidence)

    def _build_download_response(self, evidence: IncidentEvidence) -> Response:
        storage_service = build_storage_service_by_name(evidence.storage_provider or "local")

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        if descriptor.kind == "signed_url":
            return RedirectResponse(
                url=descriptor.download_url,
                status_code=307,
            )

        return FileResponse(
            path=descriptor.absolute_file_path,
            media_type=descriptor.media_type or "application/octet-stream",
            filename=descriptor.filename,
        )

    def _build_evidence_response(self, evidence: IncidentEvidence) -> IncidentEvidenceResponse:
        uploaded_by_user_payload = None

        if evidence.uploaded_by_user is not None:
            uploaded_user = evidence.uploaded_by_user
            uploaded_by_user_payload = EvidenceUploaderResponse(
                id=str(uploaded_user.id),
                email=uploaded_user.email,
                first_name=uploaded_user.first_name,
                last_name=uploaded_user.last_name,
                full_name=uploaded_user.full_name,
            )

        return IncidentEvidenceResponse(
            id=str(evidence.id),
            incident_id=str(evidence.incident_id),
            uploaded_by_user_id=str(evidence.uploaded_by_user_id) if evidence.uploaded_by_user_id else None,
            evidence_type=evidence.evidence_type,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            file_extension=evidence.file_extension,
            mime_type=evidence.mime_type,
            file_size_bytes=evidence.file_size_bytes,
            description=evidence.description,
            text_content_snapshot=evidence.text_content_snapshot,
            storage_provider=evidence.storage_provider,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            download_url=f"{settings.api_v1_prefix}/evidences/{evidence.id}/download",
            audio_processing_status=evidence.audio_processing_status,
            audio_provider_name=evidence.audio_provider_name,
            transcript_text=evidence.transcript_text,
            transcript_language_code=evidence.transcript_language_code,
            transcript_confidence=evidence.transcript_confidence,
            transcript_segments_json=evidence.transcript_segments_json,
            audio_processed_at=evidence.audio_processed_at,
            audio_error_message=evidence.audio_error_message,
            image_processing_status=evidence.image_processing_status,
            image_provider_name=evidence.image_provider_name,
            image_labels_json=evidence.image_labels_json,
            image_detections_json=evidence.image_detections_json,
            image_summary=evidence.image_summary,
            image_processed_at=evidence.image_processed_at,
            image_error_message=evidence.image_error_message,
            created_at=evidence.created_at,
            updated_at=evidence.updated_at,
            uploaded_by_user=uploaded_by_user_payload,
        )

    def _extract_file_extension(
        self,
        original_filename: str | None,
        stored_filename: str,
    ) -> str | None:
        original_extension = Path(original_filename).suffix.lower() if original_filename else ""
        if original_extension:
            return original_extension

        stored_extension = Path(stored_filename).suffix.lower()
        return stored_extension or None
