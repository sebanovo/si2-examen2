from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.ratings.repository import RatingsRepository
from app.services.ratings.schemas import CreateOrUpdateProviderRatingRequest
from app.services.ratings.service import RatingsService

router = APIRouter(prefix="/ratings", tags=["Ratings"])


@router.post("/client/incidents/{incident_id}")
def create_or_update_my_incident_rating(
    incident_id: str,
    payload: CreateOrUpdateProviderRatingRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.create_or_update_my_incident_rating(current_user, incident_id, payload)

    return success_response(
        message="Incident rating saved successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/incidents/{incident_id}")
def get_my_incident_rating(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.get_my_incident_rating(current_user, incident_id)

    return success_response(
        message="Incident rating loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/me")
def list_my_provider_ratings(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.list_my_provider_ratings(current_user, limit=limit, offset=offset)

    return success_response(
        message="Provider ratings loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/provider/me/stats")
def get_my_provider_rating_stats(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.get_my_provider_rating_stats(current_user)

    return success_response(
        message="Provider rating stats loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/me/incidents/{incident_id}")
def get_my_provider_incident_rating(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.get_my_provider_incident_rating(current_user, incident_id)

    return success_response(
        message="Provider incident rating loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform")
def list_platform_ratings(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.list_platform_ratings(limit=limit, offset=offset)

    return success_response(
        message="Platform ratings loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/platform/providers/{provider_id}")
def list_platform_provider_ratings(
    provider_id: str,
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.list_platform_provider_ratings(
        provider_id=provider_id,
        limit=limit,
        offset=offset,
    )

    return success_response(
        message="Platform provider ratings loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/platform/providers/{provider_id}/stats")
def get_platform_provider_rating_stats(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = RatingsService(RatingsRepository(db))
    result = service.get_platform_provider_rating_stats(provider_id)

    return success_response(
        message="Platform provider rating stats loaded successfully.",
        data=result.model_dump(mode="json"),
    )