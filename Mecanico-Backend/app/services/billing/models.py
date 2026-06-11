from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentBilling(Base):
    __tablename__ = "incident_billings"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    client_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    currency_code: Mapped[str] = mapped_column(String(10), nullable=False, default="BOB", server_default="BOB")

    estimated_price_min: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_price_max: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    final_price_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    platform_commission_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 4),
        nullable=False,
        default=Decimal("0.1000"),
        server_default="0.1000",
    )
    platform_commission_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    provider_gross_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    provider_net_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    client_plan_subscription_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("client_plan_subscriptions.id", ondelete="SET NULL"),
        nullable=True,
    )
    plan_coverage_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plan_coverages.id", ondelete="SET NULL"),
        nullable=True,
    )
    coverage_applied_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    client_payable_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    payment_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="PENDING_PRICING",
        server_default="PENDING_PRICING",
        index=True,
    )
    payment_method: Mapped[str | None] = mapped_column(String(30), nullable=True)
    payment_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    payment_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)

    checkout_reference: Mapped[str | None] = mapped_column(String(120), nullable=True)
    checkout_payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    pricing_note: Mapped[str | None] = mapped_column(Text, nullable=True)

    pricing_finalized_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    payment_completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

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

    incident = relationship("Incident", lazy="selectin")
    client_user = relationship("User", foreign_keys=[client_user_id], lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
