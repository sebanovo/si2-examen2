from sqlalchemy import Select, delete, select
from sqlalchemy.orm import Session, selectinload

from app.services.assignment.models import IncidentAssignmentCandidate
from app.services.catalog.models import ProviderService
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class AssignmentRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
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

    def list_eligible_provider_pool(self) -> list[Provider]:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.technicians),
                selectinload(Provider.provider_services).selectinload(
                    ProviderService.service_catalog_item
                ),
            )
            .where(
                Provider.is_active.is_(True),
                Provider.is_available.is_(True),
            )
            .order_by(Provider.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def delete_non_accepted_candidates_by_incident_id(self, incident_id: str) -> None:
        self.db.execute(
            delete(IncidentAssignmentCandidate).where(
                IncidentAssignmentCandidate.incident_id == incident_id,
                IncidentAssignmentCandidate.status != "ACCEPTED",
            )
        )

    def create_candidates(self, candidates: list[IncidentAssignmentCandidate]) -> None:
        for candidate in candidates:
            self.db.add(candidate)

    def list_candidates_by_incident_id(
        self,
        incident_id: str,
    ) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(IncidentAssignmentCandidate.incident_id == incident_id)
            .order_by(
                IncidentAssignmentCandidate.recommendation_rank.asc(),
                IncidentAssignmentCandidate.score.desc(),
                IncidentAssignmentCandidate.created_at.asc(),
            )
        )
        return list(self.db.execute(query).scalars().all())

    def get_candidate_by_id(self, candidate_id: str) -> IncidentAssignmentCandidate | None:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(IncidentAssignmentCandidate.id == candidate_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_candidate_by_id_for_update(self, candidate_id: str) -> IncidentAssignmentCandidate | None:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .where(IncidentAssignmentCandidate.id == candidate_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_available_candidates_for_provider(self, provider_id: str) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(
                IncidentAssignmentCandidate.provider_id == provider_id,
                IncidentAssignmentCandidate.status == "AVAILABLE",
            )
            .order_by(
                IncidentAssignmentCandidate.recommendation_rank.asc(),
                IncidentAssignmentCandidate.score.desc(),
                IncidentAssignmentCandidate.created_at.asc(),
            )
        )
        return list(self.db.execute(query).scalars().all())

    def list_available_candidates_by_incident_id_for_update(
        self,
        incident_id: str,
    ) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .where(
                IncidentAssignmentCandidate.incident_id == incident_id,
                IncidentAssignmentCandidate.status == "AVAILABLE",
            )
            .with_for_update()
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def flush(self) -> None:
        self.db.flush()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
