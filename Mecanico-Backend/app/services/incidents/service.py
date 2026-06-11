from datetime import datetime, timezone

from app.common.constants import (
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_IN_REVIEW,
    INCIDENT_STATUS_PENDING,
    PROCESSING_STATUS_NOT_REQUESTED,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.incidents.repository import IncidentsRepository
from app.services.incidents.schemas import (
    CreateIncidentRequest,
    IncidentClientSummaryResponse,
    IncidentProviderSummaryResponse,
    IncidentResponse,
    IncidentTechnicianSummaryResponse,
    IncidentVehicleSummaryResponse,
    UpdateOwnPendingIncidentRequest,
)


class IncidentsService:
    def __init__(self, repository: IncidentsRepository) -> None:
        self.repository = repository

    def create_own_incident(
        self,
        current_user: User,
        payload: CreateIncidentRequest,
    ) -> IncidentResponse:
        vehicle = self.repository.get_vehicle_by_id(payload.vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        if not vehicle.is_active:
            raise ConflictException("The selected vehicle is inactive.")

        new_incident = Incident(
            client_user_id=current_user.id,
            vehicle_id=vehicle.id,
            provider_id=None,
            assigned_technician_id=None,
            dispatch_mode=None,
            status=INCIDENT_STATUS_PENDING,
            priority=payload.priority,
            reported_category=payload.reported_category,
            title=payload.title.strip(),
            description=payload.description.strip(),
            client_contact_phone_snapshot=current_user.phone_number,
            incident_latitude=payload.incident_latitude,
            incident_longitude=payload.incident_longitude,
            address_reference=payload.address_reference.strip() if payload.address_reference else None,
            estimated_price_min=None,
            estimated_price_max=None,
            ai_summary_status=PROCESSING_STATUS_NOT_REQUESTED,
            summary_provider_name=None,
            structured_summary=None,
            suggested_category=None,
            suggested_priority=None,
            requires_more_information=False,
            summary_processed_at=None,
            summary_error_message=None,
            responder_last_latitude=None,
            responder_last_longitude=None,
            responder_last_source_type=None,
            responder_last_recorded_at=None,
            route_provider_name=None,
            route_distance_meters=None,
            route_duration_seconds=None,
            route_eta_seconds=None,
            route_polyline=None,
            route_last_calculated_at=None,
            route_error_message=None,
        )

        created_incident = self.repository.create_incident(new_incident)
        return self._build_incident_response(created_incident)

    def list_own_incidents(self, current_user: User) -> list[IncidentResponse]:
        incidents = self.repository.list_incidents_by_client_user_id(str(current_user.id))
        return [self._build_incident_response(item) for item in incidents]

    def get_own_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        return self._build_incident_response(incident)

    def update_own_pending_incident(
        self,
        current_user: User,
        incident_id: str,
        payload: UpdateOwnPendingIncidentRequest,
    ) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        if incident.status not in (INCIDENT_STATUS_PENDING, INCIDENT_STATUS_IN_REVIEW):
            raise ConflictException("Only pending or in-review incidents can be updated by the client.")

        if payload.reported_category is not None:
            incident.reported_category = payload.reported_category

        if payload.priority is not None:
            incident.priority = payload.priority

        if payload.title is not None:
            incident.title = payload.title.strip()

        if payload.description is not None:
            incident.description = payload.description.strip()

        if payload.incident_latitude is not None:
            incident.incident_latitude = payload.incident_latitude

        if payload.incident_longitude is not None:
            incident.incident_longitude = payload.incident_longitude

        if payload.address_reference is not None:
            cleaned_value = payload.address_reference.strip()
            incident.address_reference = cleaned_value or None

        updated_incident = self.repository.save_incident(incident)
        return self._build_incident_response(updated_incident)

    def cancel_own_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        if incident.status not in (INCIDENT_STATUS_PENDING, INCIDENT_STATUS_IN_REVIEW):
            raise ConflictException("Only pending or in-review incidents can be cancelled by the client.")

        incident.status = INCIDENT_STATUS_CANCELLED
        incident.cancelled_at = datetime.now(timezone.utc)

        updated_incident = self.repository.save_incident(incident)
        return self._build_incident_response(updated_incident)

    def list_all_incidents(self, limit: int = 50, offset: int = 0) -> list[IncidentResponse]:
        incidents = self.repository.list_all_incidents(limit=limit, offset=offset)
        return [self._build_incident_response(item) for item in incidents]

    def get_incident_by_id_for_platform(self, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_incident_response(incident)

    def list_provider_incidents(self, current_user: User) -> list[IncidentResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incidents = self.repository.list_incidents_by_provider_id(str(provider.id))
        return [self._build_incident_response(item) for item in incidents]

    def get_provider_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_incident_response(incident)

    def _build_incident_response(self, incident: Incident) -> IncidentResponse:
        vehicle_payload = IncidentVehicleSummaryResponse(
            id=str(incident.vehicle.id),
            plate_number=incident.vehicle.plate_number,
            vehicle_type=incident.vehicle.vehicle_type,
            brand=incident.vehicle.brand,
            model=incident.vehicle.model,
            year=incident.vehicle.year,
            color=incident.vehicle.color,
        )

        client_payload = IncidentClientSummaryResponse(
            id=str(incident.client_user.id),
            email=incident.client_user.email,
            first_name=incident.client_user.first_name,
            last_name=incident.client_user.last_name,
            full_name=incident.client_user.full_name,
            phone_number=incident.client_user.phone_number,
        )

        provider_payload = None
        if incident.provider is not None:
            provider_payload = IncidentProviderSummaryResponse(
                id=str(incident.provider.id),
                provider_type=incident.provider.provider_type,
                business_name=incident.provider.business_name,
                contact_phone=incident.provider.contact_phone,
                city=incident.provider.city,
                is_available=incident.provider.is_available,
                average_rating=incident.provider.average_rating,
            )

        assigned_technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            assigned_technician_payload = IncidentTechnicianSummaryResponse(
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

        estimated_price_min = (
            float(incident.estimated_price_min)
            if incident.estimated_price_min is not None
            else None
        )
        estimated_price_max = (
            float(incident.estimated_price_max)
            if incident.estimated_price_max is not None
            else None
        )

        route_distance_km = (
            round(incident.route_distance_meters / 1000.0, 2)
            if incident.route_distance_meters is not None
            else None
        )
        route_eta_minutes = (
            int(round(incident.route_eta_seconds / 60))
            if incident.route_eta_seconds is not None
            else None
        )

        return IncidentResponse(
            id=str(incident.id),
            client_user_id=str(incident.client_user_id),
            vehicle_id=str(incident.vehicle_id),
            provider_id=str(incident.provider_id) if incident.provider_id is not None else None,
            assigned_technician_id=(
                str(incident.assigned_technician_id)
                if incident.assigned_technician_id is not None
                else None
            ),
            dispatch_mode=incident.dispatch_mode,
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            client_contact_phone_snapshot=incident.client_contact_phone_snapshot,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            estimated_price_min=estimated_price_min,
            estimated_price_max=estimated_price_max,
            ai_summary_status=incident.ai_summary_status,
            summary_provider_name=incident.summary_provider_name,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
            summary_processed_at=incident.summary_processed_at,
            summary_error_message=incident.summary_error_message,
            responder_last_latitude=incident.responder_last_latitude,
            responder_last_longitude=incident.responder_last_longitude,
            responder_last_source_type=incident.responder_last_source_type,
            responder_last_recorded_at=incident.responder_last_recorded_at,
            route_provider_name=incident.route_provider_name,
            route_distance_meters=incident.route_distance_meters,
            route_distance_km=route_distance_km,
            route_duration_seconds=incident.route_duration_seconds,
            route_eta_seconds=incident.route_eta_seconds,
            route_eta_minutes=route_eta_minutes,
            route_polyline=incident.route_polyline,
            route_last_calculated_at=incident.route_last_calculated_at,
            route_error_message=incident.route_error_message,
            requested_at=incident.requested_at,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            created_at=incident.created_at,
            updated_at=incident.updated_at,
            vehicle=vehicle_payload,
            client_user=client_payload,
            provider=provider_payload,
            assigned_technician=assigned_technician_payload,
        )
