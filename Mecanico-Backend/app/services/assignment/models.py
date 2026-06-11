from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentAssignmentCandidate(Base):
    __tablename__ = "incident_assignment_candidates"
    __table_args__ = (
        UniqueConstraint(
            "incident_id",
            "provider_id",
            name="uq_incident_assignment_candidate_incident_provider",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    recommendation_rank: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    score: Mapped[float] = mapped_column(Float, nullable=False)

    distance_km: Mapped[float | None] = mapped_column(Float, nullable=True)

    required_service_codes_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    matched_service_codes_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    rationale_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    provider_average_rating_snapshot: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    provider_available_capacity_snapshot: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    available_technicians_count_snapshot: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    responded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

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
    provider = relationship("Provider", lazy="selectin")
