import math
from datetime import datetime, timezone

from app.common.constants import (
    ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
    ACCOUNT_TYPE_WORKSHOP,
    ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
    ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
    ASSIGNMENT_CANDIDATE_STATUS_EXPIRED,
    ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OTHER,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_UNCERTAIN,
    INCIDENT_PRIORITY_CRITICAL,
    INCIDENT_PRIORITY_HIGH,
    INCIDENT_PRIORITY_LOW,
    INCIDENT_PRIORITY_MEDIUM,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_PENDING,
    INCIDENT_STATUS_PUBLISHED,
    PROVIDER_TYPE_WORKSHOP,
    SERVICE_CODE_ACCIDENT_SUPPORT,
    SERVICE_CODE_BATTERY_JUMPSTART,
    SERVICE_CODE_ENGINE_DIAGNOSTIC,
    SERVICE_CODE_LOCKOUT_ASSISTANCE,
    SERVICE_CODE_OVERHEATING_ASSISTANCE,
    SERVICE_CODE_TIRE_CHANGE,
    SERVICE_CODE_TOWING,
    PUSH_EVENT_INCIDENT_ACCEPTED,
    PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
    AUDIT_EVENT_INCIDENT_ACCEPTED,
    AUDIT_EVENT_INCIDENT_PUBLISHED,

)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.assignment.models import IncidentAssignmentCandidate
from app.services.assignment.repository import AssignmentRepository
from app.services.assignment.schemas import (
    AssignmentActionResponse,
    AssignmentCandidateIncidentResponse,
    AssignmentCandidateMatchedServiceResponse,
    AssignmentCandidateProviderOwnerResponse,
    AssignmentCandidateProviderResponse,
    AssignmentCandidateResponse,
    AssignmentPublishResponse,
)
from app.services.auth.models import User
from app.services.catalog.models import ProviderService
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.services.audit.dispatcher import AuditEventDispatcher


