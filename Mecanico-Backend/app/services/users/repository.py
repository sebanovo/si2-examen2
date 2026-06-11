from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import User


class UsersRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_users(self, limit: int = 50, offset: int = 0) -> list[User]:
        query: Select[tuple[User]] = (
            select(User)
            .order_by(User.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user