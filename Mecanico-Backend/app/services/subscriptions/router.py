from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.subscriptions.repository import SubscriptionsRepository
from app.services.subscriptions.schemas import (
    ClientSubscribeToPlanRequest,
    ProviderPlanCoverageUpsertRequest,
    ProviderPlanUpsertRequest,
)
from app.services.subscriptions.service import SubscriptionsService

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


@router.get("/provider/me/plans")
def list_my_provider_plans(
    include_inactive: bool = Query(default=False),
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_my_provider_plans(current_user, include_inactive=include_inactive)

    return success_response(
        message="Provider subscription plans loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result), "include_inactive": include_inactive},
    )


@router.post("/provider/me/plans")
def create_my_provider_plan(
    payload: ProviderPlanUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.create_my_provider_plan(current_user, payload)

    return success_response(
        message="Provider subscription plan created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.put("/provider/me/plans/{plan_id}")
def update_my_provider_plan(
    plan_id: str,
    payload: ProviderPlanUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.update_my_provider_plan(current_user, plan_id, payload)

    return success_response(
        message="Provider subscription plan updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/plans/{plan_id}/coverages")
def upsert_my_provider_plan_coverage(
    plan_id: str,
    payload: ProviderPlanCoverageUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.upsert_my_provider_plan_coverage(current_user, plan_id, payload)

    return success_response(
        message="Provider plan coverage configured successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/providers/{provider_id}/plans")
def list_provider_plans_for_client(
    provider_id: str,
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_provider_plans_for_client(provider_id)

    return success_response(
        message="Provider available plans loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.post("/client/plans/{plan_id}/subscribe")
def subscribe_client_to_plan(
    plan_id: str,
    payload: ClientSubscribeToPlanRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.subscribe_client_to_plan(current_user, plan_id, payload)

    return success_response(
        message="Client subscribed to plan successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/me/subscriptions")
def list_my_client_subscriptions(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_my_client_subscriptions(current_user)

    return success_response(
        message="Client subscriptions loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/client/incidents/{incident_id}/coverage-preview")
def preview_applicable_coverage_for_incident(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.preview_applicable_coverage_for_incident(current_user, incident_id)

    return success_response(
        message="Applicable incident coverage preview loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/apply-coverage")
def apply_best_coverage_for_incident(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.apply_best_coverage_for_incident(current_user, incident_id)

    return success_response(
        message="Incident subscription coverage applied successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/applications")
def list_platform_incident_subscription_applications(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_platform_incident_subscription_applications(incident_id)

    return success_response(
        message="Incident subscription applications loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
