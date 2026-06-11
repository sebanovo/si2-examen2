from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery, UserDeviceToken
from app.services.providers.models import Provider


class NotificationsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_user_device_token_by_token(self, device_token: str) -> UserDeviceToken | None:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken).where(UserDeviceToken.device_token == device_token)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_user_device_token_by_id(self, device_token_id: str) -> UserDeviceToken | None:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken).where(UserDeviceToken.id == device_token_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_active_user_device_tokens_by_user_id(self, user_id: str) -> list[UserDeviceToken]:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken)
            .where(
                UserDeviceToken.user_id == user_id,
                UserDeviceToken.is_active.is_(True),
            )
            .order_by(UserDeviceToken.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_active_user_device_tokens_by_user_ids(self, user_ids: list[str]) -> list[UserDeviceToken]:
        if not user_ids:
            return []

        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken)
            .where(
                UserDeviceToken.user_id.in_(user_ids),
                UserDeviceToken.is_active.is_(True),
            )
            .order_by(UserDeviceToken.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.assigned_technician),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_deliveries_by_incident_id(self, incident_id: str) -> list[PushNotificationDelivery]:
        query: Select[tuple[PushNotificationDelivery]] = (
            select(PushNotificationDelivery)
            .options(
                selectinload(PushNotificationDelivery.recipient_user),
                selectinload(PushNotificationDelivery.user_device_token),
                selectinload(PushNotificationDelivery.background_job),
            )
            .where(PushNotificationDelivery.incident_id == incident_id)
            .order_by(PushNotificationDelivery.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_background_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.flush()
        return job

    def create_delivery(self, delivery: PushNotificationDelivery) -> PushNotificationDelivery:
        self.db.add(delivery)
        self.db.flush()
        return delivery

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
