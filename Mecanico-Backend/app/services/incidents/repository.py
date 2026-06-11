from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.incidents.models import Incident
from app.services.providers.models import Provider
from app.services.vehicles.models import Vehicle


class IncidentsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_vehicle_by_id(self, vehicle_id: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.id == vehicle_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_incident(self, incident: Incident) -> Incident:
        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)
        return incident

    def save_incident(self, incident: Incident) -> Incident:
        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)
        return incident

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_incidents_by_client_user_id(self, client_user_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.client_user_id == client_user_id)
            .order_by(Incident.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_incidents_by_provider_id(self, provider_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.provider_id == provider_id)
            .order_by(Incident.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_all_incidents(self, limit: int = 50, offset: int = 0) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .order_by(Incident.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())