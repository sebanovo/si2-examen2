from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.audit.models import AuditLog, MetricSnapshot


class AuditRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_audit_log(self, audit_log: AuditLog) -> AuditLog:
        self.db.add(audit_log)
        self.db.flush()
        return audit_log

    def get_audit_log_by_id(self, audit_log_id: str) -> AuditLog | None:
        query: Select[tuple[AuditLog]] = (
            select(AuditLog)
            .options(
                selectinload(AuditLog.actor_user),
                selectinload(AuditLog.incident),
                selectinload(AuditLog.provider),
            )
            .where(AuditLog.id == audit_log_id)
        )
        return self.db.execute(query).scalar_one_or_none()

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
    ) -> list[AuditLog]:
        query: Select[tuple[AuditLog]] = (
            select(AuditLog)
            .options(
                selectinload(AuditLog.actor_user),
                selectinload(AuditLog.incident),
                selectinload(AuditLog.provider),
            )
            .order_by(AuditLog.created_at.desc())
            .limit(limit)
            .offset(offset)
        )

        if event_type:
            query = query.where(AuditLog.event_type == event_type)

        if actor_user_id:
            query = query.where(AuditLog.actor_user_id == actor_user_id)

        if incident_id:
            query = query.where(AuditLog.incident_id == incident_id)

        if provider_id:
            query = query.where(AuditLog.provider_id == provider_id)

        if request_id:
            query = query.where(AuditLog.request_id == request_id)

        return list(self.db.execute(query).scalars().all())

    def create_metric_snapshot(self, snapshot: MetricSnapshot) -> MetricSnapshot:
        self.db.add(snapshot)
        self.db.flush()
        return snapshot

    def list_metric_snapshots(self, *, limit: int, offset: int, snapshot_type: str | None = None) -> list[MetricSnapshot]:
        query: Select[tuple[MetricSnapshot]] = (
            select(MetricSnapshot)
            .options(selectinload(MetricSnapshot.captured_by_user))
            .order_by(MetricSnapshot.created_at.desc())
            .limit(limit)
            .offset(offset)
        )

        if snapshot_type:
            query = query.where(MetricSnapshot.snapshot_type == snapshot_type)

        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
