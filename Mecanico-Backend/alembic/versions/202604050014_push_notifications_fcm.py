"""push notifications with device tokens and delivery tracking

Revision ID: 202604050014
Revises: 202604050013
Create Date: 2026-04-20 00:30:00.000000
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050014"
down_revision = "202604050013"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_device_tokens",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("device_token", sa.String(length=512), nullable=False),
        sa.Column("device_platform", sa.String(length=20), nullable=False),
        sa.Column("device_label", sa.String(length=120), nullable=True),
        sa.Column("app_role", sa.String(length=30), nullable=True),
        sa.Column("push_provider_name", sa.String(length=50), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column(
            "last_seen_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
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
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("device_token", name="uq_user_device_tokens_device_token"),
    )
    op.create_index("ix_user_device_tokens_user_id", "user_device_tokens", ["user_id"], unique=False)
    op.create_index(
        "ix_user_device_tokens_device_platform",
        "user_device_tokens",
        ["device_platform"],
        unique=False,
    )

    op.create_table(
        "push_notification_deliveries",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("background_job_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("recipient_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("user_device_token_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("provider_name", sa.String(length=50), nullable=True),
        sa.Column("event_code", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("data_json", sa.JSON(), nullable=True),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("provider_message_id", sa.String(length=255), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("sent_at", sa.DateTime(timezone=True), nullable=True),
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
        sa.ForeignKeyConstraint(["background_job_id"], ["background_jobs.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["recipient_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["user_device_token_id"], ["user_device_tokens.id"], ondelete="SET NULL"),
    )
    op.create_index(
        "ix_push_notification_deliveries_background_job_id",
        "push_notification_deliveries",
        ["background_job_id"],
        unique=False,
    )
    op.create_index(
        "ix_push_notification_deliveries_incident_id",
        "push_notification_deliveries",
        ["incident_id"],
        unique=False,
    )
    op.create_index(
        "ix_push_notification_deliveries_recipient_user_id",
        "push_notification_deliveries",
        ["recipient_user_id"],
        unique=False,
    )
    op.create_index(
        "ix_push_notification_deliveries_user_device_token_id",
        "push_notification_deliveries",
        ["user_device_token_id"],
        unique=False,
    )
    op.create_index(
        "ix_push_notification_deliveries_event_code",
        "push_notification_deliveries",
        ["event_code"],
        unique=False,
    )
    op.create_index(
        "ix_push_notification_deliveries_status",
        "push_notification_deliveries",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_push_notification_deliveries_status",
        table_name="push_notification_deliveries",
    )
    op.drop_index(
        "ix_push_notification_deliveries_event_code",
        table_name="push_notification_deliveries",
    )
    op.drop_index(
        "ix_push_notification_deliveries_user_device_token_id",
        table_name="push_notification_deliveries",
    )
    op.drop_index(
        "ix_push_notification_deliveries_recipient_user_id",
        table_name="push_notification_deliveries",
    )
    op.drop_index(
        "ix_push_notification_deliveries_incident_id",
        table_name="push_notification_deliveries",
    )
    op.drop_index(
        "ix_push_notification_deliveries_background_job_id",
        table_name="push_notification_deliveries",
    )
    op.drop_table("push_notification_deliveries")

    op.drop_index("ix_user_device_tokens_device_platform", table_name="user_device_tokens")
    op.drop_index("ix_user_device_tokens_user_id", table_name="user_device_tokens")
    op.drop_table("user_device_tokens")
