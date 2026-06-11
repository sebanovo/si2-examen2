from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import Role, User
from app.services.providers.models import Provider, Technician


class ProvidersRepository:
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

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_provider(self, provider: Provider) -> Provider:
        self.db.add(provider)
        self.db.commit()
        self.db.refresh(provider)
        return provider

    def save_provider(self, provider: Provider) -> Provider:
        self.db.add(provider)
        self.db.commit()
        self.db.refresh(provider)
        return provider

    def list_providers(self, limit: int = 50, offset: int = 0) -> list[Provider]:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .order_by(Provider.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.id == provider_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_technician(self, technician: Technician) -> Technician:
        self.db.add(technician)
        self.db.commit()
        self.db.refresh(technician)
        return technician

    def save_technician(self, technician: Technician) -> Technician:
        self.db.add(technician)
        self.db.commit()
        self.db.refresh(technician)
        return technician

    def list_technicians_by_provider_id(self, provider_id: str) -> list[Technician]:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.provider_id == provider_id)
            .order_by(Technician.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_technician_by_id(self, technician_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = select(Technician).where(Technician.id == technician_id)
        return self.db.execute(query).scalar_one_or_none()