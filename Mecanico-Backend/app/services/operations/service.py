from datetime import datetime, timezone

from app.common.constants import (
    DISPATCH_MODE_PROVIDER_SELF,
    DISPATCH_MODE_TECHNICIAN,
    INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
    INCIDENT_OPERATION_EVENT_DISPATCHED,
    INCIDENT_OPERATION_EVENT_SERVICE_CANCELLED,
    INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
    INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    PROVIDER_TYPE_WORKSHOP,
    PUSH_EVENT_INCIDENT_CANCELLED,
    PUSH_EVENT_INCIDENT_COMPLETED,
    PUSH_EVENT_PROVIDER_ARRIVED,
    PUSH_EVENT_PROVIDER_EN_ROUTE,
    PUSH_EVENT_TECHNICIAN_ASSIGNED,
    AUDIT_EVENT_INCIDENT_ARRIVED,
    AUDIT_EVENT_INCIDENT_CANCELLED,
    AUDIT_EVENT_INCIDENT_COMPLETED,
    AUDIT_EVENT_INCIDENT_DISPATCHED,


)
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.operations.models import IncidentOperationEvent
from app.services.operations.repository import OperationsRepository
from app.services.operations.schemas import (
    CompleteIncidentRequest,
    DispatchIncidentRequest,
    IncidentOperationEventResponse,
    IncidentOperationStateResponse,
    OperationClientSummaryResponse,
    OperationEventActorResponse,
    OperationNoteRequest,
    OperationTechnicianSummaryResponse,
)
from app.services.billing.repository import BillingRepository
from app.services.billing.service import BillingService



