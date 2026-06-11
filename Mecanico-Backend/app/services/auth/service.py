from app.common.constants import (
    ACCOUNT_TYPE_CLIENT,
    ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
    ACCOUNT_TYPE_WORKSHOP,
    ROLE_CLIENT,
    ROLE_PROVIDER_ADMIN,
)
from app.common.exceptions import ConflictException, NotFoundException, UnauthorizedException
from app.core.config import settings
from app.core.security import create_access_token, hash_password, verify_password
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository
from app.services.auth.schemas import (
    AccessTokenResponse,
    AuthenticatedUserResponse,
    LoginRequest,
    RegisterRequest,
    RoleResponse,
)
from app.services.providers.models import Provider


class AuthService:
    def __init__(self, repository: AuthRepository) -> None:
        self.repository = repository

    def register_user(self, payload: RegisterRequest) -> AccessTokenResponse:
        normalized_email = payload.email.strip().lower()

        existing_user = self.repository.get_user_by_email(normalized_email)
        if existing_user is not None:
            raise ConflictException("A user with this email already exists.")

        account_type = payload.account_type.strip().upper()

        if account_type == ACCOUNT_TYPE_CLIENT:
            client_role = self.repository.get_role_by_code(ROLE_CLIENT)
            if client_role is None:
                raise NotFoundException("Default CLIENT role was not found.")

            new_user = User(
                email=normalized_email,
                password_hash=hash_password(payload.password),
                first_name=payload.first_name.strip(),
                last_name=payload.last_name.strip(),
                phone_number=payload.phone_number.strip() if payload.phone_number else None,
                is_active=True,
                is_superuser=False,
                roles=[client_role],
            )

            created_user = self.repository.create_user_and_optional_provider(new_user)
            return self._build_token_response(created_user)

        if account_type in (ACCOUNT_TYPE_INDEPENDENT_MECHANIC, ACCOUNT_TYPE_WORKSHOP):
            provider_admin_role = self.repository.get_role_by_code(ROLE_PROVIDER_ADMIN)
            if provider_admin_role is None:
                raise NotFoundException("Default PROVIDER_ADMIN role was not found.")

            if payload.provider_profile is None:
                raise ConflictException(
                    "Provider profile information is required for mechanic or workshop registration."
                )

            new_user = User(
                email=normalized_email,
                password_hash=hash_password(payload.password),
                first_name=payload.first_name.strip(),
                last_name=payload.last_name.strip(),
                phone_number=payload.phone_number.strip() if payload.phone_number else None,
                is_active=True,
                is_superuser=False,
                roles=[provider_admin_role],
            )

            new_provider = Provider(
                owner_user_id=None,
                provider_type=account_type,
                business_name=payload.provider_profile.business_name.strip(),
                legal_name=(
                    payload.provider_profile.legal_name.strip()
                    if payload.provider_profile.legal_name
                    else None
                ),
                description=(
                    payload.provider_profile.description.strip()
                    if payload.provider_profile.description
                    else None
                ),
                contact_email=(
                    payload.provider_profile.contact_email.strip().lower()
                    if payload.provider_profile.contact_email
                    else None
                ),
                contact_phone=(
                    payload.provider_profile.contact_phone.strip()
                    if payload.provider_profile.contact_phone
                    else None
                ),
                city=payload.provider_profile.city.strip() if payload.provider_profile.city else None,
                address=(
                    payload.provider_profile.address.strip()
                    if payload.provider_profile.address
                    else None
                ),
                base_latitude=payload.provider_profile.base_latitude,
                base_longitude=payload.provider_profile.base_longitude,
                is_active=True,
                is_available=True,
                max_concurrent_services=payload.provider_profile.max_concurrent_services,
                current_active_services=0,
                average_rating=0.0,
            )

            created_user = self.repository.create_user_and_optional_provider(
                user=new_user,
                provider=new_provider,
            )
            return self._build_token_response(created_user)

        raise ConflictException("Unsupported account type.")

    def login_user(self, payload: LoginRequest) -> AccessTokenResponse:
        normalized_email = payload.email.strip().lower()

        user = self.repository.get_user_by_email(normalized_email)
        if user is None:
            raise UnauthorizedException("Invalid email or password.")

        if not user.is_active:
            raise UnauthorizedException("This user account is inactive.")

        if not verify_password(payload.password, user.password_hash):
            raise UnauthorizedException("Invalid email or password.")

        return self._build_token_response(user)

    def build_authenticated_user(self, user: User) -> AuthenticatedUserResponse:
        role_items = [
            RoleResponse(
                id=str(role.id),
                code=role.code,
                name=role.name,
                description=role.description,
            )
            for role in sorted(user.roles, key=lambda item: item.code)
        ]

        role_codes = [role.code for role in role_items]

        return AuthenticatedUserResponse(
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

    def _build_token_response(self, user: User) -> AccessTokenResponse:
        role_codes = sorted(role.code for role in user.roles)

        token = create_access_token(
            subject=str(user.id),
            email=user.email,
            role_codes=role_codes,
            expires_minutes=settings.access_token_expire_minutes,
        )

        return AccessTokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_minutes=settings.access_token_expire_minutes,
            user=self.build_authenticated_user(user),
        )
