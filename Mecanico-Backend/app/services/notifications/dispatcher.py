from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_PUSH_NOTIFICATION,
    CELERY_QUEUE_PUSH,
    PUSH_DELIVERY_STATUS_PENDING,
)
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery
from app.services.notifications.repository import NotificationsRepository


class PushNotificationDispatcher:
    def __init__(self, db) -> None:
        self.repository = NotificationsRepository(db)
        self.db = db

    def enqueue_event_for_user_ids(
        self,
        *,
        requested_by_user_id: str | None,
        incident_id: str | None,
        event_code: str,
        recipient_user_ids: list[str],
        title: str,
        body: str,
        data: dict[str, str] | None = None,
    ) -> list[BackgroundJob]:
        active_tokens = self.repository.list_active_user_device_tokens_by_user_ids(recipient_user_ids)
        if not active_tokens:
            return []

        normalized_data = {
            str(key): str(value)
            for key, value in (data or {}).items()
            if value is not None
        }

        try:
            created_jobs: list[BackgroundJob] = []

            for device_token in active_tokens:
                job = BackgroundJob(
                    requested_by_user_id=requested_by_user_id,
                    job_type=BACKGROUND_JOB_TYPE_PUSH_NOTIFICATION,
                    status=BACKGROUND_JOB_STATUS_PENDING,
                    provider_name="celery",
                    queue_name=CELERY_QUEUE_PUSH,
                    entity_type="PUSH_NOTIFICATION_DELIVERY",
                    entity_id=None,
                    payload_json={
                        "event_code": event_code,
                        "incident_id": incident_id,
                        "recipient_user_id": str(device_token.user_id),
                        "user_device_token_id": str(device_token.id),
                        "title": title,
                        "body": body,
                        "data": normalized_data,
                    },
                )
                self.repository.create_background_job(job)

                delivery = PushNotificationDelivery(
                    background_job_id=job.id,
                    incident_id=incident_id,
                    recipient_user_id=device_token.user_id,
                    user_device_token_id=device_token.id,
                    provider_name=None,
                    event_code=event_code,
                    title=title,
                    body=body,
                    data_json=normalized_data or None,
                    status=PUSH_DELIVERY_STATUS_PENDING,
                    provider_message_id=None,
                    error_message=None,
                    sent_at=None,
                )
                self.repository.create_delivery(delivery)

                job.entity_id = str(delivery.id)
                self.repository.save(job)

                from app.tasks.task_definitions import push_notification_task

                async_result = push_notification_task.apply_async(
                    args=[str(job.id), str(delivery.id)],
                    queue=CELERY_QUEUE_PUSH,
                )

                job.celery_task_id = async_result.id
                self.repository.save(job)
                created_jobs.append(job)

            self.repository.commit()

            for job in created_jobs:
                self.repository.refresh(job)

            return created_jobs
        except Exception:
            self.repository.rollback()
            raise
