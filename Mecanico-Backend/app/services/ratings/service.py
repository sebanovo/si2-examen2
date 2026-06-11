from app.common.constants import (
    AUDIT_OUTCOME_SUCCESS,
    AUDIT_SCOPE_DOMAIN,
    INCIDENT_STATUS_COMPLETED,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.audit.dispatcher import AuditEventDispatcher
from app.services.auth.models import User
from app.services.ratings.models import ProviderRating
from app.services.ratings.repository import RatingsRepository
from app.services.ratings.schemas import (
    CreateOrUpdateProviderRatingRequest,
    ProviderRatingIncidentSummaryResponse,
    ProviderRatingProviderSummaryResponse,
    ProviderRatingResponse,
    ProviderRatingStatsResponse,
    ProviderRatingTechnicianSummaryResponse,
    ProviderRatingUserSummaryResponse,
)


class RatingsService:
    def __init__(self, repository: RatingsRepository) -> None:
        self.repository = repository

    def create_or_update_my_incident_rating(
        self,
        current_user: User,
        incident_id: str,
        payload: CreateOrUpdateProviderRatingRequest,
    ) -> ProviderRatingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        if incident.status != INCIDENT_STATUS_COMPLETED:
            raise ConflictException("Only completed incidents can be rated.")

        if incident.provider_id is None:
            raise ConflictException("This incident does not have an assigned provider.")

        try:
            provider = self.repository.get_provider_by_id_for_update(str(incident.provider_id))
            if provider is None:
                raise NotFoundException("Provider not found.")

            rating = self.repository.get_rating_by_incident_and_client(
                incident_id=incident_id,
                client_user_id=str(current_user.id),
            )

            if rating is None:
                rating = ProviderRating(
                    incident_id=incident.id,
                    client_user_id=current_user.id,
                    provider_id=provider.id,
                    technician_id=incident.assigned_technician_id,
                    rating_score=payload.rating_score,
                    punctuality_score=payload.punctuality_score,
                    service_quality_score=payload.service_quality_score,
                    communication_score=payload.communication_score,
                    comment=self._normalize_optional_text(payload.comment),
                    would_recommend=payload.would_recommend,
                    provider_average_after_rating=None,
                )
                self.repository.save(rating)
            else:
                rating.provider_id = provider.id
                rating.technician_id = incident.assigned_technician_id
                rating.rating_score = payload.rating_score
                rating.punctuality_score = payload.punctuality_score
                rating.service_quality_score = payload.service_quality_score
                rating.communication_score = payload.communication_score
                rating.comment = self._normalize_optional_text(payload.comment)
                rating.would_recommend = payload.would_recommend
                self.repository.save(rating)

            self.repository.flush()

            provider.average_rating = self.repository.calculate_provider_average_rating(
                str(provider.id)
            )
            rating.provider_average_after_rating = provider.average_rating

            self.repository.save(provider)
            self.repository.save(rating)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        rating = self.repository.get_rating_by_incident_and_client(
            incident_id=incident_id,
            client_user_id=str(current_user.id),
        )
        if rating is None:
            raise NotFoundException("Rating not found after save.")

        self._emit_audit_safely(
            actor_user_id=str(current_user.id),
            incident_id=incident_id,
            provider_id=str(rating.provider_id),
            event_type="PROVIDER_RATED",
            entity_id=str(rating.id),
            payload_json={
                "rating_score": rating.rating_score,
                "punctuality_score": rating.punctuality_score,
                "service_quality_score": rating.service_quality_score,
                "communication_score": rating.communication_score,
                "would_recommend": rating.would_recommend,
                "provider_average_after_rating": rating.provider_average_after_rating,
            },
        )

        return self._build_rating_response(rating)

    def get_my_incident_rating(
        self,
        current_user: User,
        incident_id: str,
    ) -> ProviderRatingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        rating = self.repository.get_rating_by_incident_and_client(
            incident_id=incident_id,
            client_user_id=str(current_user.id),
        )
        if rating is None:
            raise NotFoundException("Rating not found.")

        return self._build_rating_response(rating)

    def get_my_provider_incident_rating(
        self,
        current_user: User,
        incident_id: str,
    ) -> ProviderRatingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        rating = self.repository.get_rating_by_incident_and_provider(
            incident_id=incident_id,
            provider_id=str(provider.id),
        )
        if rating is None:
            raise NotFoundException("Rating not found.")

        return self._build_rating_response(rating)

    def list_my_provider_ratings(
        self,
        current_user: User,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ProviderRatingResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        ratings = self.repository.list_provider_ratings(
            provider_id=str(provider.id),
            limit=limit,
            offset=offset,
        )

        return [self._build_rating_response(rating) for rating in ratings]

    def get_my_provider_rating_stats(
        self,
        current_user: User,
    ) -> ProviderRatingStatsResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        return self._build_provider_stats_response(provider_id=str(provider.id))

    def list_platform_ratings(
        self,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ProviderRatingResponse]:
        ratings = self.repository.list_ratings(limit=limit, offset=offset)
        return [self._build_rating_response(rating) for rating in ratings]

    def list_platform_provider_ratings(
        self,
        provider_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ProviderRatingResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        ratings = self.repository.list_provider_ratings(
            provider_id=provider_id,
            limit=limit,
            offset=offset,
        )

        return [self._build_rating_response(rating) for rating in ratings]

    def get_platform_provider_rating_stats(
        self,
        provider_id: str,
    ) -> ProviderRatingStatsResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        return self._build_provider_stats_response(provider_id=provider_id)

    def _build_provider_stats_response(self, provider_id: str) -> ProviderRatingStatsResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        ratings_count = self.repository.count_provider_ratings(provider_id)
        average_rating = self.repository.calculate_provider_average_rating(provider_id)

        return ProviderRatingStatsResponse(
            provider_id=str(provider.id),
            provider_name=provider.business_name,
            average_rating=average_rating,
            ratings_count=ratings_count,
            five_star_count=self.repository.count_provider_ratings_by_score(provider_id, 5),
            four_star_count=self.repository.count_provider_ratings_by_score(provider_id, 4),
            three_star_count=self.repository.count_provider_ratings_by_score(provider_id, 3),
            two_star_count=self.repository.count_provider_ratings_by_score(provider_id, 2),
            one_star_count=self.repository.count_provider_ratings_by_score(provider_id, 1),
            would_recommend_count=self.repository.count_provider_recommendations(provider_id),
        )

    def _build_rating_response(self, rating: ProviderRating) -> ProviderRatingResponse:
        client_payload = None
        if rating.client_user is not None:
            client_payload = ProviderRatingUserSummaryResponse(
                id=str(rating.client_user.id),
                email=rating.client_user.email,
                first_name=rating.client_user.first_name,
                last_name=rating.client_user.last_name,
                full_name=rating.client_user.full_name,
            )

        provider_payload = None
        if rating.provider is not None:
            provider_payload = ProviderRatingProviderSummaryResponse(
                id=str(rating.provider.id),
                business_name=rating.provider.business_name,
                provider_type=rating.provider.provider_type,
                average_rating=rating.provider.average_rating,
            )

        technician_payload = None
        if rating.technician is not None:
            technician_payload = ProviderRatingTechnicianSummaryResponse(
                id=str(rating.technician.id),
                full_name=rating.technician.full_name,
                phone_number=rating.technician.phone_number,
            )

        incident_payload = None
        if rating.incident is not None:
            incident_payload = ProviderRatingIncidentSummaryResponse(
                id=str(rating.incident.id),
                title=rating.incident.title,
                status=rating.incident.status,
                completed_at=rating.incident.completed_at,
            )

        return ProviderRatingResponse(
            id=str(rating.id),
            incident_id=str(rating.incident_id),
            client_user_id=str(rating.client_user_id),
            provider_id=str(rating.provider_id),
            technician_id=str(rating.technician_id) if rating.technician_id else None,
            rating_score=rating.rating_score,
            punctuality_score=rating.punctuality_score,
            service_quality_score=rating.service_quality_score,
            communication_score=rating.communication_score,
            comment=rating.comment,
            would_recommend=rating.would_recommend,
            provider_average_after_rating=rating.provider_average_after_rating,
            created_at=rating.created_at,
            updated_at=rating.updated_at,
            client_user=client_payload,
            provider=provider_payload,
            technician=technician_payload,
            incident=incident_payload,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None

    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        entity_id: str | None,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope=AUDIT_SCOPE_DOMAIN,
                event_type=event_type,
                entity_type="PROVIDER_RATING",
                entity_id=entity_id,
                outcome=AUDIT_OUTCOME_SUCCESS,
                payload_json=payload_json,
            )
        except Exception:
            return