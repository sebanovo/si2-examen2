from app.core.database import SessionLocal
from app.services.audit.repository import AuditRepository
from app.services.audit.service import AuditService


class AuditEventDispatcher:
    def emit(
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
        http_method: str | None = None,
        route_path: str | None = None,
        ip_address: str | None = None,
        user_agent: str | None = None,
        status_code: int | None = None,
        outcome: str = "SUCCESS",
        payload_json: dict | None = None,
    ) -> None:
        db = SessionLocal()
        try:
            service = AuditService(AuditRepository(db))
            service.log_event(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=request_id,
                event_scope=event_scope,
                event_type=event_type,
                entity_type=entity_type,
                entity_id=entity_id,
                http_method=http_method,
                route_path=route_path,
                ip_address=ip_address,
                user_agent=user_agent,
                status_code=status_code,
                outcome=outcome,
                payload_json=payload_json,
            )
        finally:
            db.close()
