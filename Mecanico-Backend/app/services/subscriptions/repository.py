from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload

from app.services.billing.models import IncidentBilling
from app.services.catalog.models import ServiceCatalogItem
from app.services.incidents.models import Incident
from app.services.providers.models import Provider
from app.services.subscriptions.models import (
    ClientPlanSubscription,
    IncidentSubscriptionApplication,
    ProviderSubscriptionPlan,
    ProviderSubscriptionPlanCoverage,
)


class SubscriptionsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
            .where(Provider.id == provider_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_plans(self, provider_id: str, include_inactive: bool = False) -> list[ProviderSubscriptionPlan]:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .options(
                selectinload(ProviderSubscriptionPlan.provider).selectinload(Provider.owner_user),
                selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ProviderSubscriptionPlan.provider_id == provider_id)
            .order_by(ProviderSubscriptionPlan.created_at.asc())
        )

        if not include_inactive:
            query = query.where(ProviderSubscriptionPlan.is_active.is_(True))

        return list(self.db.execute(query).scalars().all())

    def get_plan_by_id(self, plan_id: str) -> ProviderSubscriptionPlan | None:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .options(
                selectinload(ProviderSubscriptionPlan.provider).selectinload(Provider.owner_user),
                selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ProviderSubscriptionPlan.id == plan_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_by_id_for_update(self, plan_id: str) -> ProviderSubscriptionPlan | None:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .where(ProviderSubscriptionPlan.id == plan_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = (
            select(ServiceCatalogItem).where(ServiceCatalogItem.id == service_catalog_item_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_coverage_by_id(self, coverage_id: str) -> ProviderSubscriptionPlanCoverage | None:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .options(
                selectinload(ProviderSubscriptionPlanCoverage.plan).selectinload(
                    ProviderSubscriptionPlan.provider
                ),
                selectinload(ProviderSubscriptionPlanCoverage.service_catalog_item),
            )
            .where(ProviderSubscriptionPlanCoverage.id == coverage_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_coverage_by_id_for_update(self, coverage_id: str) -> ProviderSubscriptionPlanCoverage | None:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .where(ProviderSubscriptionPlanCoverage.id == coverage_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_plan_coverages(self, plan_id: str) -> list[ProviderSubscriptionPlanCoverage]:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .options(selectinload(ProviderSubscriptionPlanCoverage.service_catalog_item))
            .where(ProviderSubscriptionPlanCoverage.plan_id == plan_id)
            .order_by(ProviderSubscriptionPlanCoverage.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_available_provider_plans_for_client(self, provider_id: str) -> list[ProviderSubscriptionPlan]:
        return self.list_provider_plans(provider_id=provider_id, include_inactive=False)

    def list_client_subscriptions(self, client_user_id: str) -> list[ClientPlanSubscription]:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .options(
                selectinload(ClientPlanSubscription.provider).selectinload(Provider.owner_user),
                selectinload(ClientPlanSubscription.plan).selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ClientPlanSubscription.client_user_id == client_user_id)
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_active_subscription_for_client_and_plan(
        self,
        client_user_id: str,
        plan_id: str,
    ) -> ClientPlanSubscription | None:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .where(
                ClientPlanSubscription.client_user_id == client_user_id,
                ClientPlanSubscription.plan_id == plan_id,
                ClientPlanSubscription.status == "ACTIVE",
            )
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_active_subscriptions_for_client_and_provider(
        self,
        client_user_id: str,
        provider_id: str,
    ) -> list[ClientPlanSubscription]:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .options(
                selectinload(ClientPlanSubscription.plan).selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
                selectinload(ClientPlanSubscription.provider).selectinload(Provider.owner_user),
            )
            .where(
                ClientPlanSubscription.client_user_id == client_user_id,
                ClientPlanSubscription.provider_id == provider_id,
                ClientPlanSubscription.status == "ACTIVE",
            )
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.vehicle),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_billing_by_incident_id(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling).where(IncidentBilling.incident_id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_billing_by_incident_id_for_update(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .where(IncidentBilling.incident_id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_incident_applications(self, incident_id: str) -> list[IncidentSubscriptionApplication]:
        query: Select[tuple[IncidentSubscriptionApplication]] = (
            select(IncidentSubscriptionApplication)
            .options(
                selectinload(IncidentSubscriptionApplication.client_plan_subscription).selectinload(
                    ClientPlanSubscription.plan
                ),
                selectinload(IncidentSubscriptionApplication.plan_coverage).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(IncidentSubscriptionApplication.incident_id == incident_id)
            .order_by(IncidentSubscriptionApplication.applied_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_incident_applications_for_update(self, incident_id: str) -> list[IncidentSubscriptionApplication]:
        query: Select[tuple[IncidentSubscriptionApplication]] = (
            select(IncidentSubscriptionApplication)
            .where(
                IncidentSubscriptionApplication.incident_id == incident_id,
                IncidentSubscriptionApplication.status == "APPLIED",
            )
            .with_for_update()
        )
        return list(self.db.execute(query).scalars().all())

    def count_applied_coverage_usages(
        self,
        subscription_id: str,
        coverage_id: str,
    ) -> int:
        query = (
            select(func.count(IncidentSubscriptionApplication.id))
            .where(
                IncidentSubscriptionApplication.client_plan_subscription_id == subscription_id,
                IncidentSubscriptionApplication.plan_coverage_id == coverage_id,
                IncidentSubscriptionApplication.status == "APPLIED",
            )
        )
        return int(self.db.execute(query).scalar_one() or 0)

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
