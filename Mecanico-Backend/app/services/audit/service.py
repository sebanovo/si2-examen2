from app.services.audit.models import AuditLog, MetricSnapshot
from app.services.audit.repository import AuditRepository
from app.services.audit.schemas import (
    AuditActorUserResponse,
    AuditLogResponse,
    MetricSnapshotCapturedByUserResponse,
    MetricSnapshotResponse,
)


class AuditService:
    def __init__(self, repository: AuditRepository) -> None:
        self.repository = repository

    def log_event(
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
        http_method: str | None,
        route_path: str | None,
        ip_address: str | None,
        user_agent: str | None,
        status_code: int | None,
        outcome: str,
        payload_json: dict | None,
    ) -> AuditLogResponse:
        audit_log = AuditLog(
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

        try:
            self.repository.create_audit_log(audit_log)
            self.repository.commit()
            self.repository.refresh(audit_log)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_audit_log_response(audit_log)

    def list_audit_logs(
        self,
        *,
        limit: int,
        offset: int,
        event_type: str | None = None,
        actor_user_id: str | None = None,
        incident_id: str | None = None,
        provider_id: str | None = None,
        request_id: str | None = None,
    ) -> list[AuditLogResponse]:
        logs = self.repository.list_audit_logs(
            limit=limit,
            offset=offset,
            event_type=event_type,
            actor_user_id=actor_user_id,
            incident_id=incident_id,
            provider_id=provider_id,
            request_id=request_id,
        )
        return [self._build_audit_log_response(item) for item in logs]

    def get_audit_log_by_id(self, audit_log_id: str) -> AuditLogResponse:
        audit_log = self.repository.get_audit_log_by_id(audit_log_id)
        if audit_log is None:
            raise ValueError("Audit log not found.")

        return self._build_audit_log_response(audit_log)

    def create_metric_snapshot(
        self,
        *,
        captured_by_user_id: str | None,
        snapshot_type: str,
        payload_json: dict,
    ) -> MetricSnapshotResponse:
        snapshot = MetricSnapshot(
            captured_by_user_id=captured_by_user_id,
            snapshot_type=snapshot_type,
            payload_json=payload_json,
        )

        try:
            self.repository.create_metric_snapshot(snapshot)
            self.repository.commit()
            self.repository.refresh(snapshot)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_metric_snapshot_response(snapshot)

    def list_metric_snapshots(
        self,
        *,
        limit: int,
        offset: int,
        snapshot_type: str | None = None,
    ) -> list[MetricSnapshotResponse]:
        snapshots = self.repository.list_metric_snapshots(
            limit=limit,
            offset=offset,
            snapshot_type=snapshot_type,
        )
        return [self._build_metric_snapshot_response(item) for item in snapshots]

    def _build_audit_log_response(self, audit_log: AuditLog) -> AuditLogResponse:
        actor_payload = None
        if audit_log.actor_user is not None:
            actor = audit_log.actor_user
            actor_payload = AuditActorUserResponse(
                id=str(actor.id),
                email=actor.email,
                first_name=actor.first_name,
                last_name=actor.last_name,
                full_name=actor.full_name,
            )

        return AuditLogResponse(
            id=str(audit_log.id),
            actor_user_id=str(audit_log.actor_user_id) if audit_log.actor_user_id else None,
            incident_id=str(audit_log.incident_id) if audit_log.incident_id else None,
            provider_id=str(audit_log.provider_id) if audit_log.provider_id else None,
            request_id=audit_log.request_id,
            event_scope=audit_log.event_scope,
            event_type=audit_log.event_type,
            entity_type=audit_log.entity_type,
            entity_id=audit_log.entity_id,
            http_method=audit_log.http_method,
            route_path=audit_log.route_path,
            ip_address=audit_log.ip_address,
            user_agent=audit_log.user_agent,
            status_code=audit_log.status_code,
            outcome=audit_log.outcome,
            payload_json=audit_log.payload_json,
            created_at=audit_log.created_at,
            actor_user=actor_payload,
        )

    def _build_metric_snapshot_response(self, snapshot: MetricSnapshot) -> MetricSnapshotResponse:
        captured_by_payload = None
        if snapshot.captured_by_user is not None:
            user = snapshot.captured_by_user
            captured_by_payload = MetricSnapshotCapturedByUserResponse(
                id=str(user.id),
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                full_name=user.full_name,
            )

        return MetricSnapshotResponse(
            id=str(snapshot.id),
            captured_by_user_id=str(snapshot.captured_by_user_id) if snapshot.captured_by_user_id else None,
            snapshot_type=snapshot.snapshot_type,
            payload_json=snapshot.payload_json,
            created_at=snapshot.created_at,
            captured_by_user=captured_by_payload,
        )
