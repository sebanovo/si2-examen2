"""evidences storage metadata

Revision ID: 202604050008
Revises: 202604050007
Create Date: 2026-04-17 00:30:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "202604050008"
down_revision = "202604050007"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "incident_evidences",
        sa.Column(
            "storage_provider",
            sa.String(length=30),
            nullable=False,
            server_default="local",
        ),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("storage_bucket", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("storage_object_key", sa.Text(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("public_url", sa.Text(), nullable=True),
    )

    op.create_index(
        "ix_incident_evidences_storage_provider",
        "incident_evidences",
        ["storage_provider"],
        unique=False,
    )

    op.execute(
        "UPDATE incident_evidences SET storage_provider = 'local' WHERE storage_provider IS NULL"
    )

    op.alter_column(
        "incident_evidences",
        "absolute_file_path",
        existing_type=sa.Text(),
        nullable=True,
    )


def downgrade() -> None:
    op.execute(
        "UPDATE incident_evidences SET absolute_file_path = '' WHERE absolute_file_path IS NULL"
    )

    op.alter_column(
        "incident_evidences",
        "absolute_file_path",
        existing_type=sa.Text(),
        nullable=False,
    )

    op.drop_index("ix_incident_evidences_storage_provider", table_name="incident_evidences")
    op.drop_column("incident_evidences", "public_url")
    op.drop_column("incident_evidences", "storage_object_key")
    op.drop_column("incident_evidences", "storage_bucket")
    op.drop_column("incident_evidences", "storage_provider")
