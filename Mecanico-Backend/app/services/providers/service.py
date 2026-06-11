from app.common.constants import (
    PROVIDER_TYPE_INDEPENDENT_MECHANIC,
    PROVIDER_TYPE_WORKSHOP,
    ROLE_PROVIDER_ADMIN,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.core.security import hash_password
from app.services.auth.models import User
from app.services.providers.models import Provider, Technician
from app.services.providers.repository import ProvidersRepository
from app.services.providers.schemas import (
    CreateTechnicianRequest,
    ProviderConfiguredServiceSummaryResponse,
    ProviderOnboardingRequest,
    ProviderOwnerResponse,
    ProviderResponse,
    TechnicianResponse,
    UpdateOwnProviderRequest,
    UpdateProviderOperationsRequest,
    UpdateTechnicianRequest,
)


class ProvidersService:
    def __init__(self, repository: ProvidersRepository) -> None:
        self.repository = repository

    def onboard_provider(self, payload: ProviderOnboardingRequest) -> ProviderResponse:
        normalized_email = payload.admin_user.email.strip().lower()

        existing_user = self.repository.get_user_by_email(normalized_email)
        if existing_user is not None:
            raise ConflictException("A user with this email already exists.")

        provider_admin_role = self.repository.get_role_by_code(ROLE_PROVIDER_ADMIN)
        if provider_admin_role is None:
            raise NotFoundException("PROVIDER_ADMIN role was not found.")

        provider_type = payload.provider.provider_type.strip().upper()
        if provider_type not in (
            PROVIDER_TYPE_INDEPENDENT_MECHANIC,
            PROVIDER_TYPE_WORKSHOP,
        ):
            raise ConflictException("Invalid provider type.")

        new_owner_user = User(
            email=normalized_email,
            password_hash=hash_password(payload.admin_user.password),
            first_name=payload.admin_user.first_name.strip(),
            last_name=payload.admin_user.last_name.strip(),
            phone_number=payload.admin_user.phone_number.strip() if payload.admin_user.phone_number else None,
            is_active=True,
            is_superuser=False,
            roles=[provider_admin_role],
        )

        created_owner_user = self.repository.create_user(new_owner_user)

        new_provider = Provider(
            owner_user_id=created_owner_user.id,
            provider_type=provider_type,
            business_name=payload.provider.business_name.strip(),
            legal_name=payload.provider.legal_name.strip() if payload.provider.legal_name else None,
            description=payload.provider.description.strip() if payload.provider.description else None,
            contact_email=payload.provider.contact_email.strip().lower() if payload.provider.contact_email else None,
            contact_phone=payload.provider.contact_phone.strip() if payload.provider.contact_phone else None,
            city=payload.provider.city.strip() if payload.provider.city else None,
            address=payload.provider.address.strip() if payload.provider.address else None,
            base_latitude=payload.provider.base_latitude,
            base_longitude=payload.provider.base_longitude,
            is_active=True,
            is_available=True,
            max_concurrent_services=payload.provider.max_concurrent_services,
            current_active_services=0,
            average_rating=0.0,
        )

        created_provider = self.repository.create_provider(new_provider)
        return self._build_provider_response(created_provider)

    def list_providers(self, limit: int = 50, offset: int = 0) -> list[ProviderResponse]:
        providers = self.repository.list_providers(limit=limit, offset=offset)
        return [self._build_provider_response(provider) for provider in providers]

    def get_provider_by_id(self, provider_id: str) -> ProviderResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        return self._build_provider_response(provider)

    def get_my_provider(self, current_user: User) -> ProviderResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        return self._build_provider_response(provider)

    def update_my_provider(self, current_user: User, payload: UpdateOwnProviderRequest) -> ProviderResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        if payload.business_name is not None:
            provider.business_name = payload.business_name.strip()

        if payload.legal_name is not None:
            cleaned_value = payload.legal_name.strip()
            provider.legal_name = cleaned_value or None

        if payload.description is not None:
            cleaned_value = payload.description.strip()
            provider.description = cleaned_value or None

        if payload.contact_email is not None:
            cleaned_value = payload.contact_email.strip().lower()
            provider.contact_email = cleaned_value or None

        if payload.contact_phone is not None:
            cleaned_value = payload.contact_phone.strip()
            provider.contact_phone = cleaned_value or None

        if payload.city is not None:
            cleaned_value = payload.city.strip()
            provider.city = cleaned_value or None

        if payload.address is not None:
            cleaned_value = payload.address.strip()
            provider.address = cleaned_value or None

        if payload.base_latitude is not None:
            provider.base_latitude = payload.base_latitude

        if payload.base_longitude is not None:
            provider.base_longitude = payload.base_longitude

        if payload.is_available is not None:
            provider.is_available = payload.is_available

        if payload.max_concurrent_services is not None:
            provider.max_concurrent_services = payload.max_concurrent_services

        if provider.current_active_services > provider.max_concurrent_services:
            raise ConflictException(
                "Current active services cannot be greater than max concurrent services."
            )

        updated_provider = self.repository.save_provider(provider)
        return self._build_provider_response(updated_provider)

    def update_provider_operations(
        self,
        provider_id: str,
        payload: UpdateProviderOperationsRequest,
    ) -> ProviderResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        if payload.is_active is not None:
            provider.is_active = payload.is_active

        if payload.is_available is not None:
            provider.is_available = payload.is_available

        if payload.max_concurrent_services is not None:
            provider.max_concurrent_services = payload.max_concurrent_services

        if payload.current_active_services is not None:
            provider.current_active_services = payload.current_active_services

        if provider.current_active_services > provider.max_concurrent_services:
            raise ConflictException(
                "Current active services cannot be greater than max concurrent services."
            )

        updated_provider = self.repository.save_provider(provider)
        return self._build_provider_response(updated_provider)

    def list_my_technicians(self, current_user: User) -> list[TechnicianResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        technicians = self.repository.list_technicians_by_provider_id(str(provider.id))
        return [self._build_technician_response(item) for item in technicians]

    def list_provider_technicians(self, provider_id: str) -> list[TechnicianResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        technicians = self.repository.list_technicians_by_provider_id(provider_id)
        return [self._build_technician_response(item) for item in technicians]

    def create_my_technician(
        self,
        current_user: User,
        payload: CreateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        new_technician = Technician(
            provider_id=provider.id,
            first_name=payload.first_name.strip(),
            last_name=payload.last_name.strip(),
            phone_number=payload.phone_number.strip() if payload.phone_number else None,
            specialty=payload.specialty.strip() if payload.specialty else None,
            is_active=True,
            is_available=payload.is_available,
            current_latitude=payload.current_latitude,
            current_longitude=payload.current_longitude,
        )

        created_technician = self.repository.create_technician(new_technician)
        return self._build_technician_response(created_technician)

    def create_provider_technician(
        self,
        provider_id: str,
        payload: CreateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        new_technician = Technician(
            provider_id=provider.id,
            first_name=payload.first_name.strip(),
            last_name=payload.last_name.strip(),
            phone_number=payload.phone_number.strip() if payload.phone_number else None,
            specialty=payload.specialty.strip() if payload.specialty else None,
            is_active=True,
            is_available=payload.is_available,
            current_latitude=payload.current_latitude,
            current_longitude=payload.current_longitude,
        )

        created_technician = self.repository.create_technician(new_technician)
        return self._build_technician_response(created_technician)

    def update_my_technician(
        self,
        current_user: User,
        technician_id: str,
        payload: UpdateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        technician = self.repository.get_technician_by_id(technician_id)
        if technician is None:
            raise NotFoundException("Technician not found.")

        if str(technician.provider_id) != str(provider.id):
            raise ForbiddenException("This technician does not belong to your provider.")

        updated_technician = self._apply_technician_changes(technician, payload)
        saved_technician = self.repository.save_technician(updated_technician)
        return self._build_technician_response(saved_technician)

    def update_provider_technician(
        self,
        provider_id: str,
        technician_id: str,
        payload: UpdateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        technician = self.repository.get_technician_by_id(technician_id)
        if technician is None:
            raise NotFoundException("Technician not found.")

        if str(technician.provider_id) != str(provider.id):
            raise ConflictException("Technician does not belong to the selected provider.")

        updated_technician = self._apply_technician_changes(technician, payload)
        saved_technician = self.repository.save_technician(updated_technician)
        return self._build_technician_response(saved_technician)

    def _apply_technician_changes(
        self,
        technician: Technician,
        payload: UpdateTechnicianRequest,
    ) -> Technician:
        if payload.first_name is not None:
            technician.first_name = payload.first_name.strip()

        if payload.last_name is not None:
            technician.last_name = payload.last_name.strip()

        if payload.phone_number is not None:
            cleaned_value = payload.phone_number.strip()
            technician.phone_number = cleaned_value or None

        if payload.specialty is not None:
            cleaned_value = payload.specialty.strip()
            technician.specialty = cleaned_value or None

        if payload.is_active is not None:
            technician.is_active = payload.is_active

        if payload.is_available is not None:
            technician.is_available = payload.is_available

        if payload.current_latitude is not None:
            technician.current_latitude = payload.current_latitude

        if payload.current_longitude is not None:
            technician.current_longitude = payload.current_longitude

        return technician

    def _build_provider_response(self, provider: Provider) -> ProviderResponse:
        owner_user = provider.owner_user

        technicians = list(provider.technicians)
        available_technicians_count = sum(
            1 for technician in technicians if technician.is_available and technician.is_active
        )

        active_provider_services = []
        for provider_service in provider.provider_services:
            catalog_item = provider_service.service_catalog_item
            if not provider_service.is_active:
                continue
            if catalog_item is None or not catalog_item.is_active:
                continue

            price_estimate_min = (
                float(provider_service.price_estimate_min)
                if provider_service.price_estimate_min is not None
                else None
            )
            price_estimate_max = (
                float(provider_service.price_estimate_max)
                if provider_service.price_estimate_max is not None
                else None
            )

            active_provider_services.append(
                ProviderConfiguredServiceSummaryResponse(
                    id=str(provider_service.id),
                    service_catalog_item_id=str(provider_service.service_catalog_item_id),
                    code=catalog_item.code,
                    category=catalog_item.category,
                    title=provider_service.effective_title,
                    price_estimate_min=price_estimate_min,
                    price_estimate_max=price_estimate_max,
                    estimated_duration_minutes=provider_service.estimated_duration_minutes,
                    is_mobile_service_enabled=provider_service.is_mobile_service_enabled,
                    is_emergency_service_enabled=provider_service.is_emergency_service_enabled,
                    is_active=provider_service.is_active,
                )
            )

        owner_payload = ProviderOwnerResponse(
            id=str(owner_user.id),
            email=owner_user.email,
            first_name=owner_user.first_name,
            last_name=owner_user.last_name,
            full_name=owner_user.full_name,
            phone_number=owner_user.phone_number,
            is_active=owner_user.is_active,
        )

        return ProviderResponse(
            id=str(provider.id),
            owner_user_id=str(provider.owner_user_id),
            provider_type=provider.provider_type,
            business_name=provider.business_name,
            legal_name=provider.legal_name,
            description=provider.description,
            contact_email=provider.contact_email,
            contact_phone=provider.contact_phone,
            city=provider.city,
            address=provider.address,
            base_latitude=provider.base_latitude,
            base_longitude=provider.base_longitude,
            is_active=provider.is_active,
            is_available=provider.is_available,
            max_concurrent_services=provider.max_concurrent_services,
            current_active_services=provider.current_active_services,
            available_capacity=provider.available_capacity,
            average_rating=provider.average_rating,
            owner_user=owner_payload,
            technicians_count=len(technicians),
            available_technicians_count=available_technicians_count,
            configured_services_count=len(provider.provider_services),
            active_services_count=len(active_provider_services),
            active_services=active_provider_services,
            created_at=provider.created_at,
            updated_at=provider.updated_at,
        )

    def _build_technician_response(self, technician: Technician) -> TechnicianResponse:
        return TechnicianResponse(
            id=str(technician.id),
            provider_id=str(technician.provider_id),
            first_name=technician.first_name,
            last_name=technician.last_name,
            full_name=technician.full_name,
            phone_number=technician.phone_number,
            specialty=technician.specialty,
            is_active=technician.is_active,
            is_available=technician.is_available,
            current_latitude=technician.current_latitude,
            current_longitude=technician.current_longitude,
            created_at=technician.created_at,
            updated_at=technician.updated_at,
        )
