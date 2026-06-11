from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "mechanic_api",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=["app.tasks.task_definitions"],
)

celery_app.conf.update(
    task_default_queue=settings.celery_default_queue,
    task_track_started=True,
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_routes={
        "jobs.demo_echo_task": {"queue": "default"},
        "jobs.audio_transcription_task": {"queue": "audio"},
        "jobs.image_analysis_task": {"queue": "image"},
        "jobs.incident_summary_task": {"queue": "summary"},
        "jobs.push_notification_task": {"queue": "push"},
    },
)
