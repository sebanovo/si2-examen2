from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ServiceCatalogItem(Base):
    __tablename__ = "service_catalog_items"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(80), nullable=False, unique=True, index=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    supports_mobile_service: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    supports_emergency_service: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    provider_services: Mapped[list["ProviderService"]] = relationship(
        back_populates="service_catalog_item",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class ProviderService(Base):
    __tablename__ = "provider_services"
    __table_args__ = (
        UniqueConstraint(
            "provider_id",
            "service_catalog_item_id",
            name="uq_provider_services_provider_catalog_item",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    service_catalog_item_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    custom_title: Mapped[str | None] = mapped_column(String(150), nullable=True)
    custom_description: Mapped[str | None] = mapped_column(Text, nullable=True)

    price_estimate_min: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    price_estimate_max: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    is_mobile_service_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_emergency_service_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    provider = relationship("Provider", back_populates="provider_services", lazy="selectin")
    service_catalog_item: Mapped[ServiceCatalogItem] = relationship(
        back_populates="provider_services",
        lazy="selectin",
    )

    @property
    def effective_title(self) -> str:
        if self.custom_title and self.custom_title.strip():
            return self.custom_title.strip()
        return self.service_catalog_item.title

    @property
    def effective_description(self) -> str | None:
        if self.custom_description and self.custom_description.strip():
            return self.custom_description.strip()
        return self.service_catalog_item.description