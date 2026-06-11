from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import Role, User
from app.services.providers.models import Provider


class AuthRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_role_by_code(self, role_code: str) -> Role | None:
        query: Select[tuple[Role]] = select(Role).where(Role.code == role_code)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(
        self,
        email: str,
        password_hash: str,
        first_name: str,
        last_name: str,
        phone_number: str | None,
        assigned_roles: list[Role],
        is_superuser: bool = False,
    ) -> User:
        new_user = User(
            email=email,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_active=True,
            is_superuser=is_superuser,
            roles=assigned_roles,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def create_user_and_optional_provider(
        self,
        user: User,
        provider: Provider | None = None,
    ) -> User:
        self.db.add(user)
        self.db.flush()

        if provider is not None:
            provider.owner_user_id = user.id
            self.db.add(provider)

        self.db.commit()
        self.db.refresh(user)
        return user