"""subscriptions, coverages and incident applications

Revision ID: 202604050016
Revises: 202604050015
Create Date: 2026-04-20 02:45:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050016"
down_revision = "202604050015"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "provider_subscription_plans",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("code", sa.String(length=60), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("billing_period", sa.String(length=20), nullable=False),
        sa.Column("price_amount", sa.Numeric(10, 2), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=False, server_default="BOB"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("auto_renews", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
    )
    op.create_index(
        "ix_provider_subscription_plans_provider_id",
        "provider_subscription_plans",
        ["provider_id"],
        unique=False,
    )
    op.create_index(
        "ix_provider_subscription_plans_code",
        "provider_subscription_plans",
        ["code"],
        unique=False,
    )
    op.create_index(
        "ix_provider_subscription_plans_billing_period",
        "provider_subscription_plans",
        ["billing_period"],
        unique=False,
    )

    op.create_table(
        "provider_subscription_plan_coverages",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("plan_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("service_catalog_item_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("incident_category", sa.String(length=50), nullable=True),
        sa.Column("coverage_type", sa.String(length=30), nullable=False),
        sa.Column("coverage_value", sa.Numeric(10, 2), nullable=False),
        sa.Column("max_coverage_amount", sa.Numeric(10, 2), nullable=True),
        sa.Column("waiting_period_days", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("max_applications_per_subscription", sa.Integer(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["plan_id"], ["provider_subscription_plans.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["service_catalog_item_id"], ["service_catalog_items.id"], ondelete="SET NULL"),
    )
    op.create_index(
        "ix_provider_subscription_plan_coverages_plan_id",
        "provider_subscription_plan_coverages",
        ["plan_id"],
        unique=False,
    )
    op.create_index(
        "ix_provider_subscription_plan_coverages_service_catalog_item_id",
        "provider_subscription_plan_coverages",
        ["service_catalog_item_id"],
        unique=False,
    )
    op.create_index(
        "ix_provider_subscription_plan_coverages_incident_category",
        "provider_subscription_plan_coverages",
        ["incident_category"],
        unique=False,
    )
    op.create_index(
        "ix_provider_subscription_plan_coverages_coverage_type",
        "provider_subscription_plan_coverages",
        ["coverage_type"],
        unique=False,
    )

    op.create_table(
        "client_plan_subscriptions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("client_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("plan_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("cancelled_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("external_reference", sa.String(length=120), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["client_user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["plan_id"], ["provider_subscription_plans.id"], ondelete="CASCADE"),
    )
    op.create_index(
        "ix_client_plan_subscriptions_client_user_id",
        "client_plan_subscriptions",
        ["client_user_id"],
        unique=False,
    )
    op.create_index(
        "ix_client_plan_subscriptions_provider_id",
        "client_plan_subscriptions",
        ["provider_id"],
        unique=False,
    )
    op.create_index(
        "ix_client_plan_subscriptions_plan_id",
        "client_plan_subscriptions",
        ["plan_id"],
        unique=False,
    )
    op.create_index(
        "ix_client_plan_subscriptions_status",
        "client_plan_subscriptions",
        ["status"],
        unique=False,
    )

    op.add_column(
        "incident_billings",
        sa.Column("client_plan_subscription_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.add_column(
        "incident_billings",
        sa.Column("plan_coverage_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.add_column(
        "incident_billings",
        sa.Column("coverage_applied_amount", sa.Numeric(10, 2), nullable=True),
    )
    op.add_column(
        "incident_billings",
        sa.Column("client_payable_amount", sa.Numeric(10, 2), nullable=True),
    )

    op.create_foreign_key(
        "fk_incident_billings_client_plan_subscription_id",
        "incident_billings",
        "client_plan_subscriptions",
        ["client_plan_subscription_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        "fk_incident_billings_plan_coverage_id",
        "incident_billings",
        "provider_subscription_plan_coverages",
        ["plan_coverage_id"],
        ["id"],
        ondelete="SET NULL",
    )

    op.create_table(
        "incident_subscription_applications",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("incident_billing_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("client_plan_subscription_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("plan_coverage_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("matched_service_catalog_item_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("matched_incident_category", sa.String(length=50), nullable=True),
        sa.Column("coverage_type", sa.String(length=30), nullable=False),
        sa.Column("coverage_value", sa.Numeric(10, 2), nullable=False),
        sa.Column("original_amount", sa.Numeric(10, 2), nullable=False),
        sa.Column("coverage_applied_amount", sa.Numeric(10, 2), nullable=False),
        sa.Column("client_payable_amount", sa.Numeric(10, 2), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("snapshot_json", sa.JSON(), nullable=True),
        sa.Column("applied_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["incident_billing_id"], ["incident_billings.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["client_plan_subscription_id"], ["client_plan_subscriptions.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["plan_coverage_id"], ["provider_subscription_plan_coverages.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["matched_service_catalog_item_id"], ["service_catalog_items.id"], ondelete="SET NULL"),
    )
    op.create_index(
        "ix_incident_subscription_applications_incident_id",
        "incident_subscription_applications",
        ["incident_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_subscription_applications_incident_billing_id",
        "incident_subscription_applications",
        ["incident_billing_id"],
        unique=False,
    )
    op.create_index(
        "ix_inc_sub_apps_plan_sub_id",
        "incident_subscription_applications",
        ["client_plan_subscription_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_subscription_applications_plan_coverage_id",
        "incident_subscription_applications",
        ["plan_coverage_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_subscription_applications_status",
        "incident_subscription_applications",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_incident_subscription_applications_status",
        table_name="incident_subscription_applications",
    )
    op.drop_index(
        "ix_incident_subscription_applications_plan_coverage_id",
        table_name="incident_subscription_applications",
    )
    op.drop_index(
        "ix_incident_subscription_applications_client_plan_subscription_id",
        table_name="incident_subscription_applications",
    )
    op.drop_index(
        "ix_incident_subscription_applications_incident_billing_id",
        table_name="incident_subscription_applications",
    )
    op.drop_index(
        "ix_incident_subscription_applications_incident_id",
        table_name="incident_subscription_applications",
    )
    op.drop_table("incident_subscription_applications")

    op.drop_constraint("fk_incident_billings_plan_coverage_id", "incident_billings", type_="foreignkey")
    op.drop_constraint("fk_incident_billings_client_plan_subscription_id", "incident_billings", type_="foreignkey")
    op.drop_column("incident_billings", "client_payable_amount")
    op.drop_column("incident_billings", "coverage_applied_amount")
    op.drop_column("incident_billings", "plan_coverage_id")
    op.drop_column("incident_billings", "client_plan_subscription_id")

    op.drop_index(
        "ix_client_plan_subscriptions_status",
        table_name="client_plan_subscriptions",
    )
    op.drop_index(
        "ix_client_plan_subscriptions_plan_id",
        table_name="client_plan_subscriptions",
    )
    op.drop_index(
        "ix_client_plan_subscriptions_provider_id",
        table_name="client_plan_subscriptions",
    )
    op.drop_index(
        "ix_client_plan_subscriptions_client_user_id",
        table_name="client_plan_subscriptions",
    )
    op.drop_table("client_plan_subscriptions")

    op.drop_index(
        "ix_provider_subscription_plan_coverages_coverage_type",
        table_name="provider_subscription_plan_coverages",
    )
    op.drop_index(
        "ix_provider_subscription_plan_coverages_incident_category",
        table_name="provider_subscription_plan_coverages",
    )
    op.drop_index(
        "ix_provider_subscription_plan_coverages_service_catalog_item_id",
        table_name="provider_subscription_plan_coverages",
    )
    op.drop_index(
        "ix_provider_subscription_plan_coverages_plan_id",
        table_name="provider_subscription_plan_coverages",
    )
    op.drop_table("provider_subscription_plan_coverages")

    op.drop_index(
        "ix_provider_subscription_plans_billing_period",
        table_name="provider_subscription_plans",
    )
    op.drop_index(
        "ix_provider_subscription_plans_code",
        table_name="provider_subscription_plans",
    )
    op.drop_index(
        "ix_provider_subscription_plans_provider_id",
        table_name="provider_subscription_plans",
    )
    op.drop_table("provider_subscription_plans")
