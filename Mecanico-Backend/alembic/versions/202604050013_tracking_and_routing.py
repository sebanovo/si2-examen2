"""tracking and routing

Revision ID: 202604050013
Revises: 202604050012
Create Date: 2026-04-17 04:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050013"
down_revision = "202604050012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("incidents", sa.Column("responder_last_latitude", sa.Float(), nullable=True))
    op.add_column("incidents", sa.Column("responder_last_longitude", sa.Float(), nullable=True))
    op.add_column("incidents", sa.Column("responder_last_source_type", sa.String(length=30), nullable=True))
    op.add_column("incidents", sa.Column("responder_last_recorded_at", sa.DateTime(timezone=True), nullable=True))

    op.add_column("incidents", sa.Column("route_provider_name", sa.String(length=50), nullable=True))
    op.add_column("incidents", sa.Column("route_distance_meters", sa.Float(), nullable=True))
    op.add_column("incidents", sa.Column("route_duration_seconds", sa.Integer(), nullable=True))
    op.add_column("incidents", sa.Column("route_eta_seconds", sa.Integer(), nullable=True))
    op.add_column("incidents", sa.Column("route_polyline", sa.Text(), nullable=True))
    op.add_column("incidents", sa.Column("route_last_calculated_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("incidents", sa.Column("route_error_message", sa.Text(), nullable=True))

    op.create_table(
        "incident_responder_location_pings",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("technician_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_type", sa.String(length=30), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("accuracy_meters", sa.Float(), nullable=True),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["technician_id"], ["technicians.id"], ondelete="SET NULL"),
    )

    op.create_index(
        "ix_incident_responder_location_pings_incident_id",
        "incident_responder_location_pings",
        ["incident_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_responder_location_pings_provider_id",
        "incident_responder_location_pings",
        ["provider_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_responder_location_pings_technician_id",
        "incident_responder_location_pings",
        ["technician_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_responder_location_pings_source_type",
        "incident_responder_location_pings",
        ["source_type"],
        unique=False,
    )
    op.create_index(
        "ix_incident_responder_location_pings_recorded_at",
        "incident_responder_location_pings",
        ["recorded_at"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_incident_responder_location_pings_recorded_at", table_name="incident_responder_location_pings")
    op.drop_index("ix_incident_responder_location_pings_source_type", table_name="incident_responder_location_pings")
    op.drop_index("ix_incident_responder_location_pings_technician_id", table_name="incident_responder_location_pings")
    op.drop_index("ix_incident_responder_location_pings_provider_id", table_name="incident_responder_location_pings")
    op.drop_index("ix_incident_responder_location_pings_incident_id", table_name="incident_responder_location_pings")
    op.drop_table("incident_responder_location_pings")

    op.drop_column("incidents", "route_error_message")
    op.drop_column("incidents", "route_last_calculated_at")
    op.drop_column("incidents", "route_polyline")
    op.drop_column("incidents", "route_eta_seconds")
    op.drop_column("incidents", "route_duration_seconds")
    op.drop_column("incidents", "route_distance_meters")
    op.drop_column("incidents", "route_provider_name")

    op.drop_column("incidents", "responder_last_recorded_at")
    op.drop_column("incidents", "responder_last_source_type")
    op.drop_column("incidents", "responder_last_longitude")
    op.drop_column("incidents", "responder_last_latitude")
