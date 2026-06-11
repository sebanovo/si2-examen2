import time
from dataclasses import asdict

from app.core.database import SessionLocal
from app.integrations.factory import (
    build_llm_provider,
    build_push_provider,
    build_speech_to_text_provider,
    build_vision_provider,
)
from app.integrations.llm.base import IncidentSummaryRequest
from app.integrations.push.base import PushNotificationRequest
from app.integrations.speech_to_text.base import AudioTranscriptionRequest
from app.integrations.vision.base import ImageAnalysisRequest
from app.services.jobs.dispatcher import PipelineDispatcher
from app.tasks.celery_app import celery_app
from app.tasks.job_runtime import mark_job_failed, mark_job_running, mark_job_succeeded
from app.tasks.notification_runtime import (
    build_push_notification_delivery_context,
    mark_delivery_failed,
    mark_delivery_running,
    mark_delivery_succeeded,
)
from app.tasks.pipeline_runtime import (
    build_audio_evidence_processing_context,
    build_image_evidence_processing_context,
    build_incident_summary_request_data,
    mark_audio_processing_failed,
    mark_audio_processing_running,
    mark_audio_processing_succeeded,
    mark_image_processing_failed,
    mark_image_processing_running,
    mark_image_processing_succeeded,
    mark_incident_summary_failed,
    mark_incident_summary_running,
    mark_incident_summary_succeeded,
)


@celery_app.task(bind=True, name="jobs.demo_echo_task")
def demo_echo_task(self, job_id: str, message: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        time.sleep(2)

        result = {
            "message": message,
            "worker_task_id": self.request.id,
            "info": "Demo background task finished successfully.",
        }

        mark_job_succeeded(job_id, result)
        return result
    except Exception as exc:
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.audio_transcription_task")
def audio_transcription_task(self, job_id: str, evidence_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_audio_processing_running(evidence_id)

        context = build_audio_evidence_processing_context(evidence_id)

        provider = build_speech_to_text_provider()
        result = provider.transcribe_audio(
            AudioTranscriptionRequest(
                evidence_id=evidence_id,
                audio_file_path=context["audio_file_path"],
                source_url=context["source_url"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = context["incident_id"]

        mark_audio_processing_succeeded(
            evidence_id=evidence_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        try:
            db = SessionLocal()
            try:
                dispatcher = PipelineDispatcher(db)
                summary_job = dispatcher.enqueue_incident_summary_job(
                    requested_by_user_id=None,
                    incident_id=context["incident_id"],
                    enqueue_reason="audio_transcription_succeeded",
                )
                result_payload["followup_incident_summary_job_id"] = str(summary_job.id)
            finally:
                db.close()
        except Exception as followup_exc:
            result_payload["followup_incident_summary_enqueue_error"] = str(followup_exc)

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_audio_processing_failed(evidence_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.image_analysis_task")
def image_analysis_task(self, job_id: str, evidence_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_image_processing_running(evidence_id)

        context = build_image_evidence_processing_context(evidence_id)

        provider = build_vision_provider()
        result = provider.analyze_image(
            ImageAnalysisRequest(
                evidence_id=evidence_id,
                image_file_path=context["image_file_path"],
                source_url=context["source_url"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = context["incident_id"]

        mark_image_processing_succeeded(
            evidence_id=evidence_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        try:
            db = SessionLocal()
            try:
                dispatcher = PipelineDispatcher(db)
                summary_job = dispatcher.enqueue_incident_summary_job(
                    requested_by_user_id=None,
                    incident_id=context["incident_id"],
                    enqueue_reason="image_analysis_succeeded",
                )
                result_payload["followup_incident_summary_job_id"] = str(summary_job.id)
            finally:
                db.close()
        except Exception as followup_exc:
            result_payload["followup_incident_summary_enqueue_error"] = str(followup_exc)

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_image_processing_failed(evidence_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.incident_summary_task")
def incident_summary_task(self, job_id: str, incident_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_incident_summary_running(incident_id)

        request_payload = build_incident_summary_request_data(incident_id)

        provider = build_llm_provider()
        result = provider.summarize_incident(
            IncidentSummaryRequest(
                incident_id=incident_id,
                user_text=request_payload["user_text"],
                transcript_text=request_payload["transcript_text"],
                image_analysis_summary=request_payload["image_analysis_summary"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = incident_id

        mark_incident_summary_succeeded(
            incident_id=incident_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_incident_summary_failed(incident_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.push_notification_task")
def push_notification_task(self, job_id: str, delivery_id: str) -> dict:
    provider_name = None

    try:
        mark_job_running(job_id, self.request.id)
        mark_delivery_running(delivery_id)

        context = build_push_notification_delivery_context(delivery_id)

        provider = build_push_provider()
        provider_name = provider.provider_name

        result = provider.send_push_notification(
            PushNotificationRequest(
                recipient_token=context["recipient_token"],
                title=context["title"],
                body=context["body"],
                data=context["data"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["delivery_id"] = delivery_id

        if not result.accepted:
            error_message = (
                result_payload.get("error_message")
                or "Push notification provider did not accept the message."
            )
            deactivate_device = _should_deactivate_device(error_message)
            mark_delivery_failed(
                delivery_id=delivery_id,
                provider_name=provider.provider_name,
                error_message=error_message,
                deactivate_device=deactivate_device,
            )
            mark_job_failed(job_id, error_message)
            return result_payload

        mark_delivery_succeeded(
            delivery_id=delivery_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )
        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        error_message = str(exc)
        deactivate_device = _should_deactivate_device(error_message)
        mark_delivery_failed(
            delivery_id=delivery_id,
            provider_name=provider_name,
            error_message=error_message,
            deactivate_device=deactivate_device,
        )
        mark_job_failed(job_id, error_message)
        raise


def _should_deactivate_device(error_message: str) -> bool:
    normalized_error = error_message.lower()
    return (
        "not registered" in normalized_error
        or "registration token is not a valid fcm registration token" in normalized_error
        or "requested entity was not found" in normalized_error
        or "unregistered" in normalized_error
    )
