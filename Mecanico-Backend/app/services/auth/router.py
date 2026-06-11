from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository
from app.services.auth.schemas import LoginRequest, RegisterRequest
from app.services.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.register_user(payload)

    return success_response(
        message="User registered successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.login_user(payload)

    return success_response(
        message="Login completed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me")
def get_authenticated_user_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.build_authenticated_user(current_user)

    return success_response(
        message="Authenticated user loaded successfully.",
        data=result.model_dump(mode="json"),
    )