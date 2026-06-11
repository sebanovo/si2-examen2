from __future__ import annotations

import logging
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.common.constants import ROLE_TECHNICIAN
from app.core.security import hash_password
from app.services.auth.models import Role, User
from app.services.providers.models import Technician

logger = logging.getLogger(__name__)

TECHNICIAN_DEMO_PASSWORD = "Demo12345"


@dataclass(frozen=True)
class TechnicianUserSeed:
    email: str
    first_name: str
    last_name: str
    phone_number: str
    technician_phone_number: str


TECHNICIAN_USER_SEEDS: tuple[TechnicianUserSeed, ...] = (
    TechnicianUserSeed(
        email="tecnico.pedro@mechanic.local",
        first_name="Pedro",
        last_name="Salvatierra",
        phone_number="70100001",
        technician_phone_number="70100001",
    ),
    TechnicianUserSeed(
        email="tecnico.silvia@mechanic.local",
        first_name="Silvia",
        last_name="Aguilera",
        phone_number="70100003",
        technician_phone_number="70100003",
    ),
    TechnicianUserSeed(
        email="tecnico.marcelo@mechanic.local",
        first_name="Marcelo",
        last_name="Vaca",
        phone_number="70100008",
        technician_phone_number="70100008",
    ),
)


def seed_step_06_technician_mobile_users(db: Session) -> None:
    """
    Crea usuarios demo con rol TECHNICIAN y los vincula con registros Technician.

    Es idempotente: puede ejecutarse varias veces sin duplicar usuarios ni romper
    técnicos existentes.
    """

    logger.info("Starting demo seed step 06: technician mobile users.")

    technician_role = get_role_by_code(db, ROLE_TECHNICIAN)
    if technician_role is None:
        raise RuntimeError("Role TECHNICIAN was not found.")

    for seed in TECHNICIAN_USER_SEEDS:
        user = get_user_by_email(db, seed.email)

        if user is None:
            user = User(
                email=normalize_email(seed.email),
                password_hash=hash_password(TECHNICIAN_DEMO_PASSWORD),
                first_name=seed.first_name.strip(),
                last_name=seed.last_name.strip(),
                phone_number=seed.phone_number.strip(),
                is_active=True,
                is_superuser=False,
                roles=[technician_role],
            )
            db.add(user)
            logger.info("Created technician demo user: %s", seed.email)
        else:
            user.password_hash = hash_password(TECHNICIAN_DEMO_PASSWORD)
            user.first_name = seed.first_name.strip()
            user.last_name = seed.last_name.strip()
            user.phone_number = seed.phone_number.strip()
            user.is_active = True
            ensure_user_has_role(user, technician_role)
            db.add(user)
            logger.info("Updated technician demo user: %s", seed.email)

        db.flush()

        technician = get_technician_by_phone_number(db, seed.technician_phone_number)
        if technician is None:
            raise RuntimeError(
                f"Technician with phone {seed.technician_phone_number} was not found."
            )

        technician.user_id = user.id
        technician.is_active = True
        db.add(technician)
        logger.info(
            "Linked technician user %s to technician phone %s.",
            seed.email,
            seed.technician_phone_number,
        )

    db.flush()

    logger.info("Finished demo seed step 06.")


def get_role_by_code(db: Session, role_code: str) -> Role | None:
    query = select(Role).where(Role.code == role_code)
    return db.execute(query).scalar_one_or_none()


def get_user_by_email(db: Session, email: str) -> User | None:
    query = select(User).where(User.email == normalize_email(email))
    return db.execute(query).scalar_one_or_none()


def get_technician_by_phone_number(
    db: Session,
    phone_number: str,
) -> Technician | None:
    query = select(Technician).where(Technician.phone_number == phone_number.strip())
    return db.execute(query).scalar_one_or_none()


def ensure_user_has_role(user: User, role: Role) -> None:
    current_role_codes = {existing_role.code for existing_role in user.roles}

    if role.code not in current_role_codes:
        user.roles.append(role)


def normalize_email(email: str) -> str:
    return email.strip().lower()