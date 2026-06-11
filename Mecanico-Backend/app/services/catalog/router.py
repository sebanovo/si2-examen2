from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.catalog.repository import CatalogRepository
from app.services.catalog.schemas import (
    CreateServiceCatalogItemRequest,
    UpdateProviderServiceRequest,
    UpdateServiceCatalogItemRequest,
    UpsertProviderServiceRequest,
)
from app.services.catalog.service import CatalogService

router = APIRouter(prefix="/catalog", tags=["Catalog"])


@router.post("/services")
def create_service_catalog_item(
    payload: CreateServiceCatalogItemRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.create_service_catalog_item(payload)

    return success_response(
        message="Catalog service created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/services")
def list_service_catalog_items(
    include_inactive: bool = Query(default=False),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_service_catalog_items(include_inactive=include_inactive)

    return success_response(
        message="Catalog services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
            "include_inactive": include_inactive,
        },
    )


@router.get("/services/{service_catalog_item_id}")
def get_service_catalog_item_by_id(
    service_catalog_item_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.get_service_catalog_item_by_id(service_catalog_item_id)

    return success_response(
        message="Catalog service loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/services/{service_catalog_item_id}")
def update_service_catalog_item(
    service_catalog_item_id: str,
    payload: UpdateServiceCatalogItemRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.update_service_catalog_item(service_catalog_item_id, payload)

    return success_response(
        message="Catalog service updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/providers/{provider_id}/services")
def list_provider_services_for_platform(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_provider_services_for_platform(provider_id)

    return success_response(
        message="Provider services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/me/services/catalog")
def list_my_catalog_with_configuration(
    include_inactive_catalog: bool = Query(default=False),
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_my_catalog_with_configuration(
        current_user=current_user,
        include_inactive_catalog=include_inactive_catalog,
    )

    return success_response(
        message="Provider catalog with configuration loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
            "include_inactive_catalog": include_inactive_catalog,
        },
    )


@router.get("/me/services")
def list_my_provider_services(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_my_provider_services(current_user)

    return success_response(
        message="Configured provider services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/me/services")
def upsert_my_provider_service(
    payload: UpsertProviderServiceRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.upsert_my_provider_service(current_user, payload)

    return success_response(
        message="Provider service configured successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/services/{provider_service_id}")
def update_my_provider_service(
    provider_service_id: str,
    payload: UpdateProviderServiceRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.update_my_provider_service(
        current_user=current_user,
        provider_service_id=provider_service_id,
        payload=payload,
    )

    return success_response(
        message="Provider service updated successfully.",
        data=result.model_dump(mode="json"),
    )
