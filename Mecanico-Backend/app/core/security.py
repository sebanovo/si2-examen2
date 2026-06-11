from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.common.exceptions import ForbiddenException, UnauthorizedException
from app.core.config import settings
from app.core.dependencies import get_db_session
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository

password_hasher = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)


def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return password_hasher.verify(plain_password, password_hash)


def create_access_token(
    subject: str,
    email: str,
    role_codes: list[str],
    expires_minutes: int | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    expiration_minutes = expires_minutes or settings.access_token_expire_minutes
    expires_at = now + timedelta(minutes=expiration_minutes)

    payload: dict[str, Any] = {
        "sub": subject,
        "email": email,
        "roles": role_codes,
        "iat": int(now.timestamp()),
        "exp": int(expires_at.timestamp()),
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.jwt_algorithm,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except InvalidTokenError as exc:
        raise UnauthorizedException("Invalid or expired access token.") from exc


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db_session),
) -> User:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise UnauthorizedException("Bearer token is required.")

    payload = decode_access_token(credentials.credentials)
    user_id = payload.get("sub")

    if not user_id:
        raise UnauthorizedException("Invalid token payload.")

    repository = AuthRepository(db)
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise UnauthorizedException("Authenticated user was not found.")

    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise UnauthorizedException("This user account is inactive.")

    return current_user


def require_roles(*allowed_role_codes: str):
    def dependency(current_user: User = Depends(get_current_active_user)) -> User:
        user_role_codes = {role.code for role in current_user.roles}

        if not user_role_codes.intersection(set(allowed_role_codes)):
            raise ForbiddenException(
                "You do not have the required role to access this resource."
            )

        return current_user

    return dependency