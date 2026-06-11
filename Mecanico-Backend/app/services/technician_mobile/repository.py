from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.incidents.models import Incident
from app.services.operations.models import IncidentOperationEvent
from app.services.providers.models import Provider, Technician
from app.services.tracking.models import IncidentResponderLocationPing


class TechnicianMobileRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_technician_by_user_id(self, user_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .options(
                selectinload(Technician.user),
                selectinload(Technician.provider).selectinload(Provider.owner_user),
            )
            .where(Technician.user_id == user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_technician_by_user_id_for_update(self, user_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.user_id == user_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician).selectinload(Technician.user),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id_for_update(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_my_assigned_incidents(
        self,
        technician_id: str,
        active_only: bool = True,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician).selectinload(Technician.user),
            )
            .where(Incident.assigned_technician_id == technician_id)
        )

        if active_only:
            query = query.where(
                Incident.status.in_(
                    [
                        "ASSIGNED",
                        "EN_ROUTE",
                        "ON_SITE",
                        "IN_PROGRESS",
                    ]
                )
            )

        query = (
            query.order_by(Incident.assigned_at.desc().nullslast(), Incident.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        return list(self.db.execute(query).scalars().all())

    def create_operation_event(
        self,
        event: IncidentOperationEvent,
    ) -> IncidentOperationEvent:
        self.db.add(event)
        self.db.flush()
        return event

    def create_location_ping(
        self,
        ping: IncidentResponderLocationPing,
    ) -> IncidentResponderLocationPing:
        self.db.add(ping)
        self.db.flush()
        return ping

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