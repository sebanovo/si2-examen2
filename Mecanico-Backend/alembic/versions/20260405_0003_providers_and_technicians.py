"""providers and technicians base

Revision ID: 202604050003
Revises: 202604050002
Create Date: 2026-04-05 02:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050003"
down_revision = "202604050002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "providers",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("owner_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_type", sa.String(length=30), nullable=False),
        sa.Column("business_name", sa.String(length=150), nullable=False),
        sa.Column("legal_name", sa.String(length=180), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("contact_email", sa.String(length=255), nullable=True),
        sa.Column("contact_phone", sa.String(length=30), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("base_latitude", sa.Float(), nullable=True),
        sa.Column("base_longitude", sa.Float(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_available", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("max_concurrent_services", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("current_active_services", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("average_rating", sa.Float(), nullable=False, server_default="0"),
        sa.Column("offers_towing", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_battery_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_tire_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_lockout_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_engine_diagnosis", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"], ondelete="RESTRICT"),
        sa.UniqueConstraint("owner_user_id", name="uq_providers_owner_user_id"),
    )

    op.create_index("ix_providers_provider_type", "providers", ["provider_type"], unique=False)
    op.create_index("ix_providers_business_name", "providers", ["business_name"], unique=False)
    op.create_index("ix_providers_city", "providers", ["city"], unique=False)

    op.create_table(
        "technicians",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("first_name", sa.String(length=120), nullable=False),
        sa.Column("last_name", sa.String(length=120), nullable=False),
        sa.Column("phone_number", sa.String(length=30), nullable=True),
        sa.Column("specialty", sa.String(length=120), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_available", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("current_latitude", sa.Float(), nullable=True),
        sa.Column("current_longitude", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("provider_id", "phone_number", name="uq_technician_provider_phone"),
    )

    op.create_index("ix_technicians_provider_id", "technicians", ["provider_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_technicians_provider_id", table_name="technicians")
    op.drop_table("technicians")

    op.drop_index("ix_providers_city", table_name="providers")
    op.drop_index("ix_providers_business_name", table_name="providers")
    op.drop_index("ix_providers_provider_type", table_name="providers")
    op.drop_table("providers")