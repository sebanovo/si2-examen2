from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.catalog.models import ProviderService, ServiceCatalogItem
from app.services.catalog.repository import CatalogRepository
from app.services.catalog.schemas import (
    CreateServiceCatalogItemRequest,
    ProviderCatalogAvailabilityResponse,
    ProviderServiceResponse,
    ServiceCatalogItemResponse,
    UpdateProviderServiceRequest,
    UpdateServiceCatalogItemRequest,
    UpsertProviderServiceRequest,
)


class CatalogService:
    def __init__(self, repository: CatalogRepository) -> None:
        self.repository = repository

    def create_service_catalog_item(
        self,
        payload: CreateServiceCatalogItemRequest,
    ) -> ServiceCatalogItemResponse:
        existing_item = self.repository.get_service_catalog_item_by_code(payload.code)
        if existing_item is not None:
            raise ConflictException("A catalog service with this code already exists.")

        item = ServiceCatalogItem(
            code=payload.code,
            category=payload.category,
            title=payload.title.strip(),
            description=payload.description.strip() if payload.description else None,
            supports_mobile_service=payload.supports_mobile_service,
            supports_emergency_service=payload.supports_emergency_service,
            is_active=payload.is_active,
            sort_order=payload.sort_order,
        )

        created_item = self.repository.create_service_catalog_item(item)
        return self._build_service_catalog_item_response(created_item)

    def list_service_catalog_items(self, include_inactive: bool = False) -> list[ServiceCatalogItemResponse]:
        items = self.repository.list_service_catalog_items(include_inactive=include_inactive)
        return [self._build_service_catalog_item_response(item) for item in items]

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItemResponse:
        item = self.repository.get_service_catalog_item_by_id(service_catalog_item_id)
        if item is None:
            raise NotFoundException("Catalog service not found.")

        return self._build_service_catalog_item_response(item)

    def update_service_catalog_item(
        self,
        service_catalog_item_id: str,
        payload: UpdateServiceCatalogItemRequest,
    ) -> ServiceCatalogItemResponse:
        item = self.repository.get_service_catalog_item_by_id(service_catalog_item_id)
        if item is None:
            raise NotFoundException("Catalog service not found.")

        if "category" in payload.model_fields_set:
            item.category = payload.category if payload.category is not None else item.category

        if "title" in payload.model_fields_set and payload.title is not None:
            item.title = payload.title.strip()

        if "description" in payload.model_fields_set:
            item.description = self._normalize_nullable_text(payload.description)

        if "supports_mobile_service" in payload.model_fields_set:
            item.supports_mobile_service = bool(payload.supports_mobile_service)

        if "supports_emergency_service" in payload.model_fields_set:
            item.supports_emergency_service = bool(payload.supports_emergency_service)

        if "is_active" in payload.model_fields_set:
            item.is_active = bool(payload.is_active)

        if "sort_order" in payload.model_fields_set and payload.sort_order is not None:
            item.sort_order = payload.sort_order

        updated_item = self.repository.save_service_catalog_item(item)
        return self._build_service_catalog_item_response(updated_item)

    def list_provider_services_for_platform(self, provider_id: str) -> list[ProviderServiceResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=provider_id,
            include_inactive=True,
        )
        return [self._build_provider_service_response(item) for item in provider_services]

    def list_my_catalog_with_configuration(
        self,
        current_user: User,
        include_inactive_catalog: bool = False,
    ) -> list[ProviderCatalogAvailabilityResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        catalog_items = self.repository.list_service_catalog_items(
            include_inactive=include_inactive_catalog,
        )
        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=str(provider.id),
            include_inactive=True,
        )
        provider_services_by_catalog_item_id = {
            str(item.service_catalog_item_id): item for item in provider_services
        }

        results: list[ProviderCatalogAvailabilityResponse] = []
        for catalog_item in catalog_items:
            provider_service = provider_services_by_catalog_item_id.get(str(catalog_item.id))
            results.append(
                ProviderCatalogAvailabilityResponse(
                    catalog_item=self._build_service_catalog_item_response(catalog_item),
                    provider_service=(
                        self._build_provider_service_response(provider_service)
                        if provider_service is not None
                        else None
                    ),
                    is_configured=provider_service is not None,
                )
            )

        return results

    def list_my_provider_services(self, current_user: User) -> list[ProviderServiceResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=str(provider.id),
            include_inactive=True,
        )
        return [self._build_provider_service_response(item) for item in provider_services]

    def upsert_my_provider_service(
        self,
        current_user: User,
        payload: UpsertProviderServiceRequest,
    ) -> ProviderServiceResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        catalog_item = self.repository.get_service_catalog_item_by_id(payload.service_catalog_item_id)
        if catalog_item is None:
            raise NotFoundException("Catalog service not found.")

        if not catalog_item.is_active and payload.is_active:
            raise ConflictException("Inactive catalog services cannot be enabled for providers.")

        self._validate_service_capabilities(
            catalog_item=catalog_item,
            is_mobile_service_enabled=payload.is_mobile_service_enabled,
            is_emergency_service_enabled=payload.is_emergency_service_enabled,
        )

        existing_provider_service = self.repository.get_provider_service_by_provider_and_catalog_item(
            provider_id=str(provider.id),
            service_catalog_item_id=payload.service_catalog_item_id,
        )

        if existing_provider_service is not None:
            existing_provider_service.custom_title = self._normalize_nullable_text(payload.custom_title)
            existing_provider_service.custom_description = self._normalize_nullable_text(
                payload.custom_description
            )
            existing_provider_service.price_estimate_min = payload.price_estimate_min
            existing_provider_service.price_estimate_max = payload.price_estimate_max
            existing_provider_service.estimated_duration_minutes = payload.estimated_duration_minutes
            existing_provider_service.is_mobile_service_enabled = payload.is_mobile_service_enabled
            existing_provider_service.is_emergency_service_enabled = payload.is_emergency_service_enabled
            existing_provider_service.is_active = payload.is_active

            updated_provider_service = self.repository.save_provider_service(existing_provider_service)
            return self._build_provider_service_response(updated_provider_service)

        provider_service = ProviderService(
            provider_id=provider.id,
            service_catalog_item_id=catalog_item.id,
            custom_title=self._normalize_nullable_text(payload.custom_title),
            custom_description=self._normalize_nullable_text(payload.custom_description),
            price_estimate_min=payload.price_estimate_min,
            price_estimate_max=payload.price_estimate_max,
            estimated_duration_minutes=payload.estimated_duration_minutes,
            is_mobile_service_enabled=payload.is_mobile_service_enabled,
            is_emergency_service_enabled=payload.is_emergency_service_enabled,
            is_active=payload.is_active,
        )

        created_provider_service = self.repository.create_provider_service(provider_service)
        return self._build_provider_service_response(created_provider_service)

    def update_my_provider_service(
        self,
        current_user: User,
        provider_service_id: str,
        payload: UpdateProviderServiceRequest,
    ) -> ProviderServiceResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        provider_service = self.repository.get_provider_service_by_id(provider_service_id)
        if provider_service is None:
            raise NotFoundException("Provider service configuration not found.")

        if str(provider_service.provider_id) != str(provider.id):
            raise ForbiddenException("This provider service configuration does not belong to your provider.")

        catalog_item = provider_service.service_catalog_item

        next_mobile_value = (
            payload.is_mobile_service_enabled
            if payload.is_mobile_service_enabled is not None
            else provider_service.is_mobile_service_enabled
        )
        next_emergency_value = (
            payload.is_emergency_service_enabled
            if payload.is_emergency_service_enabled is not None
            else provider_service.is_emergency_service_enabled
        )

        self._validate_service_capabilities(
            catalog_item=catalog_item,
            is_mobile_service_enabled=next_mobile_value,
            is_emergency_service_enabled=next_emergency_value,
        )

        if payload.is_active is not None and payload.is_active and not catalog_item.is_active:
            raise ConflictException("Inactive catalog services cannot be enabled for providers.")

        if "custom_title" in payload.model_fields_set:
            provider_service.custom_title = self._normalize_nullable_text(payload.custom_title)

        if "custom_description" in payload.model_fields_set:
            provider_service.custom_description = self._normalize_nullable_text(payload.custom_description)

        if "price_estimate_min" in payload.model_fields_set:
            provider_service.price_estimate_min = payload.price_estimate_min

        if "price_estimate_max" in payload.model_fields_set:
            provider_service.price_estimate_max = payload.price_estimate_max

        if "estimated_duration_minutes" in payload.model_fields_set:
            provider_service.estimated_duration_minutes = payload.estimated_duration_minutes

        if "is_mobile_service_enabled" in payload.model_fields_set:
            provider_service.is_mobile_service_enabled = bool(payload.is_mobile_service_enabled)

        if "is_emergency_service_enabled" in payload.model_fields_set:
            provider_service.is_emergency_service_enabled = bool(payload.is_emergency_service_enabled)

        if "is_active" in payload.model_fields_set:
            provider_service.is_active = bool(payload.is_active)

        if (
            provider_service.price_estimate_min is not None
            and provider_service.price_estimate_max is not None
            and provider_service.price_estimate_max < provider_service.price_estimate_min
        ):
            raise ConflictException(
                "price_estimate_max cannot be lower than price_estimate_min."
            )

        updated_provider_service = self.repository.save_provider_service(provider_service)
        return self._build_provider_service_response(updated_provider_service)

    def _validate_service_capabilities(
        self,
        catalog_item: ServiceCatalogItem,
        is_mobile_service_enabled: bool,
        is_emergency_service_enabled: bool,
    ) -> None:
        if is_mobile_service_enabled and not catalog_item.supports_mobile_service:
            raise ConflictException(
                "This catalog service does not allow mobile service activation."
            )

        if is_emergency_service_enabled and not catalog_item.supports_emergency_service:
            raise ConflictException(
                "This catalog service does not allow emergency service activation."
            )

    def _build_service_catalog_item_response(
        self,
        item: ServiceCatalogItem,
    ) -> ServiceCatalogItemResponse:
        return ServiceCatalogItemResponse(
            id=str(item.id),
            code=item.code,
            category=item.category,
            title=item.title,
            description=item.description,
            supports_mobile_service=item.supports_mobile_service,
            supports_emergency_service=item.supports_emergency_service,
            is_active=item.is_active,
            sort_order=item.sort_order,
            created_at=item.created_at,
            updated_at=item.updated_at,
        )

    def _build_provider_service_response(
        self,
        provider_service: ProviderService,
    ) -> ProviderServiceResponse:
        catalog_item = provider_service.service_catalog_item

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

        return ProviderServiceResponse(
            id=str(provider_service.id),
            provider_id=str(provider_service.provider_id),
            service_catalog_item_id=str(provider_service.service_catalog_item_id),
            service_code=catalog_item.code,
            service_category=catalog_item.category,
            catalog_title=catalog_item.title,
            catalog_description=catalog_item.description,
            custom_title=provider_service.custom_title,
            custom_description=provider_service.custom_description,
            effective_title=provider_service.effective_title,
            effective_description=provider_service.effective_description,
            price_estimate_min=price_estimate_min,
            price_estimate_max=price_estimate_max,
            estimated_duration_minutes=provider_service.estimated_duration_minutes,
            supports_mobile_service=catalog_item.supports_mobile_service,
            supports_emergency_service=catalog_item.supports_emergency_service,
            is_mobile_service_enabled=provider_service.is_mobile_service_enabled,
            is_emergency_service_enabled=provider_service.is_emergency_service_enabled,
            is_active=provider_service.is_active,
            created_at=provider_service.created_at,
            updated_at=provider_service.updated_at,
        )

    def _normalize_nullable_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None
