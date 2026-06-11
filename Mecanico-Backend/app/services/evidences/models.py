from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentEvidence(Base):
    __tablename__ = "incident_evidences"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    uploaded_by_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    evidence_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    original_filename: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stored_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_extension: Mapped[str | None] = mapped_column(String(20), nullable=True)
    mime_type: Mapped[str | None] = mapped_column(String(120), nullable=True)
    file_size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    text_content_snapshot: Mapped[str | None] = mapped_column(Text, nullable=True)

    storage_provider: Mapped[str] = mapped_column(String(30), nullable=False, default="local", index=True)
    storage_bucket: Mapped[str | None] = mapped_column(String(255), nullable=True)
    storage_object_key: Mapped[str | None] = mapped_column(Text, nullable=True)
    public_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    absolute_file_path: Mapped[str | None] = mapped_column(Text, nullable=True)

    audio_processing_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    audio_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    transcript_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript_language_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    transcript_confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    transcript_segments_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    audio_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    audio_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    image_processing_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    image_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    image_labels_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    image_detections_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    image_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    image_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

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

    incident = relationship("Incident", lazy="selectin")
    uploaded_by_user = relationship("User", lazy="selectin")
