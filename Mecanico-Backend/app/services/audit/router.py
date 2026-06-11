from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.audit.repository import AuditRepository
from app.services.audit.service import AuditService
from app.services.auth.models import User

router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get("/logs")
def list_audit_logs(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    event_type: str | None = None,
    actor_user_id: str | None = None,
    incident_id: str | None = None,
    provider_id: str | None = None,
    request_id: str | None = None,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuditService(AuditRepository(db))
    result = service.list_audit_logs(
        limit=limit,
        offset=offset,
        event_type=event_type,
        actor_user_id=actor_user_id,
        incident_id=incident_id,
        provider_id=provider_id,
        request_id=request_id,
    )

    return success_response(
        message="Audit logs loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/metric-snapshots")
def list_metric_snapshots(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    snapshot_type: str | None = None,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuditService(AuditRepository(db))
    result = service.list_metric_snapshots(
        limit=limit,
        offset=offset,
        snapshot_type=snapshot_type,
    )

    return success_response(
        message="Metric snapshots loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )
