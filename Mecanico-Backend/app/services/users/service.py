from app.common.exceptions import NotFoundException
from app.services.auth.models import User
from app.services.users.repository import UsersRepository
from app.services.users.schemas import (
    UpdateOwnProfileRequest,
    UserProfileResponse,
    UserRoleItemResponse,
)


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def get_own_profile(self, current_user: User) -> UserProfileResponse:
        return self._build_profile_response(current_user)

    def update_own_profile(
        self,
        current_user: User,
        payload: UpdateOwnProfileRequest,
    ) -> UserProfileResponse:
        if payload.first_name is not None:
            current_user.first_name = payload.first_name.strip()

        if payload.last_name is not None:
            current_user.last_name = payload.last_name.strip()

        if payload.phone_number is not None:
            cleaned_phone = payload.phone_number.strip()
            current_user.phone_number = cleaned_phone or None

        updated_user = self.repository.save(current_user)
        return self._build_profile_response(updated_user)

    def get_user_by_id(self, user_id: str) -> UserProfileResponse:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise NotFoundException("User not found.")

        return self._build_profile_response(user)

    def list_users(self, limit: int = 50, offset: int = 0) -> list[UserProfileResponse]:
        users = self.repository.list_users(limit=limit, offset=offset)
        return [self._build_profile_response(user) for user in users]

    def _build_profile_response(self, user: User) -> UserProfileResponse:
        role_items = [
            UserRoleItemResponse(
                id=str(role.id),
                code=role.code,
                name=role.name,
                description=role.description,
            )
            for role in sorted(user.roles, key=lambda item: item.code)
        ]

        role_codes = [role.code for role in role_items]

        return UserProfileResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            full_name=user.full_name,
            phone_number=user.phone_number,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            role_codes=role_codes,
            roles=role_items,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )