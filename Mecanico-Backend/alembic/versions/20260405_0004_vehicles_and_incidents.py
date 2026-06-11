"""vehicles and incidents base

Revision ID: 202604050004
Revises: 202604050003
Create Date: 2026-04-05 03:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050004"
down_revision = "202604050003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "vehicles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("owner_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("plate_number", sa.String(length=20), nullable=False),
        sa.Column("vehicle_type", sa.String(length=30), nullable=False),
        sa.Column("brand", sa.String(length=80), nullable=False),
        sa.Column("model", sa.String(length=80), nullable=False),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("color", sa.String(length=50), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_vehicles_owner_user_id", "vehicles", ["owner_user_id"], unique=False)
    op.create_index("ix_vehicles_plate_number", "vehicles", ["plate_number"], unique=True)
    op.create_index("ix_vehicles_vehicle_type", "vehicles", ["vehicle_type"], unique=False)

    op.create_table(
        "incidents",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("client_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("vehicle_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("priority", sa.String(length=30), nullable=False),
        sa.Column("reported_category", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("client_contact_phone_snapshot", sa.String(length=30), nullable=True),
        sa.Column("incident_latitude", sa.Float(), nullable=True),
        sa.Column("incident_longitude", sa.Float(), nullable=True),
        sa.Column("address_reference", sa.String(length=255), nullable=True),
        sa.Column("estimated_price_min", sa.Numeric(10, 2), nullable=True),
        sa.Column("estimated_price_max", sa.Numeric(10, 2), nullable=True),
        sa.Column("requested_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("assigned_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancelled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["client_user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["vehicle_id"], ["vehicles.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="SET NULL"),
    )

    op.create_index("ix_incidents_client_user_id", "incidents", ["client_user_id"], unique=False)
    op.create_index("ix_incidents_vehicle_id", "incidents", ["vehicle_id"], unique=False)
    op.create_index("ix_incidents_provider_id", "incidents", ["provider_id"], unique=False)
    op.create_index("ix_incidents_status", "incidents", ["status"], unique=False)
    op.create_index("ix_incidents_priority", "incidents", ["priority"], unique=False)
    op.create_index("ix_incidents_reported_category", "incidents", ["reported_category"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_incidents_reported_category", table_name="incidents")
    op.drop_index("ix_incidents_priority", table_name="incidents")
    op.drop_index("ix_incidents_status", table_name="incidents")
    op.drop_index("ix_incidents_provider_id", table_name="incidents")
    op.drop_index("ix_incidents_vehicle_id", table_name="incidents")
    op.drop_index("ix_incidents_client_user_id", table_name="incidents")
    op.drop_table("incidents")

    op.drop_index("ix_vehicles_vehicle_type", table_name="vehicles")
    op.drop_index("ix_vehicles_plate_number", table_name="vehicles")
    op.drop_index("ix_vehicles_owner_user_id", table_name="vehicles")
    op.drop_table("vehicles")