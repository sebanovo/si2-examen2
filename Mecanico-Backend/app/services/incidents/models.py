from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    client_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    vehicle_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vehicles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    assigned_technician_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("technicians.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    priority: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    reported_category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    client_contact_phone_snapshot: Mapped[str | None] = mapped_column(String(30), nullable=True)

    incident_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    incident_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    address_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)

    estimated_price_min: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_price_max: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)

    ai_summary_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    summary_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    structured_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    suggested_category: Mapped[str | None] = mapped_column(String(50), nullable=True)
    suggested_priority: Mapped[str | None] = mapped_column(String(30), nullable=True)
    requires_more_information: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    summary_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    summary_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    dispatch_mode: Mapped[str | None] = mapped_column(String(30), nullable=True)

    responder_last_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    responder_last_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    responder_last_source_type: Mapped[str | None] = mapped_column(String(30), nullable=True)
    responder_last_recorded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    route_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    route_distance_meters: Mapped[float | None] = mapped_column(Float, nullable=True)
    route_duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    route_eta_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    route_polyline: Mapped[str | None] = mapped_column(Text, nullable=True)
    route_last_calculated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    route_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    requested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    assigned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    en_route_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    arrived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

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

    client_user = relationship("User", lazy="selectin")
    vehicle = relationship("Vehicle", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    assigned_technician = relationship(
        "Technician",
        lazy="selectin",
        foreign_keys="Incident.assigned_technician_id",
    )
