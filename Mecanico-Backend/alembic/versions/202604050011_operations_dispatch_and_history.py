"""operations dispatch and history

Revision ID: 202604050011
Revises: 202604050010
Create Date: 2026-04-17 03:10:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050011"
down_revision = "202604050010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "incidents",
        sa.Column("assigned_technician_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("dispatch_mode", sa.String(length=30), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("en_route_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("arrived_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.create_foreign_key(
        "fk_incidents_assigned_technician_id_technicians",
        "incidents",
        "technicians",
        ["assigned_technician_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_index("ix_incidents_assigned_technician_id", "incidents", ["assigned_technician_id"], unique=False)

    op.create_table(
        "incident_operation_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("technician_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("actor_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("event_type", sa.String(length=50), nullable=False),
        sa.Column("from_status", sa.String(length=30), nullable=True),
        sa.Column("to_status", sa.String(length=30), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("payload_json", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["technician_id"], ["technicians.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["actor_user_id"], ["users.id"], ondelete="SET NULL"),
    )

    op.create_index("ix_incident_operation_events_incident_id", "incident_operation_events", ["incident_id"], unique=False)
    op.create_index("ix_incident_operation_events_provider_id", "incident_operation_events", ["provider_id"], unique=False)
    op.create_index("ix_incident_operation_events_technician_id", "incident_operation_events", ["technician_id"], unique=False)
    op.create_index("ix_incident_operation_events_actor_user_id", "incident_operation_events", ["actor_user_id"], unique=False)
    op.create_index("ix_incident_operation_events_event_type", "incident_operation_events", ["event_type"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_incident_operation_events_event_type", table_name="incident_operation_events")
    op.drop_index("ix_incident_operation_events_actor_user_id", table_name="incident_operation_events")
    op.drop_index("ix_incident_operation_events_technician_id", table_name="incident_operation_events")
    op.drop_index("ix_incident_operation_events_provider_id", table_name="incident_operation_events")
    op.drop_index("ix_incident_operation_events_incident_id", table_name="incident_operation_events")
    op.drop_table("incident_operation_events")

    op.drop_index("ix_incidents_assigned_technician_id", table_name="incidents")
    op.drop_constraint("fk_incidents_assigned_technician_id_technicians", "incidents", type_="foreignkey")
    op.drop_column("incidents", "arrived_at")
    op.drop_column("incidents", "en_route_at")
    op.drop_column("incidents", "dispatch_mode")
    op.drop_column("incidents", "assigned_technician_id")
