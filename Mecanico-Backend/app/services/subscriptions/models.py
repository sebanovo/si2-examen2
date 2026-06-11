from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ProviderSubscriptionPlan(Base):
    __tablename__ = "provider_subscription_plans"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    code: Mapped[str] = mapped_column(String(60), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    billing_period: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    price_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=False, default="BOB", server_default="BOB")

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    auto_renews: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    provider = relationship("Provider", lazy="selectin")
    coverages = relationship(
        "ProviderSubscriptionPlanCoverage",
        back_populates="plan",
        lazy="selectin",
        cascade="all, delete-orphan",
    )


class ProviderSubscriptionPlanCoverage(Base):
    __tablename__ = "provider_subscription_plan_coverages"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    plan_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plans.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    service_catalog_item_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    incident_category: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)

    coverage_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    coverage_value: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    max_coverage_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    waiting_period_days: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    max_applications_per_subscription: Mapped[int | None] = mapped_column(Integer, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    plan = relationship("ProviderSubscriptionPlan", back_populates="coverages", lazy="selectin")
    service_catalog_item = relationship("ServiceCatalogItem", lazy="selectin")


class ClientPlanSubscription(Base):
    __tablename__ = "client_plan_subscriptions"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    client_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    plan_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plans.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    external_reference: Mapped[str | None] = mapped_column(String(120), nullable=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    client_user = relationship("User", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    plan = relationship("ProviderSubscriptionPlan", lazy="selectin")


class IncidentSubscriptionApplication(Base):
    __tablename__ = "incident_subscription_applications"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    incident_billing_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incident_billings.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    client_plan_subscription_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("client_plan_subscriptions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    plan_coverage_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plan_coverages.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    matched_service_catalog_item_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="SET NULL"),
        nullable=True,
    )

    matched_incident_category: Mapped[str | None] = mapped_column(String(50), nullable=True)
    coverage_type: Mapped[str] = mapped_column(String(30), nullable=False)
    coverage_value: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    original_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    coverage_applied_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    client_payable_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    snapshot_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    applied_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    incident_billing = relationship("IncidentBilling", lazy="selectin")
    client_plan_subscription = relationship("ClientPlanSubscription", lazy="selectin")
    plan_coverage = relationship("ProviderSubscriptionPlanCoverage", lazy="selectin")
    matched_service_catalog_item = relationship("ServiceCatalogItem", lazy="selectin")
