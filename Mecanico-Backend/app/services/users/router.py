from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.users.repository import UsersRepository
from app.services.users.schemas import UpdateOwnProfileRequest
from app.services.users.service import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me/profile")
def get_own_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.get_own_profile(current_user)

    return success_response(
        message="Own profile loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/profile")
def update_own_profile(
    payload: UpdateOwnProfileRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.update_own_profile(current_user, payload)

    return success_response(
        message="Own profile updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_users(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.list_users(limit=limit, offset=offset)

    return success_response(
        message="Users loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{user_id}")
def get_user_by_id(
    user_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.get_user_by_id(user_id)

    return success_response(
        message="User loaded successfully.",
        data=result.model_dump(mode="json"),
    )