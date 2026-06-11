from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.incidents.models import Incident
from app.services.operations.models import IncidentOperationEvent
from app.services.providers.models import Provider, Technician


class OperationsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.technicians),
            )
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_id_for_update(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .where(Provider.id == provider_id)
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
                selectinload(Incident.assigned_technician),
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

    def get_technician_by_id_for_update(self, technician_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.id == technician_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_active_incidents(self, provider_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician),
            )
            .where(
                Incident.provider_id == provider_id,
                Incident.status.in_(["ASSIGNED", "EN_ROUTE", "ON_SITE", "IN_PROGRESS"]),
            )
            .order_by(Incident.assigned_at.asc(), Incident.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_operation_events_by_incident_id(self, incident_id: str) -> list[IncidentOperationEvent]:
        query: Select[tuple[IncidentOperationEvent]] = (
            select(IncidentOperationEvent)
            .options(
                selectinload(IncidentOperationEvent.actor_user),
                selectinload(IncidentOperationEvent.technician),
                selectinload(IncidentOperationEvent.provider).selectinload(Provider.owner_user),
            )
            .where(IncidentOperationEvent.incident_id == incident_id)
            .order_by(IncidentOperationEvent.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_event(self, event: IncidentOperationEvent) -> IncidentOperationEvent:
        self.db.add(event)
        self.db.flush()
        return event

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
