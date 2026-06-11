"""service catalog master

Revision ID: 202604050007
Revises: 202604050006
Create Date: 2026-04-17 00:00:00.000000
"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050007"
down_revision = "202604050006"
branch_labels = None
depends_on = None


INITIAL_SERVICE_CATALOG_ITEMS = (
    {
        "code": "TOWING",
        "category": "ACCIDENT",
        "title": "Servicio de grúa",
        "description": "Traslado del vehículo cuando no puede circular o requiere remolque.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 10,
    },
    {
        "code": "BATTERY_JUMPSTART",
        "category": "BATTERY",
        "title": "Auxilio de batería",
        "description": "Paso de corriente, revisión básica o apoyo por batería descargada.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 20,
    },
    {
        "code": "TIRE_CHANGE",
        "category": "TIRE",
        "title": "Cambio o auxilio de llanta",
        "description": "Cambio de llanta, apoyo por pinchazo o revisión rápida en carretera.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 30,
    },
    {
        "code": "LOCKOUT_ASSISTANCE",
        "category": "LOCKOUT",
        "title": "Apertura por llave encerrada",
        "description": "Asistencia para apertura del vehículo por bloqueo o llave olvidada.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 40,
    },
    {
        "code": "ENGINE_DIAGNOSTIC",
        "category": "ENGINE",
        "title": "Diagnóstico mecánico básico",
        "description": "Evaluación inicial de fallas mecánicas o del motor en sitio o taller.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 50,
    },
    {
        "code": "OVERHEATING_ASSISTANCE",
        "category": "OVERHEATING",
        "title": "Auxilio por sobrecalentamiento",
        "description": "Atención preliminar para vehículos detenidos por calentamiento excesivo.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 60,
    },
    {
        "code": "ACCIDENT_SUPPORT",
        "category": "ACCIDENT",
        "title": "Atención inicial por choque leve",
        "description": "Inspección preliminar del daño visible y definición del tipo de auxilio requerido.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 70,
    },
)


def upgrade() -> None:
    op.create_table(
        "service_catalog_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("code", sa.String(length=80), nullable=False),
        sa.Column("category", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("supports_mobile_service", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("supports_emergency_service", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_service_catalog_items_code", "service_catalog_items", ["code"], unique=True)
    op.create_index("ix_service_catalog_items_category", "service_catalog_items", ["category"], unique=False)
    op.create_index("ix_service_catalog_items_is_active", "service_catalog_items", ["is_active"], unique=False)
    op.create_index("ix_service_catalog_items_sort_order", "service_catalog_items", ["sort_order"], unique=False)

    op.create_table(
        "provider_services",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("service_catalog_item_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("custom_title", sa.String(length=150), nullable=True),
        sa.Column("custom_description", sa.Text(), nullable=True),
        sa.Column("price_estimate_min", sa.Numeric(10, 2), nullable=True),
        sa.Column("price_estimate_max", sa.Numeric(10, 2), nullable=True),
        sa.Column("estimated_duration_minutes", sa.Integer(), nullable=True),
        sa.Column("is_mobile_service_enabled", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_emergency_service_enabled", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["service_catalog_item_id"], ["service_catalog_items.id"], ondelete="CASCADE"),
        sa.UniqueConstraint(
            "provider_id",
            "service_catalog_item_id",
            name="uq_provider_services_provider_catalog_item",
        ),
    )
    op.create_index("ix_provider_services_provider_id", "provider_services", ["provider_id"], unique=False)
    op.create_index(
        "ix_provider_services_service_catalog_item_id",
        "provider_services",
        ["service_catalog_item_id"],
        unique=False,
    )
    op.create_index("ix_provider_services_is_active", "provider_services", ["is_active"], unique=False)

    service_catalog_items_table = sa.table(
        "service_catalog_items",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("category", sa.String),
        sa.column("title", sa.String),
        sa.column("description", sa.Text),
        sa.column("supports_mobile_service", sa.Boolean),
        sa.column("supports_emergency_service", sa.Boolean),
        sa.column("is_active", sa.Boolean),
        sa.column("sort_order", sa.Integer),
    )

    op.bulk_insert(
        service_catalog_items_table,
        [
            {
                "id": uuid4(),
                "code": item["code"],
                "category": item["category"],
                "title": item["title"],
                "description": item["description"],
                "supports_mobile_service": item["supports_mobile_service"],
                "supports_emergency_service": item["supports_emergency_service"],
                "is_active": True,
                "sort_order": item["sort_order"],
            }
            for item in INITIAL_SERVICE_CATALOG_ITEMS
        ],
    )


def downgrade() -> None:
    op.drop_index("ix_provider_services_is_active", table_name="provider_services")
    op.drop_index("ix_provider_services_service_catalog_item_id", table_name="provider_services")
    op.drop_index("ix_provider_services_provider_id", table_name="provider_services")
    op.drop_table("provider_services")

    op.drop_index("ix_service_catalog_items_sort_order", table_name="service_catalog_items")
    op.drop_index("ix_service_catalog_items_is_active", table_name="service_catalog_items")
    op.drop_index("ix_service_catalog_items_category", table_name="service_catalog_items")
    op.drop_index("ix_service_catalog_items_code", table_name="service_catalog_items")
    op.drop_table("service_catalog_items")
