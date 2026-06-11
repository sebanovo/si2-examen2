"""provider ratings

Revision ID: 202604050018
Revises: 202604050017
Create Date: 2026-04-28 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050018"
down_revision = "202604050017"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "provider_ratings",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("client_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("technician_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("rating_score", sa.Integer(), nullable=False),
        sa.Column("punctuality_score", sa.Integer(), nullable=True),
        sa.Column("service_quality_score", sa.Integer(), nullable=True),
        sa.Column("communication_score", sa.Integer(), nullable=True),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column("would_recommend", sa.Boolean(), nullable=True),
        sa.Column("provider_average_after_rating", sa.Float(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["client_user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["technician_id"], ["technicians.id"], ondelete="SET NULL"),
        sa.UniqueConstraint(
            "incident_id",
            "client_user_id",
            name="uq_provider_ratings_incident_client",
        ),
    )

    op.create_index("ix_provider_ratings_incident_id", "provider_ratings", ["incident_id"], unique=False)
    op.create_index("ix_provider_ratings_client_user_id", "provider_ratings", ["client_user_id"], unique=False)
    op.create_index("ix_provider_ratings_provider_id", "provider_ratings", ["provider_id"], unique=False)
    op.create_index("ix_provider_ratings_technician_id", "provider_ratings", ["technician_id"], unique=False)
    op.create_index("ix_provider_ratings_rating_score", "provider_ratings", ["rating_score"], unique=False)
    op.create_index("ix_provider_ratings_created_at", "provider_ratings", ["created_at"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_provider_ratings_created_at", table_name="provider_ratings")
    op.drop_index("ix_provider_ratings_rating_score", table_name="provider_ratings")
    op.drop_index("ix_provider_ratings_technician_id", table_name="provider_ratings")
    op.drop_index("ix_provider_ratings_provider_id", table_name="provider_ratings")
    op.drop_index("ix_provider_ratings_client_user_id", table_name="provider_ratings")
    op.drop_index("ix_provider_ratings_incident_id", table_name="provider_ratings")
    op.drop_table("provider_ratings")