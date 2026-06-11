from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.providers.repository import ProvidersRepository
from app.services.providers.schemas import (
    CreateTechnicianRequest,
    ProviderOnboardingRequest,
    UpdateOwnProviderRequest,
    UpdateProviderOperationsRequest,
    UpdateTechnicianRequest,
)
from app.services.providers.service import ProvidersService

router = APIRouter(prefix="/providers", tags=["Providers"])


@router.post("/onboarding")
def onboard_provider(
    payload: ProviderOnboardingRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.onboard_provider(payload)

    return success_response(
        message="Provider and provider admin user created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_providers(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_providers(limit=limit, offset=offset)

    return success_response(
        message="Providers loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{provider_id}")
def get_provider_by_id(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.get_provider_by_id(provider_id)

    return success_response(
        message="Provider loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{provider_id}/operations")
def update_provider_operations(
    provider_id: str,
    payload: UpdateProviderOperationsRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_provider_operations(provider_id, payload)

    return success_response(
        message="Provider operations updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/profile")
def get_my_provider(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.get_my_provider(current_user)

    return success_response(
        message="Own provider profile loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/profile")
def update_my_provider(
    payload: UpdateOwnProviderRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_my_provider(current_user, payload)

    return success_response(
        message="Own provider profile updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/technicians")
def list_my_technicians(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_my_technicians(current_user)

    return success_response(
        message="Own provider technicians loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/me/technicians")
def create_my_technician(
    payload: CreateTechnicianRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.create_my_technician(current_user, payload)

    return success_response(
        message="Technician created successfully for own provider.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/technicians/{technician_id}")
def update_my_technician(
    technician_id: str,
    payload: UpdateTechnicianRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_my_technician(current_user, technician_id, payload)

    return success_response(
        message="Technician updated successfully for own provider.",
        data=result.model_dump(mode="json"),
    )


@router.get("/{provider_id}/technicians")
def list_provider_technicians(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_provider_technicians(provider_id)

    return success_response(
        message="Provider technicians loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/{provider_id}/technicians")
def create_provider_technician(
    provider_id: str,
    payload: CreateTechnicianRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.create_provider_technician(provider_id, payload)

    return success_response(
        message="Technician created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{provider_id}/technicians/{technician_id}")
def update_provider_technician(
    provider_id: str,
    technician_id: str,
    payload: UpdateTechnicianRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_provider_technician(provider_id, technician_id, payload)

    return success_response(
        message="Technician updated successfully.",
        data=result.model_dump(mode="json"),
    )