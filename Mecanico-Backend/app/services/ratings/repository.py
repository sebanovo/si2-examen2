from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload

from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.providers.models import Provider, Technician
from app.services.ratings.models import ProviderRating


class RatingsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
            .where(Provider.id == provider_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
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

    def get_rating_by_incident_and_client(
        self,
        incident_id: str,
        client_user_id: str,
    ) -> ProviderRating | None:
        query: Select[tuple[ProviderRating]] = (
            select(ProviderRating)
            .options(
                selectinload(ProviderRating.client_user),
                selectinload(ProviderRating.provider),
                selectinload(ProviderRating.technician),
                selectinload(ProviderRating.incident),
            )
            .where(
                ProviderRating.incident_id == incident_id,
                ProviderRating.client_user_id == client_user_id,
            )
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_rating_by_incident_and_provider(
        self,
        incident_id: str,
        provider_id: str,
    ) -> ProviderRating | None:
        query: Select[tuple[ProviderRating]] = (
            select(ProviderRating)
            .options(
                selectinload(ProviderRating.client_user),
                selectinload(ProviderRating.provider),
                selectinload(ProviderRating.technician),
                selectinload(ProviderRating.incident),
            )
            .where(
                ProviderRating.incident_id == incident_id,
                ProviderRating.provider_id == provider_id,
            )
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_ratings(
        self,
        provider_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ProviderRating]:
        query: Select[tuple[ProviderRating]] = (
            select(ProviderRating)
            .options(
                selectinload(ProviderRating.client_user),
                selectinload(ProviderRating.provider),
                selectinload(ProviderRating.technician),
                selectinload(ProviderRating.incident),
            )
            .where(ProviderRating.provider_id == provider_id)
            .order_by(ProviderRating.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def list_ratings(
        self,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ProviderRating]:
        query: Select[tuple[ProviderRating]] = (
            select(ProviderRating)
            .options(
                selectinload(ProviderRating.client_user),
                selectinload(ProviderRating.provider),
                selectinload(ProviderRating.technician),
                selectinload(ProviderRating.incident),
            )
            .order_by(ProviderRating.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def count_provider_ratings(self, provider_id: str) -> int:
        query = select(func.count(ProviderRating.id)).where(
            ProviderRating.provider_id == provider_id
        )
        return int(self.db.execute(query).scalar_one() or 0)

    def calculate_provider_average_rating(self, provider_id: str) -> float:
        query = select(func.coalesce(func.avg(ProviderRating.rating_score), 0)).where(
            ProviderRating.provider_id == provider_id
        )
        value = self.db.execute(query).scalar_one()
        return round(float(value or 0), 2)

    def count_provider_ratings_by_score(self, provider_id: str, rating_score: int) -> int:
        query = select(func.count(ProviderRating.id)).where(
            ProviderRating.provider_id == provider_id,
            ProviderRating.rating_score == rating_score,
        )
        return int(self.db.execute(query).scalar_one() or 0)

    def count_provider_recommendations(self, provider_id: str) -> int:
        query = select(func.count(ProviderRating.id)).where(
            ProviderRating.provider_id == provider_id,
            ProviderRating.would_recommend.is_(True),
        )
        return int(self.db.execute(query).scalar_one() or 0)

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