from datetime import datetime, timezone

from app.common.constants import (
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    PROVIDER_TYPE_WORKSHOP,
    TRACKING_SOURCE_PROVIDER_SELF,
    TRACKING_SOURCE_TECHNICIAN,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.integrations.routing.base import RouteCalculationRequest, RoutingProvider
from app.integrations.routing.null_provider import NullRoutingProvider
from app.services.auth.models import User
from app.services.tracking.models import IncidentResponderLocationPing
from app.services.tracking.repository import TrackingRepository
from app.services.tracking.schemas import (
    IncidentLiveTrackingResponse,
    IncidentTrackingClientSummaryResponse,
    IncidentTrackingProviderSummaryResponse,
    IncidentTrackingResponderPositionResponse,
    IncidentTrackingRouteResponse,
    IncidentTrackingTechnicianSummaryResponse,
    LocationPingRequest,
    TrackingHistoryItemResponse,
)


class TrackingService:
    def __init__(
        self,
        repository: TrackingRepository,
        routing_provider: RoutingProvider,
    ) -> None:
        self.repository = repository
        self.routing_provider = routing_provider

    def report_my_location(
        self,
        current_user: User,
        incident_id: str,
        payload: LocationPingRequest,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException("Tracking is only available for assigned or active incidents.")

            source_type = TRACKING_SOURCE_PROVIDER_SELF
            technician = None

            if provider.provider_type == PROVIDER_TYPE_WORKSHOP and locked_incident.assigned_technician_id is not None:
                technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )
                if technician is None:
                    raise NotFoundException("Assigned technician not found.")

                if payload.technician_id and str(payload.technician_id) != str(technician.id):
                    raise ForbiddenException("The provided technician_id does not match the incident technician.")

                technician.current_latitude = payload.latitude
                technician.current_longitude = payload.longitude
                self.repository.save(technician)
                source_type = TRACKING_SOURCE_TECHNICIAN
            else:
                if payload.technician_id:
                    raise ConflictException("Independent providers cannot report location using technician_id.")

            ping = IncidentResponderLocationPing(
                incident_id=locked_incident.id,
                provider_id=provider.id,
                technician_id=technician.id if technician is not None else None,
                source_type=source_type,
                latitude=payload.latitude,
                longitude=payload.longitude,
                accuracy_meters=payload.accuracy_meters,
                recorded_at=now,
            )

            self.repository.create_ping(ping)

            locked_incident.responder_last_latitude = payload.latitude
            locked_incident.responder_last_longitude = payload.longitude
            locked_incident.responder_last_source_type = source_type
            locked_incident.responder_last_recorded_at = now

            self._apply_route_calculation(
                incident=locked_incident,
                origin_latitude=payload.latitude,
                origin_longitude=payload.longitude,
            )

            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def refresh_my_route(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException("Route refresh is only available for assigned or active incidents.")

            origin_latitude, origin_longitude = self._resolve_origin_coordinates(
                incident=locked_incident,
                provider=provider,
            )

            self._apply_route_calculation(
                incident=locked_incident,
                origin_latitude=origin_latitude,
                origin_longitude=origin_longitude,
            )

            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def get_provider_live_tracking(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_live_response(incident)

    def get_client_live_tracking(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        return self._build_live_response(incident)

    def get_platform_live_tracking(
        self,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def list_provider_tracking_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def list_client_tracking_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def list_platform_tracking_history(
        self,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def _resolve_origin_coordinates(self, incident, provider) -> tuple[float, float]:
        if incident.responder_last_latitude is not None and incident.responder_last_longitude is not None:
            return incident.responder_last_latitude, incident.responder_last_longitude

        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            if technician.current_latitude is not None and technician.current_longitude is not None:
                return technician.current_latitude, technician.current_longitude

        if provider.base_latitude is not None and provider.base_longitude is not None:
            return provider.base_latitude, provider.base_longitude

        raise ConflictException("No origin coordinates are available to calculate the route.")

    def _apply_route_calculation(
        self,
        incident,
        origin_latitude: float,
        origin_longitude: float,
    ) -> None:
        if incident.incident_latitude is None or incident.incident_longitude is None:
            raise ConflictException("The incident does not have coordinates to calculate a route.")

        route_request = RouteCalculationRequest(
            origin_latitude=origin_latitude,
            origin_longitude=origin_longitude,
            destination_latitude=incident.incident_latitude,
            destination_longitude=incident.incident_longitude,
            profile=None,
        )

        try:
            route_result = self.routing_provider.calculate_route(route_request)
            incident.route_error_message = None
            incident.route_provider_name = self.routing_provider.provider_name
        except Exception as exc:
            fallback_provider = NullRoutingProvider()
            route_result = fallback_provider.calculate_route(route_request)
            incident.route_error_message = f"Primary routing provider failed: {str(exc)}"
            incident.route_provider_name = fallback_provider.provider_name

        incident.route_distance_meters = route_result.distance_meters
        incident.route_duration_seconds = route_result.duration_seconds
        incident.route_eta_seconds = route_result.duration_seconds
        incident.route_polyline = route_result.polyline
        incident.route_last_calculated_at = datetime.now(timezone.utc)

    def _build_live_response(self, incident) -> IncidentLiveTrackingResponse:
        provider_payload = None
        if incident.provider is not None:
            provider = incident.provider
            provider_payload = IncidentTrackingProviderSummaryResponse(
                id=str(provider.id),
                provider_type=provider.provider_type,
                business_name=provider.business_name,
                contact_phone=provider.contact_phone,
                city=provider.city,
                average_rating=provider.average_rating,
            )

        technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            technician_payload = IncidentTrackingTechnicianSummaryResponse(
                id=str(technician.id),
                provider_id=str(technician.provider_id),
                first_name=technician.first_name,
                last_name=technician.last_name,
                full_name=technician.full_name,
                phone_number=technician.phone_number,
                specialty=technician.specialty,
                is_active=technician.is_active,
                is_available=technician.is_available,
            )

        client_user = incident.client_user
        client_payload = IncidentTrackingClientSummaryResponse(
            id=str(client_user.id),
            email=client_user.email,
            first_name=client_user.first_name,
            last_name=client_user.last_name,
            full_name=client_user.full_name,
            phone_number=client_user.phone_number,
        )

        route_distance_km = (
            round(incident.route_distance_meters / 1000.0, 2)
            if incident.route_distance_meters is not None
            else None
        )
        eta_minutes = (
            int(round(incident.route_eta_seconds / 60))
            if incident.route_eta_seconds is not None
            else None
        )

        return IncidentLiveTrackingResponse(
            incident_id=str(incident.id),
            status=incident.status,
            priority=incident.priority,
            title=incident.title,
            description=incident.description,
            address_reference=incident.address_reference,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            provider=provider_payload,
            assigned_technician=technician_payload,
            client_user=client_payload,
            responder_position=IncidentTrackingResponderPositionResponse(
                latitude=incident.responder_last_latitude,
                longitude=incident.responder_last_longitude,
                source_type=incident.responder_last_source_type,
                recorded_at=incident.responder_last_recorded_at,
            ),
            route=IncidentTrackingRouteResponse(
                provider_name=incident.route_provider_name,
                distance_meters=incident.route_distance_meters,
                distance_km=route_distance_km,
                duration_seconds=incident.route_duration_seconds,
                eta_seconds=incident.route_eta_seconds,
                eta_minutes=eta_minutes,
                polyline=incident.route_polyline,
                last_calculated_at=incident.route_last_calculated_at,
                error_message=incident.route_error_message,
            ),
        )

    def _build_history_item(self, ping: IncidentResponderLocationPing) -> TrackingHistoryItemResponse:
        provider_business_name = ping.provider.business_name if ping.provider is not None else None
        technician_full_name = ping.technician.full_name if ping.technician is not None else None

        return TrackingHistoryItemResponse(
            id=str(ping.id),
            incident_id=str(ping.incident_id),
            provider_id=str(ping.provider_id) if ping.provider_id else None,
            technician_id=str(ping.technician_id) if ping.technician_id else None,
            source_type=ping.source_type,
            latitude=ping.latitude,
            longitude=ping.longitude,
            accuracy_meters=ping.accuracy_meters,
            recorded_at=ping.recorded_at,
            provider_business_name=provider_business_name,
            technician_full_name=technician_full_name,
        )
