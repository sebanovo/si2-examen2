from datetime import datetime, timezone

from sqlalchemy import select

from app.common.constants import (
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_FAILED,
    PROCESSING_STATUS_RUNNING,
    PROCESSING_STATUS_SUCCEEDED,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.core.database import SessionLocal
from app.integrations.factory import build_storage_service_by_name
from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident


def build_audio_evidence_processing_context(evidence_id: str) -> dict:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        storage_service = build_storage_service_by_name(evidence.storage_provider)

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        return {
            "evidence_id": str(evidence.id),
            "incident_id": str(evidence.incident_id),
            "audio_file_path": descriptor.absolute_file_path if descriptor.kind == "local_file" else None,
            "source_url": descriptor.download_url if descriptor.kind == "signed_url" else None,
        }
    finally:
        db.close()


def build_image_evidence_processing_context(evidence_id: str) -> dict:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        storage_service = build_storage_service_by_name(evidence.storage_provider)

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        return {
            "evidence_id": str(evidence.id),
            "incident_id": str(evidence.incident_id),
            "image_file_path": descriptor.absolute_file_path if descriptor.kind == "local_file" else None,
            "source_url": descriptor.download_url if descriptor.kind == "signed_url" else None,
        }
    finally:
        db.close()


def build_incident_summary_request_data(incident_id: str) -> dict:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            raise NotFoundException("Incident not found.")

        evidences = list(
            db.execute(
                select(IncidentEvidence)
                .where(IncidentEvidence.incident_id == incident_id)
                .order_by(IncidentEvidence.created_at.asc())
            ).scalars().all()
        )

        additional_texts = [
            evidence.text_content_snapshot.strip()
            for evidence in evidences
            if evidence.evidence_type == EVIDENCE_TYPE_TEXT and evidence.text_content_snapshot
        ]

        successful_transcripts = [
            evidence.transcript_text.strip()
            for evidence in evidences
            if evidence.transcript_text and evidence.audio_processing_status == PROCESSING_STATUS_SUCCEEDED
        ]

        successful_image_summaries = [
            evidence.image_summary.strip()
            for evidence in evidences
            if evidence.image_summary and evidence.image_processing_status == PROCESSING_STATUS_SUCCEEDED
        ]

        user_text_sections = [
            f"Título reportado: {incident.title}",
            f"Descripción reportada: {incident.description}",
        ]

        if additional_texts:
            user_text_sections.append(
                "Texto adicional del cliente:\n- " + "\n- ".join(additional_texts)
            )

        return {
            "incident_id": str(incident.id),
            "user_text": "\n\n".join(user_text_sections).strip() or None,
            "transcript_text": "\n\n".join(successful_transcripts).strip() or None,
            "image_analysis_summary": "\n\n".join(successful_image_summaries).strip() or None,
        }
    finally:
        db.close()


def mark_audio_processing_running(evidence_id: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_RUNNING
        evidence.audio_error_message = None
        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_audio_processing_succeeded(
    evidence_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_SUCCEEDED
        evidence.audio_provider_name = provider_name
        evidence.transcript_text = result_payload.get("transcript_text")
        evidence.transcript_language_code = result_payload.get("language_code")
        evidence.transcript_confidence = result_payload.get("confidence")
        evidence.transcript_segments_json = result_payload.get("segments")
        evidence.audio_processed_at = datetime.now(timezone.utc)
        evidence.audio_error_message = None

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_audio_processing_failed(evidence_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_FAILED
        evidence.audio_error_message = error_message
        evidence.audio_processed_at = datetime.now(timezone.utc)

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_running(evidence_id: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_RUNNING
        evidence.image_error_message = None
        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_succeeded(
    evidence_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_SUCCEEDED
        evidence.image_provider_name = provider_name
        evidence.image_labels_json = result_payload.get("labels")
        evidence.image_detections_json = result_payload.get("detections")
        evidence.image_summary = result_payload.get("summary")
        evidence.image_processed_at = datetime.now(timezone.utc)
        evidence.image_error_message = None

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_failed(evidence_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_FAILED
        evidence.image_error_message = error_message
        evidence.image_processed_at = datetime.now(timezone.utc)

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_running(incident_id: str) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_RUNNING
        incident.summary_error_message = None

        db.add(incident)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_succeeded(
    incident_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_SUCCEEDED
        incident.summary_provider_name = provider_name
        incident.structured_summary = result_payload.get("structured_summary")
        incident.suggested_category = result_payload.get("suggested_category")
        incident.suggested_priority = result_payload.get("suggested_priority")
        incident.requires_more_information = bool(
            result_payload.get("requires_more_information", False)
        )
        incident.summary_processed_at = datetime.now(timezone.utc)
        incident.summary_error_message = None

        db.add(incident)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_failed(incident_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_FAILED
        incident.summary_error_message = error_message
        incident.summary_processed_at = datetime.now(timezone.utc)

        db.add(incident)
        db.commit()
    finally:
        db.close()
