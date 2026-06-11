"""evidences base

Revision ID: 202604050005
Revises: 202604050004
Create Date: 2026-04-05 04:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050005"
down_revision = "202604050004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "incident_evidences",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("uploaded_by_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("evidence_type", sa.String(length=30), nullable=False),
        sa.Column("original_filename", sa.String(length=255), nullable=True),
        sa.Column("stored_filename", sa.String(length=255), nullable=False),
        sa.Column("file_extension", sa.String(length=20), nullable=True),
        sa.Column("mime_type", sa.String(length=120), nullable=True),
        sa.Column("file_size_bytes", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("absolute_file_path", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["uploaded_by_user_id"], ["users.id"], ondelete="SET NULL"),
    )

    op.create_index("ix_incident_evidences_incident_id", "incident_evidences", ["incident_id"], unique=False)
    op.create_index("ix_incident_evidences_uploaded_by_user_id", "incident_evidences", ["uploaded_by_user_id"], unique=False)
    op.create_index("ix_incident_evidences_evidence_type", "incident_evidences", ["evidence_type"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_incident_evidences_evidence_type", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_uploaded_by_user_id", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_incident_id", table_name="incident_evidences")
    op.drop_table("incident_evidences")