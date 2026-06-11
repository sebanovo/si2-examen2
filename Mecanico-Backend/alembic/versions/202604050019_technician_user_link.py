"""technician user link

Revision ID: 202604050019
Revises: 202604050018
Create Date: 2026-04-28 01:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050019"
down_revision = "202604050018"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "technicians",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=True),
    )

    op.create_foreign_key(
        "fk_technicians_user_id_users",
        "technicians",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )

    op.create_index(
        "ix_technicians_user_id",
        "technicians",
        ["user_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_technicians_user_id", table_name="technicians")
    op.drop_constraint("fk_technicians_user_id_users", "technicians", type_="foreignkey")
    op.drop_column("technicians", "user_id")