from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.billing.payment_schemas import (
    ClientCreateCheckoutRequest,
    ClientSimulatePaymentFailureRequest,
    ClientSimulatePaymentSuccessRequest,
)
from app.services.billing.payment_service import PaymentSimulationService
from app.services.billing.repository import BillingRepository
from app.services.billing.schemas import (
    ClientCheckoutPreviewRequest,
    ClientMarkIncidentPaidRequest,
    ProviderEstimateIncidentPricingRequest,
    ProviderFinalizeIncidentPricingRequest,
)
from app.services.billing.service import BillingService

router = APIRouter(prefix="/billing", tags=["Billing"])


@router.get("/client/incidents/{incident_id}")
def get_my_client_incident_billing(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_my_client_incident_billing(current_user, incident_id)

    return success_response(
        message="Client incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/checkout-preview")
def create_client_checkout_preview(
    incident_id: str,
    payload: ClientCheckoutPreviewRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.create_client_checkout_preview(current_user, incident_id, payload)

    return success_response(
        message="Client checkout preview created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/checkout")
def create_client_checkout(
    incident_id: str,
    payload: ClientCreateCheckoutRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = PaymentSimulationService(BillingRepository(db))
    result = service.create_client_checkout(current_user, incident_id, payload)

    return success_response(
        message="Mock checkout created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/simulate-success")
def simulate_client_payment_success(
    incident_id: str,
    payload: ClientSimulatePaymentSuccessRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = PaymentSimulationService(BillingRepository(db))
    result = service.simulate_client_payment_success(current_user, incident_id, payload)

    return success_response(
        message="Mock payment approved successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/simulate-failure")
def simulate_client_payment_failure(
    incident_id: str,
    payload: ClientSimulatePaymentFailureRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = PaymentSimulationService(BillingRepository(db))
    result = service.simulate_client_payment_failure(current_user, incident_id, payload)

    return success_response(
        message="Mock payment failure simulated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/mark-paid")
def mark_client_incident_as_paid(
    incident_id: str,
    payload: ClientMarkIncidentPaidRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.mark_client_incident_as_paid(current_user, incident_id, payload)

    return success_response(
        message="Incident payment marked as paid successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}")
def get_my_provider_incident_billing(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_my_provider_incident_billing(current_user, incident_id)

    return success_response(
        message="Provider incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/estimate")
def upsert_provider_incident_estimate(
    incident_id: str,
    payload: ProviderEstimateIncidentPricingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.upsert_provider_incident_estimate(current_user, incident_id, payload)

    return success_response(
        message="Incident estimate updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/finalize")
def finalize_provider_incident_pricing(
    incident_id: str,
    payload: ProviderFinalizeIncidentPricingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.finalize_provider_incident_pricing(current_user, incident_id, payload)

    return success_response(
        message="Incident pricing finalized successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}")
def get_platform_incident_billing(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_platform_incident_billing(incident_id)

    return success_response(
        message="Platform incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )