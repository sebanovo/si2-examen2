from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.billing.models import IncidentBilling
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class BillingRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

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

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.provider_services).selectinload(
                    Provider.provider_services.property.entity.class_.service_catalog_item
                ),
            )
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_billing_by_incident_id(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .options(
                selectinload(IncidentBilling.client_user),
                selectinload(IncidentBilling.provider).selectinload(Provider.owner_user),
                selectinload(IncidentBilling.incident),
            )
            .where(IncidentBilling.incident_id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_billing_by_incident_id_for_update(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .where(IncidentBilling.incident_id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

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
