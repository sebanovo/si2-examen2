import logging

from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.core.config import settings
from app.core.security import hash_password
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository

logger = logging.getLogger(__name__)


def seed_initial_platform_admin(db: Session) -> None:
    repository = AuthRepository(db)

    admin_email = settings.initial_platform_admin_email.strip().lower()
    existing_user = repository.get_user_by_email(admin_email)

    if existing_user is not None:
        logger.info(
            "Initial platform admin already exists with email=%s",
            admin_email,
        )
        return

    platform_admin_role = repository.get_role_by_code(ROLE_PLATFORM_ADMIN)
    if platform_admin_role is None:
        raise RuntimeError("PLATFORM_ADMIN role was not found during bootstrap seeding.")

    new_admin = User(
        email=admin_email,
        password_hash=hash_password(settings.initial_platform_admin_password),
        first_name=settings.initial_platform_admin_first_name.strip(),
        last_name=settings.initial_platform_admin_last_name.strip(),
        phone_number=(
            settings.initial_platform_admin_phone.strip()
            if settings.initial_platform_admin_phone
            else None
        ),
        is_active=True,
        is_superuser=True,
        roles=[platform_admin_role],
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    logger.info(
        "Initial platform admin created successfully with email=%s",
        admin_email,
    )