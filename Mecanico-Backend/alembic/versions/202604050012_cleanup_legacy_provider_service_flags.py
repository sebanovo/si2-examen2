"""cleanup legacy provider service flags

Revision ID: 202604050012
Revises: 202604050011
Create Date: 2026-04-17 03:45:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "202604050012"
down_revision = "202604050011"
branch_labels = None
depends_on = None


LEGACY_PROVIDER_FLAG_COLUMNS = (
    "offers_towing",
    "offers_battery_service",
    "offers_tire_service",
    "offers_lockout_service",
    "offers_engine_diagnosis",
)


def _column_exists(table_name: str, column_name: str) -> bool:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = inspector.get_columns(table_name)
    return any(column["name"] == column_name for column in columns)


def upgrade() -> None:
    for column_name in LEGACY_PROVIDER_FLAG_COLUMNS:
        if _column_exists("providers", column_name):
            op.drop_column("providers", column_name)


def downgrade() -> None:
    if not _column_exists("providers", "offers_towing"):
        op.add_column(
            "providers",
            sa.Column(
                "offers_towing",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )

    if not _column_exists("providers", "offers_battery_service"):
        op.add_column(
            "providers",
            sa.Column(
                "offers_battery_service",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )

    if not _column_exists("providers", "offers_tire_service"):
        op.add_column(
            "providers",
            sa.Column(
                "offers_tire_service",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )

    if not _column_exists("providers", "offers_lockout_service"):
        op.add_column(
            "providers",
            sa.Column(
                "offers_lockout_service",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )

    if not _column_exists("providers", "offers_engine_diagnosis"):
        op.add_column(
            "providers",
            sa.Column(
                "offers_engine_diagnosis",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            ),
        )
