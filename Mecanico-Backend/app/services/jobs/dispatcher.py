from sqlalchemy import select
from sqlalchemy.orm import Session

from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_AUDIO_TRANSCRIPTION,
    BACKGROUND_JOB_TYPE_IMAGE_ANALYSIS,
    BACKGROUND_JOB_TYPE_INCIDENT_SUMMARY,
    CELERY_QUEUE_AUDIO,
    CELERY_QUEUE_IMAGE,
    CELERY_QUEUE_SUMMARY,
    EVIDENCE_TYPE_AUDIO,
    EVIDENCE_TYPE_IMAGE,
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_PENDING,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob


class PipelineDispatcher:
    def __init__(self, db: Session) -> None:
        self.db = db

    def dispatch_for_new_evidence(
        self,
        evidence: IncidentEvidence,
        requested_by_user_id: str | None,
    ) -> list[BackgroundJob]:
        created_jobs: list[BackgroundJob] = []

        if evidence.evidence_type == EVIDENCE_TYPE_AUDIO:
            created_jobs.append(
                self.enqueue_audio_transcription_job(
                    requested_by_user_id=requested_by_user_id,
                    evidence_id=str(evidence.id),
                    enqueue_reason="new_audio_evidence_uploaded",
                )
            )
            return created_jobs

        if evidence.evidence_type == EVIDENCE_TYPE_IMAGE:
            created_jobs.append(
                self.enqueue_image_analysis_job(
                    requested_by_user_id=requested_by_user_id,
                    evidence_id=str(evidence.id),
                    enqueue_reason="new_image_evidence_uploaded",
                )
            )
            return created_jobs

        if evidence.evidence_type == EVIDENCE_TYPE_TEXT:
            created_jobs.append(
                self.enqueue_incident_summary_job(
                    requested_by_user_id=requested_by_user_id,
                    incident_id=str(evidence.incident_id),
                    enqueue_reason="new_text_evidence_uploaded",
                )
            )
            return created_jobs

        return created_jobs

    def enqueue_audio_transcription_job(
        self,
        requested_by_user_id: str | None,
        evidence_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        evidence = self._get_evidence_or_raise(evidence_id)

        if evidence.evidence_type != EVIDENCE_TYPE_AUDIO:
            raise ConflictException("The selected evidence is not an AUDIO evidence.")

        evidence.audio_processing_status = PROCESSING_STATUS_PENDING
        evidence.audio_provider_name = None
        evidence.transcript_text = None
        evidence.transcript_language_code = None
        evidence.transcript_confidence = None
        evidence.transcript_segments_json = None
        evidence.audio_processed_at = None
        evidence.audio_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_AUDIO_TRANSCRIPTION,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_AUDIO,
            entity_type="INCIDENT_EVIDENCE",
            entity_id=evidence_id,
            payload_json={
                "evidence_id": evidence_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(evidence)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import audio_transcription_task

        async_result = audio_transcription_task.apply_async(
            args=[str(job.id), evidence_id],
            queue=CELERY_QUEUE_AUDIO,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def enqueue_image_analysis_job(
        self,
        requested_by_user_id: str | None,
        evidence_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        evidence = self._get_evidence_or_raise(evidence_id)

        if evidence.evidence_type != EVIDENCE_TYPE_IMAGE:
            raise ConflictException("The selected evidence is not an IMAGE evidence.")

        evidence.image_processing_status = PROCESSING_STATUS_PENDING
        evidence.image_provider_name = None
        evidence.image_labels_json = None
        evidence.image_detections_json = None
        evidence.image_summary = None
        evidence.image_processed_at = None
        evidence.image_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_IMAGE_ANALYSIS,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_IMAGE,
            entity_type="INCIDENT_EVIDENCE",
            entity_id=evidence_id,
            payload_json={
                "evidence_id": evidence_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(evidence)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import image_analysis_task

        async_result = image_analysis_task.apply_async(
            args=[str(job.id), evidence_id],
            queue=CELERY_QUEUE_IMAGE,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def enqueue_incident_summary_job(
        self,
        requested_by_user_id: str | None,
        incident_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        incident = self._get_incident_or_raise(incident_id)

        incident.ai_summary_status = PROCESSING_STATUS_PENDING
        incident.summary_provider_name = None
        incident.structured_summary = None
        incident.suggested_category = None
        incident.suggested_priority = None
        incident.requires_more_information = False
        incident.summary_processed_at = None
        incident.summary_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_INCIDENT_SUMMARY,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_SUMMARY,
            entity_type="INCIDENT",
            entity_id=incident_id,
            payload_json={
                "incident_id": incident_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(incident)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import incident_summary_task

        async_result = incident_summary_task.apply_async(
            args=[str(job.id), incident_id],
            queue=CELERY_QUEUE_SUMMARY,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def _get_evidence_or_raise(self, evidence_id: str) -> IncidentEvidence:
        evidence = self.db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        return evidence

    def _get_incident_or_raise(self, incident_id: str) -> Incident:
        incident = self.db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            raise NotFoundException("Incident not found.")

        return incident
