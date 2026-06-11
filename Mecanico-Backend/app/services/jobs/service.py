from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_DEMO,
    CELERY_QUEUE_DEFAULT,
)
from app.common.exceptions import NotFoundException
from app.services.auth.models import User
from app.services.jobs.dispatcher import PipelineDispatcher
from app.services.jobs.models import BackgroundJob
from app.services.jobs.repository import JobsRepository
from app.services.jobs.schemas import (
    BackgroundJobRequestedByUserResponse,
    BackgroundJobResponse,
    DemoJobEnqueueRequest,
)
from app.tasks.task_definitions import demo_echo_task


class JobsService:
    def __init__(self, repository: JobsRepository) -> None:
        self.repository = repository
        self.dispatcher = PipelineDispatcher(repository.db)

    def enqueue_demo_job(
        self,
        current_user: User,
        payload: DemoJobEnqueueRequest,
    ) -> BackgroundJobResponse:
        job = BackgroundJob(
            requested_by_user_id=current_user.id,
            job_type=BACKGROUND_JOB_TYPE_DEMO,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_DEFAULT,
            entity_type=None,
            entity_id=None,
            payload_json={
                "message": payload.message,
                "countdown_seconds": payload.countdown_seconds,
            },
        )

        created_job = self.repository.create_job(job)

        async_result = demo_echo_task.apply_async(
            args=[str(created_job.id), payload.message],
            countdown=payload.countdown_seconds,
            queue=CELERY_QUEUE_DEFAULT,
        )

        created_job.celery_task_id = async_result.id
        updated_job = self.repository.save_job(created_job)

        return self._build_job_response(updated_job)

    def enqueue_audio_transcription_job(
        self,
        current_user: User,
        evidence_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_audio_transcription_job(
            requested_by_user_id=str(current_user.id),
            evidence_id=evidence_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def enqueue_image_analysis_job(
        self,
        current_user: User,
        evidence_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_image_analysis_job(
            requested_by_user_id=str(current_user.id),
            evidence_id=evidence_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def enqueue_incident_summary_job(
        self,
        current_user: User,
        incident_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_incident_summary_job(
            requested_by_user_id=str(current_user.id),
            incident_id=incident_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def list_jobs(self, limit: int = 50, offset: int = 0) -> list[BackgroundJobResponse]:
        jobs = self.repository.list_jobs(limit=limit, offset=offset)
        return [self._build_job_response(job) for job in jobs]

    def get_job_by_id(self, job_id: str) -> BackgroundJobResponse:
        job = self.repository.get_job_by_id(job_id)
        if job is None:
            raise NotFoundException("Background job not found.")

        return self._build_job_response(job)

    def _build_job_response(self, job: BackgroundJob) -> BackgroundJobResponse:
        requested_by_user_payload = None

        if job.requested_by_user is not None:
            user = job.requested_by_user
            requested_by_user_payload = BackgroundJobRequestedByUserResponse(
                id=str(user.id),
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                full_name=user.full_name,
            )

        return BackgroundJobResponse(
            id=str(job.id),
            requested_by_user_id=str(job.requested_by_user_id) if job.requested_by_user_id else None,
            job_type=job.job_type,
            status=job.status,
            provider_name=job.provider_name,
            queue_name=job.queue_name,
            celery_task_id=job.celery_task_id,
            entity_type=job.entity_type,
            entity_id=job.entity_id,
            payload_json=job.payload_json,
            result_json=job.result_json,
            error_message=job.error_message,
            attempts_count=job.attempts_count,
            started_at=job.started_at,
            finished_at=job.finished_at,
            created_at=job.created_at,
            updated_at=job.updated_at,
            requested_by_user=requested_by_user_payload,
        )
