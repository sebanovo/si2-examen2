from datetime import datetime, timezone

from app.common.constants import (
    INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
    INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
    INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    TRACKING_SOURCE_TECHNICIAN,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.integrations.routing.base import RouteCalculationRequest, RoutingProvider
from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.operations.models import IncidentOperationEvent
from app.services.providers.models import Provider, Technician
from app.services.technician_mobile.repository import TechnicianMobileRepository
from app.services.technician_mobile.schemas import (
    TechnicianAvailabilityUpdateRequest,
    TechnicianClientSummaryResponse,
    TechnicianCompleteIncidentRequest,
    TechnicianIncidentResponse,
    TechnicianLocationPingRequest,
    TechnicianLocationPingResponse,
    TechnicianOperationNoteRequest,
    TechnicianProfileResponse,
    TechnicianProviderSummaryResponse,
    TechnicianUserSummaryResponse,
    TechnicianVehicleSummaryResponse,
)
from app.services.tracking.models import IncidentResponderLocationPing


class TechnicianMobileService:
    def __init__(
        self,
        repository: TechnicianMobileRepository,
        routing_provider: RoutingProvider,
    ) -> None:
        self.repository = repository
        self.routing_provider = routing_provider

    def get_my_profile(self, current_user: User) -> TechnicianProfileResponse:
        technician = self._require_my_technician(current_user)
        return self._build_technician_profile_response(technician)

    def update_my_availability(
        self,
        current_user: User,
        payload: TechnicianAvailabilityUpdateRequest,
    ) -> TechnicianProfileResponse:
        try:
            technician = self.repository.get_technician_by_user_id_for_update(str(current_user.id))
            if technician is None:
                raise NotFoundException("No technician profile is linked to this account.")

            if not technician.is_active:
                raise ConflictException("Inactive technicians cannot update availability.")

            technician.is_available = payload.is_available

            if payload.current_latitude is not None:
                technician.current_latitude = payload.current_latitude

            if payload.current_longitude is not None:
                technician.current_longitude = payload.current_longitude

            self.repository.save(technician)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        technician = self._require_my_technician(current_user)
        return self._build_technician_profile_response(technician)

    def list_my_incidents(
        self,
        current_user: User,
        active_only: bool = True,
        limit: int = 50,
        offset: int = 0,
    ) -> list[TechnicianIncidentResponse]:
        technician = self._require_my_technician(current_user)

        incidents = self.repository.list_my_assigned_incidents(
            technician_id=str(technician.id),
            active_only=active_only,
            limit=limit,
            offset=offset,
        )

        return [self._build_incident_response(incident) for incident in incidents]

    def get_my_incident(
        self,
        current_user: User,
        incident_id: str,
    ) -> TechnicianIncidentResponse:
        technician = self._require_my_technician(current_user)
        incident = self._require_assigned_incident(technician, incident_id)
        return self._build_incident_response(incident)

    def mark_en_route(
        self,
        current_user: User,
        incident_id: str,
        payload: TechnicianOperationNoteRequest,
    ) -> TechnicianIncidentResponse:
        return self._transition_incident(
            current_user=current_user,
            incident_id=incident_id,
            allowed_statuses=(INCIDENT_STATUS_ASSIGNED, INCIDENT_STATUS_EN_ROUTE),
            target_status=INCIDENT_STATUS_EN_ROUTE,
            event_type="TECHNICIAN_EN_ROUTE",
            note=payload.note,
            update_timestamps={"en_route_at": datetime.now(timezone.utc)},
        )

    def mark_arrived(
        self,
        current_user: User,
        incident_id: str,
        payload: TechnicianOperationNoteRequest,
    ) -> TechnicianIncidentResponse:
        return self._transition_incident(
            current_user=current_user,
            incident_id=incident_id,
            allowed_statuses=(INCIDENT_STATUS_ASSIGNED, INCIDENT_STATUS_EN_ROUTE, INCIDENT_STATUS_ON_SITE),
            target_status=INCIDENT_STATUS_ON_SITE,
            event_type=INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
            note=payload.note,
            update_timestamps={"arrived_at": datetime.now(timezone.utc)},
        )

    def start_service(
        self,
        current_user: User,
        incident_id: str,
        payload: TechnicianOperationNoteRequest,
    ) -> TechnicianIncidentResponse:
        return self._transition_incident(
            current_user=current_user,
            incident_id=incident_id,
            allowed_statuses=(INCIDENT_STATUS_ON_SITE, INCIDENT_STATUS_IN_PROGRESS),
            target_status=INCIDENT_STATUS_IN_PROGRESS,
            event_type=INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
            note=payload.note,
            update_timestamps={"started_at": datetime.now(timezone.utc)},
        )

    def complete_service(
        self,
        current_user: User,
        incident_id: str,
        payload: TechnicianCompleteIncidentRequest,
    ) -> TechnicianIncidentResponse:
        note = payload.note or payload.completion_summary

        return self._transition_incident(
            current_user=current_user,
            incident_id=incident_id,
            allowed_statuses=(INCIDENT_STATUS_ON_SITE, INCIDENT_STATUS_IN_PROGRESS),
            target_status=INCIDENT_STATUS_COMPLETED,
            event_type=INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
            note=note,
            update_timestamps={"completed_at": datetime.now(timezone.utc)},
            payload_json={
                "completion_summary": payload.completion_summary,
            },
            release_technician=True,
        )

    def report_my_location(
        self,
        current_user: User,
        incident_id: str,
        payload: TechnicianLocationPingRequest,
    ) -> TechnicianLocationPingResponse:
        now = datetime.now(timezone.utc)

        try:
            technician = self.repository.get_technician_by_user_id_for_update(str(current_user.id))
            if technician is None:
                raise NotFoundException("No technician profile is linked to this account.")

            if not technician.is_active:
                raise ConflictException("Inactive technicians cannot report location.")

            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            self._validate_incident_belongs_to_technician(incident, technician)

            if incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException("Location can only be reported for assigned or active incidents.")

            technician.current_latitude = payload.latitude
            technician.current_longitude = payload.longitude
            self.repository.save(technician)

            ping = IncidentResponderLocationPing(
                incident_id=incident.id,
                provider_id=technician.provider_id,
                technician_id=technician.id,
                source_type=TRACKING_SOURCE_TECHNICIAN,
                latitude=payload.latitude,
                longitude=payload.longitude,
                accuracy_meters=payload.accuracy_meters,
                recorded_at=now,
            )
            self.repository.create_location_ping(ping)

            incident.responder_last_latitude = payload.latitude
            incident.responder_last_longitude = payload.longitude
            incident.responder_last_source_type = TRACKING_SOURCE_TECHNICIAN
            incident.responder_last_recorded_at = now

            self._apply_route_calculation_safely(
                incident=incident,
                origin_latitude=payload.latitude,
                origin_longitude=payload.longitude,
            )

            self.repository.save(incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found after location update.")

        return TechnicianLocationPingResponse(
            incident_id=str(incident.id),
            technician_id=str(technician.id),
            provider_id=str(technician.provider_id),
            latitude=payload.latitude,
            longitude=payload.longitude,
            accuracy_meters=payload.accuracy_meters,
            recorded_at=now,
            route_provider_name=incident.route_provider_name,
            route_distance_meters=incident.route_distance_meters,
            route_duration_seconds=incident.route_duration_seconds,
            route_eta_seconds=incident.route_eta_seconds,
            route_polyline=incident.route_polyline,
        )

    def _transition_incident(
        self,
        *,
        current_user: User,
        incident_id: str,
        allowed_statuses: tuple[str, ...],
        target_status: str,
        event_type: str,
        note: str | None,
        update_timestamps: dict[str, datetime],
        payload_json: dict | None = None,
        release_technician: bool = False,
    ) -> TechnicianIncidentResponse:
        try:
            technician = self.repository.get_technician_by_user_id_for_update(str(current_user.id))
            if technician is None:
                raise NotFoundException("No technician profile is linked to this account.")

            if not technician.is_active:
                raise ConflictException("Inactive technicians cannot update incident operations.")

            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            self._validate_incident_belongs_to_technician(incident, technician)

            if incident.status not in allowed_statuses:
                raise ConflictException(
                    f"Incident cannot move from {incident.status} to {target_status}."
                )

            previous_status = incident.status
            incident.status = target_status

            for field_name, value in update_timestamps.items():
                current_value = getattr(incident, field_name, None)
                if current_value is None:
                    setattr(incident, field_name, value)

            if target_status == INCIDENT_STATUS_EN_ROUTE:
                technician.is_available = False

            if release_technician:
                technician.is_available = True

                provider = technician.provider
                if provider is not None and provider.current_active_services > 0:
                    provider.current_active_services -= 1
                    self.repository.save(provider)

            event = IncidentOperationEvent(
                incident_id=incident.id,
                provider_id=technician.provider_id,
                technician_id=technician.id,
                actor_user_id=current_user.id,
                event_type=event_type,
                from_status=previous_status,
                to_status=target_status,
                note=self._normalize_optional_text(note),
                payload_json=payload_json,
            )

            self.repository.create_operation_event(event)
            self.repository.save(technician)
            self.repository.save(incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found after operation update.")

        return self._build_incident_response(incident)

    def _require_my_technician(self, current_user: User) -> Technician:
        technician = self.repository.get_technician_by_user_id(str(current_user.id))
        if technician is None:
            raise NotFoundException("No technician profile is linked to this account.")

        return technician

    def _require_assigned_incident(
        self,
        technician: Technician,
        incident_id: str,
    ) -> Incident:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        self._validate_incident_belongs_to_technician(incident, technician)

        return incident

    def _validate_incident_belongs_to_technician(
        self,
        incident: Incident,
        technician: Technician,
    ) -> None:
        if incident.assigned_technician_id is None:
            raise ForbiddenException("This incident does not have an assigned technician.")

        if str(incident.assigned_technician_id) != str(technician.id):
            raise ForbiddenException("This incident is not assigned to the authenticated technician.")

        if incident.provider_id is None or str(incident.provider_id) != str(technician.provider_id):
            raise ForbiddenException("This incident does not belong to the technician provider.")

    def _apply_route_calculation_safely(
        self,
        *,
        incident: Incident,
        origin_latitude: float,
        origin_longitude: float,
    ) -> None:
        if incident.incident_latitude is None or incident.incident_longitude is None:
            return

        try:
            route_result = self.routing_provider.calculate_route(
                RouteCalculationRequest(
                    origin_latitude=origin_latitude,
                    origin_longitude=origin_longitude,
                    destination_latitude=incident.incident_latitude,
                    destination_longitude=incident.incident_longitude,
                )
            )

            incident.route_provider_name = self.routing_provider.provider_name
            incident.route_distance_meters = route_result.distance_meters
            incident.route_duration_seconds = route_result.duration_seconds
            incident.route_eta_seconds = route_result.duration_seconds
            incident.route_polyline = route_result.polyline
            incident.route_last_calculated_at = datetime.now(timezone.utc)
            incident.route_error_message = None
        except Exception as exc:
            incident.route_error_message = str(exc)

    def _build_incident_response(self, incident: Incident) -> TechnicianIncidentResponse:
        client_payload = None
        if incident.client_user is not None:
            client_payload = TechnicianClientSummaryResponse(
                id=str(incident.client_user.id),
                full_name=incident.client_user.full_name,
                phone_number=incident.client_user.phone_number,
            )

        vehicle_payload = None
        if incident.vehicle is not None:
            vehicle_payload = TechnicianVehicleSummaryResponse(
                id=str(incident.vehicle.id),
                plate_number=incident.vehicle.plate_number,
                vehicle_type=incident.vehicle.vehicle_type,
                brand=incident.vehicle.brand,
                model=incident.vehicle.model,
                color=incident.vehicle.color,
            )

        provider_payload = None
        if incident.provider is not None:
            provider_payload = self._build_provider_summary_response(incident.provider)

        technician_payload = None
        if incident.assigned_technician is not None:
            technician_payload = self._build_technician_profile_response(
                incident.assigned_technician
            )

        return TechnicianIncidentResponse(
            id=str(incident.id),
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            client_contact_phone_snapshot=incident.client_contact_phone_snapshot,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            requested_at=incident.requested_at,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            route_provider_name=incident.route_provider_name,
            route_distance_meters=incident.route_distance_meters,
            route_duration_seconds=incident.route_duration_seconds,
            route_eta_seconds=incident.route_eta_seconds,
            route_polyline=incident.route_polyline,
            route_last_calculated_at=incident.route_last_calculated_at,
            client=client_payload,
            vehicle=vehicle_payload,
            provider=provider_payload,
            technician=technician_payload,
        )

    def _build_technician_profile_response(
        self,
        technician: Technician,
    ) -> TechnicianProfileResponse:
        user_payload = None
        if technician.user is not None:
            user_payload = TechnicianUserSummaryResponse(
                id=str(technician.user.id),
                email=technician.user.email,
                first_name=technician.user.first_name,
                last_name=technician.user.last_name,
                full_name=technician.user.full_name,
                phone_number=technician.user.phone_number,
            )

        provider_payload = None
        if technician.provider is not None:
            provider_payload = self._build_provider_summary_response(technician.provider)

        return TechnicianProfileResponse(
            id=str(technician.id),
            user_id=str(technician.user_id) if technician.user_id else None,
            provider_id=str(technician.provider_id),
            first_name=technician.first_name,
            last_name=technician.last_name,
            full_name=technician.full_name,
            phone_number=technician.phone_number,
            specialty=technician.specialty,
            is_active=technician.is_active,
            is_available=technician.is_available,
            current_latitude=technician.current_latitude,
            current_longitude=technician.current_longitude,
            created_at=technician.created_at,
            updated_at=technician.updated_at,
            user=user_payload,
            provider=provider_payload,
        )

    def _build_provider_summary_response(
        self,
        provider: Provider,
    ) -> TechnicianProviderSummaryResponse:
        return TechnicianProviderSummaryResponse(
            id=str(provider.id),
            business_name=provider.business_name,
            provider_type=provider.provider_type,
            contact_phone=provider.contact_phone,
            average_rating=provider.average_rating,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None