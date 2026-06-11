from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.catalog.models import ProviderService, ServiceCatalogItem
from app.services.providers.models import Provider


class CatalogRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_service_catalog_item(self, item: ServiceCatalogItem) -> ServiceCatalogItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def save_service_catalog_item(self, item: ServiceCatalogItem) -> ServiceCatalogItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = select(ServiceCatalogItem).where(
            ServiceCatalogItem.id == service_catalog_item_id
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_service_catalog_item_by_code(self, code: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = select(ServiceCatalogItem).where(
            ServiceCatalogItem.code == code
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_service_catalog_items(
        self,
        include_inactive: bool = False,
    ) -> list[ServiceCatalogItem]:
        query = select(ServiceCatalogItem)

        if not include_inactive:
            query = query.where(ServiceCatalogItem.is_active.is_(True))

        query = query.order_by(ServiceCatalogItem.sort_order.asc(), ServiceCatalogItem.title.asc())
        return list(self.db.execute(query).scalars().all())

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.id == provider_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_provider_service(self, provider_service: ProviderService) -> ProviderService:
        self.db.add(provider_service)
        self.db.commit()
        self.db.refresh(provider_service)
        return provider_service

    def save_provider_service(self, provider_service: ProviderService) -> ProviderService:
        self.db.add(provider_service)
        self.db.commit()
        self.db.refresh(provider_service)
        return provider_service

    def get_provider_service_by_id(self, provider_service_id: str) -> ProviderService | None:
        query: Select[tuple[ProviderService]] = select(ProviderService).where(
            ProviderService.id == provider_service_id
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_service_by_provider_and_catalog_item(
        self,
        provider_id: str,
        service_catalog_item_id: str,
    ) -> ProviderService | None:
        query: Select[tuple[ProviderService]] = select(ProviderService).where(
            ProviderService.provider_id == provider_id,
            ProviderService.service_catalog_item_id == service_catalog_item_id,
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_services_by_provider_id(
        self,
        provider_id: str,
        include_inactive: bool = True,
    ) -> list[ProviderService]:
        query = (
            select(ProviderService)
            .where(ProviderService.provider_id == provider_id)
            .order_by(ProviderService.created_at.asc())
        )

        if not include_inactive:
            query = query.where(ProviderService.is_active.is_(True))

        return list(self.db.execute(query).scalars().all())
