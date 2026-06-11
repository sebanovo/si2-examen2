"""assignment candidates

Revision ID: 202604050010
Revises: 202604050009
Create Date: 2026-04-17 02:20:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050010"
down_revision = "202604050009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "incident_assignment_candidates",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("recommendation_rank", sa.Integer(), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("distance_km", sa.Float(), nullable=True),
        sa.Column("required_service_codes_json", sa.JSON(), nullable=True),
        sa.Column("matched_service_codes_json", sa.JSON(), nullable=True),
        sa.Column("rationale_json", sa.JSON(), nullable=True),
        sa.Column("provider_average_rating_snapshot", sa.Float(), nullable=False, server_default="0"),
        sa.Column("provider_available_capacity_snapshot", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("available_technicians_count_snapshot", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("responded_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.UniqueConstraint(
            "incident_id",
            "provider_id",
            name="uq_incident_assignment_candidate_incident_provider",
        ),
    )

    op.create_index(
        "ix_incident_assignment_candidates_incident_id",
        "incident_assignment_candidates",
        ["incident_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_provider_id",
        "incident_assignment_candidates",
        ["provider_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_status",
        "incident_assignment_candidates",
        ["status"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_recommendation_rank",
        "incident_assignment_candidates",
        ["recommendation_rank"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_incident_assignment_candidates_recommendation_rank",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_status",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_provider_id",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_incident_id",
        table_name="incident_assignment_candidates",
    )
    op.drop_table("incident_assignment_candidates")
