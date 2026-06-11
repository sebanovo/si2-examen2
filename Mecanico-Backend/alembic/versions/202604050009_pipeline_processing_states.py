"""pipeline processing states

Revision ID: 202604050009
Revises: 202604050008
Create Date: 2026-04-17 01:10:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "202604050009"
down_revision = "202604050008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "incident_evidences",
        sa.Column("text_content_snapshot", sa.Text(), nullable=True),
    )

    op.add_column(
        "incident_evidences",
        sa.Column(
            "audio_processing_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_text", sa.Text(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_language_code", sa.String(length=20), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_confidence", sa.Float(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_segments_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_error_message", sa.Text(), nullable=True),
    )

    op.add_column(
        "incident_evidences",
        sa.Column(
            "image_processing_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_labels_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_detections_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_error_message", sa.Text(), nullable=True),
    )

    op.create_index(
        "ix_incident_evidences_audio_processing_status",
        "incident_evidences",
        ["audio_processing_status"],
        unique=False,
    )
    op.create_index(
        "ix_incident_evidences_image_processing_status",
        "incident_evidences",
        ["image_processing_status"],
        unique=False,
    )

    op.add_column(
        "incidents",
        sa.Column(
            "ai_summary_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("structured_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("suggested_category", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("suggested_priority", sa.String(length=30), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("requires_more_information", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_error_message", sa.Text(), nullable=True),
    )

    op.create_index(
        "ix_incidents_ai_summary_status",
        "incidents",
        ["ai_summary_status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_incidents_ai_summary_status", table_name="incidents")
    op.drop_column("incidents", "summary_error_message")
    op.drop_column("incidents", "summary_processed_at")
    op.drop_column("incidents", "requires_more_information")
    op.drop_column("incidents", "suggested_priority")
    op.drop_column("incidents", "suggested_category")
    op.drop_column("incidents", "structured_summary")
    op.drop_column("incidents", "summary_provider_name")
    op.drop_column("incidents", "ai_summary_status")

    op.drop_index("ix_incident_evidences_image_processing_status", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_audio_processing_status", table_name="incident_evidences")

    op.drop_column("incident_evidences", "image_error_message")
    op.drop_column("incident_evidences", "image_processed_at")
    op.drop_column("incident_evidences", "image_summary")
    op.drop_column("incident_evidences", "image_detections_json")
    op.drop_column("incident_evidences", "image_labels_json")
    op.drop_column("incident_evidences", "image_provider_name")
    op.drop_column("incident_evidences", "image_processing_status")

    op.drop_column("incident_evidences", "audio_error_message")
    op.drop_column("incident_evidences", "audio_processed_at")
    op.drop_column("incident_evidences", "transcript_segments_json")
    op.drop_column("incident_evidences", "transcript_confidence")
    op.drop_column("incident_evidences", "transcript_language_code")
    op.drop_column("incident_evidences", "transcript_text")
    op.drop_column("incident_evidences", "audio_provider_name")
    op.drop_column("incident_evidences", "audio_processing_status")

    op.drop_column("incident_evidences", "text_content_snapshot")