class OperationsService:
    def __init__(self, repository: OperationsRepository) -> None:
        self.repository = repository

    def list_my_active_operations(self, current_user: User) -> list[IncidentOperationStateResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incidents = self.repository.list_provider_active_incidents(str(provider.id))
        return [self._build_operation_state_response(item) for item in incidents]

    def get_my_operation_state(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_operation_state_response(incident)

    def dispatch_my_incident(
        self,
        current_user: User,
        incident_id: str,
        payload: DispatchIncidentRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status != INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("Only assigned incidents can be dispatched.")

            assigned_technician = None
            dispatch_mode = DISPATCH_MODE_PROVIDER_SELF

            if locked_provider.provider_type == PROVIDER_TYPE_WORKSHOP:
                if not payload.technician_id:
                    raise ConflictException("A technician is required to dispatch a workshop incident.")

                assigned_technician = self.repository.get_technician_by_id_for_update(payload.technician_id)
                if assigned_technician is None:
                    raise NotFoundException("Technician not found.")

                if str(assigned_technician.provider_id) != str(locked_provider.id):
                    raise ForbiddenException("This technician does not belong to your provider.")

                if not assigned_technician.is_active:
                    raise ConflictException("The selected technician is inactive.")

                if not assigned_technician.is_available:
                    raise ConflictException("The selected technician is not available.")

                assigned_technician.is_available = False
                dispatch_mode = DISPATCH_MODE_TECHNICIAN
                locked_incident.assigned_technician_id = assigned_technician.id
                self.repository.save(assigned_technician)
            else:
                if payload.technician_id:
                    raise ConflictException("Independent mechanics cannot dispatch using a technician_id.")
                locked_incident.assigned_technician_id = None

            previous_status = locked_incident.status
            locked_incident.dispatch_mode = dispatch_mode
            locked_incident.status = INCIDENT_STATUS_EN_ROUTE
            locked_incident.en_route_at = now

            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=assigned_technician.id if assigned_technician is not None else None,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_DISPATCHED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json={
                        "dispatch_mode": dispatch_mode,
                        "assigned_technician_id": (
                            str(assigned_technician.id)
                            if assigned_technician is not None
                            else None
                        ),
                    },
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")
        
        self._enqueue_notification_safely(
        lambda: self._enqueue_dispatch_notification(incident_id)
        )

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_DISPATCHED,
        payload_json={
            "dispatch_mode": incident.dispatch_mode,
            "assigned_technician_id": str(incident.assigned_technician_id) if incident.assigned_technician_id else None,
            "status": incident.status,
        },
    )


        return self._build_operation_state_response(incident)

    def mark_my_arrival(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
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

            if locked_incident.status != INCIDENT_STATUS_EN_ROUTE:
                raise ConflictException("Only incidents en route can be marked as arrived.")

            previous_status = locked_incident.status
            locked_incident.status = INCIDENT_STATUS_ON_SITE
            locked_incident.arrived_at = now
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        self._enqueue_notification_safely(
        lambda: self._enqueue_arrival_notification(incident_id)
        )

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_ARRIVED,
        payload_json={
            "status": incident.status,
            "arrived_at": incident.arrived_at.isoformat() if incident.arrived_at else None,
        },
    )


        return self._build_operation_state_response(incident)

    def start_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
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

            if locked_incident.status not in (INCIDENT_STATUS_EN_ROUTE, INCIDENT_STATUS_ON_SITE):
                raise ConflictException(
                    "Only incidents en route or on site can be started."
                )

            previous_status = locked_incident.status
            if locked_incident.arrived_at is None:
                locked_incident.arrived_at = now

            if locked_incident.started_at is None:
                locked_incident.started_at = now

            locked_incident.status = INCIDENT_STATUS_IN_PROGRESS
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_operation_state_response(incident)

    def complete_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: CompleteIncidentRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (INCIDENT_STATUS_ON_SITE, INCIDENT_STATUS_IN_PROGRESS):
                raise ConflictException(
                    "Only incidents on site or in progress can be completed."
                )

            assigned_technician = None
            if locked_incident.assigned_technician_id is not None:
                assigned_technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )

            previous_status = locked_incident.status

            if locked_incident.arrived_at is None:
                locked_incident.arrived_at = now

            if locked_incident.started_at is None:
                locked_incident.started_at = now

            locked_incident.status = INCIDENT_STATUS_COMPLETED
            locked_incident.completed_at = now

            if assigned_technician is not None and assigned_technician.is_active:
                assigned_technician.is_available = True
                self.repository.save(assigned_technician)

            locked_provider.current_active_services = max(
                locked_provider.current_active_services - 1,
                0,
            )

            self.repository.save(locked_provider)
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json={
                        "completion_summary": self._normalize_optional_text(payload.completion_summary),
                    },
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        self._enqueue_notification_safely(
        lambda: self._enqueue_completion_notification(incident_id)
        )


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_COMPLETED,
        payload_json={
            "status": incident.status,
            "completed_at": incident.completed_at.isoformat() if incident.completed_at else None,
        },
    )

        return self._build_operation_state_response(incident)

    def cancel_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException(
                    "Only assigned or active incidents can be cancelled by the provider."
                )

            assigned_technician = None
            if locked_incident.assigned_technician_id is not None:
                assigned_technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )

            previous_status = locked_incident.status
            locked_incident.status = INCIDENT_STATUS_CANCELLED
            locked_incident.cancelled_at = now

            if assigned_technician is not None and assigned_technician.is_active:
                assigned_technician.is_available = True
                self.repository.save(assigned_technician)

            locked_provider.current_active_services = max(
                locked_provider.current_active_services - 1,
                0,
            )

            self.repository.save(locked_provider)
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_CANCELLED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")


        self._enqueue_notification_safely(
        lambda: self._enqueue_cancellation_notification(incident_id)
        )

        self._sync_billing_cancellation_safely(incident_id)

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_CANCELLED,
        payload_json={
            "status": incident.status,
            "cancelled_at": incident.cancelled_at.isoformat() if incident.cancelled_at else None,
        },
    )

        return self._build_operation_state_response(incident)

    def list_my_operation_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[IncidentOperationEventResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        events = self.repository.list_operation_events_by_incident_id(incident_id)
        return [self._build_event_response(item) for item in events]

    def list_platform_operation_history(
        self,
        incident_id: str,
    ) -> list[IncidentOperationEventResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        events = self.repository.list_operation_events_by_incident_id(incident_id)
        return [self._build_event_response(item) for item in events]

    def _build_operation_state_response(self, incident) -> IncidentOperationStateResponse:
        client_user = incident.client_user

        assigned_technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            assigned_technician_payload = OperationTechnicianSummaryResponse(
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

        client_payload = OperationClientSummaryResponse(
            id=str(client_user.id),
            email=client_user.email,
            first_name=client_user.first_name,
            last_name=client_user.last_name,
            full_name=client_user.full_name,
            phone_number=client_user.phone_number,
        )

        return IncidentOperationStateResponse(
            incident_id=str(incident.id),
            provider_id=str(incident.provider_id) if incident.provider_id else None,
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
            ai_summary_status=incident.ai_summary_status,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            client_user=client_payload,
            assigned_technician=assigned_technician_payload,
        )

    def _build_event_response(self, event: IncidentOperationEvent) -> IncidentOperationEventResponse:
        actor_payload = None
        if event.actor_user is not None:
            actor_user = event.actor_user
            actor_payload = OperationEventActorResponse(
                id=str(actor_user.id),
                email=actor_user.email,
                first_name=actor_user.first_name,
                last_name=actor_user.last_name,
                full_name=actor_user.full_name,
            )

        technician_payload = None
        if event.technician is not None:
            technician = event.technician
            technician_payload = OperationTechnicianSummaryResponse(
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

        return IncidentOperationEventResponse(
            id=str(event.id),
            incident_id=str(event.incident_id),
            provider_id=str(event.provider_id) if event.provider_id else None,
            technician_id=str(event.technician_id) if event.technician_id else None,
            actor_user_id=str(event.actor_user_id) if event.actor_user_id else None,
            event_type=event.event_type,
            from_status=event.from_status,
            to_status=event.to_status,
            note=event.note,
            payload_json=event.payload_json,
            created_at=event.created_at,
            actor_user=actor_payload,
            technician=technician_payload,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None


    def _enqueue_dispatch_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)

        if incident.dispatch_mode == DISPATCH_MODE_TECHNICIAN and incident.assigned_technician is not None:
            dispatcher.enqueue_event_for_user_ids(
                requested_by_user_id=None,
                incident_id=incident_id,
                event_code=PUSH_EVENT_TECHNICIAN_ASSIGNED,
                recipient_user_ids=[str(incident.client_user_id)],
                title="Técnico asignado",
                body=f"{incident.assigned_technician.full_name} fue asignado y ya va en camino.",
                data={
                "event_code": PUSH_EVENT_TECHNICIAN_ASSIGNED,
                "incident_id": str(incident.id),
                "provider_id": str(incident.provider_id),
                "technician_id": str(incident.assigned_technician_id),
                "technician_name": incident.assigned_technician.full_name,
                "status": incident.status,
                },
            )
            return

        dispatcher.enqueue_event_for_user_ids(
        requested_by_user_id=None,
        incident_id=incident_id,
        event_code=PUSH_EVENT_PROVIDER_EN_ROUTE,
        recipient_user_ids=[str(incident.client_user_id)],
        title="Ayuda en camino",
        body=f"{incident.provider.business_name} ya va en camino hacia tu ubicación.",
        data={
            "event_code": PUSH_EVENT_PROVIDER_EN_ROUTE,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_arrival_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_PROVIDER_ARRIVED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Proveedor en el lugar",
            body=f"{incident.provider.business_name} llegó al punto del incidente.",
            data={
            "event_code": PUSH_EVENT_PROVIDER_ARRIVED,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_completion_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_COMPLETED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Servicio finalizado",
            body=f"{incident.provider.business_name} finalizó la atención de tu incidente.",
            data={
            "event_code": PUSH_EVENT_INCIDENT_COMPLETED,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_cancellation_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_CANCELLED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Servicio cancelado",
            body=f"{incident.provider.business_name} canceló la atención del incidente.",
            data={
            "event_code": PUSH_EVENT_INCIDENT_CANCELLED,
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

    def _sync_billing_cancellation_safely(self, incident_id: str) -> None:
        try:
            billing_service = BillingService(BillingRepository(self.repository.db))
            billing_service.cancel_billing_due_to_incident_cancellation(incident_id)
        except Exception:
            return


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type="INCIDENT",
                entity_id=incident_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return
