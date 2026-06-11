from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.incidents.models import Incident
from app.services.providers.models import Provider, Technician
from app.services.tracking.models import IncidentResponderLocationPing


class TrackingRepository:
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

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.assigned_technician),
                selectinload(Incident.vehicle),
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

    def create_ping(
        self,
        ping: IncidentResponderLocationPing,
    ) -> IncidentResponderLocationPing:
        self.db.add(ping)
        self.db.flush()
        return ping

    def list_pings_by_incident_id(
        self,
        incident_id: str,
    ) -> list[IncidentResponderLocationPing]:
        query: Select[tuple[IncidentResponderLocationPing]] = (
            select(IncidentResponderLocationPing)
            .options(
                selectinload(IncidentResponderLocationPing.provider).selectinload(Provider.owner_user),
                selectinload(IncidentResponderLocationPing.technician),
            )
            .where(IncidentResponderLocationPing.incident_id == incident_id)
            .order_by(IncidentResponderLocationPing.recorded_at.asc(), IncidentResponderLocationPing.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
