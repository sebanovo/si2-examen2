from dataclasses import asdict
from datetime import datetime, timezone

from app.common.constants import (
    BACKGROUND_JOB_STATUS_FAILED,
    BACKGROUND_JOB_STATUS_RUNNING,
    BACKGROUND_JOB_STATUS_SUCCEEDED,
)
from app.core.database import SessionLocal
from app.services.jobs.repository import JobsRepository


def mark_job_running(job_id: str, celery_task_id: str | None = None) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_RUNNING
        job.celery_task_id = celery_task_id or job.celery_task_id
        job.started_at = datetime.now(timezone.utc)
        job.finished_at = None
        job.error_message = None
        job.attempts_count += 1

        repository.save_job(job)
    finally:
        db.close()


def mark_job_succeeded(job_id: str, result_payload: dict | object | None = None) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_SUCCEEDED
        job.finished_at = datetime.now(timezone.utc)
        job.error_message = None

        if result_payload is None:
            job.result_json = None
        elif isinstance(result_payload, dict):
            job.result_json = result_payload
        else:
            job.result_json = asdict(result_payload)

        repository.save_job(job)
    finally:
        db.close()


def mark_job_failed(job_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_FAILED
        job.error_message = error_message
        job.finished_at = datetime.now(timezone.utc)

        repository.save_job(job)
    finally:
        db.close()
