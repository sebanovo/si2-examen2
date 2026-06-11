"""incident billing and payments base

Revision ID: 202604050015
Revises: 202604050014
Create Date: 2026-04-20 01:40:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050015"
down_revision = "202604050014"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "incident_billings",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("client_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("currency_code", sa.String(length=10), nullable=False, server_default="BOB"),
        sa.Column("estimated_price_min", sa.Numeric(10, 2), nullable=True),
        sa.Column("estimated_price_max", sa.Numeric(10, 2), nullable=True),
        sa.Column("final_price_amount", sa.Numeric(10, 2), nullable=True),
        sa.Column("platform_commission_rate", sa.Numeric(5, 4), nullable=False, server_default="0.1000"),
        sa.Column("platform_commission_amount", sa.Numeric(10, 2), nullable=True),
        sa.Column("provider_gross_amount", sa.Numeric(10, 2), nullable=True),
        sa.Column("provider_net_amount", sa.Numeric(10, 2), nullable=True),
        sa.Column("payment_status", sa.String(length=30), nullable=False, server_default="PENDING_PRICING"),
        sa.Column("payment_method", sa.String(length=30), nullable=True),
        sa.Column("payment_provider_name", sa.String(length=50), nullable=True),
        sa.Column("payment_reference", sa.String(length=255), nullable=True),
        sa.Column("checkout_reference", sa.String(length=120), nullable=True),
        sa.Column("checkout_payload_json", sa.JSON(), nullable=True),
        sa.Column("pricing_note", sa.Text(), nullable=True),
        sa.Column("pricing_finalized_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("payment_completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancelled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["client_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="SET NULL"),
        sa.UniqueConstraint("incident_id", name="uq_incident_billings_incident_id"),
    )

    op.create_index("ix_incident_billings_incident_id", "incident_billings", ["incident_id"], unique=False)
    op.create_index("ix_incident_billings_client_user_id", "incident_billings", ["client_user_id"], unique=False)
    op.create_index("ix_incident_billings_provider_id", "incident_billings", ["provider_id"], unique=False)
    op.create_index("ix_incident_billings_payment_status", "incident_billings", ["payment_status"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_incident_billings_payment_status", table_name="incident_billings")
    op.drop_index("ix_incident_billings_provider_id", table_name="incident_billings")
    op.drop_index("ix_incident_billings_client_user_id", table_name="incident_billings")
    op.drop_index("ix_incident_billings_incident_id", table_name="incident_billings")
    op.drop_table("incident_billings")