class AssignmentService:
    def __init__(self, repository: AssignmentRepository) -> None:
        self.repository = repository

    def publish_incident_for_assignment(self, incident_id: str) -> AssignmentPublishResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.status in (
            INCIDENT_STATUS_ASSIGNED,
            INCIDENT_STATUS_IN_PROGRESS,
            INCIDENT_STATUS_COMPLETED,
            INCIDENT_STATUS_CANCELLED,
        ):
            raise ConflictException(
                "This incident cannot be published for assignment in its current status."
            )

        if incident.provider_id is not None:
            raise ConflictException("This incident is already linked to a provider.")

        used_category = (
            incident.suggested_category.strip().upper()
            if incident.suggested_category
            else incident.reported_category.strip().upper()
        )
        used_priority = (
            incident.suggested_priority.strip().upper()
            if incident.suggested_priority
            else incident.priority.strip().upper()
        )
        required_service_codes = self._map_incident_category_to_required_service_codes(used_category)

        provider_pool = self.repository.list_eligible_provider_pool()
        ranked_candidates = self._build_ranked_candidates(
            incident=incident,
            providers=provider_pool,
            used_category=used_category,
            used_priority=used_priority,
            required_service_codes=required_service_codes,
        )

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by a provider.")

            self.repository.delete_non_accepted_candidates_by_incident_id(incident_id)

            candidates_to_create = []
            for index, ranked_candidate in enumerate(ranked_candidates, start=1):
                candidate = IncidentAssignmentCandidate(
                    incident_id=locked_incident.id,
                    provider_id=ranked_candidate["provider"].id,
                    status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
                    recommendation_rank=index,
                    score=ranked_candidate["score"],
                    distance_km=ranked_candidate["distance_km"],
                    required_service_codes_json=required_service_codes,
                    matched_service_codes_json=ranked_candidate["matched_service_codes"],
                    rationale_json=ranked_candidate["rationale"],
                    provider_average_rating_snapshot=ranked_candidate["provider"].average_rating,
                    provider_available_capacity_snapshot=ranked_candidate["available_capacity"],
                    available_technicians_count_snapshot=ranked_candidate["available_technicians_count"],
                    published_at=datetime.now(timezone.utc),
                    responded_at=None,
                    expires_at=None,
                )
                candidates_to_create.append(candidate)

            locked_incident.status = INCIDENT_STATUS_PUBLISHED
            self.repository.save(locked_incident)
            self.repository.create_candidates(candidates_to_create)
            self.repository.commit()
            self._emit_audit_safely(
            actor_user_id=None,
            incident_id=str(locked_incident.id),
            provider_id=None,
            request_id=None,
            event_scope="DOMAIN",
            event_type=AUDIT_EVENT_INCIDENT_PUBLISHED,
            entity_type="INCIDENT",
            entity_id=str(locked_incident.id),
            payload_json={
                "used_category": used_category,
                "used_priority": used_priority,
                "required_service_codes": required_service_codes,
                "published_candidates_count": len(ranked_candidates),
            },
            )

        except Exception:
            self.repository.rollback()
            raise

        recommended_candidate = ranked_candidates[0] if ranked_candidates else None
        self._enqueue_notification_safely(
        lambda: self._enqueue_candidate_publication_notifications(incident_id)
        )


        return AssignmentPublishResponse(
            incident_id=str(incident.id),
            incident_status=INCIDENT_STATUS_PUBLISHED,
            used_category=used_category,
            used_priority=used_priority,
            required_service_codes=required_service_codes,
            published_candidates_count=len(ranked_candidates),
            recommended_candidate_id=None,
            recommended_provider_id=(
                str(recommended_candidate["provider"].id)
                if recommended_candidate is not None
                else None
            ),
        )

    def list_platform_candidates_for_incident(
        self,
        incident_id: str,
    ) -> list[AssignmentCandidateResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        candidates = self.repository.list_candidates_by_incident_id(incident_id)
        return [self._build_candidate_response(item) for item in candidates]

    def list_my_available_candidates(self, current_user: User) -> list[AssignmentCandidateResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        candidates = self.repository.list_available_candidates_for_provider(str(provider.id))
        visible_candidates = [
            candidate
            for candidate in candidates
            if candidate.incident.status == INCIDENT_STATUS_PUBLISHED
            and candidate.incident.provider_id is None
        ]
        return [self._build_candidate_response(item) for item in visible_candidates]

    def get_my_available_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentCandidateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        candidate = self.repository.get_candidate_by_id(candidate_id)
        if candidate is None:
            raise NotFoundException("Assignment candidate not found.")

        if str(candidate.provider_id) != str(provider.id):
            raise ForbiddenException("This assignment candidate does not belong to your provider.")

        if candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
            raise ConflictException("This assignment candidate is no longer available.")

        if candidate.incident.status != INCIDENT_STATUS_PUBLISHED or candidate.incident.provider_id is not None:
            raise ConflictException("This incident is no longer available for assignment.")

        return self._build_candidate_response(candidate)

    def accept_my_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentActionResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_candidate = self.repository.get_candidate_by_id_for_update(candidate_id)
            if locked_candidate is None:
                raise NotFoundException("Assignment candidate not found.")

            if str(locked_candidate.provider_id) != str(provider.id):
                raise ForbiddenException("This assignment candidate does not belong to your provider.")

            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            if locked_provider.available_capacity <= 0:
                raise ConflictException("Your provider has no available capacity for a new incident.")

            locked_incident = self.repository.get_incident_by_id_for_update(str(locked_candidate.incident_id))
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by another provider.")

            if locked_incident.status != INCIDENT_STATUS_PUBLISHED:
                raise ConflictException("This incident is not currently published for assignment.")

            if locked_candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
                raise ConflictException("This assignment candidate is no longer available.")

            locked_candidate.status = ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED
            locked_candidate.responded_at = now

            locked_incident.provider_id = locked_provider.id
            locked_incident.status = INCIDENT_STATUS_ASSIGNED
            locked_incident.assigned_at = now

            locked_provider.current_active_services += 1

            sibling_candidates = self.repository.list_available_candidates_by_incident_id_for_update(
                str(locked_incident.id)
            )

            for sibling in sibling_candidates:
                if str(sibling.id) == str(locked_candidate.id):
                    continue

                sibling.status = ASSIGNMENT_CANDIDATE_STATUS_EXPIRED
                sibling.responded_at = now
                existing_rationale = sibling.rationale_json or {}
                existing_rationale["closed_reason"] = "incident_taken_by_another_provider"
                sibling.rationale_json = existing_rationale
                self.repository.save(sibling)

            self.repository.save(locked_provider)
            self.repository.save(locked_candidate)
            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        self._enqueue_notification_safely(
        lambda: self._enqueue_incident_accepted_notification(str(locked_incident.id))
        )


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(locked_incident.id),
        provider_id=str(locked_provider.id),
        request_id=None,
        event_scope="DOMAIN",
        event_type=AUDIT_EVENT_INCIDENT_ACCEPTED,
        entity_type="INCIDENT",
        entity_id=str(locked_incident.id),
        payload_json={
            "candidate_id": str(locked_candidate.id),
            "provider_id": str(locked_provider.id),
            "incident_status": locked_incident.status,
        },
        )


        return AssignmentActionResponse(
            candidate_id=str(locked_candidate.id),
            candidate_status=locked_candidate.status,
            incident_id=str(locked_incident.id),
            incident_status=locked_incident.status,
            assigned_provider_id=str(locked_incident.provider_id) if locked_incident.provider_id else None,
            assigned_at=locked_incident.assigned_at,
        )

    def reject_my_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentActionResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_candidate = self.repository.get_candidate_by_id_for_update(candidate_id)
            if locked_candidate is None:
                raise NotFoundException("Assignment candidate not found.")

            if str(locked_candidate.provider_id) != str(provider.id):
                raise ForbiddenException("This assignment candidate does not belong to your provider.")

            locked_incident = self.repository.get_incident_by_id_for_update(str(locked_candidate.incident_id))
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by another provider.")

            if locked_incident.status != INCIDENT_STATUS_PUBLISHED:
                raise ConflictException("This incident is not currently published for assignment.")

            if locked_candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
                raise ConflictException("This assignment candidate is no longer available.")

            locked_candidate.status = ASSIGNMENT_CANDIDATE_STATUS_REJECTED
            locked_candidate.responded_at = now

            existing_rationale = locked_candidate.rationale_json or {}
            existing_rationale["provider_response"] = "rejected_by_provider"
            locked_candidate.rationale_json = existing_rationale

            self.repository.save(locked_candidate)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        return AssignmentActionResponse(
            candidate_id=str(locked_candidate.id),
            candidate_status=locked_candidate.status,
            incident_id=str(locked_incident.id),
            incident_status=locked_incident.status,
            assigned_provider_id=str(locked_incident.provider_id) if locked_incident.provider_id else None,
            assigned_at=locked_incident.assigned_at,
        )

    def _build_ranked_candidates(
        self,
        incident,
        providers,
        used_category: str,
        used_priority: str,
        required_service_codes: list[str],
    ) -> list[dict]:
        ranked_candidates: list[dict] = []

        for provider in providers:
            if not provider.is_active or not provider.is_available:
                continue

            available_capacity = provider.available_capacity
            if available_capacity <= 0:
                continue

            available_technicians_count = sum(
                1 for technician in provider.technicians
                if technician.is_active and technician.is_available
            )

            if provider.provider_type == PROVIDER_TYPE_WORKSHOP and available_technicians_count <= 0:
                continue

            active_mobile_services = self._get_active_mobile_emergency_services(provider.provider_services)
            if not active_mobile_services:
                continue

            matched_services = self._match_services_for_incident(
                active_provider_services=active_mobile_services,
                used_category=used_category,
                required_service_codes=required_service_codes,
            )
            if not matched_services:
                continue

            if not self._provider_type_is_allowed(provider.provider_type, required_service_codes):
                continue

            distance_km = self._calculate_distance_km(
                incident_latitude=incident.incident_latitude,
                incident_longitude=incident.incident_longitude,
                provider_latitude=provider.base_latitude,
                provider_longitude=provider.base_longitude,
            )

            score, rationale = self._calculate_candidate_score(
                provider=provider,
                matched_services=matched_services,
                used_priority=used_priority,
                distance_km=distance_km,
                available_capacity=available_capacity,
                available_technicians_count=available_technicians_count,
            )

            ranked_candidates.append(
                {
                    "provider": provider,
                    "score": score,
                    "distance_km": distance_km,
                    "matched_services": matched_services,
                    "matched_service_codes": [item.service_catalog_item.code for item in matched_services],
                    "available_capacity": available_capacity,
                    "available_technicians_count": available_technicians_count,
                    "rationale": rationale,
                }
            )

        ranked_candidates.sort(
            key=lambda item: (
                -item["score"],
                item["distance_km"] if item["distance_km"] is not None else 999999,
                -item["provider"].average_rating,
                item["provider"].created_at,
            )
        )

        return ranked_candidates

    def _get_active_mobile_emergency_services(
        self,
        provider_services: list[ProviderService],
    ) -> list[ProviderService]:
        active_services: list[ProviderService] = []

        for provider_service in provider_services:
            catalog_item = provider_service.service_catalog_item
            if catalog_item is None:
                continue
            if not provider_service.is_active:
                continue
            if not catalog_item.is_active:
                continue
            if not provider_service.is_mobile_service_enabled:
                continue
            if not provider_service.is_emergency_service_enabled:
                continue

            active_services.append(provider_service)

        return active_services

    def _match_services_for_incident(
        self,
        active_provider_services: list[ProviderService],
        used_category: str,
        required_service_codes: list[str],
    ) -> list[ProviderService]:
        if required_service_codes:
            exact_matches = [
                item
                for item in active_provider_services
                if item.service_catalog_item.code in required_service_codes
            ]
            if exact_matches:
                return exact_matches

        if used_category in (
            INCIDENT_CATEGORY_OTHER,
            INCIDENT_CATEGORY_UNCERTAIN,
        ):
            return active_provider_services[:3]

        category_matches = [
            item
            for item in active_provider_services
            if item.service_catalog_item.category == used_category
        ]
        return category_matches

    def _provider_type_is_allowed(
        self,
        provider_type: str,
        required_service_codes: list[str],
    ) -> bool:
        if SERVICE_CODE_TOWING in required_service_codes:
            return provider_type in (ACCOUNT_TYPE_WORKSHOP,)

        return provider_type in (
            ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
            ACCOUNT_TYPE_WORKSHOP,
        )

    def _map_incident_category_to_required_service_codes(self, category: str) -> list[str]:
        mapping = {
            INCIDENT_CATEGORY_BATTERY: [SERVICE_CODE_BATTERY_JUMPSTART],
            INCIDENT_CATEGORY_TIRE: [SERVICE_CODE_TIRE_CHANGE],
            INCIDENT_CATEGORY_LOCKOUT: [SERVICE_CODE_LOCKOUT_ASSISTANCE],
            INCIDENT_CATEGORY_OVERHEATING: [SERVICE_CODE_OVERHEATING_ASSISTANCE],
            INCIDENT_CATEGORY_ENGINE: [SERVICE_CODE_ENGINE_DIAGNOSTIC],
            INCIDENT_CATEGORY_ACCIDENT: [SERVICE_CODE_ACCIDENT_SUPPORT, SERVICE_CODE_TOWING],
            INCIDENT_CATEGORY_OTHER: [],
            INCIDENT_CATEGORY_UNCERTAIN: [],
        }

        return mapping.get(category, [])

    def _calculate_candidate_score(
        self,
        provider,
        matched_services: list[ProviderService],
        used_priority: str,
        distance_km: float | None,
        available_capacity: int,
        available_technicians_count: int,
    ) -> tuple[float, dict]:
        rating_score = float(provider.average_rating) * 12.0
        capacity_score = min(available_capacity, 5) * 6.0
        technician_score = min(available_technicians_count, 5) * 3.0

        if distance_km is None:
            distance_score = 8.0
        else:
            if used_priority == INCIDENT_PRIORITY_CRITICAL:
                distance_score = max(0.0, 50.0 - (distance_km * 3.2))
            elif used_priority == INCIDENT_PRIORITY_HIGH:
                distance_score = max(0.0, 42.0 - (distance_km * 2.7))
            elif used_priority == INCIDENT_PRIORITY_MEDIUM:
                distance_score = max(0.0, 34.0 - (distance_km * 2.0))
            else:
                distance_score = max(0.0, 26.0 - (distance_km * 1.5))

        matched_service_codes = [item.service_catalog_item.code for item in matched_services]
        if SERVICE_CODE_TOWING in matched_service_codes:
            service_score = 26.0
        elif matched_services:
            service_score = 20.0
        else:
            service_score = 0.0

        total_score = rating_score + capacity_score + technician_score + distance_score + service_score

        rationale = {
            "rating_score": round(rating_score, 2),
            "capacity_score": round(capacity_score, 2),
            "technician_score": round(technician_score, 2),
            "distance_score": round(distance_score, 2),
            "service_score": round(service_score, 2),
            "matched_service_codes": matched_service_codes,
            "distance_km": round(distance_km, 2) if distance_km is not None else None,
            "priority_used": used_priority,
        }

        return round(total_score, 2), rationale

    def _calculate_distance_km(
        self,
        incident_latitude: float | None,
        incident_longitude: float | None,
        provider_latitude: float | None,
        provider_longitude: float | None,
    ) -> float | None:
        if (
            incident_latitude is None
            or incident_longitude is None
            or provider_latitude is None
            or provider_longitude is None
        ):
            return None

        earth_radius_km = 6371.0

        lat1 = math.radians(incident_latitude)
        lon1 = math.radians(incident_longitude)
        lat2 = math.radians(provider_latitude)
        lon2 = math.radians(provider_longitude)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = (
            math.sin(delta_lat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return round(earth_radius_km * c, 2)

    def _build_candidate_response(
        self,
        candidate: IncidentAssignmentCandidate,
    ) -> AssignmentCandidateResponse:
        provider = candidate.provider
        owner_user = provider.owner_user

        available_technicians_count = sum(
            1 for technician in provider.technicians
            if technician.is_active and technician.is_available
        )

        matched_services = [
            provider_service
            for provider_service in provider.provider_services
            if provider_service.service_catalog_item.code in (candidate.matched_service_codes_json or [])
        ]

        provider_payload = AssignmentCandidateProviderResponse(
            id=str(provider.id),
            provider_type=provider.provider_type,
            business_name=provider.business_name,
            city=provider.city,
            contact_phone=provider.contact_phone,
            average_rating=provider.average_rating,
            available_capacity=provider.available_capacity,
            available_technicians_count=available_technicians_count,
            base_latitude=provider.base_latitude,
            base_longitude=provider.base_longitude,
            owner_user=AssignmentCandidateProviderOwnerResponse(
                id=str(owner_user.id),
                email=owner_user.email,
                first_name=owner_user.first_name,
                last_name=owner_user.last_name,
                full_name=owner_user.full_name,
                phone_number=owner_user.phone_number,
            ),
            matched_services=[
                AssignmentCandidateMatchedServiceResponse(
                    code=item.service_catalog_item.code,
                    category=item.service_catalog_item.category,
                    title=item.effective_title,
                )
                for item in matched_services
            ],
        )

        incident = candidate.incident
        incident_payload = AssignmentCandidateIncidentResponse(
            id=str(incident.id),
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            ai_summary_status=incident.ai_summary_status,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
        )

        return AssignmentCandidateResponse(
            id=str(candidate.id),
            incident_id=str(candidate.incident_id),
            provider_id=str(candidate.provider_id),
            status=candidate.status,
            recommendation_rank=candidate.recommendation_rank,
            score=round(candidate.score, 2),
            distance_km=round(candidate.distance_km, 2) if candidate.distance_km is not None else None,
            required_service_codes=list(candidate.required_service_codes_json or []),
            matched_service_codes=list(candidate.matched_service_codes_json or []),
            rationale=candidate.rationale_json,
            provider_average_rating_snapshot=candidate.provider_average_rating_snapshot,
            provider_available_capacity_snapshot=candidate.provider_available_capacity_snapshot,
            available_technicians_count_snapshot=candidate.available_technicians_count_snapshot,
            published_at=candidate.published_at,
            responded_at=candidate.responded_at,
            expires_at=candidate.expires_at,
            provider=provider_payload,
            incident=incident_payload,
        )

    def _enqueue_candidate_publication_notifications(self, incident_id: str) -> None:
        dispatcher = PushNotificationDispatcher(self.repository.db)
        candidates = self.repository.list_candidates_by_incident_id(incident_id)

        for candidate in candidates:
            if candidate.provider is None or candidate.provider.owner_user is None:
                continue

        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
            recipient_user_ids=[str(candidate.provider.owner_user.id)],
            title="Nueva solicitud disponible",
            body=(
                f"Hay una nueva solicitud de auxilio: {candidate.incident.title}. "
                "Revísala y decide si deseas aceptarla."
            ),
            data={
                "event_code": PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
                "incident_id": str(candidate.incident_id),
                "candidate_id": str(candidate.id),
                "reported_category": candidate.incident.reported_category,
                "priority": candidate.incident.priority,
                "status": candidate.incident.status,
            },
        )


    def _enqueue_incident_accepted_notification(self, incident_id: str) -> None:
        dispatcher = PushNotificationDispatcher(self.repository.db)
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_ACCEPTED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Solicitud tomada",
            body=(
                f"{incident.provider.business_name} tomó tu solicitud y está preparando la atención."
            ),
            data={
                "event_code": PUSH_EVENT_INCIDENT_ACCEPTED,
                "incident_id": str(incident.id),
                "provider_id": str(incident.provider_id),
                "provider_name": incident.provider.business_name,
                "status": incident.status,
            },
        )


    def _enqueue_notification_safely(self, callback) -> None:
        try:
            callback()
        except Exception:
            return


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        request_id: str | None,
        event_scope: str,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
            actor_user_id=actor_user_id,
            incident_id=incident_id,
            provider_id=provider_id,
            request_id=request_id,
            event_scope=event_scope,
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            outcome="SUCCESS",
            payload_json=payload_json,
            )
        except Exception:
            return
