# Export completo del backend `mechanic-api`

- Generado el: `2026-04-25 13:43:24 UTC`
- Archivo de salida: `C:\Users\braya\Desktop\SI2-2026\1erExamen\mechanic-system\mechanic-api-backend.md`

## Resumen general

- Carpeta exportada: `C:\Users\braya\Desktop\SI2-2026\1erExamen\mechanic-system\mechanic-api`
- Total de archivos incluidos: `175`
- Extensiones detectadas: `9`
- Distribucion por extension:
  - `.py`: 166
  - `.sh`: 2
  - `.dev`: 1
  - `.ini`: 1
  - `.json`: 1
  - `.mako`: 1
  - `.prod`: 1
  - `.txt`: 1
  - `<sin_extension>`: 1
- Distribucion por area principal:
  - `app`: 148 archivos
  - `alembic`: 19 archivos
  - `.devcontainer`: 2 archivos
  - `scripts`: 2 archivos
  - `Dockerfile.dev`: 1 archivos
  - `Dockerfile.prod`: 1 archivos
  - `alembic.ini`: 1 archivos
  - `requirements.txt`: 1 archivos

## Infraestructura relevante

- Archivos y rutas de infraestructura detectados:
  - `.devcontainer/devcontainer.json`
  - `.devcontainer/Dockerfile`
  - `alembic/env.py`
  - `alembic/script.py.mako`
  - `alembic/versions/202604050005_evidences_base.py`
  - `alembic/versions/202604050006_background_jobs.py`
  - `alembic/versions/202604050007_service_catalog_master.py`
  - `alembic/versions/202604050008_evidences_storage_metadata.py`
  - `alembic/versions/202604050009_pipeline_processing_states.py`
  - `alembic/versions/202604050010_assignment_candidates.py`
  - `alembic/versions/202604050011_operations_dispatch_and_history.py`
  - `alembic/versions/202604050012_cleanup_legacy_provider_service_flags.py`
  - `alembic/versions/202604050013_tracking_and_routing.py`
  - `alembic/versions/202604050014_push_notifications_fcm.py`
  - `alembic/versions/202604050015_incident_billing_and_payments.py`
  - `alembic/versions/202604050016_subscriptions_and_incident_coverages.py`
  - `alembic/versions/202604050017_audit_metrics_and_hardening_base.py`
  - `alembic/versions/20260405_0001_initial_base.py`
  - `alembic/versions/20260405_0002_auth_and_users.py`
  - `alembic/versions/20260405_0003_providers_and_technicians.py`
  - `alembic/versions/20260405_0004_vehicles_and_incidents.py`
  - `alembic.ini`
  - `app/integrations/storage/__init__.py`
  - `app/integrations/storage/base.py`
  - `app/integrations/storage/local_storage.py`
  - `app/integrations/storage/s3_storage.py`
  - `Dockerfile.dev`
  - `Dockerfile.prod`
  - `requirements.txt`
  - `scripts/start.sh`
  - `scripts/start_worker.sh`

## Arbol de directorios

```text
mechanic-api
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── alembic
│   ├── versions
│   │   ├── 202604050005_evidences_base.py
│   │   ├── 202604050006_background_jobs.py
│   │   ├── 202604050007_service_catalog_master.py
│   │   ├── 202604050008_evidences_storage_metadata.py
│   │   ├── 202604050009_pipeline_processing_states.py
│   │   ├── 202604050010_assignment_candidates.py
│   │   ├── 202604050011_operations_dispatch_and_history.py
│   │   ├── 202604050012_cleanup_legacy_provider_service_flags.py
│   │   ├── 202604050013_tracking_and_routing.py
│   │   ├── 202604050014_push_notifications_fcm.py
│   │   ├── 202604050015_incident_billing_and_payments.py
│   │   ├── 202604050016_subscriptions_and_incident_coverages.py
│   │   ├── 202604050017_audit_metrics_and_hardening_base.py
│   │   ├── 20260405_0001_initial_base.py
│   │   ├── 20260405_0002_auth_and_users.py
│   │   ├── 20260405_0003_providers_and_technicians.py
│   │   └── 20260405_0004_vehicles_and_incidents.py
│   ├── env.py
│   └── script.py.mako
├── app
│   ├── bootstrap
│   │   ├── __init__.py
│   │   └── seed.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── responses.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── logging_config.py
│   │   ├── middleware.py
│   │   └── security.py
│   ├── integrations
│   │   ├── ai
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── null_provider.py
│   │   ├── llm
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── null_provider.py
│   │   │   └── openrouter_provider.py
│   │   ├── push
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── firebase_fcm_provider.py
│   │   │   └── null_provider.py
│   │   ├── routing
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── graphhopper_provider.py
│   │   │   └── null_provider.py
│   │   ├── speech_to_text
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── faster_whisper_provider.py
│   │   │   └── null_provider.py
│   │   ├── storage
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── local_storage.py
│   │   │   └── s3_storage.py
│   │   ├── vision
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── null_provider.py
│   │   │   └── ultralytics_yolo_provider.py
│   │   ├── __init__.py
│   │   └── factory.py
│   ├── services
│   │   ├── assignment
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── audit
│   │   │   ├── __init__.py
│   │   │   ├── dispatcher.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── billing
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── catalog
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── evidences
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── incidents
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── jobs
│   │   │   ├── __init__.py
│   │   │   ├── dispatcher.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── notifications
│   │   │   ├── __init__.py
│   │   │   ├── dispatcher.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── operations
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── providers
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── subscriptions
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── system
│   │   │   ├── __init__.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── tracking
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── users
│   │   │   ├── __init__.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   ├── vehicles
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   └── __init__.py
│   ├── tasks
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   ├── job_runtime.py
│   │   ├── notification_runtime.py
│   │   ├── pipeline_runtime.py
│   │   └── task_definitions.py
│   ├── __init__.py
│   └── main.py
├── scripts
│   ├── start.sh
│   └── start_worker.sh
├── storage
├── alembic.ini
├── Dockerfile.dev
├── Dockerfile.prod
└── requirements.txt
```

## Codigo completo por archivo

### `.devcontainer/devcontainer.json`

- Ruta relativa: `.devcontainer/devcontainer.json`
- Nombre de archivo: `devcontainer.json`

```json
{
  "name": "mechanic-api-dev",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "workspaceFolder": "/mechanic-api",
  "mounts": [
    "source=${localWorkspaceFolder},target=/mechanic-api,type=bind,consistency=cached"
  ],
  "forwardPorts": [8000],
  "runArgs": [
    "--network=mechanic-system_mechanic-net",
    "--env-file=../.env.sample",
    "--hostname=serv-mech-api"
  ],
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "charliermarsh.ruff",
        "ms-python.black-formatter",
        "ms-azuretools.vscode-docker"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.analysis.typeCheckingMode": "basic",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.organizeImports": "explicit"
        }
      }
    }
  },
  "postCreateCommand": "pip install --no-cache-dir -r requirements.txt",
  "remoteUser": "root"
}
```

### `.devcontainer/Dockerfile`

- Ruta relativa: `.devcontainer/Dockerfile`
- Nombre de archivo: `Dockerfile`

```text
FROM python:3.12-slim

# Prevents Python from generating .pyc files inside the container.
ENV PYTHONDONTWRITEBYTECODE=1

# Ensures Python logs are printed immediately in Docker.
ENV PYTHONUNBUFFERED=1

WORKDIR /mechanic-api

# Basic tools for development:
# - build-essential: compile native dependencies if needed
# - git, curl: common developer tools
# - libpq-dev, postgresql-client: PostgreSQL support
# - netcat-openbsd: useful for connectivity checks
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    netcat-openbsd \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Keeps the container ready for VS Code remote development.
CMD ["sleep", "infinity"]
```

### `alembic/env.py`

- Ruta relativa: `alembic/env.py`
- Nombre de archivo: `env.py`

```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import settings
from app.core.database import Base
from app.services.assignment import models as assignment_models  # noqa: F401
from app.services.audit import models as audit_models  # noqa: F401
from app.services.auth import models as auth_models  # noqa: F401
from app.services.billing import models as billing_models  # noqa: F401
from app.services.catalog import models as catalog_models  # noqa: F401
from app.services.evidences import models as evidences_models  # noqa: F401
from app.services.incidents import models as incidents_models  # noqa: F401
from app.services.jobs import models as jobs_models  # noqa: F401
from app.services.notifications import models as notifications_models  # noqa: F401
from app.services.operations import models as operations_models  # noqa: F401
from app.services.providers import models as providers_models  # noqa: F401
from app.services.subscriptions import models as subscriptions_models  # noqa: F401
from app.services.tracking import models as tracking_models  # noqa: F401
from app.services.vehicles import models as vehicles_models  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", settings.database_url)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

### `alembic/script.py.mako`

- Ruta relativa: `alembic/script.py.mako`
- Nombre de archivo: `script.py.mako`

```text
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}


# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
```

### `alembic/versions/202604050005_evidences_base.py`

- Ruta relativa: `alembic/versions/202604050005_evidences_base.py`
- Nombre de archivo: `202604050005_evidences_base.py`

```python
"""evidences base

Revision ID: 202604050005
Revises: 202604050004
Create Date: 2026-04-05 04:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050005"
down_revision = "202604050004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "incident_evidences",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("uploaded_by_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("evidence_type", sa.String(length=30), nullable=False),
        sa.Column("original_filename", sa.String(length=255), nullable=True),
        sa.Column("stored_filename", sa.String(length=255), nullable=False),
        sa.Column("file_extension", sa.String(length=20), nullable=True),
        sa.Column("mime_type", sa.String(length=120), nullable=True),
        sa.Column("file_size_bytes", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("absolute_file_path", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["uploaded_by_user_id"], ["users.id"], ondelete="SET NULL"),
    )

    op.create_index("ix_incident_evidences_incident_id", "incident_evidences", ["incident_id"], unique=False)
    op.create_index("ix_incident_evidences_uploaded_by_user_id", "incident_evidences", ["uploaded_by_user_id"], unique=False)
    op.create_index("ix_incident_evidences_evidence_type", "incident_evidences", ["evidence_type"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_incident_evidences_evidence_type", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_uploaded_by_user_id", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_incident_id", table_name="incident_evidences")
    op.drop_table("incident_evidences")
```

### `alembic/versions/202604050006_background_jobs.py`

- Ruta relativa: `alembic/versions/202604050006_background_jobs.py`
- Nombre de archivo: `202604050006_background_jobs.py`

```python
"""background jobs base

Revision ID: 202604050006
Revises: 202604050005
Create Date: 2026-04-05 05:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050006"
down_revision = "202604050005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "background_jobs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("requested_by_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("job_type", sa.String(length=50), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("provider_name", sa.String(length=50), nullable=True),
        sa.Column("queue_name", sa.String(length=50), nullable=False),
        sa.Column("celery_task_id", sa.String(length=100), nullable=True),
        sa.Column("entity_type", sa.String(length=50), nullable=True),
        sa.Column("entity_id", sa.String(length=100), nullable=True),
        sa.Column("payload_json", sa.JSON(), nullable=True),
        sa.Column("result_json", sa.JSON(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("attempts_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["requested_by_user_id"], ["users.id"], ondelete="SET NULL"),
    )

    op.create_index("ix_background_jobs_requested_by_user_id", "background_jobs", ["requested_by_user_id"], unique=False)
    op.create_index("ix_background_jobs_job_type", "background_jobs", ["job_type"], unique=False)
    op.create_index("ix_background_jobs_status", "background_jobs", ["status"], unique=False)
    op.create_index("ix_background_jobs_celery_task_id", "background_jobs", ["celery_task_id"], unique=False)
    op.create_index("ix_background_jobs_entity_type", "background_jobs", ["entity_type"], unique=False)
    op.create_index("ix_background_jobs_entity_id", "background_jobs", ["entity_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_background_jobs_entity_id", table_name="background_jobs")
    op.drop_index("ix_background_jobs_entity_type", table_name="background_jobs")
    op.drop_index("ix_background_jobs_celery_task_id", table_name="background_jobs")
    op.drop_index("ix_background_jobs_status", table_name="background_jobs")
    op.drop_index("ix_background_jobs_job_type", table_name="background_jobs")
    op.drop_index("ix_background_jobs_requested_by_user_id", table_name="background_jobs")
    op.drop_table("background_jobs")
```

### `alembic/versions/202604050007_service_catalog_master.py`

- Ruta relativa: `alembic/versions/202604050007_service_catalog_master.py`
- Nombre de archivo: `202604050007_service_catalog_master.py`

```python
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
```

### `alembic/versions/202604050008_evidences_storage_metadata.py`

- Ruta relativa: `alembic/versions/202604050008_evidences_storage_metadata.py`
- Nombre de archivo: `202604050008_evidences_storage_metadata.py`

```python
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
```

### `alembic/versions/202604050009_pipeline_processing_states.py`

- Ruta relativa: `alembic/versions/202604050009_pipeline_processing_states.py`
- Nombre de archivo: `202604050009_pipeline_processing_states.py`

```python
"""pipeline processing states

Revision ID: 202604050009
Revises: 202604050008
Create Date: 2026-04-17 01:10:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "202604050009"
down_revision = "202604050008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "incident_evidences",
        sa.Column("text_content_snapshot", sa.Text(), nullable=True),
    )

    op.add_column(
        "incident_evidences",
        sa.Column(
            "audio_processing_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_text", sa.Text(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_language_code", sa.String(length=20), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_confidence", sa.Float(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("transcript_segments_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("audio_error_message", sa.Text(), nullable=True),
    )

    op.add_column(
        "incident_evidences",
        sa.Column(
            "image_processing_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_labels_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_detections_json", sa.JSON(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incident_evidences",
        sa.Column("image_error_message", sa.Text(), nullable=True),
    )

    op.create_index(
        "ix_incident_evidences_audio_processing_status",
        "incident_evidences",
        ["audio_processing_status"],
        unique=False,
    )
    op.create_index(
        "ix_incident_evidences_image_processing_status",
        "incident_evidences",
        ["image_processing_status"],
        unique=False,
    )

    op.add_column(
        "incidents",
        sa.Column(
            "ai_summary_status",
            sa.String(length=30),
            nullable=False,
            server_default="NOT_REQUESTED",
        ),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_provider_name", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("structured_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("suggested_category", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("suggested_priority", sa.String(length=30), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("requires_more_information", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_processed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "incidents",
        sa.Column("summary_error_message", sa.Text(), nullable=True),
    )

    op.create_index(
        "ix_incidents_ai_summary_status",
        "incidents",
        ["ai_summary_status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_incidents_ai_summary_status", table_name="incidents")
    op.drop_column("incidents", "summary_error_message")
    op.drop_column("incidents", "summary_processed_at")
    op.drop_column("incidents", "requires_more_information")
    op.drop_column("incidents", "suggested_priority")
    op.drop_column("incidents", "suggested_category")
    op.drop_column("incidents", "structured_summary")
    op.drop_column("incidents", "summary_provider_name")
    op.drop_column("incidents", "ai_summary_status")

    op.drop_index("ix_incident_evidences_image_processing_status", table_name="incident_evidences")
    op.drop_index("ix_incident_evidences_audio_processing_status", table_name="incident_evidences")

    op.drop_column("incident_evidences", "image_error_message")
    op.drop_column("incident_evidences", "image_processed_at")
    op.drop_column("incident_evidences", "image_summary")
    op.drop_column("incident_evidences", "image_detections_json")
    op.drop_column("incident_evidences", "image_labels_json")
    op.drop_column("incident_evidences", "image_provider_name")
    op.drop_column("incident_evidences", "image_processing_status")

    op.drop_column("incident_evidences", "audio_error_message")
    op.drop_column("incident_evidences", "audio_processed_at")
    op.drop_column("incident_evidences", "transcript_segments_json")
    op.drop_column("incident_evidences", "transcript_confidence")
    op.drop_column("incident_evidences", "transcript_language_code")
    op.drop_column("incident_evidences", "transcript_text")
    op.drop_column("incident_evidences", "audio_provider_name")
    op.drop_column("incident_evidences", "audio_processing_status")

    op.drop_column("incident_evidences", "text_content_snapshot")
```

### `alembic/versions/202604050010_assignment_candidates.py`

- Ruta relativa: `alembic/versions/202604050010_assignment_candidates.py`
- Nombre de archivo: `202604050010_assignment_candidates.py`

```python
"""assignment candidates

Revision ID: 202604050010
Revises: 202604050009
Create Date: 2026-04-17 02:20:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050010"
down_revision = "202604050009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "incident_assignment_candidates",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("recommendation_rank", sa.Integer(), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("distance_km", sa.Float(), nullable=True),
        sa.Column("required_service_codes_json", sa.JSON(), nullable=True),
        sa.Column("matched_service_codes_json", sa.JSON(), nullable=True),
        sa.Column("rationale_json", sa.JSON(), nullable=True),
        sa.Column("provider_average_rating_snapshot", sa.Float(), nullable=False, server_default="0"),
        sa.Column("provider_available_capacity_snapshot", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("available_technicians_count_snapshot", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("responded_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.UniqueConstraint(
            "incident_id",
            "provider_id",
            name="uq_incident_assignment_candidate_incident_provider",
        ),
    )

    op.create_index(
        "ix_incident_assignment_candidates_incident_id",
        "incident_assignment_candidates",
        ["incident_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_provider_id",
        "incident_assignment_candidates",
        ["provider_id"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_status",
        "incident_assignment_candidates",
        ["status"],
        unique=False,
    )
    op.create_index(
        "ix_incident_assignment_candidates_recommendation_rank",
        "incident_assignment_candidates",
        ["recommendation_rank"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_incident_assignment_candidates_recommendation_rank",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_status",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_provider_id",
        table_name="incident_assignment_candidates",
    )
    op.drop_index(
        "ix_incident_assignment_candidates_incident_id",
        table_name="incident_assignment_candidates",
    )
    op.drop_table("incident_assignment_candidates")
```

### `alembic/versions/202604050011_operations_dispatch_and_history.py`

- Ruta relativa: `alembic/versions/202604050011_operations_dispatch_and_history.py`
- Nombre de archivo: `202604050011_operations_dispatch_and_history.py`

```python
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
```

### `alembic/versions/202604050012_cleanup_legacy_provider_service_flags.py`

- Ruta relativa: `alembic/versions/202604050012_cleanup_legacy_provider_service_flags.py`
- Nombre de archivo: `202604050012_cleanup_legacy_provider_service_flags.py`

```python
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
```

### `alembic/versions/202604050013_tracking_and_routing.py`

- Ruta relativa: `alembic/versions/202604050013_tracking_and_routing.py`
- Nombre de archivo: `202604050013_tracking_and_routing.py`

```python
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
```

### `alembic/versions/202604050014_push_notifications_fcm.py`

- Ruta relativa: `alembic/versions/202604050014_push_notifications_fcm.py`
- Nombre de archivo: `202604050014_push_notifications_fcm.py`

```python
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
```

### `alembic/versions/202604050015_incident_billing_and_payments.py`

- Ruta relativa: `alembic/versions/202604050015_incident_billing_and_payments.py`
- Nombre de archivo: `202604050015_incident_billing_and_payments.py`

```python
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
```

### `alembic/versions/202604050016_subscriptions_and_incident_coverages.py`

- Ruta relativa: `alembic/versions/202604050016_subscriptions_and_incident_coverages.py`
- Nombre de archivo: `202604050016_subscriptions_and_incident_coverages.py`

```python
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
```

### `alembic/versions/202604050017_audit_metrics_and_hardening_base.py`

- Ruta relativa: `alembic/versions/202604050017_audit_metrics_and_hardening_base.py`
- Nombre de archivo: `202604050017_audit_metrics_and_hardening_base.py`

```python
"""audit, metric snapshots and hardening base

Revision ID: 202604050017
Revises: 202604050016
Create Date: 2026-04-20 03:40:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "202604050017"
down_revision = "202604050016"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "audit_logs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("actor_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("incident_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("request_id", sa.String(length=100), nullable=True),
        sa.Column("event_scope", sa.String(length=30), nullable=False),
        sa.Column("event_type", sa.String(length=80), nullable=False),
        sa.Column("entity_type", sa.String(length=50), nullable=True),
        sa.Column("entity_id", sa.String(length=120), nullable=True),
        sa.Column("http_method", sa.String(length=10), nullable=True),
        sa.Column("route_path", sa.String(length=255), nullable=True),
        sa.Column("ip_address", sa.String(length=120), nullable=True),
        sa.Column("user_agent", sa.Text(), nullable=True),
        sa.Column("status_code", sa.Integer(), nullable=True),
        sa.Column("outcome", sa.String(length=30), nullable=False),
        sa.Column("payload_json", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["actor_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["incident_id"], ["incidents.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="SET NULL"),
    )
    op.create_index("ix_audit_logs_actor_user_id", "audit_logs", ["actor_user_id"], unique=False)
    op.create_index("ix_audit_logs_incident_id", "audit_logs", ["incident_id"], unique=False)
    op.create_index("ix_audit_logs_provider_id", "audit_logs", ["provider_id"], unique=False)
    op.create_index("ix_audit_logs_request_id", "audit_logs", ["request_id"], unique=False)
    op.create_index("ix_audit_logs_event_scope", "audit_logs", ["event_scope"], unique=False)
    op.create_index("ix_audit_logs_event_type", "audit_logs", ["event_type"], unique=False)
    op.create_index("ix_audit_logs_entity_type", "audit_logs", ["entity_type"], unique=False)
    op.create_index("ix_audit_logs_entity_id", "audit_logs", ["entity_id"], unique=False)
    op.create_index("ix_audit_logs_outcome", "audit_logs", ["outcome"], unique=False)
    op.create_index("ix_audit_logs_created_at", "audit_logs", ["created_at"], unique=False)

    op.create_table(
        "metric_snapshots",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("captured_by_user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("snapshot_type", sa.String(length=50), nullable=False),
        sa.Column("payload_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["captured_by_user_id"], ["users.id"], ondelete="SET NULL"),
    )
    op.create_index("ix_metric_snapshots_captured_by_user_id", "metric_snapshots", ["captured_by_user_id"], unique=False)
    op.create_index("ix_metric_snapshots_snapshot_type", "metric_snapshots", ["snapshot_type"], unique=False)
    op.create_index("ix_metric_snapshots_created_at", "metric_snapshots", ["created_at"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_metric_snapshots_created_at", table_name="metric_snapshots")
    op.drop_index("ix_metric_snapshots_snapshot_type", table_name="metric_snapshots")
    op.drop_index("ix_metric_snapshots_captured_by_user_id", table_name="metric_snapshots")
    op.drop_table("metric_snapshots")

    op.drop_index("ix_audit_logs_created_at", table_name="audit_logs")
    op.drop_index("ix_audit_logs_outcome", table_name="audit_logs")
    op.drop_index("ix_audit_logs_entity_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_entity_type", table_name="audit_logs")
    op.drop_index("ix_audit_logs_event_type", table_name="audit_logs")
    op.drop_index("ix_audit_logs_event_scope", table_name="audit_logs")
    op.drop_index("ix_audit_logs_request_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_provider_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_incident_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_actor_user_id", table_name="audit_logs")
    op.drop_table("audit_logs")
```

### `alembic/versions/20260405_0001_initial_base.py`

- Ruta relativa: `alembic/versions/20260405_0001_initial_base.py`
- Nombre de archivo: `20260405_0001_initial_base.py`

```python
"""initial base structure

Revision ID: 202604050001
Revises: 
Create Date: 2026-04-05 00:00:00.000000
"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "202604050001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
```

### `alembic/versions/20260405_0002_auth_and_users.py`

- Ruta relativa: `alembic/versions/20260405_0002_auth_and_users.py`
- Nombre de archivo: `20260405_0002_auth_and_users.py`

```python
"""auth and users base

Revision ID: 202604050002
Revises: 202604050001
Create Date: 2026-04-05 01:00:00.000000
"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050002"
down_revision = "202604050001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("is_system", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_roles_code", "roles", ["code"], unique=True)

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("first_name", sa.String(length=120), nullable=False),
        sa.Column("last_name", sa.String(length=120), nullable=False),
        sa.Column("phone_number", sa.String(length=30), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_superuser", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "user_role_links",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "role_id"),
    )

    roles_table = sa.table(
        "roles",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("name", sa.String),
        sa.column("description", sa.String),
        sa.column("is_system", sa.Boolean),
    )

    op.bulk_insert(
        roles_table,
        [
            {
                "id": uuid4(),
                "code": "CLIENT",
                "name": "Client",
                "description": "Mobile customer who requests roadside assistance.",
                "is_system": True,
            },
            {
                "id": uuid4(),
                "code": "PROVIDER_ADMIN",
                "name": "Provider Admin",
                "description": "Workshop administrator who manages provider operations.",
                "is_system": True,
            },
            {
                "id": uuid4(),
                "code": "TECHNICIAN",
                "name": "Technician",
                "description": "Technician assigned to attend incidents.",
                "is_system": True,
            },
            {
                "id": uuid4(),
                "code": "PLATFORM_ADMIN",
                "name": "Platform Admin",
                "description": "System administrator with platform-wide visibility.",
                "is_system": True,
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("user_role_links")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
    op.drop_index("ix_roles_code", table_name="roles")
    op.drop_table("roles")
```

### `alembic/versions/20260405_0003_providers_and_technicians.py`

- Ruta relativa: `alembic/versions/20260405_0003_providers_and_technicians.py`
- Nombre de archivo: `20260405_0003_providers_and_technicians.py`

```python
"""providers and technicians base

Revision ID: 202604050003
Revises: 202604050002
Create Date: 2026-04-05 02:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "202604050003"
down_revision = "202604050002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "providers",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("owner_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("provider_type", sa.String(length=30), nullable=False),
        sa.Column("business_name", sa.String(length=150), nullable=False),
        sa.Column("legal_name", sa.String(length=180), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("contact_email", sa.String(length=255), nullable=True),
        sa.Column("contact_phone", sa.String(length=30), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("base_latitude", sa.Float(), nullable=True),
        sa.Column("base_longitude", sa.Float(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_available", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("max_concurrent_services", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("current_active_services", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("average_rating", sa.Float(), nullable=False, server_default="0"),
        sa.Column("offers_towing", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_battery_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_tire_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_lockout_service", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("offers_engine_diagnosis", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["owner_user_id"], ["users.id"], ondelete="RESTRICT"),
        sa.UniqueConstraint("owner_user_id", name="uq_providers_owner_user_id"),
    )

    op.create_index("ix_providers_provider_type", "providers", ["provider_type"], unique=False)
    op.create_index("ix_providers_business_name", "providers", ["business_name"], unique=False)
    op.create_index("ix_providers_city", "providers", ["city"], unique=False)

    op.create_table(
        "technicians",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("provider_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("first_name", sa.String(length=120), nullable=False),
        sa.Column("last_name", sa.String(length=120), nullable=False),
        sa.Column("phone_number", sa.String(length=30), nullable=True),
        sa.Column("specialty", sa.String(length=120), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_available", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("current_latitude", sa.Float(), nullable=True),
        sa.Column("current_longitude", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("provider_id", "phone_number", name="uq_technician_provider_phone"),
    )

    op.create_index("ix_technicians_provider_id", "technicians", ["provider_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_technicians_provider_id", table_name="technicians")
    op.drop_table("technicians")

    op.drop_index("ix_providers_city", table_name="providers")
    op.drop_index("ix_providers_business_name", table_name="providers")
    op.drop_index("ix_providers_provider_type", table_name="providers")
    op.drop_table("providers")
```

### `alembic/versions/20260405_0004_vehicles_and_incidents.py`

- Ruta relativa: `alembic/versions/20260405_0004_vehicles_and_incidents.py`
- Nombre de archivo: `20260405_0004_vehicles_and_incidents.py`

```python
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
```

### `alembic.ini`

- Ruta relativa: `alembic.ini`
- Nombre de archivo: `alembic.ini`

```ini
[alembic]
script_location = alembic
prepend_sys_path = .
sqlalchemy.url = postgresql+psycopg://mechanic_user:mechanic_password@serv-mech-db:5432/mechanic_db

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers = console
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
```

### `app/__init__.py`

- Ruta relativa: `app/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/bootstrap/__init__.py`

- Ruta relativa: `app/bootstrap/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/bootstrap/seed.py`

- Ruta relativa: `app/bootstrap/seed.py`
- Nombre de archivo: `seed.py`

```python
import logging

from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.core.config import settings
from app.core.security import hash_password
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository

logger = logging.getLogger(__name__)


def seed_initial_platform_admin(db: Session) -> None:
    repository = AuthRepository(db)

    admin_email = settings.initial_platform_admin_email.strip().lower()
    existing_user = repository.get_user_by_email(admin_email)

    if existing_user is not None:
        logger.info(
            "Initial platform admin already exists with email=%s",
            admin_email,
        )
        return

    platform_admin_role = repository.get_role_by_code(ROLE_PLATFORM_ADMIN)
    if platform_admin_role is None:
        raise RuntimeError("PLATFORM_ADMIN role was not found during bootstrap seeding.")

    new_admin = User(
        email=admin_email,
        password_hash=hash_password(settings.initial_platform_admin_password),
        first_name=settings.initial_platform_admin_first_name.strip(),
        last_name=settings.initial_platform_admin_last_name.strip(),
        phone_number=(
            settings.initial_platform_admin_phone.strip()
            if settings.initial_platform_admin_phone
            else None
        ),
        is_active=True,
        is_superuser=True,
        roles=[platform_admin_role],
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    logger.info(
        "Initial platform admin created successfully with email=%s",
        admin_email,
    )
```

### `app/common/__init__.py`

- Ruta relativa: `app/common/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/common/constants.py`

- Ruta relativa: `app/common/constants.py`
- Nombre de archivo: `constants.py`

```python
ROLE_CLIENT = "CLIENT"
ROLE_PROVIDER_ADMIN = "PROVIDER_ADMIN"
ROLE_TECHNICIAN = "TECHNICIAN"
ROLE_PLATFORM_ADMIN = "PLATFORM_ADMIN"

INITIAL_SYSTEM_ROLE_CODES = (
    ROLE_CLIENT,
    ROLE_PROVIDER_ADMIN,
    ROLE_TECHNICIAN,
    ROLE_PLATFORM_ADMIN,
)

ACCOUNT_TYPE_CLIENT = "CLIENT"
ACCOUNT_TYPE_INDEPENDENT_MECHANIC = "INDEPENDENT_MECHANIC"
ACCOUNT_TYPE_WORKSHOP = "WORKSHOP"

PUBLIC_ACCOUNT_TYPES = (
    ACCOUNT_TYPE_CLIENT,
    ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
    ACCOUNT_TYPE_WORKSHOP,
)

PROVIDER_TYPE_INDEPENDENT_MECHANIC = "INDEPENDENT_MECHANIC"
PROVIDER_TYPE_WORKSHOP = "WORKSHOP"

PUBLIC_PROVIDER_TYPES = (
    PROVIDER_TYPE_INDEPENDENT_MECHANIC,
    PROVIDER_TYPE_WORKSHOP,
)

VEHICLE_TYPE_CAR = "CAR"
VEHICLE_TYPE_MOTORCYCLE = "MOTORCYCLE"
VEHICLE_TYPE_TRUCK = "TRUCK"
VEHICLE_TYPE_VAN = "VAN"
VEHICLE_TYPE_OTHER = "OTHER"

INCIDENT_STATUS_PENDING = "PENDING"
INCIDENT_STATUS_IN_REVIEW = "IN_REVIEW"
INCIDENT_STATUS_PUBLISHED = "PUBLISHED"
INCIDENT_STATUS_ASSIGNED = "ASSIGNED"
INCIDENT_STATUS_EN_ROUTE = "EN_ROUTE"
INCIDENT_STATUS_ON_SITE = "ON_SITE"
INCIDENT_STATUS_IN_PROGRESS = "IN_PROGRESS"
INCIDENT_STATUS_COMPLETED = "COMPLETED"
INCIDENT_STATUS_CANCELLED = "CANCELLED"

INCIDENT_PRIORITY_LOW = "LOW"
INCIDENT_PRIORITY_MEDIUM = "MEDIUM"
INCIDENT_PRIORITY_HIGH = "HIGH"
INCIDENT_PRIORITY_CRITICAL = "CRITICAL"

INCIDENT_CATEGORY_BATTERY = "BATTERY"
INCIDENT_CATEGORY_TIRE = "TIRE"
INCIDENT_CATEGORY_ACCIDENT = "ACCIDENT"
INCIDENT_CATEGORY_ENGINE = "ENGINE"
INCIDENT_CATEGORY_LOCKOUT = "LOCKOUT"
INCIDENT_CATEGORY_OVERHEATING = "OVERHEATING"
INCIDENT_CATEGORY_OTHER = "OTHER"
INCIDENT_CATEGORY_UNCERTAIN = "UNCERTAIN"

PUBLIC_INCIDENT_CATEGORIES = (
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_OTHER,
    INCIDENT_CATEGORY_UNCERTAIN,
)

SERVICE_CODE_TOWING = "TOWING"
SERVICE_CODE_BATTERY_JUMPSTART = "BATTERY_JUMPSTART"
SERVICE_CODE_TIRE_CHANGE = "TIRE_CHANGE"
SERVICE_CODE_LOCKOUT_ASSISTANCE = "LOCKOUT_ASSISTANCE"
SERVICE_CODE_ENGINE_DIAGNOSTIC = "ENGINE_DIAGNOSTIC"
SERVICE_CODE_OVERHEATING_ASSISTANCE = "OVERHEATING_ASSISTANCE"
SERVICE_CODE_ACCIDENT_SUPPORT = "ACCIDENT_SUPPORT"

INITIAL_SERVICE_CATALOG_ITEMS = (
    {
        "code": SERVICE_CODE_TOWING,
        "category": INCIDENT_CATEGORY_ACCIDENT,
        "title": "Servicio de grúa",
        "description": "Traslado del vehículo cuando no puede circular o requiere remolque.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 10,
    },
    {
        "code": SERVICE_CODE_BATTERY_JUMPSTART,
        "category": INCIDENT_CATEGORY_BATTERY,
        "title": "Auxilio de batería",
        "description": "Paso de corriente, revisión básica o apoyo por batería descargada.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 20,
    },
    {
        "code": SERVICE_CODE_TIRE_CHANGE,
        "category": INCIDENT_CATEGORY_TIRE,
        "title": "Cambio o auxilio de llanta",
        "description": "Cambio de llanta, apoyo por pinchazo o revisión rápida en carretera.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 30,
    },
    {
        "code": SERVICE_CODE_LOCKOUT_ASSISTANCE,
        "category": INCIDENT_CATEGORY_LOCKOUT,
        "title": "Apertura por llave encerrada",
        "description": "Asistencia para apertura del vehículo por bloqueo o llave olvidada.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 40,
    },
    {
        "code": SERVICE_CODE_ENGINE_DIAGNOSTIC,
        "category": INCIDENT_CATEGORY_ENGINE,
        "title": "Diagnóstico mecánico básico",
        "description": "Evaluación inicial de fallas mecánicas o del motor en sitio o taller.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 50,
    },
    {
        "code": SERVICE_CODE_OVERHEATING_ASSISTANCE,
        "category": INCIDENT_CATEGORY_OVERHEATING,
        "title": "Auxilio por sobrecalentamiento",
        "description": "Atención preliminar para vehículos detenidos por calentamiento excesivo.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 60,
    },
    {
        "code": SERVICE_CODE_ACCIDENT_SUPPORT,
        "category": INCIDENT_CATEGORY_ACCIDENT,
        "title": "Atención inicial por choque leve",
        "description": "Inspección preliminar del daño visible y definición del tipo de auxilio requerido.",
        "supports_mobile_service": True,
        "supports_emergency_service": True,
        "sort_order": 70,
    },
)

EVIDENCE_TYPE_IMAGE = "IMAGE"
EVIDENCE_TYPE_AUDIO = "AUDIO"
EVIDENCE_TYPE_TEXT = "TEXT"

PROCESSING_STATUS_NOT_REQUESTED = "NOT_REQUESTED"
PROCESSING_STATUS_PENDING = "PENDING"
PROCESSING_STATUS_RUNNING = "RUNNING"
PROCESSING_STATUS_SUCCEEDED = "SUCCEEDED"
PROCESSING_STATUS_FAILED = "FAILED"

ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE = "AVAILABLE"
ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED = "ACCEPTED"
ASSIGNMENT_CANDIDATE_STATUS_REJECTED = "REJECTED"
ASSIGNMENT_CANDIDATE_STATUS_EXPIRED = "EXPIRED"

DISPATCH_MODE_PROVIDER_SELF = "PROVIDER_SELF"
DISPATCH_MODE_TECHNICIAN = "TECHNICIAN"

TRACKING_SOURCE_PROVIDER_SELF = "PROVIDER_SELF"
TRACKING_SOURCE_TECHNICIAN = "TECHNICIAN"

INCIDENT_OPERATION_EVENT_DISPATCHED = "DISPATCHED"
INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE = "ARRIVED_ON_SITE"
INCIDENT_OPERATION_EVENT_SERVICE_STARTED = "SERVICE_STARTED"
INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED = "SERVICE_COMPLETED"
INCIDENT_OPERATION_EVENT_SERVICE_CANCELLED = "SERVICE_CANCELLED"

BACKGROUND_JOB_STATUS_PENDING = "PENDING"
BACKGROUND_JOB_STATUS_RUNNING = "RUNNING"
BACKGROUND_JOB_STATUS_SUCCEEDED = "SUCCEEDED"
BACKGROUND_JOB_STATUS_FAILED = "FAILED"

BACKGROUND_JOB_TYPE_DEMO = "DEMO"
BACKGROUND_JOB_TYPE_AUDIO_TRANSCRIPTION = "AUDIO_TRANSCRIPTION"
BACKGROUND_JOB_TYPE_IMAGE_ANALYSIS = "IMAGE_ANALYSIS"
BACKGROUND_JOB_TYPE_INCIDENT_SUMMARY = "INCIDENT_SUMMARY"

CELERY_QUEUE_DEFAULT = "default"
CELERY_QUEUE_AUDIO = "audio"
CELERY_QUEUE_IMAGE = "image"
CELERY_QUEUE_SUMMARY = "summary"
CELERY_QUEUE_PUSH = "push"


BACKGROUND_JOB_TYPE_PUSH_NOTIFICATION = "PUSH_NOTIFICATION"

DEVICE_PLATFORM_ANDROID = "ANDROID"
DEVICE_PLATFORM_IOS = "IOS"
DEVICE_PLATFORM_WEB = "WEB"

PUSH_DELIVERY_STATUS_PENDING = "PENDING"
PUSH_DELIVERY_STATUS_RUNNING = "RUNNING"
PUSH_DELIVERY_STATUS_SUCCEEDED = "SUCCEEDED"
PUSH_DELIVERY_STATUS_FAILED = "FAILED"

PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE = "NEW_ASSIGNMENT_AVAILABLE"
PUSH_EVENT_INCIDENT_ACCEPTED = "INCIDENT_ACCEPTED"
PUSH_EVENT_TECHNICIAN_ASSIGNED = "TECHNICIAN_ASSIGNED"
PUSH_EVENT_PROVIDER_EN_ROUTE = "PROVIDER_EN_ROUTE"
PUSH_EVENT_PROVIDER_ARRIVED = "PROVIDER_ARRIVED"
PUSH_EVENT_INCIDENT_CANCELLED = "INCIDENT_CANCELLED"
PUSH_EVENT_INCIDENT_COMPLETED = "INCIDENT_COMPLETED"
PUSH_EVENT_TEST = "TEST"

PUBLIC_DEVICE_PLATFORMS = (
    DEVICE_PLATFORM_ANDROID,
    DEVICE_PLATFORM_IOS,
    DEVICE_PLATFORM_WEB,
)


DEFAULT_CURRENCY_CODE = "BOB"
DEFAULT_PLATFORM_COMMISSION_RATE = 0.10

PAYMENT_STATUS_PENDING_PRICING = "PENDING_PRICING"
PAYMENT_STATUS_ESTIMATED = "ESTIMATED"
PAYMENT_STATUS_PENDING_PAYMENT = "PENDING_PAYMENT"
PAYMENT_STATUS_PAID = "PAID"
PAYMENT_STATUS_CANCELLED = "CANCELLED"

PAYMENT_METHOD_CASH = "CASH"
PAYMENT_METHOD_QR = "QR"
PAYMENT_METHOD_GATEWAY = "GATEWAY"
PAYMENT_METHOD_TRANSFER = "TRANSFER"
PAYMENT_METHOD_CARD = "CARD"

PUBLIC_PAYMENT_METHODS = (
    PAYMENT_METHOD_CASH,
    PAYMENT_METHOD_QR,
    PAYMENT_METHOD_GATEWAY,
    PAYMENT_METHOD_TRANSFER,
    PAYMENT_METHOD_CARD,
)


PLAN_BILLING_PERIOD_MONTHLY = "MONTHLY"
PLAN_BILLING_PERIOD_ANNUAL = "ANNUAL"

PLAN_COVERAGE_TYPE_FIXED_AMOUNT = "FIXED_AMOUNT"
PLAN_COVERAGE_TYPE_PERCENTAGE = "PERCENTAGE"
PLAN_COVERAGE_TYPE_FULL = "FULL"

SUBSCRIPTION_STATUS_ACTIVE = "ACTIVE"
SUBSCRIPTION_STATUS_CANCELLED = "CANCELLED"
SUBSCRIPTION_STATUS_EXPIRED = "EXPIRED"

SUBSCRIPTION_APPLICATION_STATUS_APPLIED = "APPLIED"
SUBSCRIPTION_APPLICATION_STATUS_VOIDED = "VOIDED"



AUDIT_SCOPE_HTTP = "HTTP"
AUDIT_SCOPE_DOMAIN = "DOMAIN"

AUDIT_OUTCOME_SUCCESS = "SUCCESS"
AUDIT_OUTCOME_ERROR = "ERROR"

AUDIT_EVENT_HTTP_REQUEST = "HTTP_REQUEST"
AUDIT_EVENT_INCIDENT_PUBLISHED = "INCIDENT_PUBLISHED"
AUDIT_EVENT_INCIDENT_ACCEPTED = "INCIDENT_ACCEPTED"
AUDIT_EVENT_INCIDENT_DISPATCHED = "INCIDENT_DISPATCHED"
AUDIT_EVENT_INCIDENT_ARRIVED = "INCIDENT_ARRIVED"
AUDIT_EVENT_INCIDENT_COMPLETED = "INCIDENT_COMPLETED"
AUDIT_EVENT_INCIDENT_CANCELLED = "INCIDENT_CANCELLED"
AUDIT_EVENT_BILLING_ESTIMATED = "BILLING_ESTIMATED"
AUDIT_EVENT_BILLING_FINALIZED = "BILLING_FINALIZED"
AUDIT_EVENT_PAYMENT_MARKED_PAID = "PAYMENT_MARKED_PAID"
AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED = "SUBSCRIPTION_PLAN_CREATED"
AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN = "CLIENT_SUBSCRIBED_TO_PLAN"
AUDIT_EVENT_COVERAGE_APPLIED = "COVERAGE_APPLIED"
```

### `app/common/exceptions.py`

- Ruta relativa: `app/common/exceptions.py`
- Nombre de archivo: `exceptions.py`

```python
import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


class AppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "app_error",
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found.") -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="not_found",
        )


class ConflictException(AppException):
    def __init__(self, message: str = "Resource already exists.") -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_409_CONFLICT,
            error_code="conflict",
        )


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Authentication required.") -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="unauthorized",
        )


class ForbiddenException(AppException):
    def __init__(self, message: str = "You do not have permission to perform this action.") -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="forbidden",
        )


class ServiceUnavailableException(AppException):
    def __init__(self, message: str = "Service unavailable.") -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_code="service_unavailable",
        )


def register_exception_handlers(app: FastAPI) -> None:
    def _request_id(request: Request) -> str | None:
        return getattr(getattr(request, "state", None), "request_id", None)

    @app.exception_handler(AppException)
    async def handle_app_exception(request: Request, exc: AppException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
                "error": {
                    "code": exc.error_code,
                },
                "meta": {
                    "request_id": _request_id(request),
                },
            },
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_exception(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "success": False,
                "message": "Validation error.",
                "error": {
                    "code": "validation_error",
                    "details": exc.errors(),
                },
                "meta": {
                    "request_id": _request_id(request),
                },
            },
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_exception(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("Unhandled exception: %s", exc)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Internal server error.",
                "error": {
                    "code": "internal_server_error",
                },
                "meta": {
                    "request_id": _request_id(request),
                },
            },
        )
```

### `app/common/responses.py`

- Ruta relativa: `app/common/responses.py`
- Nombre de archivo: `responses.py`

```python
from typing import Any


def success_response(
    message: str,
    data: Any | None = None,
    meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "success": True,
        "message": message,
        "data": data,
        "meta": meta,
    }
```

### `app/core/__init__.py`

- Ruta relativa: `app/core/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/core/config.py`

- Ruta relativa: `app/core/config.py`
- Nombre de archivo: `config.py`

```python
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    env_mode: str = "development"

    app_name: str = "Mechanic System API"
    app_version: str = "0.1.0"
    api_v1_prefix: str = "/api"
    log_level: str = "INFO"
    cors_allow_origins: str = "http://localhost:4200,http://127.0.0.1:4200"
    sql_echo: bool = False

    postgres_serv: str = "serv-mech-db"
    postgres_db: str = "mechanic_db"
    postgres_user: str = "mechanic_user"
    postgres_password: str = "mechanic_password"
    postgres_port: int = 5432

    redis_host: str = "serv-mech-redis"
    redis_port: int = 6379
    redis_db: int = 0

    celery_default_queue: str = "default"

    backend_host: str = "0.0.0.0"
    backend_port: int = 8000

    secret_key: str = "mechanic_dev_secret_key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    ai_provider: str = "null"
    storage_provider: str = "local"
    speech_to_text_provider: str = "null"
    vision_provider: str = "null"
    llm_provider: str = "null"
    routing_provider: str = "null"
    push_provider: str = "null"

    local_storage_root: str = "/app/storage"
    max_upload_size_bytes: int = 10 * 1024 * 1024

    s3_bucket_name: str | None = None
    s3_region: str | None = None
    s3_access_key_id: str | None = None
    s3_secret_access_key: str | None = None
    s3_endpoint_url: str | None = None
    s3_public_base_url: str | None = None
    s3_presigned_url_expiration_seconds: int = 900

    faster_whisper_model_size: str = "small"
    faster_whisper_device: str = "cpu"
    faster_whisper_compute_type: str = "int8"
    faster_whisper_beam_size: int = 5
    faster_whisper_vad_filter: bool = True
    faster_whisper_word_timestamps: bool = True
    faster_whisper_condition_on_previous_text: bool = False
    faster_whisper_language: str | None = None
    faster_whisper_download_timeout_seconds: int = 120

    ultralytics_yolo_model: str = "yolo11n.pt"
    ultralytics_yolo_device: str = "cpu"
    ultralytics_yolo_confidence_threshold: float = 0.25
    ultralytics_yolo_iou_threshold: float = 0.45
    ultralytics_yolo_image_size: int = 640
    ultralytics_yolo_max_detections: int = 50

    openrouter_api_key: str | None = None
    openrouter_api_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_model: str = "openrouter/auto"
    openrouter_fallback_models: str = ""
    openrouter_temperature: float = 0.2
    openrouter_max_tokens: int = 350
    openrouter_http_referer: str | None = None
    openrouter_x_title: str | None = None
    openrouter_timeout_seconds: int = 120

    graphhopper_api_key: str | None = None
    graphhopper_api_base_url: str = "https://graphhopper.com/api/1"
    graphhopper_profile: str = "car"
    graphhopper_timeout_seconds: int = 60
    graphhopper_points_encoded: bool = True

    fallback_routing_average_speed_kmh: int = 25

    maptiler_api_key: str | None = None

    firebase_project_id: str | None = None
    firebase_client_email: str | None = None
    firebase_private_key: str | None = None
    firebase_private_key_id: str | None = None
    firebase_client_id: str | None = None
    firebase_token_uri: str = "https://oauth2.googleapis.com/token"
    firebase_service_account_type: str = "service_account"
    firebase_service_account_json: str | None = None

    trusted_hosts: str = "localhost,127.0.0.1"
    docs_enabled_in_production: bool = False
    security_headers_enabled: bool = True
    https_redirect_enabled: bool = False
    hsts_max_age_seconds: int = 31536000

    request_id_header_name: str = "X-Request-ID"
    response_time_header_name: str = "X-Response-Time-Ms"

    audit_http_enabled: bool = True
    audit_http_methods: str = "POST,PUT,PATCH,DELETE"
    audit_excluded_paths: str = "/docs,/redoc,/openapi.json,/api/system/health,/api/system/readiness"

    metrics_snapshot_retention_days: int = 30

    initial_platform_admin_email: str = "admin@mechanic.local"
    initial_platform_admin_password: str = "Admin12345"
    initial_platform_admin_first_name: str = "Platform"
    initial_platform_admin_last_name: str = "Admin"
    initial_platform_admin_phone: str | None = "70000001"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_serv}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @property
    def celery_broker_url(self) -> str:
        return self.redis_url

    @property
    def celery_result_backend(self) -> str:
        return self.redis_url

    @property
    def cors_origins(self) -> list[str]:
        value = self.cors_allow_origins.strip()

        if value == "*":
            return ["*"]

        return [origin.strip() for origin in value.split(",") if origin.strip()]

    @property
    def storage_root_path(self) -> Path:
        return Path(self.local_storage_root).resolve()

    @property
    def openrouter_fallback_models_list(self) -> list[str]:
        return [
            item.strip()
            for item in self.openrouter_fallback_models.split(",")
            if item.strip()
        ]

    @property
    def firebase_private_key_normalized(self) -> str | None:
        if not self.firebase_private_key:
            return None
        return self.firebase_private_key.replace("\\n", "\n")

    @property
    def firebase_service_account_json_normalized(self) -> str | None:
        if not self.firebase_service_account_json:
            return None
        return self.firebase_service_account_json.replace("\\n", "\n")

    @property
    def trusted_hosts_list(self) -> list[str]:
        return [item.strip() for item in self.trusted_hosts.split(",") if item.strip()]

    @property
    def docs_enabled(self) -> bool:
        if self.env_mode.lower() == "development":
            return True
        return self.docs_enabled_in_production

    @property
    def audit_http_methods_list(self) -> list[str]:
        return [item.strip().upper() for item in self.audit_http_methods.split(",") if item.strip()]

    @property
    def audit_excluded_paths_list(self) -> list[str]:
        return [item.strip() for item in self.audit_excluded_paths.split(",") if item.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
```

### `app/core/database.py`

- Ruta relativa: `app/core/database.py`
- Nombre de archivo: `database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.database_url,
    echo=settings.sql_echo,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

#from sqlalchemy import create_engine, text
#from sqlalchemy.exc import SQLAlchemyError

#from app.core.config import settings

# SQLAlchemy engine using centralized config
#engine = create_engine(
#    settings.database_url,
#    pool_pre_ping=True,
#)


#def check_database_connection() -> dict:
#    """
#    Verifies database connectivity by executing a simple query.
#    """

#    try:
#        with engine.connect() as connection:
#            result = connection.execute(text("SELECT 1")).scalar()

#        return {
#            "status": "ok",
#            "database": "connected, nothing to do",
#            "result": result,
#        }

#    except SQLAlchemyError as error:
#        return {
#            "status": "error",
#            "database": "disconnected",
#            "detail": str(error),
#        }
```

### `app/core/dependencies.py`

- Ruta relativa: `app/core/dependencies.py`
- Nombre de archivo: `dependencies.py`

```python
from collections.abc import Generator

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.integrations.ai.base import IncidentAIProvider
from app.integrations.factory import (
    build_ai_provider,
    build_llm_provider,
    build_push_provider,
    build_routing_provider,
    build_speech_to_text_provider,
    build_storage_service,
    build_vision_provider,
)
from app.integrations.llm.base import IncidentSummaryProvider
from app.integrations.push.base import PushNotificationProvider
from app.integrations.routing.base import RoutingProvider
from app.integrations.speech_to_text.base import SpeechToTextProvider
from app.integrations.storage.base import StorageService
from app.integrations.vision.base import VisionAnalysisProvider

_ai_provider = build_ai_provider()
_speech_to_text_provider = build_speech_to_text_provider()
_vision_provider = build_vision_provider()
_llm_provider = build_llm_provider()
_routing_provider = build_routing_provider()
_push_provider = build_push_provider()
_storage_service = build_storage_service()


def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_ai_provider() -> IncidentAIProvider:
    return _ai_provider


def get_speech_to_text_provider() -> SpeechToTextProvider:
    return _speech_to_text_provider


def get_vision_provider() -> VisionAnalysisProvider:
    return _vision_provider


def get_llm_provider() -> IncidentSummaryProvider:
    return _llm_provider


def get_routing_provider() -> RoutingProvider:
    return _routing_provider


def get_push_provider() -> PushNotificationProvider:
    return _push_provider


def get_storage_service() -> StorageService:
    return _storage_service
```

### `app/core/logging_config.py`

- Ruta relativa: `app/core/logging_config.py`
- Nombre de archivo: `logging_config.py`

```python
from logging.config import dictConfig

from app.core.config import settings


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                }
            },
            "root": {
                "level": settings.log_level.upper(),
                "handlers": ["default"],
            },
        }
    )
```

### `app/core/middleware.py`

- Ruta relativa: `app/core/middleware.py`
- Nombre de archivo: `middleware.py`

```python
import time
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.core.config import settings
from app.core.security import decode_access_token
from app.services.audit.dispatcher import AuditEventDispatcher


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get(settings.request_id_header_name) or str(uuid4())
        request.state.request_id = request_id
        start_time = time.perf_counter()

        response = await call_next(request)

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        response.headers[settings.request_id_header_name] = request_id
        response.headers[settings.response_time_header_name] = str(elapsed_ms)

        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if not settings.security_headers_enabled:
            return response

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

        if settings.https_redirect_enabled:
            response.headers["Strict-Transport-Security"] = (
                f"max-age={settings.hsts_max_age_seconds}; includeSubDomains"
            )

        return response


class AuditHttpMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if not settings.audit_http_enabled:
            return response

        normalized_path = request.url.path
        if request.method.upper() not in settings.audit_http_methods_list:
            return response

        if any(normalized_path.startswith(path) for path in settings.audit_excluded_paths_list):
            return response

        actor_user_id = self._extract_actor_user_id(request)
        request_id = getattr(request.state, "request_id", None)

        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=None,
                provider_id=None,
                request_id=request_id,
                event_scope="HTTP",
                event_type="HTTP_REQUEST",
                entity_type="ROUTE",
                entity_id=normalized_path,
                http_method=request.method.upper(),
                route_path=normalized_path,
                ip_address=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                status_code=response.status_code,
                outcome="SUCCESS" if response.status_code < 400 else "ERROR",
                payload_json={
                    "query_param_keys": sorted(list(request.query_params.keys())),
                    "response_time_ms": response.headers.get(settings.response_time_header_name),
                },
            )
        except Exception:
            return response

        return response

    def _extract_actor_user_id(self, request: Request) -> str | None:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return None

        if not authorization_header.lower().startswith("bearer "):
            return None

        token = authorization_header.split(" ", 1)[1].strip()
        if not token:
            return None

        try:
            payload = decode_access_token(token)
        except Exception:
            return None

        user_id = payload.get("sub")
        return str(user_id) if user_id else None
```

### `app/core/security.py`

- Ruta relativa: `app/core/security.py`
- Nombre de archivo: `security.py`

```python
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.common.exceptions import ForbiddenException, UnauthorizedException
from app.core.config import settings
from app.core.dependencies import get_db_session
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository

password_hasher = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)


def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return password_hasher.verify(plain_password, password_hash)


def create_access_token(
    subject: str,
    email: str,
    role_codes: list[str],
    expires_minutes: int | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    expiration_minutes = expires_minutes or settings.access_token_expire_minutes
    expires_at = now + timedelta(minutes=expiration_minutes)

    payload: dict[str, Any] = {
        "sub": subject,
        "email": email,
        "roles": role_codes,
        "iat": int(now.timestamp()),
        "exp": int(expires_at.timestamp()),
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.jwt_algorithm,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except InvalidTokenError as exc:
        raise UnauthorizedException("Invalid or expired access token.") from exc


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db_session),
) -> User:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise UnauthorizedException("Bearer token is required.")

    payload = decode_access_token(credentials.credentials)
    user_id = payload.get("sub")

    if not user_id:
        raise UnauthorizedException("Invalid token payload.")

    repository = AuthRepository(db)
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise UnauthorizedException("Authenticated user was not found.")

    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise UnauthorizedException("This user account is inactive.")

    return current_user


def require_roles(*allowed_role_codes: str):
    def dependency(current_user: User = Depends(get_current_active_user)) -> User:
        user_role_codes = {role.code for role in current_user.roles}

        if not user_role_codes.intersection(set(allowed_role_codes)):
            raise ForbiddenException(
                "You do not have the required role to access this resource."
            )

        return current_user

    return dependency
```

### `app/integrations/__init__.py`

- Ruta relativa: `app/integrations/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/ai/__init__.py`

- Ruta relativa: `app/integrations/ai/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/ai/base.py`

- Ruta relativa: `app/integrations/ai/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class AIIncidentAnalysisRequest:
    incident_id: str
    user_text: str | None = None
    audio_file_path: str | None = None
    image_file_paths: list[str] = field(default_factory=list)
    latitude: float | None = None
    longitude: float | None = None


@dataclass(slots=True)
class AIIncidentAnalysisResult:
    category: str | None = None
    summary: str | None = None
    confidence: float | None = None
    requires_more_information: bool = False
    raw_response: dict[str, Any] = field(default_factory=dict)


class IncidentAIProvider(Protocol):
    provider_name: str

    def analyze_incident(
        self,
        request: AIIncidentAnalysisRequest,
    ) -> AIIncidentAnalysisResult:
        ...
```

### `app/integrations/ai/null_provider.py`

- Ruta relativa: `app/integrations/ai/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
from app.integrations.ai.base import (
    AIIncidentAnalysisRequest,
    AIIncidentAnalysisResult,
)


class NullIncidentAIProvider:
    provider_name = "null"

    def analyze_incident(
        self,
        request: AIIncidentAnalysisRequest,
    ) -> AIIncidentAnalysisResult:
        return AIIncidentAnalysisResult(
            category="unknown",
            summary=(
                "No AI provider has been configured yet. "
                "This is a placeholder adapter prepared for future integration."
            ),
            confidence=0.0,
            requires_more_information=True,
            raw_response={
                "provider": self.provider_name,
                "incident_id": request.incident_id,
            },
        )
```

### `app/integrations/factory.py`

- Ruta relativa: `app/integrations/factory.py`
- Nombre de archivo: `factory.py`

```python
from app.common.exceptions import ServiceUnavailableException
from app.core.config import settings
from app.integrations.ai.base import IncidentAIProvider
from app.integrations.ai.null_provider import NullIncidentAIProvider
from app.integrations.llm.base import IncidentSummaryProvider
from app.integrations.llm.null_provider import NullIncidentSummaryProvider
from app.integrations.llm.openrouter_provider import OpenRouterIncidentSummaryProvider
from app.integrations.push.base import PushNotificationProvider
from app.integrations.push.firebase_fcm_provider import FirebaseFcmPushNotificationProvider
from app.integrations.push.null_provider import NullPushNotificationProvider
from app.integrations.routing.base import RoutingProvider
from app.integrations.routing.graphhopper_provider import GraphHopperRoutingProvider
from app.integrations.routing.null_provider import NullRoutingProvider
from app.integrations.speech_to_text.base import SpeechToTextProvider
from app.integrations.speech_to_text.faster_whisper_provider import (
    FasterWhisperSpeechToTextProvider,
)
from app.integrations.speech_to_text.null_provider import NullSpeechToTextProvider
from app.integrations.storage.base import StorageService
from app.integrations.storage.local_storage import LocalStorageService
from app.integrations.storage.s3_storage import S3StorageService
from app.integrations.vision.base import VisionAnalysisProvider
from app.integrations.vision.null_provider import NullVisionAnalysisProvider
from app.integrations.vision.ultralytics_yolo_provider import (
    UltralyticsYoloVisionProvider,
)


def build_ai_provider() -> IncidentAIProvider:
    if settings.ai_provider.lower() == "null":
        return NullIncidentAIProvider()

    return NullIncidentAIProvider()


def build_speech_to_text_provider() -> SpeechToTextProvider:
    selected_provider = settings.speech_to_text_provider.lower()

    if selected_provider == "null":
        return NullSpeechToTextProvider()

    if selected_provider == "faster_whisper":
        return FasterWhisperSpeechToTextProvider()

    raise ServiceUnavailableException(
        f"Unsupported speech-to-text provider configured: {selected_provider}."
    )


def build_vision_provider() -> VisionAnalysisProvider:
    selected_provider = settings.vision_provider.lower()

    if selected_provider == "null":
        return NullVisionAnalysisProvider()

    if selected_provider == "ultralytics_yolo":
        return UltralyticsYoloVisionProvider()

    raise ServiceUnavailableException(
        f"Unsupported vision provider configured: {selected_provider}."
    )


def build_llm_provider() -> IncidentSummaryProvider:
    selected_provider = settings.llm_provider.lower()

    if selected_provider == "null":
        return NullIncidentSummaryProvider()

    if selected_provider == "openrouter":
        return OpenRouterIncidentSummaryProvider()

    raise ServiceUnavailableException(
        f"Unsupported LLM provider configured: {selected_provider}."
    )


def build_routing_provider() -> RoutingProvider:
    selected_provider = settings.routing_provider.lower()

    if selected_provider == "null":
        return NullRoutingProvider()

    if selected_provider == "graphhopper":
        return GraphHopperRoutingProvider()

    raise ServiceUnavailableException(
        f"Unsupported routing provider configured: {selected_provider}."
    )


def build_push_provider() -> PushNotificationProvider:
    selected_provider = settings.push_provider.lower()

    if selected_provider == "null":
        return NullPushNotificationProvider()

    if selected_provider in {"fcm", "firebase_fcm"}:
        return FirebaseFcmPushNotificationProvider()

    raise ServiceUnavailableException(
        f"Unsupported push provider configured: {selected_provider}."
    )


def build_storage_service(provider_name: str | None = None) -> StorageService:
    selected_provider = (provider_name or settings.storage_provider).strip().lower()

    if selected_provider == "local":
        return LocalStorageService()

    if selected_provider == "s3":
        return S3StorageService()

    raise ServiceUnavailableException(
        f"Unsupported storage provider configured: {selected_provider}."
    )


def build_storage_service_by_name(provider_name: str | None) -> StorageService:
    return build_storage_service(provider_name=provider_name)
```

### `app/integrations/llm/__init__.py`

- Ruta relativa: `app/integrations/llm/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/llm/base.py`

- Ruta relativa: `app/integrations/llm/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class IncidentSummaryRequest:
    incident_id: str
    user_text: str | None = None
    transcript_text: str | None = None
    image_analysis_summary: str | None = None


@dataclass(slots=True)
class IncidentSummaryResult:
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool = False
    raw_response: dict[str, Any] = field(default_factory=dict)


class IncidentSummaryProvider(Protocol):
    provider_name: str

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        ...
```

### `app/integrations/llm/null_provider.py`

- Ruta relativa: `app/integrations/llm/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
from app.integrations.llm.base import IncidentSummaryRequest, IncidentSummaryResult


class NullIncidentSummaryProvider:
    provider_name = "null"

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        return IncidentSummaryResult(
            structured_summary=(
                "No LLM provider has been configured yet. "
                "This is a placeholder incident summary."
            ),
            suggested_category="UNCERTAIN",
            suggested_priority="MEDIUM",
            requires_more_information=True,
            raw_response={
                "provider": self.provider_name,
                "incident_id": request.incident_id,
            },
        )
```

### `app/integrations/llm/openrouter_provider.py`

- Ruta relativa: `app/integrations/llm/openrouter_provider.py`
- Nombre de archivo: `openrouter_provider.py`

```python
import json
import logging
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.common.constants import (
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OTHER,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_UNCERTAIN,
    INCIDENT_PRIORITY_CRITICAL,
    INCIDENT_PRIORITY_HIGH,
    INCIDENT_PRIORITY_LOW,
    INCIDENT_PRIORITY_MEDIUM,
    PUBLIC_INCIDENT_CATEGORIES,
)
from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.llm.base import IncidentSummaryRequest, IncidentSummaryResult

logger = logging.getLogger(__name__)


class OpenRouterIncidentSummaryProvider:
    provider_name = "openrouter"

    def __init__(self) -> None:
        self.api_key = settings.openrouter_api_key
        self.base_url = settings.openrouter_api_base_url.rstrip("/")
        self.primary_model = settings.openrouter_model
        self.fallback_models = settings.openrouter_fallback_models_list
        self.temperature = settings.openrouter_temperature
        self.max_tokens = settings.openrouter_max_tokens
        self.site_url = settings.openrouter_http_referer
        self.site_title = settings.openrouter_x_title
        self.timeout_seconds = settings.openrouter_timeout_seconds

        if not self.api_key:
            raise ConflictException(
                "OpenRouter provider is selected but OPENROUTER_API_KEY is not configured."
            )

        if not self.primary_model:
            raise ConflictException(
                "OpenRouter provider is selected but OPENROUTER_MODEL is not configured."
            )

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        messages = self._build_messages(request)
        request_body = self._build_request_body(messages)

        try:
            raw_response = self._send_request(request_body)
            assistant_content = self._extract_assistant_content(raw_response)
            parsed_payload = self._parse_json_payload(assistant_content)
            normalized_payload = self._normalize_payload(parsed_payload, assistant_content)

            response_metadata = {
                "provider": self.provider_name,
                "api_base_url": self.base_url,
                "requested_model": self.primary_model,
                "fallback_models": self.fallback_models,
                "response_id": raw_response.get("id"),
                "response_model": raw_response.get("model"),
                "usage": raw_response.get("usage"),
                "raw_message_content": assistant_content,
            }

            return IncidentSummaryResult(
                structured_summary=normalized_payload["structured_summary"],
                suggested_category=normalized_payload["suggested_category"],
                suggested_priority=normalized_payload["suggested_priority"],
                requires_more_information=normalized_payload["requires_more_information"],
                raw_response=response_metadata,
            )
        except (HTTPError, URLError) as exc:
            logger.exception(
                "OpenRouter request failed for incident_id=%s",
                request.incident_id,
            )
            raise ServiceUnavailableException(
                f"OpenRouter request failed: {self._build_network_error_message(exc)}"
            ) from exc
        except Exception as exc:
            logger.exception(
                "OpenRouter incident summary failed for incident_id=%s",
                request.incident_id,
            )
            raise ServiceUnavailableException(
                f"LLM provider failed: {str(exc)}"
            ) from exc

    def _build_messages(self, request: IncidentSummaryRequest) -> list[dict[str, str]]:
        allowed_categories = ", ".join(PUBLIC_INCIDENT_CATEGORIES)
        allowed_priorities = ", ".join(
            [
                INCIDENT_PRIORITY_LOW,
                INCIDENT_PRIORITY_MEDIUM,
                INCIDENT_PRIORITY_HIGH,
                INCIDENT_PRIORITY_CRITICAL,
            ]
        )

        system_prompt = f"""
You are an expert roadside assistance triage engine for a vehicular emergency platform.

Your task is to read multimodal incident information and produce a concise structured incident record.

Rules:
- Return ONLY valid JSON.
- Do not wrap the JSON in markdown.
- Do not include explanations outside the JSON.
- The JSON schema must be:
{{
  "structured_summary": "string",
  "suggested_category": "one of [{allowed_categories}]",
  "suggested_priority": "one of [{allowed_priorities}]",
  "requires_more_information": true or false
}}

Classification guidance:
- {INCIDENT_CATEGORY_BATTERY}: battery discharged, no ignition, dashboard/battery clues
- {INCIDENT_CATEGORY_TIRE}: flat tire, damaged tire, wheel issue
- {INCIDENT_CATEGORY_ACCIDENT}: visible crash, collision, impact scene, multiple vehicles, visible damage after a hit
- {INCIDENT_CATEGORY_ENGINE}: engine or mechanical failure without clear battery/tire/lockout specialization
- {INCIDENT_CATEGORY_LOCKOUT}: locked keys, door lock issue, inability to access vehicle
- {INCIDENT_CATEGORY_OVERHEATING}: overheating, steam, high temperature warnings
- {INCIDENT_CATEGORY_OTHER}: roadside assistance case that does not fit the above
- {INCIDENT_CATEGORY_UNCERTAIN}: insufficient or conflicting information

Priority guidance:
- {INCIDENT_PRIORITY_LOW}: low urgency, minor inconvenience, no safety signal
- {INCIDENT_PRIORITY_MEDIUM}: standard roadside assistance required
- {INCIDENT_PRIORITY_HIGH}: urgent roadside assistance, blocking situation, vulnerable location, or stronger risk
- {INCIDENT_PRIORITY_CRITICAL}: immediate danger, accident with possible injuries or high-risk scenario

Use requires_more_information=true when information is ambiguous, contradictory, too weak, or insufficient.
Make the summary practical for a workshop or mobile mechanic.
""".strip()

        user_sections = [
            f"Incident ID: {request.incident_id}",
            f"Client reported text:\n{request.user_text or 'N/A'}",
            f"Audio transcription:\n{request.transcript_text or 'N/A'}",
            f"Visual analysis summary:\n{request.image_analysis_summary or 'N/A'}",
        ]

        user_prompt = "\n\n".join(user_sections).strip()

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def _build_request_body(self, messages: list[dict[str, str]]) -> dict[str, Any]:
        request_body: dict[str, Any] = {
            "model": self.primary_model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stream": False,
        }

        if self.fallback_models:
            request_body["models"] = self.fallback_models

        return request_body

    def _send_request(self, request_body: dict[str, Any]) -> dict[str, Any]:
        payload_bytes = json.dumps(request_body).encode("utf-8")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if self.site_url:
            headers["HTTP-Referer"] = self.site_url

        if self.site_title:
            headers["X-OpenRouter-Title"] = self.site_title

        http_request = Request(
            url=f"{self.base_url}/chat/completions",
            data=payload_bytes,
            headers=headers,
            method="POST",
        )

        with urlopen(http_request, timeout=self.timeout_seconds) as response:
            response_body = response.read().decode("utf-8")

        return json.loads(response_body)

    def _extract_assistant_content(self, raw_response: dict[str, Any]) -> str:
        choices = raw_response.get("choices") or []
        if not choices:
            raise ServiceUnavailableException("OpenRouter response does not contain choices.")

        message = choices[0].get("message") or {}
        content = message.get("content")

        if isinstance(content, str):
            return content.strip()

        if isinstance(content, list):
            extracted_parts: list[str] = []
            for item in content:
                if isinstance(item, dict):
                    text_value = item.get("text")
                    if text_value:
                        extracted_parts.append(str(text_value))
                elif isinstance(item, str):
                    extracted_parts.append(item)

            merged_content = "\n".join(part.strip() for part in extracted_parts if part.strip()).strip()
            if merged_content:
                return merged_content

        raise ServiceUnavailableException("OpenRouter response does not contain message content.")

    def _parse_json_payload(self, assistant_content: str) -> dict[str, Any]:
        normalized_content = assistant_content.strip()

        if normalized_content.startswith("```"):
            normalized_content = self._strip_markdown_code_fence(normalized_content)

        try:
            return json.loads(normalized_content)
        except json.JSONDecodeError:
            extracted_json = self._extract_first_json_object(normalized_content)
            if extracted_json is None:
                raise
            return json.loads(extracted_json)

    def _normalize_payload(
        self,
        parsed_payload: dict[str, Any],
        raw_content: str,
    ) -> dict[str, Any]:
        structured_summary = self._normalize_summary(
            parsed_payload.get("structured_summary"),
            raw_content=raw_content,
        )

        suggested_category = self._normalize_category(
            parsed_payload.get("suggested_category")
        )

        suggested_priority = self._normalize_priority(
            parsed_payload.get("suggested_priority")
        )

        requires_more_information = self._normalize_requires_more_information(
            parsed_payload.get("requires_more_information"),
            suggested_category=suggested_category,
            structured_summary=structured_summary,
        )

        return {
            "structured_summary": structured_summary,
            "suggested_category": suggested_category,
            "suggested_priority": suggested_priority,
            "requires_more_information": requires_more_information,
        }

    def _normalize_summary(self, value: Any, raw_content: str) -> str:
        if isinstance(value, str):
            cleaned_value = value.strip()
            if cleaned_value:
                return cleaned_value

        fallback_summary = raw_content.strip()
        if fallback_summary:
            return fallback_summary[:4000]

        return "No se pudo generar un resumen estructurado del incidente."

    def _normalize_category(self, value: Any) -> str:
        if not isinstance(value, str):
            return INCIDENT_CATEGORY_UNCERTAIN

        normalized_value = value.strip().upper()
        if normalized_value in PUBLIC_INCIDENT_CATEGORIES:
            return normalized_value

        category_aliases = {
            "COLLISION": INCIDENT_CATEGORY_ACCIDENT,
            "CRASH": INCIDENT_CATEGORY_ACCIDENT,
            "CHOQUE": INCIDENT_CATEGORY_ACCIDENT,
            "FLAT_TIRE": INCIDENT_CATEGORY_TIRE,
            "TYRE": INCIDENT_CATEGORY_TIRE,
            "TIRE": INCIDENT_CATEGORY_TIRE,
            "BATTERY_ISSUE": INCIDENT_CATEGORY_BATTERY,
            "ENGINE_FAILURE": INCIDENT_CATEGORY_ENGINE,
            "OVERHEAT": INCIDENT_CATEGORY_OVERHEATING,
            "LOCKED_OUT": INCIDENT_CATEGORY_LOCKOUT,
            "UNKNOWN": INCIDENT_CATEGORY_UNCERTAIN,
        }

        return category_aliases.get(normalized_value, INCIDENT_CATEGORY_UNCERTAIN)

    def _normalize_priority(self, value: Any) -> str:
        allowed_priorities = {
            INCIDENT_PRIORITY_LOW,
            INCIDENT_PRIORITY_MEDIUM,
            INCIDENT_PRIORITY_HIGH,
            INCIDENT_PRIORITY_CRITICAL,
        }

        if not isinstance(value, str):
            return INCIDENT_PRIORITY_MEDIUM

        normalized_value = value.strip().upper()
        if normalized_value in allowed_priorities:
            return normalized_value

        priority_aliases = {
            "NORMAL": INCIDENT_PRIORITY_MEDIUM,
            "URGENT": INCIDENT_PRIORITY_HIGH,
            "VERY_HIGH": INCIDENT_PRIORITY_HIGH,
            "EMERGENCY": INCIDENT_PRIORITY_CRITICAL,
        }

        return priority_aliases.get(normalized_value, INCIDENT_PRIORITY_MEDIUM)

    def _normalize_requires_more_information(
        self,
        value: Any,
        suggested_category: str,
        structured_summary: str,
    ) -> bool:
        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            normalized_value = value.strip().lower()
            if normalized_value in {"true", "yes", "1"}:
                return True
            if normalized_value in {"false", "no", "0"}:
                return False

        if suggested_category == INCIDENT_CATEGORY_UNCERTAIN:
            return True

        if not structured_summary or len(structured_summary.strip()) < 20:
            return True

        return False

    def _strip_markdown_code_fence(self, content: str) -> str:
        stripped = content.strip()

        if stripped.startswith("```json"):
            stripped = stripped[len("```json"):].strip()
        elif stripped.startswith("```"):
            stripped = stripped[len("```"):].strip()

        if stripped.endswith("```"):
            stripped = stripped[:-3].strip()

        return stripped

    def _extract_first_json_object(self, content: str) -> str | None:
        start_index = content.find("{")
        end_index = content.rfind("}")

        if start_index == -1 or end_index == -1 or end_index <= start_index:
            return None

        return content[start_index : end_index + 1]

    def _build_network_error_message(self, exc: HTTPError | URLError) -> str:
        if isinstance(exc, HTTPError):
            try:
                response_body = exc.read().decode("utf-8")
            except Exception:
                response_body = ""

            if response_body:
                return f"HTTP {exc.code}: {response_body}"

            return f"HTTP {exc.code}: {exc.reason}"

        return str(exc.reason)
```

### `app/integrations/push/__init__.py`

- Ruta relativa: `app/integrations/push/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/push/base.py`

- Ruta relativa: `app/integrations/push/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class PushNotificationRequest:
    recipient_token: str
    title: str
    body: str
    data: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class PushNotificationResult:
    accepted: bool
    provider_message_id: str | None = None
    raw_response: dict[str, Any] = field(default_factory=dict)


class PushNotificationProvider(Protocol):
    provider_name: str

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        ...
```

### `app/integrations/push/firebase_fcm_provider.py`

- Ruta relativa: `app/integrations/push/firebase_fcm_provider.py`
- Nombre de archivo: `firebase_fcm_provider.py`

```python
import json
import threading

import firebase_admin
from firebase_admin import credentials, messaging

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.push.base import PushNotificationRequest, PushNotificationResult


class FirebaseFcmPushNotificationProvider:
    provider_name = "firebase_fcm"

    _firebase_app = None
    _firebase_app_lock = threading.Lock()

    def __init__(self) -> None:
        if not settings.firebase_project_id and not settings.firebase_service_account_json_normalized:
            raise ConflictException(
                "Firebase FCM provider is selected but Firebase credentials are not configured."
            )

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        firebase_app = self._get_or_initialize_app()

        normalized_data = {
            str(key): str(value)
            for key, value in (request.data or {}).items()
            if value is not None
        }

        message = messaging.Message(
            token=request.recipient_token,
            notification=messaging.Notification(
                title=request.title,
                body=request.body,
            ),
            data=normalized_data or None,
        )

        try:
            provider_message_id = messaging.send(message, app=firebase_app)

            return PushNotificationResult(
                accepted=True,
                provider_message_id=provider_message_id,
                raw_response={
                    "provider": self.provider_name,
                    "project_id": settings.firebase_project_id,
                    "device_token_suffix": request.recipient_token[-12:],
                    "data_keys": sorted(normalized_data.keys()),
                },
            )
        except Exception as exc:
            raise ServiceUnavailableException(
                f"Firebase FCM push failed: {str(exc)}"
            ) from exc

    def _get_or_initialize_app(self):
        existing_app = self.__class__._firebase_app
        if existing_app is not None:
            return existing_app

        with self.__class__._firebase_app_lock:
            existing_app = self.__class__._firebase_app
            if existing_app is not None:
                return existing_app

            credential_info = self._build_credential_info()
            firebase_credential = credentials.Certificate(credential_info)

            options = {}
            project_id = credential_info.get("project_id") or settings.firebase_project_id
            if project_id:
                options["projectId"] = project_id

            self.__class__._firebase_app = firebase_admin.initialize_app(
                credential=firebase_credential,
                options=options or None,
            )
            return self.__class__._firebase_app

    def _build_credential_info(self) -> dict:
        raw_service_account_json = settings.firebase_service_account_json_normalized
        if raw_service_account_json:
            try:
                credential_info = json.loads(raw_service_account_json)
            except json.JSONDecodeError as exc:
                raise ConflictException(
                    "FIREBASE_SERVICE_ACCOUNT_JSON is not valid JSON."
                ) from exc

            private_key = credential_info.get("private_key")
            if isinstance(private_key, str):
                credential_info["private_key"] = private_key.replace("\\n", "\n")

            return credential_info

        private_key = settings.firebase_private_key_normalized
        if not private_key:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_PRIVATE_KEY is not configured."
            )

        if not settings.firebase_client_email:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_CLIENT_EMAIL is not configured."
            )

        project_id = settings.firebase_project_id
        if not project_id:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_PROJECT_ID is not configured."
            )

        return {
            "type": settings.firebase_service_account_type,
            "project_id": project_id,
            "private_key_id": settings.firebase_private_key_id or "env",
            "private_key": private_key,
            "client_email": settings.firebase_client_email,
            "client_id": settings.firebase_client_id or "env",
            "token_uri": settings.firebase_token_uri,
        }
```

### `app/integrations/push/null_provider.py`

- Ruta relativa: `app/integrations/push/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
from app.integrations.push.base import PushNotificationRequest, PushNotificationResult


class NullPushNotificationProvider:
    provider_name = "null"

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        return PushNotificationResult(
            accepted=False,
            provider_message_id=None,
            raw_response={
                "provider": self.provider_name,
                "recipient_token": request.recipient_token,
                "title": request.title,
            },
        )
```

### `app/integrations/routing/__init__.py`

- Ruta relativa: `app/integrations/routing/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/routing/base.py`

- Ruta relativa: `app/integrations/routing/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class RouteCalculationRequest:
    origin_latitude: float
    origin_longitude: float
    destination_latitude: float
    destination_longitude: float
    profile: str | None = None


@dataclass(slots=True)
class RouteCalculationResult:
    distance_meters: float | None
    duration_seconds: int | None
    polyline: str | None
    raw_response: dict | None = None


class RoutingProvider(Protocol):
    provider_name: str

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        ...
```

### `app/integrations/routing/graphhopper_provider.py`

- Ruta relativa: `app/integrations/routing/graphhopper_provider.py`
- Nombre de archivo: `graphhopper_provider.py`

```python
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.routing.base import RouteCalculationRequest, RouteCalculationResult


class GraphHopperRoutingProvider:
    provider_name = "graphhopper"

    def __init__(self) -> None:
        self.api_key = settings.graphhopper_api_key
        self.api_base_url = settings.graphhopper_api_base_url.rstrip("/")
        self.default_profile = settings.graphhopper_profile
        self.timeout_seconds = settings.graphhopper_timeout_seconds
        self.points_encoded = settings.graphhopper_points_encoded

        if not self.api_key:
            raise ConflictException(
                "GraphHopper provider is selected but GRAPHHOPPER_API_KEY is not configured."
            )

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        profile = request.profile or self.default_profile

        query_params = [
            ("point", f"{request.origin_latitude},{request.origin_longitude}"),
            ("point", f"{request.destination_latitude},{request.destination_longitude}"),
            ("profile", profile),
            ("instructions", "false"),
            ("calc_points", "true"),
            ("points_encoded", "true" if self.points_encoded else "false"),
            ("key", self.api_key),
        ]

        url = f"{self.api_base_url}/route?{urlencode(query_params)}"

        try:
            with urlopen(url, timeout=self.timeout_seconds) as response:
                response_body = response.read().decode("utf-8")

            payload = json.loads(response_body)
            paths = payload.get("paths") or []
            if not paths:
                raise ServiceUnavailableException("GraphHopper response did not contain paths.")

            path = paths[0]
            distance_meters = path.get("distance")
            duration_millis = path.get("time")
            polyline = path.get("points")

            return RouteCalculationResult(
                distance_meters=float(distance_meters) if distance_meters is not None else None,
                duration_seconds=int(duration_millis / 1000) if duration_millis is not None else None,
                polyline=polyline if isinstance(polyline, str) else None,
                raw_response={
                    "provider": self.provider_name,
                    "profile": profile,
                    "raw_path": path,
                },
            )
        except HTTPError as exc:
            try:
                error_body = exc.read().decode("utf-8")
            except Exception:
                error_body = str(exc)

            raise ServiceUnavailableException(
                f"GraphHopper request failed with HTTP {exc.code}: {error_body}"
            ) from exc
        except URLError as exc:
            raise ServiceUnavailableException(
                f"GraphHopper request failed: {str(exc.reason)}"
            ) from exc
```

### `app/integrations/routing/null_provider.py`

- Ruta relativa: `app/integrations/routing/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
import math

from app.core.config import settings
from app.integrations.routing.base import RouteCalculationRequest, RouteCalculationResult


class NullRoutingProvider:
    provider_name = "null_haversine"

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        distance_meters = self._haversine_distance_meters(
            request.origin_latitude,
            request.origin_longitude,
            request.destination_latitude,
            request.destination_longitude,
        )

        average_speed_kmh = max(settings.fallback_routing_average_speed_kmh, 1)
        duration_seconds = int((distance_meters / 1000.0) / average_speed_kmh * 3600)

        return RouteCalculationResult(
            distance_meters=round(distance_meters, 2),
            duration_seconds=max(duration_seconds, 0),
            polyline=None,
            raw_response={
                "provider": self.provider_name,
                "approximation": "haversine",
                "average_speed_kmh": average_speed_kmh,
            },
        )

    def _haversine_distance_meters(
        self,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float,
    ) -> float:
        earth_radius_m = 6371000.0

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2) ** 2
            + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return earth_radius_m * c
```

### `app/integrations/speech_to_text/__init__.py`

- Ruta relativa: `app/integrations/speech_to_text/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/speech_to_text/base.py`

- Ruta relativa: `app/integrations/speech_to_text/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class AudioTranscriptionRequest:
    evidence_id: str
    audio_file_path: str | None = None
    source_url: str | None = None
    language_hint: str | None = None


@dataclass(slots=True)
class AudioTranscriptionResult:
    transcript_text: str | None = None
    language_code: str | None = None
    confidence: float | None = None
    segments: list[dict[str, Any]] = field(default_factory=list)
    raw_response: dict[str, Any] = field(default_factory=dict)


class SpeechToTextProvider(Protocol):
    provider_name: str

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        ...
```

### `app/integrations/speech_to_text/faster_whisper_provider.py`

- Ruta relativa: `app/integrations/speech_to_text/faster_whisper_provider.py`
- Nombre de archivo: `faster_whisper_provider.py`

```python
import logging
import os
import tempfile
import threading
from pathlib import Path
from statistics import mean
from typing import Any
from urllib.parse import urlparse
from urllib.request import urlopen

from faster_whisper import WhisperModel

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.speech_to_text.base import (
    AudioTranscriptionRequest,
    AudioTranscriptionResult,
)

logger = logging.getLogger(__name__)


class FasterWhisperSpeechToTextProvider:
    provider_name = "faster_whisper"

    _model_cache: dict[tuple[str, str, str], WhisperModel] = {}
    _model_cache_lock = threading.Lock()

    def __init__(self) -> None:
        self.model_size = settings.faster_whisper_model_size
        self.device = settings.faster_whisper_device
        self.compute_type = settings.faster_whisper_compute_type
        self.beam_size = settings.faster_whisper_beam_size
        self.vad_filter = settings.faster_whisper_vad_filter
        self.word_timestamps = settings.faster_whisper_word_timestamps
        self.condition_on_previous_text = settings.faster_whisper_condition_on_previous_text
        self.language = settings.faster_whisper_language
        self.download_timeout_seconds = settings.faster_whisper_download_timeout_seconds

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        audio_source_path, cleanup_path = self._resolve_audio_source(request)

        try:
            model = self._get_or_create_model()

            transcribe_kwargs: dict[str, Any] = {
                "beam_size": self.beam_size,
                "vad_filter": self.vad_filter,
                "word_timestamps": self.word_timestamps,
                "condition_on_previous_text": self.condition_on_previous_text,
                "task": "transcribe",
            }

            language_hint = request.language_hint or self.language
            if language_hint:
                transcribe_kwargs["language"] = language_hint

            segments, info = model.transcribe(audio_source_path, **transcribe_kwargs)
            segment_items = []
            transcript_parts: list[str] = []
            word_probabilities: list[float] = []

            for index, segment in enumerate(list(segments), start=1):
                cleaned_text = (segment.text or "").strip()
                if cleaned_text:
                    transcript_parts.append(cleaned_text)

                segment_words = []
                if getattr(segment, "words", None):
                    for word in segment.words:
                        probability = getattr(word, "probability", None)
                        if probability is not None:
                            word_probabilities.append(float(probability))

                        segment_words.append(
                            {
                                "start": getattr(word, "start", None),
                                "end": getattr(word, "end", None),
                                "word": getattr(word, "word", None),
                                "probability": probability,
                            }
                        )

                segment_items.append(
                    {
                        "segment_index": index,
                        "seek": getattr(segment, "seek", None),
                        "start": getattr(segment, "start", None),
                        "end": getattr(segment, "end", None),
                        "text": cleaned_text,
                        "avg_logprob": getattr(segment, "avg_logprob", None),
                        "no_speech_prob": getattr(segment, "no_speech_prob", None),
                        "compression_ratio": getattr(segment, "compression_ratio", None),
                        "words": segment_words,
                    }
                )

            transcript_text = "\n".join(part for part in transcript_parts if part).strip() or None
            transcript_confidence = (
                float(mean(word_probabilities))
                if word_probabilities
                else float(getattr(info, "language_probability", 0.0) or 0.0)
            )

            raw_response = {
                "provider": self.provider_name,
                "model_size": self.model_size,
                "device": self.device,
                "compute_type": self.compute_type,
                "beam_size": self.beam_size,
                "vad_filter": self.vad_filter,
                "word_timestamps": self.word_timestamps,
                "detected_language": getattr(info, "language", None),
                "language_probability": getattr(info, "language_probability", None),
                "duration": getattr(info, "duration", None),
                "duration_after_vad": getattr(info, "duration_after_vad", None),
            }

            return AudioTranscriptionResult(
                transcript_text=transcript_text,
                language_code=getattr(info, "language", None),
                confidence=transcript_confidence,
                segments=segment_items,
                raw_response=raw_response,
            )
        except Exception as exc:
            logger.exception("faster-whisper transcription failed for evidence_id=%s", request.evidence_id)
            raise ServiceUnavailableException(
                f"Speech-to-text provider failed: {str(exc)}"
            ) from exc
        finally:
            if cleanup_path and os.path.exists(cleanup_path):
                try:
                    os.remove(cleanup_path)
                except OSError:
                    logger.warning("Temporary audio file could not be removed: %s", cleanup_path)

    def _get_or_create_model(self) -> WhisperModel:
        cache_key = (self.model_size, self.device, self.compute_type)

        with self._model_cache_lock:
            existing_model = self._model_cache.get(cache_key)
            if existing_model is not None:
                return existing_model

            logger.info(
                "Loading faster-whisper model size=%s device=%s compute_type=%s",
                self.model_size,
                self.device,
                self.compute_type,
            )
            model = WhisperModel(
                self.model_size,
                device=self.device,
                compute_type=self.compute_type,
            )
            self._model_cache[cache_key] = model
            return model

    def _resolve_audio_source(
        self,
        request: AudioTranscriptionRequest,
    ) -> tuple[str, str | None]:
        if request.audio_file_path:
            audio_path = Path(request.audio_file_path).resolve()
            if not audio_path.exists():
                raise ConflictException("Audio file path does not exist for transcription.")
            return str(audio_path), None

        if request.source_url:
            temporary_file_path = self._download_remote_audio_to_tempfile(request.source_url)
            return temporary_file_path, temporary_file_path

        raise ConflictException("No audio source was provided for transcription.")

    def _download_remote_audio_to_tempfile(self, source_url: str) -> str:
        suffix = self._infer_suffix_from_url(source_url)

        with urlopen(source_url, timeout=self.download_timeout_seconds) as response:
            file_bytes = response.read()

        if not file_bytes:
            raise ConflictException("Remote audio source is empty.")

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temporary_file:
            temporary_file.write(file_bytes)
            temporary_file.flush()
            return temporary_file.name

    def _infer_suffix_from_url(self, source_url: str) -> str:
        parsed_url = urlparse(source_url)
        suffix = Path(parsed_url.path).suffix.lower()
        return suffix or ".audio"
```

### `app/integrations/speech_to_text/null_provider.py`

- Ruta relativa: `app/integrations/speech_to_text/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
from app.integrations.speech_to_text.base import (
    AudioTranscriptionRequest,
    AudioTranscriptionResult,
)


class NullSpeechToTextProvider:
    provider_name = "null"

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        return AudioTranscriptionResult(
            transcript_text=(
                "No speech-to-text provider has been configured yet. "
                "This is a placeholder transcription result."
            ),
            language_code="unknown",
            confidence=0.0,
            segments=[],
            raw_response={
                "provider": self.provider_name,
                "evidence_id": request.evidence_id,
            },
        )
```

### `app/integrations/storage/__init__.py`

- Ruta relativa: `app/integrations/storage/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/storage/base.py`

- Ruta relativa: `app/integrations/storage/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass
from typing import Protocol

from fastapi import UploadFile


@dataclass(slots=True)
class StoredObjectMetadata:
    storage_provider: str
    stored_filename: str
    mime_type: str | None
    file_size_bytes: int
    absolute_file_path: str | None = None
    storage_bucket: str | None = None
    storage_object_key: str | None = None
    public_url: str | None = None


@dataclass(slots=True)
class StorageDownloadDescriptor:
    kind: str  # local_file | signed_url
    filename: str
    media_type: str | None = None
    absolute_file_path: str | None = None
    download_url: str | None = None


class StorageService(Protocol):
    provider_name: str

    async def save_uploaded_file(
        self,
        incident_id: str,
        upload_file: UploadFile,
    ) -> StoredObjectMetadata:
        ...

    def save_text_content(
        self,
        incident_id: str,
        text_content: str,
    ) -> StoredObjectMetadata:
        ...

    def build_download_descriptor(
        self,
        *,
        absolute_file_path: str | None,
        storage_bucket: str | None,
        storage_object_key: str | None,
        public_url: str | None,
        original_filename: str | None,
        stored_filename: str,
        mime_type: str | None,
    ) -> StorageDownloadDescriptor:
        ...
```

### `app/integrations/storage/local_storage.py`

- Ruta relativa: `app/integrations/storage/local_storage.py`
- Nombre de archivo: `local_storage.py`

```python
import mimetypes
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.common.exceptions import ConflictException
from app.core.config import settings
from app.integrations.storage.base import (
    StorageDownloadDescriptor,
    StorageService,
    StoredObjectMetadata,
)


class LocalStorageService(StorageService):
    provider_name = "local"

    def __init__(self) -> None:
        self.storage_root = settings.storage_root_path
        self.storage_root.mkdir(parents=True, exist_ok=True)

    def build_incident_directory(self, incident_id: str) -> Path:
        incident_directory = self.storage_root / "incidents" / incident_id
        incident_directory.mkdir(parents=True, exist_ok=True)
        return incident_directory

    async def save_uploaded_file(
        self,
        incident_id: str,
        upload_file: UploadFile,
    ) -> StoredObjectMetadata:
        file_bytes = await upload_file.read()

        if not file_bytes:
            raise ConflictException("Uploaded file is empty.")

        if len(file_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Uploaded file exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        original_filename = upload_file.filename or "uploaded_file"
        safe_extension = Path(original_filename).suffix.lower()
        generated_filename = f"{uuid4().hex}{safe_extension}"

        incident_directory = self.build_incident_directory(incident_id)
        absolute_path = incident_directory / generated_filename
        absolute_path.write_bytes(file_bytes)

        mime_type = upload_file.content_type or self.guess_mime_type(original_filename)

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type=mime_type,
            file_size_bytes=len(file_bytes),
            absolute_file_path=str(absolute_path),
            storage_bucket=None,
            storage_object_key=None,
            public_url=None,
        )

    def save_text_content(
        self,
        incident_id: str,
        text_content: str,
    ) -> StoredObjectMetadata:
        cleaned_text = text_content.strip()

        if not cleaned_text:
            raise ConflictException("Text evidence cannot be empty.")

        text_bytes = cleaned_text.encode("utf-8")

        if len(text_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Text evidence exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        incident_directory = self.build_incident_directory(incident_id)
        generated_filename = f"{uuid4().hex}.txt"
        absolute_path = incident_directory / generated_filename

        absolute_path.write_text(cleaned_text, encoding="utf-8")

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type="text/plain",
            file_size_bytes=len(text_bytes),
            absolute_file_path=str(absolute_path),
            storage_bucket=None,
            storage_object_key=None,
            public_url=None,
        )

    def build_download_descriptor(
        self,
        *,
        absolute_file_path: str | None,
        storage_bucket: str | None,
        storage_object_key: str | None,
        public_url: str | None,
        original_filename: str | None,
        stored_filename: str,
        mime_type: str | None,
    ) -> StorageDownloadDescriptor:
        if not absolute_file_path:
            raise ConflictException("Local evidence does not contain an absolute file path.")

        file_path = Path(absolute_file_path).resolve()

        if not str(file_path).startswith(str(self.storage_root)):
            raise ConflictException("Invalid evidence file path.")

        if not file_path.exists():
            raise ConflictException("Evidence file was not found on disk.")

        return StorageDownloadDescriptor(
            kind="local_file",
            filename=original_filename or stored_filename,
            media_type=mime_type or "application/octet-stream",
            absolute_file_path=str(file_path),
            download_url=None,
        )

    def guess_mime_type(self, filename: str) -> str:
        guessed_type, _ = mimetypes.guess_type(filename)
        return guessed_type or "application/octet-stream"
```

### `app/integrations/storage/s3_storage.py`

- Ruta relativa: `app/integrations/storage/s3_storage.py`
- Nombre de archivo: `s3_storage.py`

```python
import mimetypes
from pathlib import Path
from uuid import uuid4

import boto3
from botocore.client import BaseClient

from fastapi import UploadFile

from app.common.exceptions import ConflictException
from app.core.config import settings
from app.integrations.storage.base import (
    StorageDownloadDescriptor,
    StorageService,
    StoredObjectMetadata,
)


class S3StorageService(StorageService):
    provider_name = "s3"

    def __init__(self) -> None:
        self.bucket_name = settings.s3_bucket_name
        self.region = settings.s3_region
        self.endpoint_url = settings.s3_endpoint_url
        self.public_base_url = settings.s3_public_base_url
        self.presigned_expiration_seconds = settings.s3_presigned_url_expiration_seconds

        self.client: BaseClient = boto3.client(
            "s3",
            region_name=self.region,
            aws_access_key_id=settings.s3_access_key_id,
            aws_secret_access_key=settings.s3_secret_access_key,
            endpoint_url=self.endpoint_url,
        )

    async def save_uploaded_file(
        self,
        incident_id: str,
        upload_file: UploadFile,
    ) -> StoredObjectMetadata:
        self._ensure_bucket_name()

        file_bytes = await upload_file.read()

        if not file_bytes:
            raise ConflictException("Uploaded file is empty.")

        if len(file_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Uploaded file exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        original_filename = upload_file.filename or "uploaded_file"
        safe_extension = Path(original_filename).suffix.lower()
        generated_filename = f"{uuid4().hex}{safe_extension}"
        object_key = self._build_object_key(incident_id, generated_filename)
        mime_type = upload_file.content_type or self.guess_mime_type(original_filename)

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=object_key,
            Body=file_bytes,
            ContentType=mime_type or "application/octet-stream",
        )

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type=mime_type,
            file_size_bytes=len(file_bytes),
            absolute_file_path=None,
            storage_bucket=self.bucket_name,
            storage_object_key=object_key,
            public_url=self._build_public_url(object_key),
        )

    def save_text_content(
        self,
        incident_id: str,
        text_content: str,
    ) -> StoredObjectMetadata:
        self._ensure_bucket_name()

        cleaned_text = text_content.strip()

        if not cleaned_text:
            raise ConflictException("Text evidence cannot be empty.")

        text_bytes = cleaned_text.encode("utf-8")

        if len(text_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Text evidence exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        generated_filename = f"{uuid4().hex}.txt"
        object_key = self._build_object_key(incident_id, generated_filename)

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=object_key,
            Body=text_bytes,
            ContentType="text/plain",
        )

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type="text/plain",
            file_size_bytes=len(text_bytes),
            absolute_file_path=None,
            storage_bucket=self.bucket_name,
            storage_object_key=object_key,
            public_url=self._build_public_url(object_key),
        )

    def build_download_descriptor(
        self,
        *,
        absolute_file_path: str | None,
        storage_bucket: str | None,
        storage_object_key: str | None,
        public_url: str | None,
        original_filename: str | None,
        stored_filename: str,
        mime_type: str | None,
    ) -> StorageDownloadDescriptor:
        bucket_name = storage_bucket or self.bucket_name

        if not bucket_name:
            raise ConflictException("S3 evidence does not contain a bucket reference.")

        if not storage_object_key:
            raise ConflictException("S3 evidence does not contain an object key.")

        filename = original_filename or stored_filename

        params = {
            "Bucket": bucket_name,
            "Key": storage_object_key,
            "ResponseContentDisposition": f'attachment; filename="{filename}"',
        }

        if mime_type:
            params["ResponseContentType"] = mime_type

        signed_url = self.client.generate_presigned_url(
            ClientMethod="get_object",
            Params=params,
            ExpiresIn=self.presigned_expiration_seconds,
        )

        return StorageDownloadDescriptor(
            kind="signed_url",
            filename=filename,
            media_type=mime_type or "application/octet-stream",
            absolute_file_path=None,
            download_url=signed_url,
        )

    def _build_object_key(self, incident_id: str, filename: str) -> str:
        return f"incidents/{incident_id}/{filename}"

    def _ensure_bucket_name(self) -> None:
        if not self.bucket_name:
            raise ConflictException(
                "S3 storage provider is selected but S3_BUCKET_NAME is not configured."
            )

    def _build_public_url(self, object_key: str) -> str | None:
        if not self.public_base_url:
            return None

        return f"{self.public_base_url.rstrip('/')}/{object_key}"

    def guess_mime_type(self, filename: str) -> str:
        guessed_type, _ = mimetypes.guess_type(filename)
        return guessed_type or "application/octet-stream"
```

### `app/integrations/vision/__init__.py`

- Ruta relativa: `app/integrations/vision/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/integrations/vision/base.py`

- Ruta relativa: `app/integrations/vision/base.py`
- Nombre de archivo: `base.py`

```python
from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class ImageAnalysisRequest:
    evidence_id: str
    image_file_path: str | None = None
    source_url: str | None = None


@dataclass(slots=True)
class ImageAnalysisResult:
    labels: list[str] = field(default_factory=list)
    detections: list[dict[str, Any]] = field(default_factory=list)
    summary: str | None = None
    raw_response: dict[str, Any] = field(default_factory=dict)


class VisionAnalysisProvider(Protocol):
    provider_name: str

    def analyze_image(
        self,
        request: ImageAnalysisRequest,
    ) -> ImageAnalysisResult:
        ...
```

### `app/integrations/vision/null_provider.py`

- Ruta relativa: `app/integrations/vision/null_provider.py`
- Nombre de archivo: `null_provider.py`

```python
from app.integrations.vision.base import ImageAnalysisRequest, ImageAnalysisResult


class NullVisionAnalysisProvider:
    provider_name = "null"

    def analyze_image(
        self,
        request: ImageAnalysisRequest,
    ) -> ImageAnalysisResult:
        return ImageAnalysisResult(
            labels=["unknown"],
            detections=[],
            summary=(
                "No vision provider has been configured yet. "
                "This is a placeholder image analysis result."
            ),
            raw_response={
                "provider": self.provider_name,
                "evidence_id": request.evidence_id,
            },
        )
```

### `app/integrations/vision/ultralytics_yolo_provider.py`

- Ruta relativa: `app/integrations/vision/ultralytics_yolo_provider.py`
- Nombre de archivo: `ultralytics_yolo_provider.py`

```python
import logging
import threading
from collections import Counter, defaultdict
from typing import Any

from ultralytics import YOLO

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.vision.base import ImageAnalysisRequest, ImageAnalysisResult

logger = logging.getLogger(__name__)


class UltralyticsYoloVisionProvider:
    provider_name = "ultralytics_yolo"

    _model_cache: dict[tuple[str, str], YOLO] = {}
    _model_cache_lock = threading.Lock()

    def __init__(self) -> None:
        self.model_name = settings.ultralytics_yolo_model
        self.device = settings.ultralytics_yolo_device
        self.confidence_threshold = settings.ultralytics_yolo_confidence_threshold
        self.iou_threshold = settings.ultralytics_yolo_iou_threshold
        self.image_size = settings.ultralytics_yolo_image_size
        self.max_detections = settings.ultralytics_yolo_max_detections

    def analyze_image(
        self,
        request: ImageAnalysisRequest,
    ) -> ImageAnalysisResult:
        source = self._resolve_source(request)

        try:
            model = self._get_or_create_model()

            predict_kwargs: dict[str, Any] = {
                "source": source,
                "conf": self.confidence_threshold,
                "iou": self.iou_threshold,
                "imgsz": self.image_size,
                "max_det": self.max_detections,
                "verbose": False,
                "stream": False,
            }

            if self.device:
                predict_kwargs["device"] = self.device

            results = model.predict(**predict_kwargs)

            if not results:
                return ImageAnalysisResult(
                    labels=[],
                    detections=[],
                    summary=(
                        "No se generaron resultados de visión para la imagen. "
                        "Se recomienda revisión manual."
                    ),
                    raw_response={
                        "provider": self.provider_name,
                        "model_name": self.model_name,
                        "source_kind": "url" if request.source_url else "local_file",
                    },
                )

            result = results[0]
            detections = self._extract_detections(result)
            labels = self._extract_labels(detections)
            summary = self._build_summary(labels, detections)

            return ImageAnalysisResult(
                labels=labels,
                detections=detections,
                summary=summary,
                raw_response={
                    "provider": self.provider_name,
                    "model_name": self.model_name,
                    "source_kind": "url" if request.source_url else "local_file",
                    "detection_count": len(detections),
                    "possible_incident_hint": self._infer_possible_incident_hint(labels, detections),
                    "original_image_shape": getattr(result, "orig_shape", None),
                },
            )
        except Exception as exc:
            logger.exception(
                "Ultralytics YOLO image analysis failed for evidence_id=%s",
                request.evidence_id,
            )
            raise ServiceUnavailableException(
                f"Vision provider failed: {str(exc)}"
            ) from exc

    def _get_or_create_model(self) -> YOLO:
        cache_key = (self.model_name, self.device or "auto")

        with self._model_cache_lock:
            cached_model = self._model_cache.get(cache_key)
            if cached_model is not None:
                return cached_model

            logger.info(
                "Loading Ultralytics YOLO model=%s device=%s",
                self.model_name,
                self.device or "auto",
            )
            model = YOLO(self.model_name)
            self._model_cache[cache_key] = model
            return model

    def _resolve_source(self, request: ImageAnalysisRequest) -> str:
        if request.image_file_path:
            return request.image_file_path

        if request.source_url:
            return request.source_url

        raise ConflictException("No image source was provided for visual analysis.")

    def _extract_detections(self, result: Any) -> list[dict[str, Any]]:
        boxes = getattr(result, "boxes", None)
        names = getattr(result, "names", {}) or {}

        if boxes is None or len(boxes) == 0:
            return []

        cls_values = boxes.cls.tolist() if hasattr(boxes.cls, "tolist") else list(boxes.cls)
        conf_values = boxes.conf.tolist() if hasattr(boxes.conf, "tolist") else list(boxes.conf)
        xyxy_values = boxes.xyxy.tolist() if hasattr(boxes.xyxy, "tolist") else list(boxes.xyxy)

        detections: list[dict[str, Any]] = []
        for cls_value, confidence, xyxy in zip(cls_values, conf_values, xyxy_values):
            class_id = int(cls_value)
            label = names.get(class_id, str(class_id))

            x1, y1, x2, y2 = xyxy
            detections.append(
                {
                    "class_id": class_id,
                    "label": label,
                    "confidence": round(float(confidence), 4),
                    "bbox_xyxy": {
                        "x1": round(float(x1), 2),
                        "y1": round(float(y1), 2),
                        "x2": round(float(x2), 2),
                        "y2": round(float(y2), 2),
                    },
                }
            )

        detections.sort(key=lambda item: item["confidence"], reverse=True)
        return detections

    def _extract_labels(self, detections: list[dict[str, Any]]) -> list[str]:
        if not detections:
            return []

        frequency_by_label = Counter()
        best_confidence_by_label = defaultdict(float)

        for detection in detections:
            label = detection["label"]
            frequency_by_label[label] += 1
            best_confidence_by_label[label] = max(
                best_confidence_by_label[label],
                detection["confidence"],
            )

        ordered_labels = sorted(
            frequency_by_label.keys(),
            key=lambda label: (
                -frequency_by_label[label],
                -best_confidence_by_label[label],
                label.lower(),
            ),
        )

        return ordered_labels

    def _build_summary(
        self,
        labels: list[str],
        detections: list[dict[str, Any]],
    ) -> str:
        if not detections:
            return (
                "No se detectaron objetos visibles con confianza suficiente en la imagen. "
                "La imagen puede requerir revisión manual o complementarse con texto y audio."
            )

        top_detections_text = ", ".join(
            f"{detection['label']} ({detection['confidence']:.2f})"
            for detection in detections[:3]
        )

        vehicle_labels = {"car", "truck", "bus", "motorcycle", "bicycle"}
        person_present = any(label.lower() == "person" for label in labels)
        vehicle_present = any(label.lower() in vehicle_labels for label in labels)
        multiple_vehicles = sum(
            1 for detection in detections if detection["label"].lower() in vehicle_labels
        ) >= 2

        summary_parts = [
            f"Objetos visibles detectados: {top_detections_text}.",
        ]

        if vehicle_present:
            summary_parts.append("Se observan elementos relacionados con vehículos en la escena.")

        if person_present:
            summary_parts.append("También se detecta al menos una persona en la escena.")

        if multiple_vehicles:
            summary_parts.append(
                "La presencia de múltiples vehículos puede indicar una situación vial o un incidente con más contexto visual."
            )

        summary_parts.append(
            "Este análisis visual es de apoyo y debe combinarse con audio y texto para la clasificación final del incidente."
        )

        return " ".join(summary_parts)

    def _infer_possible_incident_hint(
        self,
        labels: list[str],
        detections: list[dict[str, Any]],
    ) -> str:
        lowered_labels = {label.lower() for label in labels}

        vehicle_labels = {"car", "truck", "bus", "motorcycle", "bicycle"}
        vehicle_count = sum(
            1 for detection in detections if detection["label"].lower() in vehicle_labels
        )
        person_present = "person" in lowered_labels

        if vehicle_count >= 2 and person_present:
            return "POSSIBLE_ACCIDENT_SCENE"

        if vehicle_count >= 1:
            return "VEHICLE_PRESENT_BUT_MECHANICAL_CAUSE_NOT_DIRECTLY_VISIBLE"

        return "UNCERTAIN"
```

### `app/main.py`

- Ruta relativa: `app/main.py`
- Nombre de archivo: `main.py`

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.bootstrap.seed import seed_initial_platform_admin
from app.common.exceptions import register_exception_handlers
from app.common.responses import success_response
from app.core.config import settings
from app.core.database import SessionLocal
from app.core.logging_config import configure_logging
from app.core.middleware import AuditHttpMiddleware, RequestContextMiddleware, SecurityHeadersMiddleware
from app.services.assignment.router import router as assignment_router
from app.services.audit.router import router as audit_router
from app.services.auth.router import router as auth_router
from app.services.billing.router import router as billing_router
from app.services.catalog.router import router as catalog_router
from app.services.evidences.router import router as evidences_router
from app.services.incidents.router import router as incidents_router
from app.services.jobs.router import router as jobs_router
from app.services.notifications.router import router as notifications_router
from app.services.operations.router import router as operations_router
from app.services.providers.router import router as providers_router
from app.services.subscriptions.router import router as subscriptions_router
from app.services.system.router import router as system_router
from app.services.tracking.router import router as tracking_router
from app.services.users.router import router as users_router
from app.services.vehicles.router import router as vehicles_router

configure_logging()


@asynccontextmanager
async def lifespan(_: FastAPI):
    db = SessionLocal()
    try:
        seed_initial_platform_admin(db)
    finally:
        db.close()

    yield


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.docs_enabled else None,
        redoc_url="/redoc" if settings.docs_enabled else None,
        openapi_url="/openapi.json" if settings.docs_enabled else None,
        lifespan=lifespan,
    )

    allow_credentials = "*" not in settings.cors_origins

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(GZipMiddleware, minimum_size=500)

    if settings.trusted_hosts_list:
        application.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=settings.trusted_hosts_list,
        )

    if settings.https_redirect_enabled:
        application.add_middleware(HTTPSRedirectMiddleware)

    application.add_middleware(SecurityHeadersMiddleware)
    application.add_middleware(AuditHttpMiddleware)
    application.add_middleware(RequestContextMiddleware)

    register_exception_handlers(application)

    application.include_router(system_router, prefix=settings.api_v1_prefix)
    application.include_router(auth_router, prefix=settings.api_v1_prefix)
    application.include_router(users_router, prefix=settings.api_v1_prefix)
    application.include_router(providers_router, prefix=settings.api_v1_prefix)
    application.include_router(catalog_router, prefix=settings.api_v1_prefix)
    application.include_router(vehicles_router, prefix=settings.api_v1_prefix)
    application.include_router(incidents_router, prefix=settings.api_v1_prefix)
    application.include_router(evidences_router, prefix=settings.api_v1_prefix)
    application.include_router(jobs_router, prefix=settings.api_v1_prefix)
    application.include_router(assignment_router, prefix=settings.api_v1_prefix)
    application.include_router(operations_router, prefix=settings.api_v1_prefix)
    application.include_router(tracking_router, prefix=settings.api_v1_prefix)
    application.include_router(notifications_router, prefix=settings.api_v1_prefix)
    application.include_router(billing_router, prefix=settings.api_v1_prefix)
    application.include_router(subscriptions_router, prefix=settings.api_v1_prefix)
    application.include_router(audit_router, prefix=settings.api_v1_prefix)

    @application.get("/", tags=["Root"])
    def root() -> dict:
        return success_response(
            message="Mechanic System API initialized successfully.",
            data={
                "app_name": settings.app_name,
                "version": settings.app_version,
                "environment": settings.env_mode,
                "docs_enabled": settings.docs_enabled,
                "docs_url": "/docs" if settings.docs_enabled else None,
                "health_url": f"{settings.api_v1_prefix}/system/health",
                "readiness_url": f"{settings.api_v1_prefix}/system/readiness",
                "info_url": f"{settings.api_v1_prefix}/system/info",
                "auth_base_url": f"{settings.api_v1_prefix}/auth",
                "users_base_url": f"{settings.api_v1_prefix}/users",
                "providers_base_url": f"{settings.api_v1_prefix}/providers",
                "catalog_base_url": f"{settings.api_v1_prefix}/catalog",
                "vehicles_base_url": f"{settings.api_v1_prefix}/vehicles",
                "incidents_base_url": f"{settings.api_v1_prefix}/incidents",
                "evidences_base_url": f"{settings.api_v1_prefix}/evidences",
                "jobs_base_url": f"{settings.api_v1_prefix}/jobs",
                "assignment_base_url": f"{settings.api_v1_prefix}/assignment",
                "operations_base_url": f"{settings.api_v1_prefix}/operations",
                "tracking_base_url": f"{settings.api_v1_prefix}/tracking",
                "notifications_base_url": f"{settings.api_v1_prefix}/notifications",
                "billing_base_url": f"{settings.api_v1_prefix}/billing",
                "subscriptions_base_url": f"{settings.api_v1_prefix}/subscriptions",
                "audit_base_url": f"{settings.api_v1_prefix}/audit",
            },
        )

    return application


app = create_application()
```

### `app/services/__init__.py`

- Ruta relativa: `app/services/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/assignment/__init__.py`

- Ruta relativa: `app/services/assignment/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/assignment/models.py`

- Ruta relativa: `app/services/assignment/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentAssignmentCandidate(Base):
    __tablename__ = "incident_assignment_candidates"
    __table_args__ = (
        UniqueConstraint(
            "incident_id",
            "provider_id",
            name="uq_incident_assignment_candidate_incident_provider",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    recommendation_rank: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    score: Mapped[float] = mapped_column(Float, nullable=False)

    distance_km: Mapped[float | None] = mapped_column(Float, nullable=True)

    required_service_codes_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    matched_service_codes_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    rationale_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    provider_average_rating_snapshot: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    provider_available_capacity_snapshot: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    available_technicians_count_snapshot: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    responded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
```

### `app/services/assignment/repository.py`

- Ruta relativa: `app/services/assignment/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, delete, select
from sqlalchemy.orm import Session, selectinload

from app.services.assignment.models import IncidentAssignmentCandidate
from app.services.catalog.models import ProviderService
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class AssignmentRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id_for_update(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_id_for_update(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .where(Provider.id == provider_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_eligible_provider_pool(self) -> list[Provider]:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.technicians),
                selectinload(Provider.provider_services).selectinload(
                    ProviderService.service_catalog_item
                ),
            )
            .where(
                Provider.is_active.is_(True),
                Provider.is_available.is_(True),
            )
            .order_by(Provider.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def delete_non_accepted_candidates_by_incident_id(self, incident_id: str) -> None:
        self.db.execute(
            delete(IncidentAssignmentCandidate).where(
                IncidentAssignmentCandidate.incident_id == incident_id,
                IncidentAssignmentCandidate.status != "ACCEPTED",
            )
        )

    def create_candidates(self, candidates: list[IncidentAssignmentCandidate]) -> None:
        for candidate in candidates:
            self.db.add(candidate)

    def list_candidates_by_incident_id(
        self,
        incident_id: str,
    ) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(IncidentAssignmentCandidate.incident_id == incident_id)
            .order_by(
                IncidentAssignmentCandidate.recommendation_rank.asc(),
                IncidentAssignmentCandidate.score.desc(),
                IncidentAssignmentCandidate.created_at.asc(),
            )
        )
        return list(self.db.execute(query).scalars().all())

    def get_candidate_by_id(self, candidate_id: str) -> IncidentAssignmentCandidate | None:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(IncidentAssignmentCandidate.id == candidate_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_candidate_by_id_for_update(self, candidate_id: str) -> IncidentAssignmentCandidate | None:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .where(IncidentAssignmentCandidate.id == candidate_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_available_candidates_for_provider(self, provider_id: str) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .options(
                selectinload(IncidentAssignmentCandidate.incident),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.owner_user
                ),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.provider_services
                ).selectinload(ProviderService.service_catalog_item),
                selectinload(IncidentAssignmentCandidate.provider).selectinload(
                    Provider.technicians
                ),
            )
            .where(
                IncidentAssignmentCandidate.provider_id == provider_id,
                IncidentAssignmentCandidate.status == "AVAILABLE",
            )
            .order_by(
                IncidentAssignmentCandidate.recommendation_rank.asc(),
                IncidentAssignmentCandidate.score.desc(),
                IncidentAssignmentCandidate.created_at.asc(),
            )
        )
        return list(self.db.execute(query).scalars().all())

    def list_available_candidates_by_incident_id_for_update(
        self,
        incident_id: str,
    ) -> list[IncidentAssignmentCandidate]:
        query: Select[tuple[IncidentAssignmentCandidate]] = (
            select(IncidentAssignmentCandidate)
            .where(
                IncidentAssignmentCandidate.incident_id == incident_id,
                IncidentAssignmentCandidate.status == "AVAILABLE",
            )
            .with_for_update()
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def flush(self) -> None:
        self.db.flush()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/assignment/router.py`

- Ruta relativa: `app/services/assignment/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.assignment.repository import AssignmentRepository
from app.services.assignment.service import AssignmentService
from app.services.auth.models import User

router = APIRouter(prefix="/assignment", tags=["Assignment"])


@router.post("/platform/incidents/{incident_id}/publish")
def publish_incident_for_assignment(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.publish_incident_for_assignment(incident_id)

    return success_response(
        message="Incident published for assignment successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/candidates")
def list_platform_candidates_for_incident(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.list_platform_candidates_for_incident(incident_id)

    return success_response(
        message="Incident assignment candidates loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/available")
def list_my_available_candidates(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.list_my_available_candidates(current_user)

    return success_response(
        message="Available assignment candidates loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/available/{candidate_id}")
def get_my_available_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.get_my_available_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/available/{candidate_id}/accept")
def accept_my_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.accept_my_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate accepted successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/available/{candidate_id}/reject")
def reject_my_candidate(
    candidate_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AssignmentService(AssignmentRepository(db))
    result = service.reject_my_candidate(current_user, candidate_id)

    return success_response(
        message="Assignment candidate rejected successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/assignment/schemas.py`

- Ruta relativa: `app/services/assignment/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel


class AssignmentCandidateMatchedServiceResponse(BaseModel):
    code: str
    category: str
    title: str


class AssignmentCandidateProviderOwnerResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class AssignmentCandidateProviderResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    city: str | None = None
    contact_phone: str | None = None
    average_rating: float
    available_capacity: int
    available_technicians_count: int
    base_latitude: float | None = None
    base_longitude: float | None = None
    owner_user: AssignmentCandidateProviderOwnerResponse
    matched_services: list[AssignmentCandidateMatchedServiceResponse]


class AssignmentCandidateIncidentResponse(BaseModel):
    id: str
    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = None
    ai_summary_status: str
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool


class AssignmentCandidateResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str
    status: str
    recommendation_rank: int
    score: float
    distance_km: float | None = None
    required_service_codes: list[str]
    matched_service_codes: list[str]
    rationale: dict | None = None
    provider_average_rating_snapshot: float
    provider_available_capacity_snapshot: int
    available_technicians_count_snapshot: int
    published_at: datetime
    responded_at: datetime | None = None
    expires_at: datetime | None = None
    provider: AssignmentCandidateProviderResponse
    incident: AssignmentCandidateIncidentResponse


class AssignmentPublishResponse(BaseModel):
    incident_id: str
    incident_status: str
    used_category: str
    used_priority: str
    required_service_codes: list[str]
    published_candidates_count: int
    recommended_candidate_id: str | None = None
    recommended_provider_id: str | None = None


class AssignmentActionResponse(BaseModel):
    candidate_id: str
    candidate_status: str
    incident_id: str
    incident_status: str
    assigned_provider_id: str | None = None
    assigned_at: datetime | None = None
```

### `app/services/assignment/service.py`

- Ruta relativa: `app/services/assignment/service.py`
- Nombre de archivo: `service.py`

```python
import math
from datetime import datetime, timezone

from app.common.constants import (
    ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
    ACCOUNT_TYPE_WORKSHOP,
    ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
    ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
    ASSIGNMENT_CANDIDATE_STATUS_EXPIRED,
    ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OTHER,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_UNCERTAIN,
    INCIDENT_PRIORITY_CRITICAL,
    INCIDENT_PRIORITY_HIGH,
    INCIDENT_PRIORITY_LOW,
    INCIDENT_PRIORITY_MEDIUM,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_PENDING,
    INCIDENT_STATUS_PUBLISHED,
    PROVIDER_TYPE_WORKSHOP,
    SERVICE_CODE_ACCIDENT_SUPPORT,
    SERVICE_CODE_BATTERY_JUMPSTART,
    SERVICE_CODE_ENGINE_DIAGNOSTIC,
    SERVICE_CODE_LOCKOUT_ASSISTANCE,
    SERVICE_CODE_OVERHEATING_ASSISTANCE,
    SERVICE_CODE_TIRE_CHANGE,
    SERVICE_CODE_TOWING,
    PUSH_EVENT_INCIDENT_ACCEPTED,
    PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
    AUDIT_EVENT_INCIDENT_ACCEPTED,
    AUDIT_EVENT_INCIDENT_PUBLISHED,

)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.assignment.models import IncidentAssignmentCandidate
from app.services.assignment.repository import AssignmentRepository
from app.services.assignment.schemas import (
    AssignmentActionResponse,
    AssignmentCandidateIncidentResponse,
    AssignmentCandidateMatchedServiceResponse,
    AssignmentCandidateProviderOwnerResponse,
    AssignmentCandidateProviderResponse,
    AssignmentCandidateResponse,
    AssignmentPublishResponse,
)
from app.services.auth.models import User
from app.services.catalog.models import ProviderService
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.services.audit.dispatcher import AuditEventDispatcher


class AssignmentService:
    def __init__(self, repository: AssignmentRepository) -> None:
        self.repository = repository

    def publish_incident_for_assignment(self, incident_id: str) -> AssignmentPublishResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.status in (
            INCIDENT_STATUS_ASSIGNED,
            INCIDENT_STATUS_IN_PROGRESS,
            INCIDENT_STATUS_COMPLETED,
            INCIDENT_STATUS_CANCELLED,
        ):
            raise ConflictException(
                "This incident cannot be published for assignment in its current status."
            )

        if incident.provider_id is not None:
            raise ConflictException("This incident is already linked to a provider.")

        used_category = (
            incident.suggested_category.strip().upper()
            if incident.suggested_category
            else incident.reported_category.strip().upper()
        )
        used_priority = (
            incident.suggested_priority.strip().upper()
            if incident.suggested_priority
            else incident.priority.strip().upper()
        )
        required_service_codes = self._map_incident_category_to_required_service_codes(used_category)

        provider_pool = self.repository.list_eligible_provider_pool()
        ranked_candidates = self._build_ranked_candidates(
            incident=incident,
            providers=provider_pool,
            used_category=used_category,
            used_priority=used_priority,
            required_service_codes=required_service_codes,
        )

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by a provider.")

            self.repository.delete_non_accepted_candidates_by_incident_id(incident_id)

            candidates_to_create = []
            for index, ranked_candidate in enumerate(ranked_candidates, start=1):
                candidate = IncidentAssignmentCandidate(
                    incident_id=locked_incident.id,
                    provider_id=ranked_candidate["provider"].id,
                    status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
                    recommendation_rank=index,
                    score=ranked_candidate["score"],
                    distance_km=ranked_candidate["distance_km"],
                    required_service_codes_json=required_service_codes,
                    matched_service_codes_json=ranked_candidate["matched_service_codes"],
                    rationale_json=ranked_candidate["rationale"],
                    provider_average_rating_snapshot=ranked_candidate["provider"].average_rating,
                    provider_available_capacity_snapshot=ranked_candidate["available_capacity"],
                    available_technicians_count_snapshot=ranked_candidate["available_technicians_count"],
                    published_at=datetime.now(timezone.utc),
                    responded_at=None,
                    expires_at=None,
                )
                candidates_to_create.append(candidate)

            locked_incident.status = INCIDENT_STATUS_PUBLISHED
            self.repository.save(locked_incident)
            self.repository.create_candidates(candidates_to_create)
            self.repository.commit()
            self._emit_audit_safely(
            actor_user_id=None,
            incident_id=str(locked_incident.id),
            provider_id=None,
            request_id=None,
            event_scope="DOMAIN",
            event_type=AUDIT_EVENT_INCIDENT_PUBLISHED,
            entity_type="INCIDENT",
            entity_id=str(locked_incident.id),
            payload_json={
                "used_category": used_category,
                "used_priority": used_priority,
                "required_service_codes": required_service_codes,
                "published_candidates_count": len(ranked_candidates),
            },
            )

        except Exception:
            self.repository.rollback()
            raise

        recommended_candidate = ranked_candidates[0] if ranked_candidates else None
        self._enqueue_notification_safely(
        lambda: self._enqueue_candidate_publication_notifications(incident_id)
        )


        return AssignmentPublishResponse(
            incident_id=str(incident.id),
            incident_status=INCIDENT_STATUS_PUBLISHED,
            used_category=used_category,
            used_priority=used_priority,
            required_service_codes=required_service_codes,
            published_candidates_count=len(ranked_candidates),
            recommended_candidate_id=None,
            recommended_provider_id=(
                str(recommended_candidate["provider"].id)
                if recommended_candidate is not None
                else None
            ),
        )

    def list_platform_candidates_for_incident(
        self,
        incident_id: str,
    ) -> list[AssignmentCandidateResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        candidates = self.repository.list_candidates_by_incident_id(incident_id)
        return [self._build_candidate_response(item) for item in candidates]

    def list_my_available_candidates(self, current_user: User) -> list[AssignmentCandidateResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        candidates = self.repository.list_available_candidates_for_provider(str(provider.id))
        visible_candidates = [
            candidate
            for candidate in candidates
            if candidate.incident.status == INCIDENT_STATUS_PUBLISHED
            and candidate.incident.provider_id is None
        ]
        return [self._build_candidate_response(item) for item in visible_candidates]

    def get_my_available_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentCandidateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        candidate = self.repository.get_candidate_by_id(candidate_id)
        if candidate is None:
            raise NotFoundException("Assignment candidate not found.")

        if str(candidate.provider_id) != str(provider.id):
            raise ForbiddenException("This assignment candidate does not belong to your provider.")

        if candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
            raise ConflictException("This assignment candidate is no longer available.")

        if candidate.incident.status != INCIDENT_STATUS_PUBLISHED or candidate.incident.provider_id is not None:
            raise ConflictException("This incident is no longer available for assignment.")

        return self._build_candidate_response(candidate)

    def accept_my_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentActionResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_candidate = self.repository.get_candidate_by_id_for_update(candidate_id)
            if locked_candidate is None:
                raise NotFoundException("Assignment candidate not found.")

            if str(locked_candidate.provider_id) != str(provider.id):
                raise ForbiddenException("This assignment candidate does not belong to your provider.")

            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            if locked_provider.available_capacity <= 0:
                raise ConflictException("Your provider has no available capacity for a new incident.")

            locked_incident = self.repository.get_incident_by_id_for_update(str(locked_candidate.incident_id))
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by another provider.")

            if locked_incident.status != INCIDENT_STATUS_PUBLISHED:
                raise ConflictException("This incident is not currently published for assignment.")

            if locked_candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
                raise ConflictException("This assignment candidate is no longer available.")

            locked_candidate.status = ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED
            locked_candidate.responded_at = now

            locked_incident.provider_id = locked_provider.id
            locked_incident.status = INCIDENT_STATUS_ASSIGNED
            locked_incident.assigned_at = now

            locked_provider.current_active_services += 1

            sibling_candidates = self.repository.list_available_candidates_by_incident_id_for_update(
                str(locked_incident.id)
            )

            for sibling in sibling_candidates:
                if str(sibling.id) == str(locked_candidate.id):
                    continue

                sibling.status = ASSIGNMENT_CANDIDATE_STATUS_EXPIRED
                sibling.responded_at = now
                existing_rationale = sibling.rationale_json or {}
                existing_rationale["closed_reason"] = "incident_taken_by_another_provider"
                sibling.rationale_json = existing_rationale
                self.repository.save(sibling)

            self.repository.save(locked_provider)
            self.repository.save(locked_candidate)
            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        self._enqueue_notification_safely(
        lambda: self._enqueue_incident_accepted_notification(str(locked_incident.id))
        )


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(locked_incident.id),
        provider_id=str(locked_provider.id),
        request_id=None,
        event_scope="DOMAIN",
        event_type=AUDIT_EVENT_INCIDENT_ACCEPTED,
        entity_type="INCIDENT",
        entity_id=str(locked_incident.id),
        payload_json={
            "candidate_id": str(locked_candidate.id),
            "provider_id": str(locked_provider.id),
            "incident_status": locked_incident.status,
        },
        )


        return AssignmentActionResponse(
            candidate_id=str(locked_candidate.id),
            candidate_status=locked_candidate.status,
            incident_id=str(locked_incident.id),
            incident_status=locked_incident.status,
            assigned_provider_id=str(locked_incident.provider_id) if locked_incident.provider_id else None,
            assigned_at=locked_incident.assigned_at,
        )

    def reject_my_candidate(
        self,
        current_user: User,
        candidate_id: str,
    ) -> AssignmentActionResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_candidate = self.repository.get_candidate_by_id_for_update(candidate_id)
            if locked_candidate is None:
                raise NotFoundException("Assignment candidate not found.")

            if str(locked_candidate.provider_id) != str(provider.id):
                raise ForbiddenException("This assignment candidate does not belong to your provider.")

            locked_incident = self.repository.get_incident_by_id_for_update(str(locked_candidate.incident_id))
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is not None or locked_incident.status == INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("This incident was already taken by another provider.")

            if locked_incident.status != INCIDENT_STATUS_PUBLISHED:
                raise ConflictException("This incident is not currently published for assignment.")

            if locked_candidate.status != ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE:
                raise ConflictException("This assignment candidate is no longer available.")

            locked_candidate.status = ASSIGNMENT_CANDIDATE_STATUS_REJECTED
            locked_candidate.responded_at = now

            existing_rationale = locked_candidate.rationale_json or {}
            existing_rationale["provider_response"] = "rejected_by_provider"
            locked_candidate.rationale_json = existing_rationale

            self.repository.save(locked_candidate)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        return AssignmentActionResponse(
            candidate_id=str(locked_candidate.id),
            candidate_status=locked_candidate.status,
            incident_id=str(locked_incident.id),
            incident_status=locked_incident.status,
            assigned_provider_id=str(locked_incident.provider_id) if locked_incident.provider_id else None,
            assigned_at=locked_incident.assigned_at,
        )

    def _build_ranked_candidates(
        self,
        incident,
        providers,
        used_category: str,
        used_priority: str,
        required_service_codes: list[str],
    ) -> list[dict]:
        ranked_candidates: list[dict] = []

        for provider in providers:
            if not provider.is_active or not provider.is_available:
                continue

            available_capacity = provider.available_capacity
            if available_capacity <= 0:
                continue

            available_technicians_count = sum(
                1 for technician in provider.technicians
                if technician.is_active and technician.is_available
            )

            if provider.provider_type == PROVIDER_TYPE_WORKSHOP and available_technicians_count <= 0:
                continue

            active_mobile_services = self._get_active_mobile_emergency_services(provider.provider_services)
            if not active_mobile_services:
                continue

            matched_services = self._match_services_for_incident(
                active_provider_services=active_mobile_services,
                used_category=used_category,
                required_service_codes=required_service_codes,
            )
            if not matched_services:
                continue

            if not self._provider_type_is_allowed(provider.provider_type, required_service_codes):
                continue

            distance_km = self._calculate_distance_km(
                incident_latitude=incident.incident_latitude,
                incident_longitude=incident.incident_longitude,
                provider_latitude=provider.base_latitude,
                provider_longitude=provider.base_longitude,
            )

            score, rationale = self._calculate_candidate_score(
                provider=provider,
                matched_services=matched_services,
                used_priority=used_priority,
                distance_km=distance_km,
                available_capacity=available_capacity,
                available_technicians_count=available_technicians_count,
            )

            ranked_candidates.append(
                {
                    "provider": provider,
                    "score": score,
                    "distance_km": distance_km,
                    "matched_services": matched_services,
                    "matched_service_codes": [item.service_catalog_item.code for item in matched_services],
                    "available_capacity": available_capacity,
                    "available_technicians_count": available_technicians_count,
                    "rationale": rationale,
                }
            )

        ranked_candidates.sort(
            key=lambda item: (
                -item["score"],
                item["distance_km"] if item["distance_km"] is not None else 999999,
                -item["provider"].average_rating,
                item["provider"].created_at,
            )
        )

        return ranked_candidates

    def _get_active_mobile_emergency_services(
        self,
        provider_services: list[ProviderService],
    ) -> list[ProviderService]:
        active_services: list[ProviderService] = []

        for provider_service in provider_services:
            catalog_item = provider_service.service_catalog_item
            if catalog_item is None:
                continue
            if not provider_service.is_active:
                continue
            if not catalog_item.is_active:
                continue
            if not provider_service.is_mobile_service_enabled:
                continue
            if not provider_service.is_emergency_service_enabled:
                continue

            active_services.append(provider_service)

        return active_services

    def _match_services_for_incident(
        self,
        active_provider_services: list[ProviderService],
        used_category: str,
        required_service_codes: list[str],
    ) -> list[ProviderService]:
        if required_service_codes:
            exact_matches = [
                item
                for item in active_provider_services
                if item.service_catalog_item.code in required_service_codes
            ]
            if exact_matches:
                return exact_matches

        if used_category in (
            INCIDENT_CATEGORY_OTHER,
            INCIDENT_CATEGORY_UNCERTAIN,
        ):
            return active_provider_services[:3]

        category_matches = [
            item
            for item in active_provider_services
            if item.service_catalog_item.category == used_category
        ]
        return category_matches

    def _provider_type_is_allowed(
        self,
        provider_type: str,
        required_service_codes: list[str],
    ) -> bool:
        if SERVICE_CODE_TOWING in required_service_codes:
            return provider_type in (ACCOUNT_TYPE_WORKSHOP,)

        return provider_type in (
            ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
            ACCOUNT_TYPE_WORKSHOP,
        )

    def _map_incident_category_to_required_service_codes(self, category: str) -> list[str]:
        mapping = {
            INCIDENT_CATEGORY_BATTERY: [SERVICE_CODE_BATTERY_JUMPSTART],
            INCIDENT_CATEGORY_TIRE: [SERVICE_CODE_TIRE_CHANGE],
            INCIDENT_CATEGORY_LOCKOUT: [SERVICE_CODE_LOCKOUT_ASSISTANCE],
            INCIDENT_CATEGORY_OVERHEATING: [SERVICE_CODE_OVERHEATING_ASSISTANCE],
            INCIDENT_CATEGORY_ENGINE: [SERVICE_CODE_ENGINE_DIAGNOSTIC],
            INCIDENT_CATEGORY_ACCIDENT: [SERVICE_CODE_ACCIDENT_SUPPORT, SERVICE_CODE_TOWING],
            INCIDENT_CATEGORY_OTHER: [],
            INCIDENT_CATEGORY_UNCERTAIN: [],
        }

        return mapping.get(category, [])

    def _calculate_candidate_score(
        self,
        provider,
        matched_services: list[ProviderService],
        used_priority: str,
        distance_km: float | None,
        available_capacity: int,
        available_technicians_count: int,
    ) -> tuple[float, dict]:
        rating_score = float(provider.average_rating) * 12.0
        capacity_score = min(available_capacity, 5) * 6.0
        technician_score = min(available_technicians_count, 5) * 3.0

        if distance_km is None:
            distance_score = 8.0
        else:
            if used_priority == INCIDENT_PRIORITY_CRITICAL:
                distance_score = max(0.0, 50.0 - (distance_km * 3.2))
            elif used_priority == INCIDENT_PRIORITY_HIGH:
                distance_score = max(0.0, 42.0 - (distance_km * 2.7))
            elif used_priority == INCIDENT_PRIORITY_MEDIUM:
                distance_score = max(0.0, 34.0 - (distance_km * 2.0))
            else:
                distance_score = max(0.0, 26.0 - (distance_km * 1.5))

        matched_service_codes = [item.service_catalog_item.code for item in matched_services]
        if SERVICE_CODE_TOWING in matched_service_codes:
            service_score = 26.0
        elif matched_services:
            service_score = 20.0
        else:
            service_score = 0.0

        total_score = rating_score + capacity_score + technician_score + distance_score + service_score

        rationale = {
            "rating_score": round(rating_score, 2),
            "capacity_score": round(capacity_score, 2),
            "technician_score": round(technician_score, 2),
            "distance_score": round(distance_score, 2),
            "service_score": round(service_score, 2),
            "matched_service_codes": matched_service_codes,
            "distance_km": round(distance_km, 2) if distance_km is not None else None,
            "priority_used": used_priority,
        }

        return round(total_score, 2), rationale

    def _calculate_distance_km(
        self,
        incident_latitude: float | None,
        incident_longitude: float | None,
        provider_latitude: float | None,
        provider_longitude: float | None,
    ) -> float | None:
        if (
            incident_latitude is None
            or incident_longitude is None
            or provider_latitude is None
            or provider_longitude is None
        ):
            return None

        earth_radius_km = 6371.0

        lat1 = math.radians(incident_latitude)
        lon1 = math.radians(incident_longitude)
        lat2 = math.radians(provider_latitude)
        lon2 = math.radians(provider_longitude)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = (
            math.sin(delta_lat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return round(earth_radius_km * c, 2)

    def _build_candidate_response(
        self,
        candidate: IncidentAssignmentCandidate,
    ) -> AssignmentCandidateResponse:
        provider = candidate.provider
        owner_user = provider.owner_user

        available_technicians_count = sum(
            1 for technician in provider.technicians
            if technician.is_active and technician.is_available
        )

        matched_services = [
            provider_service
            for provider_service in provider.provider_services
            if provider_service.service_catalog_item.code in (candidate.matched_service_codes_json or [])
        ]

        provider_payload = AssignmentCandidateProviderResponse(
            id=str(provider.id),
            provider_type=provider.provider_type,
            business_name=provider.business_name,
            city=provider.city,
            contact_phone=provider.contact_phone,
            average_rating=provider.average_rating,
            available_capacity=provider.available_capacity,
            available_technicians_count=available_technicians_count,
            base_latitude=provider.base_latitude,
            base_longitude=provider.base_longitude,
            owner_user=AssignmentCandidateProviderOwnerResponse(
                id=str(owner_user.id),
                email=owner_user.email,
                first_name=owner_user.first_name,
                last_name=owner_user.last_name,
                full_name=owner_user.full_name,
                phone_number=owner_user.phone_number,
            ),
            matched_services=[
                AssignmentCandidateMatchedServiceResponse(
                    code=item.service_catalog_item.code,
                    category=item.service_catalog_item.category,
                    title=item.effective_title,
                )
                for item in matched_services
            ],
        )

        incident = candidate.incident
        incident_payload = AssignmentCandidateIncidentResponse(
            id=str(incident.id),
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            ai_summary_status=incident.ai_summary_status,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
        )

        return AssignmentCandidateResponse(
            id=str(candidate.id),
            incident_id=str(candidate.incident_id),
            provider_id=str(candidate.provider_id),
            status=candidate.status,
            recommendation_rank=candidate.recommendation_rank,
            score=round(candidate.score, 2),
            distance_km=round(candidate.distance_km, 2) if candidate.distance_km is not None else None,
            required_service_codes=list(candidate.required_service_codes_json or []),
            matched_service_codes=list(candidate.matched_service_codes_json or []),
            rationale=candidate.rationale_json,
            provider_average_rating_snapshot=candidate.provider_average_rating_snapshot,
            provider_available_capacity_snapshot=candidate.provider_available_capacity_snapshot,
            available_technicians_count_snapshot=candidate.available_technicians_count_snapshot,
            published_at=candidate.published_at,
            responded_at=candidate.responded_at,
            expires_at=candidate.expires_at,
            provider=provider_payload,
            incident=incident_payload,
        )

    def _enqueue_candidate_publication_notifications(self, incident_id: str) -> None:
        dispatcher = PushNotificationDispatcher(self.repository.db)
        candidates = self.repository.list_candidates_by_incident_id(incident_id)

        for candidate in candidates:
            if candidate.provider is None or candidate.provider.owner_user is None:
                continue

        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
            recipient_user_ids=[str(candidate.provider.owner_user.id)],
            title="Nueva solicitud disponible",
            body=(
                f"Hay una nueva solicitud de auxilio: {candidate.incident.title}. "
                "Revísala y decide si deseas aceptarla."
            ),
            data={
                "event_code": PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
                "incident_id": str(candidate.incident_id),
                "candidate_id": str(candidate.id),
                "reported_category": candidate.incident.reported_category,
                "priority": candidate.incident.priority,
                "status": candidate.incident.status,
            },
        )


    def _enqueue_incident_accepted_notification(self, incident_id: str) -> None:
        dispatcher = PushNotificationDispatcher(self.repository.db)
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_ACCEPTED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Solicitud tomada",
            body=(
                f"{incident.provider.business_name} tomó tu solicitud y está preparando la atención."
            ),
            data={
                "event_code": PUSH_EVENT_INCIDENT_ACCEPTED,
                "incident_id": str(incident.id),
                "provider_id": str(incident.provider_id),
                "provider_name": incident.provider.business_name,
                "status": incident.status,
            },
        )


    def _enqueue_notification_safely(self, callback) -> None:
        try:
            callback()
        except Exception:
            return


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        request_id: str | None,
        event_scope: str,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
            actor_user_id=actor_user_id,
            incident_id=incident_id,
            provider_id=provider_id,
            request_id=request_id,
            event_scope=event_scope,
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            outcome="SUCCESS",
            payload_json=payload_json,
            )
        except Exception:
            return
```

### `app/services/audit/__init__.py`

- Ruta relativa: `app/services/audit/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/audit/dispatcher.py`

- Ruta relativa: `app/services/audit/dispatcher.py`
- Nombre de archivo: `dispatcher.py`

```python
from app.core.database import SessionLocal
from app.services.audit.repository import AuditRepository
from app.services.audit.service import AuditService


class AuditEventDispatcher:
    def emit(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        request_id: str | None,
        event_scope: str,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        http_method: str | None = None,
        route_path: str | None = None,
        ip_address: str | None = None,
        user_agent: str | None = None,
        status_code: int | None = None,
        outcome: str = "SUCCESS",
        payload_json: dict | None = None,
    ) -> None:
        db = SessionLocal()
        try:
            service = AuditService(AuditRepository(db))
            service.log_event(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=request_id,
                event_scope=event_scope,
                event_type=event_type,
                entity_type=entity_type,
                entity_id=entity_id,
                http_method=http_method,
                route_path=route_path,
                ip_address=ip_address,
                user_agent=user_agent,
                status_code=status_code,
                outcome=outcome,
                payload_json=payload_json,
            )
        finally:
            db.close()
```

### `app/services/audit/models.py`

- Ruta relativa: `app/services/audit/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    actor_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    incident_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    request_id: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    event_scope: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    event_type: Mapped[str] = mapped_column(String(80), nullable=False, index=True)

    entity_type: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
    entity_id: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)

    http_method: Mapped[str | None] = mapped_column(String(10), nullable=True)
    route_path: Mapped[str | None] = mapped_column(String(255), nullable=True)

    ip_address: Mapped[str | None] = mapped_column(String(120), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(Text, nullable=True)

    status_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    outcome: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        index=True,
    )

    actor_user = relationship("User", lazy="selectin")
    incident = relationship("Incident", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")


class MetricSnapshot(Base):
    __tablename__ = "metric_snapshots"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    captured_by_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    snapshot_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    payload_json: Mapped[dict] = mapped_column(JSON, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        index=True,
    )

    captured_by_user = relationship("User", lazy="selectin")
```

### `app/services/audit/repository.py`

- Ruta relativa: `app/services/audit/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.audit.models import AuditLog, MetricSnapshot


class AuditRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_audit_log(self, audit_log: AuditLog) -> AuditLog:
        self.db.add(audit_log)
        self.db.flush()
        return audit_log

    def get_audit_log_by_id(self, audit_log_id: str) -> AuditLog | None:
        query: Select[tuple[AuditLog]] = (
            select(AuditLog)
            .options(
                selectinload(AuditLog.actor_user),
                selectinload(AuditLog.incident),
                selectinload(AuditLog.provider),
            )
            .where(AuditLog.id == audit_log_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_audit_logs(
        self,
        *,
        limit: int,
        offset: int,
        event_type: str | None = None,
        actor_user_id: str | None = None,
        incident_id: str | None = None,
        provider_id: str | None = None,
        request_id: str | None = None,
    ) -> list[AuditLog]:
        query: Select[tuple[AuditLog]] = (
            select(AuditLog)
            .options(
                selectinload(AuditLog.actor_user),
                selectinload(AuditLog.incident),
                selectinload(AuditLog.provider),
            )
            .order_by(AuditLog.created_at.desc())
            .limit(limit)
            .offset(offset)
        )

        if event_type:
            query = query.where(AuditLog.event_type == event_type)

        if actor_user_id:
            query = query.where(AuditLog.actor_user_id == actor_user_id)

        if incident_id:
            query = query.where(AuditLog.incident_id == incident_id)

        if provider_id:
            query = query.where(AuditLog.provider_id == provider_id)

        if request_id:
            query = query.where(AuditLog.request_id == request_id)

        return list(self.db.execute(query).scalars().all())

    def create_metric_snapshot(self, snapshot: MetricSnapshot) -> MetricSnapshot:
        self.db.add(snapshot)
        self.db.flush()
        return snapshot

    def list_metric_snapshots(self, *, limit: int, offset: int, snapshot_type: str | None = None) -> list[MetricSnapshot]:
        query: Select[tuple[MetricSnapshot]] = (
            select(MetricSnapshot)
            .options(selectinload(MetricSnapshot.captured_by_user))
            .order_by(MetricSnapshot.created_at.desc())
            .limit(limit)
            .offset(offset)
        )

        if snapshot_type:
            query = query.where(MetricSnapshot.snapshot_type == snapshot_type)

        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/audit/router.py`

- Ruta relativa: `app/services/audit/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.audit.repository import AuditRepository
from app.services.audit.service import AuditService
from app.services.auth.models import User

router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get("/logs")
def list_audit_logs(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    event_type: str | None = None,
    actor_user_id: str | None = None,
    incident_id: str | None = None,
    provider_id: str | None = None,
    request_id: str | None = None,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuditService(AuditRepository(db))
    result = service.list_audit_logs(
        limit=limit,
        offset=offset,
        event_type=event_type,
        actor_user_id=actor_user_id,
        incident_id=incident_id,
        provider_id=provider_id,
        request_id=request_id,
    )

    return success_response(
        message="Audit logs loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/metric-snapshots")
def list_metric_snapshots(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    snapshot_type: str | None = None,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuditService(AuditRepository(db))
    result = service.list_metric_snapshots(
        limit=limit,
        offset=offset,
        snapshot_type=snapshot_type,
    )

    return success_response(
        message="Metric snapshots loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )
```

### `app/services/audit/schemas.py`

- Ruta relativa: `app/services/audit/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel


class AuditActorUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class AuditLogResponse(BaseModel):
    id: str
    actor_user_id: str | None = None
    incident_id: str | None = None
    provider_id: str | None = None
    request_id: str | None = None
    event_scope: str
    event_type: str
    entity_type: str | None = None
    entity_id: str | None = None
    http_method: str | None = None
    route_path: str | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    status_code: int | None = None
    outcome: str
    payload_json: dict | None = None
    created_at: datetime
    actor_user: AuditActorUserResponse | None = None


class MetricSnapshotCapturedByUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class MetricSnapshotResponse(BaseModel):
    id: str
    captured_by_user_id: str | None = None
    snapshot_type: str
    payload_json: dict
    created_at: datetime
    captured_by_user: MetricSnapshotCapturedByUserResponse | None = None
```

### `app/services/audit/service.py`

- Ruta relativa: `app/services/audit/service.py`
- Nombre de archivo: `service.py`

```python
from app.services.audit.models import AuditLog, MetricSnapshot
from app.services.audit.repository import AuditRepository
from app.services.audit.schemas import (
    AuditActorUserResponse,
    AuditLogResponse,
    MetricSnapshotCapturedByUserResponse,
    MetricSnapshotResponse,
)


class AuditService:
    def __init__(self, repository: AuditRepository) -> None:
        self.repository = repository

    def log_event(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        request_id: str | None,
        event_scope: str,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        http_method: str | None,
        route_path: str | None,
        ip_address: str | None,
        user_agent: str | None,
        status_code: int | None,
        outcome: str,
        payload_json: dict | None,
    ) -> AuditLogResponse:
        audit_log = AuditLog(
            actor_user_id=actor_user_id,
            incident_id=incident_id,
            provider_id=provider_id,
            request_id=request_id,
            event_scope=event_scope,
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            http_method=http_method,
            route_path=route_path,
            ip_address=ip_address,
            user_agent=user_agent,
            status_code=status_code,
            outcome=outcome,
            payload_json=payload_json,
        )

        try:
            self.repository.create_audit_log(audit_log)
            self.repository.commit()
            self.repository.refresh(audit_log)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_audit_log_response(audit_log)

    def list_audit_logs(
        self,
        *,
        limit: int,
        offset: int,
        event_type: str | None = None,
        actor_user_id: str | None = None,
        incident_id: str | None = None,
        provider_id: str | None = None,
        request_id: str | None = None,
    ) -> list[AuditLogResponse]:
        logs = self.repository.list_audit_logs(
            limit=limit,
            offset=offset,
            event_type=event_type,
            actor_user_id=actor_user_id,
            incident_id=incident_id,
            provider_id=provider_id,
            request_id=request_id,
        )
        return [self._build_audit_log_response(item) for item in logs]

    def get_audit_log_by_id(self, audit_log_id: str) -> AuditLogResponse:
        audit_log = self.repository.get_audit_log_by_id(audit_log_id)
        if audit_log is None:
            raise ValueError("Audit log not found.")

        return self._build_audit_log_response(audit_log)

    def create_metric_snapshot(
        self,
        *,
        captured_by_user_id: str | None,
        snapshot_type: str,
        payload_json: dict,
    ) -> MetricSnapshotResponse:
        snapshot = MetricSnapshot(
            captured_by_user_id=captured_by_user_id,
            snapshot_type=snapshot_type,
            payload_json=payload_json,
        )

        try:
            self.repository.create_metric_snapshot(snapshot)
            self.repository.commit()
            self.repository.refresh(snapshot)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_metric_snapshot_response(snapshot)

    def list_metric_snapshots(
        self,
        *,
        limit: int,
        offset: int,
        snapshot_type: str | None = None,
    ) -> list[MetricSnapshotResponse]:
        snapshots = self.repository.list_metric_snapshots(
            limit=limit,
            offset=offset,
            snapshot_type=snapshot_type,
        )
        return [self._build_metric_snapshot_response(item) for item in snapshots]

    def _build_audit_log_response(self, audit_log: AuditLog) -> AuditLogResponse:
        actor_payload = None
        if audit_log.actor_user is not None:
            actor = audit_log.actor_user
            actor_payload = AuditActorUserResponse(
                id=str(actor.id),
                email=actor.email,
                first_name=actor.first_name,
                last_name=actor.last_name,
                full_name=actor.full_name,
            )

        return AuditLogResponse(
            id=str(audit_log.id),
            actor_user_id=str(audit_log.actor_user_id) if audit_log.actor_user_id else None,
            incident_id=str(audit_log.incident_id) if audit_log.incident_id else None,
            provider_id=str(audit_log.provider_id) if audit_log.provider_id else None,
            request_id=audit_log.request_id,
            event_scope=audit_log.event_scope,
            event_type=audit_log.event_type,
            entity_type=audit_log.entity_type,
            entity_id=audit_log.entity_id,
            http_method=audit_log.http_method,
            route_path=audit_log.route_path,
            ip_address=audit_log.ip_address,
            user_agent=audit_log.user_agent,
            status_code=audit_log.status_code,
            outcome=audit_log.outcome,
            payload_json=audit_log.payload_json,
            created_at=audit_log.created_at,
            actor_user=actor_payload,
        )

    def _build_metric_snapshot_response(self, snapshot: MetricSnapshot) -> MetricSnapshotResponse:
        captured_by_payload = None
        if snapshot.captured_by_user is not None:
            user = snapshot.captured_by_user
            captured_by_payload = MetricSnapshotCapturedByUserResponse(
                id=str(user.id),
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                full_name=user.full_name,
            )

        return MetricSnapshotResponse(
            id=str(snapshot.id),
            captured_by_user_id=str(snapshot.captured_by_user_id) if snapshot.captured_by_user_id else None,
            snapshot_type=snapshot.snapshot_type,
            payload_json=snapshot.payload_json,
            created_at=snapshot.created_at,
            captured_by_user=captured_by_payload,
        )
```

### `app/services/auth/__init__.py`

- Ruta relativa: `app/services/auth/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/auth/models.py`

- Ruta relativa: `app/services/auth/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, Table, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


user_role_links = Table(
    "user_role_links",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("role_id", UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
)


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_system: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    users: Mapped[list["User"]] = relationship(
        secondary=user_role_links,
        back_populates="roles",
        lazy="selectin",
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(30), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    roles: Mapped[list[Role]] = relationship(
        secondary=user_role_links,
        back_populates="users",
        lazy="selectin",
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()
```

### `app/services/auth/repository.py`

- Ruta relativa: `app/services/auth/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import Role, User
from app.services.providers.models import Provider


class AuthRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_role_by_code(self, role_code: str) -> Role | None:
        query: Select[tuple[Role]] = select(Role).where(Role.code == role_code)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(
        self,
        email: str,
        password_hash: str,
        first_name: str,
        last_name: str,
        phone_number: str | None,
        assigned_roles: list[Role],
        is_superuser: bool = False,
    ) -> User:
        new_user = User(
            email=email,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_active=True,
            is_superuser=is_superuser,
            roles=assigned_roles,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def create_user_and_optional_provider(
        self,
        user: User,
        provider: Provider | None = None,
    ) -> User:
        self.db.add(user)
        self.db.flush()

        if provider is not None:
            provider.owner_user_id = user.id
            self.db.add(provider)

        self.db.commit()
        self.db.refresh(user)
        return user
```

### `app/services/auth/router.py`

- Ruta relativa: `app/services/auth/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository
from app.services.auth.schemas import LoginRequest, RegisterRequest
from app.services.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.register_user(payload)

    return success_response(
        message="User registered successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.login_user(payload)

    return success_response(
        message="Login completed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me")
def get_authenticated_user_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = AuthService(AuthRepository(db))
    result = service.build_authenticated_user(current_user)

    return success_response(
        message="Authenticated user loaded successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/auth/schemas.py`

- Ruta relativa: `app/services/auth/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class RoleResponse(BaseModel):
    id: str
    code: str
    name: str
    description: str | None = None


class AuthenticatedUserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool
    is_superuser: bool
    role_codes: list[str]
    roles: list[RoleResponse]
    created_at: datetime
    updated_at: datetime


class RegisterProviderProfileRequest(BaseModel):
    business_name: str = Field(min_length=2, max_length=150)
    legal_name: str | None = Field(default=None, max_length=180)
    description: str | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=30)
    city: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=255)
    base_latitude: float | None = None
    base_longitude: float | None = None
    max_concurrent_services: int = Field(default=1, ge=1, le=100)


class RegisterRequest(BaseModel):
    account_type: Literal["CLIENT", "INDEPENDENT_MECHANIC", "WORKSHOP"] = "CLIENT"
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    provider_profile: RegisterProviderProfileRequest | None = None


class LoginRequest(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in_minutes: int
    user: AuthenticatedUserResponse
```

### `app/services/auth/service.py`

- Ruta relativa: `app/services/auth/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.constants import (
    ACCOUNT_TYPE_CLIENT,
    ACCOUNT_TYPE_INDEPENDENT_MECHANIC,
    ACCOUNT_TYPE_WORKSHOP,
    ROLE_CLIENT,
    ROLE_PROVIDER_ADMIN,
)
from app.common.exceptions import ConflictException, NotFoundException, UnauthorizedException
from app.core.config import settings
from app.core.security import create_access_token, hash_password, verify_password
from app.services.auth.models import User
from app.services.auth.repository import AuthRepository
from app.services.auth.schemas import (
    AccessTokenResponse,
    AuthenticatedUserResponse,
    LoginRequest,
    RegisterRequest,
    RoleResponse,
)
from app.services.providers.models import Provider


class AuthService:
    def __init__(self, repository: AuthRepository) -> None:
        self.repository = repository

    def register_user(self, payload: RegisterRequest) -> AccessTokenResponse:
        normalized_email = payload.email.strip().lower()

        existing_user = self.repository.get_user_by_email(normalized_email)
        if existing_user is not None:
            raise ConflictException("A user with this email already exists.")

        account_type = payload.account_type.strip().upper()

        if account_type == ACCOUNT_TYPE_CLIENT:
            client_role = self.repository.get_role_by_code(ROLE_CLIENT)
            if client_role is None:
                raise NotFoundException("Default CLIENT role was not found.")

            new_user = User(
                email=normalized_email,
                password_hash=hash_password(payload.password),
                first_name=payload.first_name.strip(),
                last_name=payload.last_name.strip(),
                phone_number=payload.phone_number.strip() if payload.phone_number else None,
                is_active=True,
                is_superuser=False,
                roles=[client_role],
            )

            created_user = self.repository.create_user_and_optional_provider(new_user)
            return self._build_token_response(created_user)

        if account_type in (ACCOUNT_TYPE_INDEPENDENT_MECHANIC, ACCOUNT_TYPE_WORKSHOP):
            provider_admin_role = self.repository.get_role_by_code(ROLE_PROVIDER_ADMIN)
            if provider_admin_role is None:
                raise NotFoundException("Default PROVIDER_ADMIN role was not found.")

            if payload.provider_profile is None:
                raise ConflictException(
                    "Provider profile information is required for mechanic or workshop registration."
                )

            new_user = User(
                email=normalized_email,
                password_hash=hash_password(payload.password),
                first_name=payload.first_name.strip(),
                last_name=payload.last_name.strip(),
                phone_number=payload.phone_number.strip() if payload.phone_number else None,
                is_active=True,
                is_superuser=False,
                roles=[provider_admin_role],
            )

            new_provider = Provider(
                owner_user_id=None,
                provider_type=account_type,
                business_name=payload.provider_profile.business_name.strip(),
                legal_name=(
                    payload.provider_profile.legal_name.strip()
                    if payload.provider_profile.legal_name
                    else None
                ),
                description=(
                    payload.provider_profile.description.strip()
                    if payload.provider_profile.description
                    else None
                ),
                contact_email=(
                    payload.provider_profile.contact_email.strip().lower()
                    if payload.provider_profile.contact_email
                    else None
                ),
                contact_phone=(
                    payload.provider_profile.contact_phone.strip()
                    if payload.provider_profile.contact_phone
                    else None
                ),
                city=payload.provider_profile.city.strip() if payload.provider_profile.city else None,
                address=(
                    payload.provider_profile.address.strip()
                    if payload.provider_profile.address
                    else None
                ),
                base_latitude=payload.provider_profile.base_latitude,
                base_longitude=payload.provider_profile.base_longitude,
                is_active=True,
                is_available=True,
                max_concurrent_services=payload.provider_profile.max_concurrent_services,
                current_active_services=0,
                average_rating=0.0,
            )

            created_user = self.repository.create_user_and_optional_provider(
                user=new_user,
                provider=new_provider,
            )
            return self._build_token_response(created_user)

        raise ConflictException("Unsupported account type.")

    def login_user(self, payload: LoginRequest) -> AccessTokenResponse:
        normalized_email = payload.email.strip().lower()

        user = self.repository.get_user_by_email(normalized_email)
        if user is None:
            raise UnauthorizedException("Invalid email or password.")

        if not user.is_active:
            raise UnauthorizedException("This user account is inactive.")

        if not verify_password(payload.password, user.password_hash):
            raise UnauthorizedException("Invalid email or password.")

        return self._build_token_response(user)

    def build_authenticated_user(self, user: User) -> AuthenticatedUserResponse:
        role_items = [
            RoleResponse(
                id=str(role.id),
                code=role.code,
                name=role.name,
                description=role.description,
            )
            for role in sorted(user.roles, key=lambda item: item.code)
        ]

        role_codes = [role.code for role in role_items]

        return AuthenticatedUserResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            full_name=user.full_name,
            phone_number=user.phone_number,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            role_codes=role_codes,
            roles=role_items,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    def _build_token_response(self, user: User) -> AccessTokenResponse:
        role_codes = sorted(role.code for role in user.roles)

        token = create_access_token(
            subject=str(user.id),
            email=user.email,
            role_codes=role_codes,
            expires_minutes=settings.access_token_expire_minutes,
        )

        return AccessTokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_minutes=settings.access_token_expire_minutes,
            user=self.build_authenticated_user(user),
        )
```

### `app/services/billing/__init__.py`

- Ruta relativa: `app/services/billing/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/billing/models.py`

- Ruta relativa: `app/services/billing/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentBilling(Base):
    __tablename__ = "incident_billings"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    client_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    currency_code: Mapped[str] = mapped_column(String(10), nullable=False, default="BOB", server_default="BOB")

    estimated_price_min: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_price_max: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    final_price_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    platform_commission_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 4),
        nullable=False,
        default=Decimal("0.1000"),
        server_default="0.1000",
    )
    platform_commission_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    provider_gross_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    provider_net_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    client_plan_subscription_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("client_plan_subscriptions.id", ondelete="SET NULL"),
        nullable=True,
    )
    plan_coverage_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plan_coverages.id", ondelete="SET NULL"),
        nullable=True,
    )
    coverage_applied_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    client_payable_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    payment_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="PENDING_PRICING",
        server_default="PENDING_PRICING",
        index=True,
    )
    payment_method: Mapped[str | None] = mapped_column(String(30), nullable=True)
    payment_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    payment_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)

    checkout_reference: Mapped[str | None] = mapped_column(String(120), nullable=True)
    checkout_payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    pricing_note: Mapped[str | None] = mapped_column(Text, nullable=True)

    pricing_finalized_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    payment_completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    client_user = relationship("User", foreign_keys=[client_user_id], lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
```

### `app/services/billing/repository.py`

- Ruta relativa: `app/services/billing/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.billing.models import IncidentBilling
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class BillingRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.assigned_technician),
                selectinload(Incident.vehicle),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id_for_update(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.provider_services).selectinload(
                    Provider.provider_services.property.entity.class_.service_catalog_item
                ),
            )
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_billing_by_incident_id(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .options(
                selectinload(IncidentBilling.client_user),
                selectinload(IncidentBilling.provider).selectinload(Provider.owner_user),
                selectinload(IncidentBilling.incident),
            )
            .where(IncidentBilling.incident_id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_billing_by_incident_id_for_update(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .where(IncidentBilling.incident_id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/billing/router.py`

- Ruta relativa: `app/services/billing/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.billing.repository import BillingRepository
from app.services.billing.schemas import (
    ClientCheckoutPreviewRequest,
    ClientMarkIncidentPaidRequest,
    ProviderEstimateIncidentPricingRequest,
    ProviderFinalizeIncidentPricingRequest,
)
from app.services.billing.service import BillingService

router = APIRouter(prefix="/billing", tags=["Billing"])


@router.get("/client/incidents/{incident_id}")
def get_my_client_incident_billing(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_my_client_incident_billing(current_user, incident_id)

    return success_response(
        message="Client incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/checkout-preview")
def create_client_checkout_preview(
    incident_id: str,
    payload: ClientCheckoutPreviewRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.create_client_checkout_preview(current_user, incident_id, payload)

    return success_response(
        message="Client checkout preview created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/mark-paid")
def mark_client_incident_as_paid(
    incident_id: str,
    payload: ClientMarkIncidentPaidRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.mark_client_incident_as_paid(current_user, incident_id, payload)

    return success_response(
        message="Incident payment marked as paid successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}")
def get_my_provider_incident_billing(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_my_provider_incident_billing(current_user, incident_id)

    return success_response(
        message="Provider incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/estimate")
def upsert_provider_incident_estimate(
    incident_id: str,
    payload: ProviderEstimateIncidentPricingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.upsert_provider_incident_estimate(current_user, incident_id, payload)

    return success_response(
        message="Incident estimate updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/finalize")
def finalize_provider_incident_pricing(
    incident_id: str,
    payload: ProviderFinalizeIncidentPricingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.finalize_provider_incident_pricing(current_user, incident_id, payload)

    return success_response(
        message="Incident pricing finalized successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}")
def get_platform_incident_billing(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = BillingService(BillingRepository(db))
    result = service.get_platform_incident_billing(incident_id)

    return success_response(
        message="Platform incident billing loaded successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/billing/schemas.py`

- Ruta relativa: `app/services/billing/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ProviderEstimateIncidentPricingRequest(BaseModel):
    estimated_price_min: float | None = Field(default=None, ge=0)
    estimated_price_max: float | None = Field(default=None, ge=0)
    note: str | None = Field(default=None, max_length=1000)


class ProviderFinalizeIncidentPricingRequest(BaseModel):
    final_price_amount: float = Field(gt=0)
    payment_method: Literal["CASH", "QR", "GATEWAY", "TRANSFER", "CARD"] | None = None
    mark_as_paid: bool = False
    payment_reference: str | None = Field(default=None, max_length=255)
    note: str | None = Field(default=None, max_length=1000)


class ClientCheckoutPreviewRequest(BaseModel):
    payment_method: Literal["QR", "GATEWAY", "TRANSFER", "CARD"]
    payment_provider_name: str | None = Field(default="mock_checkout", max_length=50)
    return_url: str | None = Field(default=None, max_length=500)


class ClientMarkIncidentPaidRequest(BaseModel):
    payment_method: Literal["QR", "GATEWAY", "TRANSFER", "CARD", "CASH"]
    payment_provider_name: str | None = Field(default="manual", max_length=50)
    payment_reference: str | None = Field(default=None, max_length=255)


class BillingUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class BillingProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    owner_user: BillingUserSummaryResponse | None = None


class IncidentBillingResponse(BaseModel):
    id: str
    incident_id: str
    client_user_id: str | None = None
    provider_id: str | None = None

    currency_code: str

    estimated_price_min: float | None = None
    estimated_price_max: float | None = None
    final_price_amount: float | None = None

    platform_commission_rate: float
    platform_commission_amount: float | None = None
    provider_gross_amount: float | None = None
    provider_net_amount: float | None = None

    client_plan_subscription_id: str | None = None
    plan_coverage_id: str | None = None
    coverage_applied_amount: float | None = None
    client_payable_amount: float | None = None

    payment_status: str
    payment_method: str | None = None
    payment_provider_name: str | None = None
    payment_reference: str | None = None

    checkout_reference: str | None = None
    checkout_payload_json: dict | None = None

    pricing_note: str | None = None
    pricing_finalized_at: datetime | None = None
    payment_completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    created_at: datetime
    updated_at: datetime

    provider: BillingProviderSummaryResponse | None = None
    client_user: BillingUserSummaryResponse | None = None


class BillingCheckoutPreviewResponse(BaseModel):
    incident_id: str
    checkout_reference: str
    payment_method: str
    payment_provider_name: str
    amount: float
    currency_code: str
    payment_status: str
    checkout_payload_json: dict | None = None
```

### `app/services/billing/service.py`

- Ruta relativa: `app/services/billing/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from uuid import uuid4

from app.common.constants import (
    DEFAULT_CURRENCY_CODE,
    DEFAULT_PLATFORM_COMMISSION_RATE,
    INCIDENT_STATUS_CANCELLED,
    PAYMENT_STATUS_CANCELLED,
    PAYMENT_STATUS_ESTIMATED,
    PAYMENT_STATUS_PAID,
    PAYMENT_STATUS_PENDING_PAYMENT,
    PAYMENT_STATUS_PENDING_PRICING,
    AUDIT_EVENT_BILLING_ESTIMATED,
    AUDIT_EVENT_BILLING_FINALIZED,
    AUDIT_EVENT_PAYMENT_MARKED_PAID,

    
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.billing.models import IncidentBilling
from app.services.billing.repository import BillingRepository
from app.services.billing.schemas import (
    BillingCheckoutPreviewResponse,
    BillingProviderSummaryResponse,
    BillingUserSummaryResponse,
    ClientCheckoutPreviewRequest,
    ClientMarkIncidentPaidRequest,
    IncidentBillingResponse,
    ProviderEstimateIncidentPricingRequest,
    ProviderFinalizeIncidentPricingRequest,
)
from app.services.audit.dispatcher import AuditEventDispatcher

MONEY_QUANTIZER = Decimal("0.01")
RATE_QUANTIZER = Decimal("0.0001")


class BillingService:
    def __init__(self, repository: BillingRepository) -> None:
        self.repository = repository

    def get_my_client_incident_billing(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def get_my_provider_incident_billing(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def get_platform_incident_billing(self, incident_id: str) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        billing = self._get_or_create_billing_snapshot(incident_id)
        return self._build_billing_response(billing)

    def upsert_provider_incident_estimate(
        self,
        current_user: User,
        incident_id: str,
        payload: ProviderEstimateIncidentPricingRequest,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if incident.status == INCIDENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled incidents cannot be estimated.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)

            estimated_min, estimated_max = self._resolve_estimate_range(
                provider=provider,
                incident=incident,
                explicit_min=payload.estimated_price_min,
                explicit_max=payload.estimated_price_max,
            )

            incident.estimated_price_min = estimated_min
            incident.estimated_price_max = estimated_max

            billing.client_user_id = incident.client_user_id
            billing.provider_id = incident.provider_id
            billing.estimated_price_min = estimated_min
            billing.estimated_price_max = estimated_max
            billing.pricing_note = self._normalize_optional_text(payload.note)

            if billing.payment_status in (PAYMENT_STATUS_PENDING_PRICING, PAYMENT_STATUS_CANCELLED):
                billing.payment_status = PAYMENT_STATUS_ESTIMATED
                billing.cancelled_at = None

            self.repository.save(incident)
            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after estimate update.")


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_BILLING_ESTIMATED,
        payload_json={
            "estimated_price_min": float(billing.estimated_price_min) if billing.estimated_price_min is not None else None,
            "estimated_price_max": float(billing.estimated_price_max) if billing.estimated_price_max is not None else None,
            "payment_status": billing.payment_status,
        },
    )

        return self._build_billing_response(billing)

    def finalize_provider_incident_pricing(
        self,
        current_user: User,
        incident_id: str,
        payload: ProviderFinalizeIncidentPricingRequest,
    ) -> IncidentBillingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        if payload.mark_as_paid and payload.payment_method is None:
            raise ConflictException("payment_method is required when mark_as_paid=true.")

        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if incident.status == INCIDENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled incidents cannot be finalized economically.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("This incident billing is cancelled and cannot be finalized.")

            final_price = self._to_money_decimal(payload.final_price_amount)
            commission_rate = self._to_rate_decimal(DEFAULT_PLATFORM_COMMISSION_RATE)
            commission_amount = (final_price * commission_rate).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)
            provider_gross = final_price
            provider_net = (provider_gross - commission_amount).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

            billing.client_user_id = incident.client_user_id
            billing.provider_id = incident.provider_id
            billing.currency_code = DEFAULT_CURRENCY_CODE

            if incident.estimated_price_min is not None:
                billing.estimated_price_min = incident.estimated_price_min
            if incident.estimated_price_max is not None:
                billing.estimated_price_max = incident.estimated_price_max

            billing.final_price_amount = final_price
            billing.platform_commission_rate = commission_rate
            billing.platform_commission_amount = commission_amount
            billing.provider_gross_amount = provider_gross
            billing.provider_net_amount = provider_net
            billing.client_plan_subscription_id = None
            billing.plan_coverage_id = None
            billing.coverage_applied_amount = None
            billing.client_payable_amount = None
            billing.payment_method = payload.payment_method
            billing.payment_reference = self._normalize_optional_text(payload.payment_reference)
            billing.pricing_note = self._normalize_optional_text(payload.note)
            billing.pricing_finalized_at = datetime.now(timezone.utc)
            billing.cancelled_at = None

            if payload.mark_as_paid:
                billing.payment_status = PAYMENT_STATUS_PAID
                billing.payment_completed_at = datetime.now(timezone.utc)
            else:
                billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT
                billing.payment_completed_at = None

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after pricing finalization.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_BILLING_FINALIZED,
        payload_json={
            "final_price_amount": float(billing.final_price_amount) if billing.final_price_amount is not None else None,
            "platform_commission_amount": float(billing.platform_commission_amount) if billing.platform_commission_amount is not None else None,
            "provider_net_amount": float(billing.provider_net_amount) if billing.provider_net_amount is not None else None,
            "payment_status": billing.payment_status,
        },
    )

        return self._build_billing_response(billing)

    def create_client_checkout_preview(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientCheckoutPreviewRequest,
    ) -> BillingCheckoutPreviewResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not have billing information yet.")

            payable_amount = billing.client_payable_amount or billing.final_price_amount
            if payable_amount is None:
                raise ConflictException("Final pricing has not been defined yet.")

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot create a checkout preview.")

            if billing.payment_status == PAYMENT_STATUS_PAID:
                raise ConflictException("This incident is already paid.")

            checkout_reference = f"CHK-{uuid4().hex[:12].upper()}"
            checkout_payload_json = {
                "checkout_reference": checkout_reference,
                "incident_id": incident_id,
                "client_user_id": str(current_user.id),
                "provider_id": str(billing.provider_id) if billing.provider_id is not None else None,
                "amount": float(payable_amount),
                "currency_code": billing.currency_code,
                "payment_method": payload.payment_method,
                "payment_provider_name": payload.payment_provider_name,
                "return_url": self._normalize_optional_text(payload.return_url),
                "status": "PREVIEW_CREATED",
            }

            billing.payment_method = payload.payment_method
            billing.payment_provider_name = payload.payment_provider_name
            billing.checkout_reference = checkout_reference
            billing.checkout_payload_json = checkout_payload_json

            if billing.payment_status == PAYMENT_STATUS_ESTIMATED:
                billing.payment_status = PAYMENT_STATUS_PENDING_PAYMENT

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after checkout preview.")

        payable_amount = billing.client_payable_amount or billing.final_price_amount
        if payable_amount is None:
            raise NotFoundException("Incident billing not found after checkout preview.")

        return BillingCheckoutPreviewResponse(
            incident_id=incident_id,
            checkout_reference=billing.checkout_reference or "",
            payment_method=billing.payment_method or payload.payment_method,
            payment_provider_name=billing.payment_provider_name or (payload.payment_provider_name or "mock_checkout"),
            amount=float(payable_amount),
            currency_code=billing.currency_code,
            payment_status=billing.payment_status,
            checkout_payload_json=billing.checkout_payload_json,
        )

    def mark_client_incident_as_paid(
        self,
        current_user: User,
        incident_id: str,
        payload: ClientMarkIncidentPaidRequest,
    ) -> IncidentBillingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not have billing information yet.")

            if billing.final_price_amount is None:
                raise ConflictException("Final pricing has not been defined yet.")

            if billing.payment_status == PAYMENT_STATUS_CANCELLED:
                raise ConflictException("Cancelled billings cannot be paid.")

            billing.payment_status = PAYMENT_STATUS_PAID
            billing.payment_method = payload.payment_method
            billing.payment_provider_name = payload.payment_provider_name
            billing.payment_reference = self._normalize_optional_text(payload.payment_reference)
            billing.payment_completed_at = datetime.now(timezone.utc)

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        billing = self.repository.get_billing_by_incident_id(incident_id)
        if billing is None:
            raise NotFoundException("Incident billing not found after payment update.")

        return self._build_billing_response(billing)

    def cancel_billing_due_to_incident_cancellation(self, incident_id: str) -> None:
        try:
            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                return

            if billing.payment_status == PAYMENT_STATUS_PAID:
                return

            billing.payment_status = PAYMENT_STATUS_CANCELLED
            billing.cancelled_at = datetime.now(timezone.utc)

            self.repository.save(billing)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

    def _get_or_create_billing_snapshot(self, incident_id: str) -> IncidentBilling:
        try:
            incident = self.repository.get_incident_by_id_for_update(incident_id)
            if incident is None:
                raise NotFoundException("Incident not found.")

            billing = self.repository.get_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                billing = self._create_empty_billing_for_incident(incident)
                self.repository.save(billing)
                self.repository.commit()
                self.repository.refresh(billing)
                return billing

            self._sync_snapshot_fields_from_incident(billing, incident)
            self.repository.save(billing)
            self.repository.commit()
            self.repository.refresh(billing)
            return billing
        except Exception:
            self.repository.rollback()
            raise

    def _create_empty_billing_for_incident(self, incident) -> IncidentBilling:
        billing = IncidentBilling(
            incident_id=incident.id,
            client_user_id=incident.client_user_id,
            provider_id=incident.provider_id,
            currency_code=DEFAULT_CURRENCY_CODE,
            estimated_price_min=incident.estimated_price_min,
            estimated_price_max=incident.estimated_price_max,
            final_price_amount=None,
            platform_commission_rate=self._to_rate_decimal(DEFAULT_PLATFORM_COMMISSION_RATE),
            platform_commission_amount=None,
            provider_gross_amount=None,
            provider_net_amount=None,
            payment_status=PAYMENT_STATUS_ESTIMATED if (
                incident.estimated_price_min is not None or incident.estimated_price_max is not None
            ) else PAYMENT_STATUS_PENDING_PRICING,
            payment_method=None,
            payment_provider_name=None,
            payment_reference=None,
            checkout_reference=None,
            checkout_payload_json=None,
            pricing_note=None,
            pricing_finalized_at=None,
            payment_completed_at=None,
            cancelled_at=None,
        )
        return billing

    def _sync_snapshot_fields_from_incident(self, billing: IncidentBilling, incident) -> None:
        billing.client_user_id = incident.client_user_id
        billing.provider_id = incident.provider_id
        if billing.final_price_amount is None:
            billing.estimated_price_min = incident.estimated_price_min
            billing.estimated_price_max = incident.estimated_price_max

        if incident.status == INCIDENT_STATUS_CANCELLED and billing.payment_status != PAYMENT_STATUS_PAID:
            billing.payment_status = PAYMENT_STATUS_CANCELLED
            if billing.cancelled_at is None:
                billing.cancelled_at = datetime.now(timezone.utc)

    def _resolve_estimate_range(
        self,
        *,
        provider,
        incident,
        explicit_min: float | None,
        explicit_max: float | None,
    ) -> tuple[Decimal | None, Decimal | None]:
        if explicit_min is not None or explicit_max is not None:
            normalized_min = self._to_money_decimal(explicit_min) if explicit_min is not None else None
            normalized_max = self._to_money_decimal(explicit_max) if explicit_max is not None else None
            return self._normalize_estimate_range(normalized_min, normalized_max)

        used_category = (
            incident.suggested_category.strip().upper()
            if incident.suggested_category
            else incident.reported_category.strip().upper()
        )

        candidate_services = []
        for provider_service in provider.provider_services:
            if not provider_service.is_active:
                continue
            if not provider_service.is_mobile_service_enabled:
                continue
            if not provider_service.is_emergency_service_enabled:
                continue
            catalog_item = provider_service.service_catalog_item
            if catalog_item is None or not catalog_item.is_active:
                continue

            if used_category in ("OTHER", "UNCERTAIN") or catalog_item.category == used_category:
                candidate_services.append(provider_service)

        derived_min_values: list[Decimal] = []
        derived_max_values: list[Decimal] = []

        for item in candidate_services:
            if item.price_estimate_min is not None:
                derived_min_values.append(self._to_money_decimal(item.price_estimate_min))
            if item.price_estimate_max is not None:
                derived_max_values.append(self._to_money_decimal(item.price_estimate_max))

        if not derived_min_values and not derived_max_values:
            raise ConflictException(
                "No estimate values were provided and no provider service estimates could be derived."
            )

        derived_min = min(derived_min_values) if derived_min_values else None
        derived_max = max(derived_max_values) if derived_max_values else None

        return self._normalize_estimate_range(derived_min, derived_max)

    def _normalize_estimate_range(
        self,
        estimated_min: Decimal | None,
        estimated_max: Decimal | None,
    ) -> tuple[Decimal, Decimal]:
        if estimated_min is None and estimated_max is None:
            raise ConflictException("At least one estimate value is required.")

        if estimated_min is None and estimated_max is not None:
            estimated_min = estimated_max

        if estimated_max is None and estimated_min is not None:
            estimated_max = estimated_min

        if estimated_min is None or estimated_max is None:
            raise ConflictException("Invalid estimate range.")

        if estimated_min > estimated_max:
            raise ConflictException("estimated_price_min cannot be greater than estimated_price_max.")

        return estimated_min, estimated_max

    def _build_billing_response(self, billing: IncidentBilling) -> IncidentBillingResponse:
        client_payload = None
        if billing.client_user is not None:
            client = billing.client_user
            client_payload = BillingUserSummaryResponse(
                id=str(client.id),
                email=client.email,
                first_name=client.first_name,
                last_name=client.last_name,
                full_name=client.full_name,
                phone_number=client.phone_number,
            )

        provider_payload = None
        if billing.provider is not None:
            provider = billing.provider
            owner_payload = None
            if provider.owner_user is not None:
                owner = provider.owner_user
                owner_payload = BillingUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = BillingProviderSummaryResponse(
                id=str(provider.id),
                provider_type=provider.provider_type,
                business_name=provider.business_name,
                owner_user=owner_payload,
            )

        return IncidentBillingResponse(
            id=str(billing.id),
            incident_id=str(billing.incident_id),
            client_user_id=str(billing.client_user_id) if billing.client_user_id is not None else None,
            provider_id=str(billing.provider_id) if billing.provider_id is not None else None,
            client_plan_subscription_id=(
                str(billing.client_plan_subscription_id)
                if billing.client_plan_subscription_id is not None
                else None
            ),
            plan_coverage_id=(
                str(billing.plan_coverage_id)
                if billing.plan_coverage_id is not None
                else None
            ),
            currency_code=billing.currency_code,
            estimated_price_min=float(billing.estimated_price_min) if billing.estimated_price_min is not None else None,
            estimated_price_max=float(billing.estimated_price_max) if billing.estimated_price_max is not None else None,
            final_price_amount=float(billing.final_price_amount) if billing.final_price_amount is not None else None,
            platform_commission_rate=float(billing.platform_commission_rate),
            platform_commission_amount=(
                float(billing.platform_commission_amount)
                if billing.platform_commission_amount is not None
                else None
            ),
            provider_gross_amount=(
                float(billing.provider_gross_amount) if billing.provider_gross_amount is not None else None
            ),
            provider_net_amount=(
                float(billing.provider_net_amount) if billing.provider_net_amount is not None else None
            ),
            coverage_applied_amount=(
                float(billing.coverage_applied_amount)
                if billing.coverage_applied_amount is not None
                else None
            ),
            client_payable_amount=(
                float(billing.client_payable_amount)
                if billing.client_payable_amount is not None
                else None
            ),
            payment_status=billing.payment_status,
            payment_method=billing.payment_method,
            payment_provider_name=billing.payment_provider_name,
            payment_reference=billing.payment_reference,
            checkout_reference=billing.checkout_reference,
            checkout_payload_json=billing.checkout_payload_json,
            pricing_note=billing.pricing_note,
            pricing_finalized_at=billing.pricing_finalized_at,
            payment_completed_at=billing.payment_completed_at,
            cancelled_at=billing.cancelled_at,
            created_at=billing.created_at,
            updated_at=billing.updated_at,
            provider=provider_payload,
            client_user=client_payload,
        )

    def _to_money_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _to_rate_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(RATE_QUANTIZER, rounding=ROUND_HALF_UP)

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type="INCIDENT_BILLING",
                entity_id=incident_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return
```

### `app/services/catalog/__init__.py`

- Ruta relativa: `app/services/catalog/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/catalog/models.py`

- Ruta relativa: `app/services/catalog/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ServiceCatalogItem(Base):
    __tablename__ = "service_catalog_items"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    code: Mapped[str] = mapped_column(String(80), nullable=False, unique=True, index=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    supports_mobile_service: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    supports_emergency_service: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    provider_services: Mapped[list["ProviderService"]] = relationship(
        back_populates="service_catalog_item",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class ProviderService(Base):
    __tablename__ = "provider_services"
    __table_args__ = (
        UniqueConstraint(
            "provider_id",
            "service_catalog_item_id",
            name="uq_provider_services_provider_catalog_item",
        ),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    service_catalog_item_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    custom_title: Mapped[str | None] = mapped_column(String(150), nullable=True)
    custom_description: Mapped[str | None] = mapped_column(Text, nullable=True)

    price_estimate_min: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    price_estimate_max: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    is_mobile_service_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_emergency_service_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    provider = relationship("Provider", back_populates="provider_services", lazy="selectin")
    service_catalog_item: Mapped[ServiceCatalogItem] = relationship(
        back_populates="provider_services",
        lazy="selectin",
    )

    @property
    def effective_title(self) -> str:
        if self.custom_title and self.custom_title.strip():
            return self.custom_title.strip()
        return self.service_catalog_item.title

    @property
    def effective_description(self) -> str | None:
        if self.custom_description and self.custom_description.strip():
            return self.custom_description.strip()
        return self.service_catalog_item.description
```

### `app/services/catalog/repository.py`

- Ruta relativa: `app/services/catalog/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.catalog.models import ProviderService, ServiceCatalogItem
from app.services.providers.models import Provider


class CatalogRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_service_catalog_item(self, item: ServiceCatalogItem) -> ServiceCatalogItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def save_service_catalog_item(self, item: ServiceCatalogItem) -> ServiceCatalogItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = select(ServiceCatalogItem).where(
            ServiceCatalogItem.id == service_catalog_item_id
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_service_catalog_item_by_code(self, code: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = select(ServiceCatalogItem).where(
            ServiceCatalogItem.code == code
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_service_catalog_items(
        self,
        include_inactive: bool = False,
    ) -> list[ServiceCatalogItem]:
        query = select(ServiceCatalogItem)

        if not include_inactive:
            query = query.where(ServiceCatalogItem.is_active.is_(True))

        query = query.order_by(ServiceCatalogItem.sort_order.asc(), ServiceCatalogItem.title.asc())
        return list(self.db.execute(query).scalars().all())

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.id == provider_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_provider_service(self, provider_service: ProviderService) -> ProviderService:
        self.db.add(provider_service)
        self.db.commit()
        self.db.refresh(provider_service)
        return provider_service

    def save_provider_service(self, provider_service: ProviderService) -> ProviderService:
        self.db.add(provider_service)
        self.db.commit()
        self.db.refresh(provider_service)
        return provider_service

    def get_provider_service_by_id(self, provider_service_id: str) -> ProviderService | None:
        query: Select[tuple[ProviderService]] = select(ProviderService).where(
            ProviderService.id == provider_service_id
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_service_by_provider_and_catalog_item(
        self,
        provider_id: str,
        service_catalog_item_id: str,
    ) -> ProviderService | None:
        query: Select[tuple[ProviderService]] = select(ProviderService).where(
            ProviderService.provider_id == provider_id,
            ProviderService.service_catalog_item_id == service_catalog_item_id,
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_services_by_provider_id(
        self,
        provider_id: str,
        include_inactive: bool = True,
    ) -> list[ProviderService]:
        query = (
            select(ProviderService)
            .where(ProviderService.provider_id == provider_id)
            .order_by(ProviderService.created_at.asc())
        )

        if not include_inactive:
            query = query.where(ProviderService.is_active.is_(True))

        return list(self.db.execute(query).scalars().all())
```

### `app/services/catalog/router.py`

- Ruta relativa: `app/services/catalog/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.catalog.repository import CatalogRepository
from app.services.catalog.schemas import (
    CreateServiceCatalogItemRequest,
    UpdateProviderServiceRequest,
    UpdateServiceCatalogItemRequest,
    UpsertProviderServiceRequest,
)
from app.services.catalog.service import CatalogService

router = APIRouter(prefix="/catalog", tags=["Catalog"])


@router.post("/services")
def create_service_catalog_item(
    payload: CreateServiceCatalogItemRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.create_service_catalog_item(payload)

    return success_response(
        message="Catalog service created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/services")
def list_service_catalog_items(
    include_inactive: bool = Query(default=False),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_service_catalog_items(include_inactive=include_inactive)

    return success_response(
        message="Catalog services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
            "include_inactive": include_inactive,
        },
    )


@router.get("/services/{service_catalog_item_id}")
def get_service_catalog_item_by_id(
    service_catalog_item_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.get_service_catalog_item_by_id(service_catalog_item_id)

    return success_response(
        message="Catalog service loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/services/{service_catalog_item_id}")
def update_service_catalog_item(
    service_catalog_item_id: str,
    payload: UpdateServiceCatalogItemRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.update_service_catalog_item(service_catalog_item_id, payload)

    return success_response(
        message="Catalog service updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/providers/{provider_id}/services")
def list_provider_services_for_platform(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_provider_services_for_platform(provider_id)

    return success_response(
        message="Provider services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/me/services/catalog")
def list_my_catalog_with_configuration(
    include_inactive_catalog: bool = Query(default=False),
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_my_catalog_with_configuration(
        current_user=current_user,
        include_inactive_catalog=include_inactive_catalog,
    )

    return success_response(
        message="Provider catalog with configuration loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
            "include_inactive_catalog": include_inactive_catalog,
        },
    )


@router.get("/me/services")
def list_my_provider_services(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.list_my_provider_services(current_user)

    return success_response(
        message="Configured provider services loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/me/services")
def upsert_my_provider_service(
    payload: UpsertProviderServiceRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.upsert_my_provider_service(current_user, payload)

    return success_response(
        message="Provider service configured successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/services/{provider_service_id}")
def update_my_provider_service(
    provider_service_id: str,
    payload: UpdateProviderServiceRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = CatalogService(CatalogRepository(db))
    result = service.update_my_provider_service(
        current_user=current_user,
        provider_service_id=provider_service_id,
        payload=payload,
    )

    return success_response(
        message="Provider service updated successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/catalog/schemas.py`

- Ruta relativa: `app/services/catalog/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator


class ServiceCatalogItemResponse(BaseModel):
    id: str
    code: str
    category: str
    title: str
    description: str | None = None
    supports_mobile_service: bool
    supports_emergency_service: bool
    is_active: bool
    sort_order: int
    created_at: datetime
    updated_at: datetime


class CreateServiceCatalogItemRequest(BaseModel):
    code: str = Field(min_length=2, max_length=80)
    category: str = Field(min_length=2, max_length=50)
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    supports_mobile_service: bool = True
    supports_emergency_service: bool = True
    is_active: bool = True
    sort_order: int = Field(default=0, ge=0, le=1000)

    @field_validator("code")
    @classmethod
    def normalize_code(cls, value: str) -> str:
        return value.strip().upper().replace(" ", "_")

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str) -> str:
        return value.strip().upper()


class UpdateServiceCatalogItemRequest(BaseModel):
    category: str | None = Field(default=None, min_length=2, max_length=50)
    title: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = None
    supports_mobile_service: bool | None = None
    supports_emergency_service: bool | None = None
    is_active: bool | None = None
    sort_order: int | None = Field(default=None, ge=0, le=1000)

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return value.strip().upper()


class ProviderServiceResponse(BaseModel):
    id: str
    provider_id: str
    service_catalog_item_id: str
    service_code: str
    service_category: str
    catalog_title: str
    catalog_description: str | None = None
    custom_title: str | None = None
    custom_description: str | None = None
    effective_title: str
    effective_description: str | None = None
    price_estimate_min: float | None = None
    price_estimate_max: float | None = None
    estimated_duration_minutes: int | None = None
    supports_mobile_service: bool
    supports_emergency_service: bool
    is_mobile_service_enabled: bool
    is_emergency_service_enabled: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime


class ProviderCatalogAvailabilityResponse(BaseModel):
    catalog_item: ServiceCatalogItemResponse
    provider_service: ProviderServiceResponse | None = None
    is_configured: bool


class UpsertProviderServiceRequest(BaseModel):
    service_catalog_item_id: str
    custom_title: str | None = Field(default=None, max_length=150)
    custom_description: str | None = None
    price_estimate_min: float | None = Field(default=None, ge=0)
    price_estimate_max: float | None = Field(default=None, ge=0)
    estimated_duration_minutes: int | None = Field(default=None, ge=1, le=1440)
    is_mobile_service_enabled: bool = True
    is_emergency_service_enabled: bool = True
    is_active: bool = True

    @model_validator(mode="after")
    def validate_price_range(self):
        if (
            self.price_estimate_min is not None
            and self.price_estimate_max is not None
            and self.price_estimate_max < self.price_estimate_min
        ):
            raise ValueError("price_estimate_max cannot be lower than price_estimate_min.")
        return self


class UpdateProviderServiceRequest(BaseModel):
    custom_title: str | None = Field(default=None, max_length=150)
    custom_description: str | None = None
    price_estimate_min: float | None = Field(default=None, ge=0)
    price_estimate_max: float | None = Field(default=None, ge=0)
    estimated_duration_minutes: int | None = Field(default=None, ge=1, le=1440)
    is_mobile_service_enabled: bool | None = None
    is_emergency_service_enabled: bool | None = None
    is_active: bool | None = None

    @model_validator(mode="after")
    def validate_price_range(self):
        if (
            self.price_estimate_min is not None
            and self.price_estimate_max is not None
            and self.price_estimate_max < self.price_estimate_min
        ):
            raise ValueError("price_estimate_max cannot be lower than price_estimate_min.")
        return self
```

### `app/services/catalog/service.py`

- Ruta relativa: `app/services/catalog/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.catalog.models import ProviderService, ServiceCatalogItem
from app.services.catalog.repository import CatalogRepository
from app.services.catalog.schemas import (
    CreateServiceCatalogItemRequest,
    ProviderCatalogAvailabilityResponse,
    ProviderServiceResponse,
    ServiceCatalogItemResponse,
    UpdateProviderServiceRequest,
    UpdateServiceCatalogItemRequest,
    UpsertProviderServiceRequest,
)


class CatalogService:
    def __init__(self, repository: CatalogRepository) -> None:
        self.repository = repository

    def create_service_catalog_item(
        self,
        payload: CreateServiceCatalogItemRequest,
    ) -> ServiceCatalogItemResponse:
        existing_item = self.repository.get_service_catalog_item_by_code(payload.code)
        if existing_item is not None:
            raise ConflictException("A catalog service with this code already exists.")

        item = ServiceCatalogItem(
            code=payload.code,
            category=payload.category,
            title=payload.title.strip(),
            description=payload.description.strip() if payload.description else None,
            supports_mobile_service=payload.supports_mobile_service,
            supports_emergency_service=payload.supports_emergency_service,
            is_active=payload.is_active,
            sort_order=payload.sort_order,
        )

        created_item = self.repository.create_service_catalog_item(item)
        return self._build_service_catalog_item_response(created_item)

    def list_service_catalog_items(self, include_inactive: bool = False) -> list[ServiceCatalogItemResponse]:
        items = self.repository.list_service_catalog_items(include_inactive=include_inactive)
        return [self._build_service_catalog_item_response(item) for item in items]

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItemResponse:
        item = self.repository.get_service_catalog_item_by_id(service_catalog_item_id)
        if item is None:
            raise NotFoundException("Catalog service not found.")

        return self._build_service_catalog_item_response(item)

    def update_service_catalog_item(
        self,
        service_catalog_item_id: str,
        payload: UpdateServiceCatalogItemRequest,
    ) -> ServiceCatalogItemResponse:
        item = self.repository.get_service_catalog_item_by_id(service_catalog_item_id)
        if item is None:
            raise NotFoundException("Catalog service not found.")

        if "category" in payload.model_fields_set:
            item.category = payload.category if payload.category is not None else item.category

        if "title" in payload.model_fields_set and payload.title is not None:
            item.title = payload.title.strip()

        if "description" in payload.model_fields_set:
            item.description = self._normalize_nullable_text(payload.description)

        if "supports_mobile_service" in payload.model_fields_set:
            item.supports_mobile_service = bool(payload.supports_mobile_service)

        if "supports_emergency_service" in payload.model_fields_set:
            item.supports_emergency_service = bool(payload.supports_emergency_service)

        if "is_active" in payload.model_fields_set:
            item.is_active = bool(payload.is_active)

        if "sort_order" in payload.model_fields_set and payload.sort_order is not None:
            item.sort_order = payload.sort_order

        updated_item = self.repository.save_service_catalog_item(item)
        return self._build_service_catalog_item_response(updated_item)

    def list_provider_services_for_platform(self, provider_id: str) -> list[ProviderServiceResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=provider_id,
            include_inactive=True,
        )
        return [self._build_provider_service_response(item) for item in provider_services]

    def list_my_catalog_with_configuration(
        self,
        current_user: User,
        include_inactive_catalog: bool = False,
    ) -> list[ProviderCatalogAvailabilityResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        catalog_items = self.repository.list_service_catalog_items(
            include_inactive=include_inactive_catalog,
        )
        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=str(provider.id),
            include_inactive=True,
        )
        provider_services_by_catalog_item_id = {
            str(item.service_catalog_item_id): item for item in provider_services
        }

        results: list[ProviderCatalogAvailabilityResponse] = []
        for catalog_item in catalog_items:
            provider_service = provider_services_by_catalog_item_id.get(str(catalog_item.id))
            results.append(
                ProviderCatalogAvailabilityResponse(
                    catalog_item=self._build_service_catalog_item_response(catalog_item),
                    provider_service=(
                        self._build_provider_service_response(provider_service)
                        if provider_service is not None
                        else None
                    ),
                    is_configured=provider_service is not None,
                )
            )

        return results

    def list_my_provider_services(self, current_user: User) -> list[ProviderServiceResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        provider_services = self.repository.list_provider_services_by_provider_id(
            provider_id=str(provider.id),
            include_inactive=True,
        )
        return [self._build_provider_service_response(item) for item in provider_services]

    def upsert_my_provider_service(
        self,
        current_user: User,
        payload: UpsertProviderServiceRequest,
    ) -> ProviderServiceResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        catalog_item = self.repository.get_service_catalog_item_by_id(payload.service_catalog_item_id)
        if catalog_item is None:
            raise NotFoundException("Catalog service not found.")

        if not catalog_item.is_active and payload.is_active:
            raise ConflictException("Inactive catalog services cannot be enabled for providers.")

        self._validate_service_capabilities(
            catalog_item=catalog_item,
            is_mobile_service_enabled=payload.is_mobile_service_enabled,
            is_emergency_service_enabled=payload.is_emergency_service_enabled,
        )

        existing_provider_service = self.repository.get_provider_service_by_provider_and_catalog_item(
            provider_id=str(provider.id),
            service_catalog_item_id=payload.service_catalog_item_id,
        )

        if existing_provider_service is not None:
            existing_provider_service.custom_title = self._normalize_nullable_text(payload.custom_title)
            existing_provider_service.custom_description = self._normalize_nullable_text(
                payload.custom_description
            )
            existing_provider_service.price_estimate_min = payload.price_estimate_min
            existing_provider_service.price_estimate_max = payload.price_estimate_max
            existing_provider_service.estimated_duration_minutes = payload.estimated_duration_minutes
            existing_provider_service.is_mobile_service_enabled = payload.is_mobile_service_enabled
            existing_provider_service.is_emergency_service_enabled = payload.is_emergency_service_enabled
            existing_provider_service.is_active = payload.is_active

            updated_provider_service = self.repository.save_provider_service(existing_provider_service)
            return self._build_provider_service_response(updated_provider_service)

        provider_service = ProviderService(
            provider_id=provider.id,
            service_catalog_item_id=catalog_item.id,
            custom_title=self._normalize_nullable_text(payload.custom_title),
            custom_description=self._normalize_nullable_text(payload.custom_description),
            price_estimate_min=payload.price_estimate_min,
            price_estimate_max=payload.price_estimate_max,
            estimated_duration_minutes=payload.estimated_duration_minutes,
            is_mobile_service_enabled=payload.is_mobile_service_enabled,
            is_emergency_service_enabled=payload.is_emergency_service_enabled,
            is_active=payload.is_active,
        )

        created_provider_service = self.repository.create_provider_service(provider_service)
        return self._build_provider_service_response(created_provider_service)

    def update_my_provider_service(
        self,
        current_user: User,
        provider_service_id: str,
        payload: UpdateProviderServiceRequest,
    ) -> ProviderServiceResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        provider_service = self.repository.get_provider_service_by_id(provider_service_id)
        if provider_service is None:
            raise NotFoundException("Provider service configuration not found.")

        if str(provider_service.provider_id) != str(provider.id):
            raise ForbiddenException("This provider service configuration does not belong to your provider.")

        catalog_item = provider_service.service_catalog_item

        next_mobile_value = (
            payload.is_mobile_service_enabled
            if payload.is_mobile_service_enabled is not None
            else provider_service.is_mobile_service_enabled
        )
        next_emergency_value = (
            payload.is_emergency_service_enabled
            if payload.is_emergency_service_enabled is not None
            else provider_service.is_emergency_service_enabled
        )

        self._validate_service_capabilities(
            catalog_item=catalog_item,
            is_mobile_service_enabled=next_mobile_value,
            is_emergency_service_enabled=next_emergency_value,
        )

        if payload.is_active is not None and payload.is_active and not catalog_item.is_active:
            raise ConflictException("Inactive catalog services cannot be enabled for providers.")

        if "custom_title" in payload.model_fields_set:
            provider_service.custom_title = self._normalize_nullable_text(payload.custom_title)

        if "custom_description" in payload.model_fields_set:
            provider_service.custom_description = self._normalize_nullable_text(payload.custom_description)

        if "price_estimate_min" in payload.model_fields_set:
            provider_service.price_estimate_min = payload.price_estimate_min

        if "price_estimate_max" in payload.model_fields_set:
            provider_service.price_estimate_max = payload.price_estimate_max

        if "estimated_duration_minutes" in payload.model_fields_set:
            provider_service.estimated_duration_minutes = payload.estimated_duration_minutes

        if "is_mobile_service_enabled" in payload.model_fields_set:
            provider_service.is_mobile_service_enabled = bool(payload.is_mobile_service_enabled)

        if "is_emergency_service_enabled" in payload.model_fields_set:
            provider_service.is_emergency_service_enabled = bool(payload.is_emergency_service_enabled)

        if "is_active" in payload.model_fields_set:
            provider_service.is_active = bool(payload.is_active)

        if (
            provider_service.price_estimate_min is not None
            and provider_service.price_estimate_max is not None
            and provider_service.price_estimate_max < provider_service.price_estimate_min
        ):
            raise ConflictException(
                "price_estimate_max cannot be lower than price_estimate_min."
            )

        updated_provider_service = self.repository.save_provider_service(provider_service)
        return self._build_provider_service_response(updated_provider_service)

    def _validate_service_capabilities(
        self,
        catalog_item: ServiceCatalogItem,
        is_mobile_service_enabled: bool,
        is_emergency_service_enabled: bool,
    ) -> None:
        if is_mobile_service_enabled and not catalog_item.supports_mobile_service:
            raise ConflictException(
                "This catalog service does not allow mobile service activation."
            )

        if is_emergency_service_enabled and not catalog_item.supports_emergency_service:
            raise ConflictException(
                "This catalog service does not allow emergency service activation."
            )

    def _build_service_catalog_item_response(
        self,
        item: ServiceCatalogItem,
    ) -> ServiceCatalogItemResponse:
        return ServiceCatalogItemResponse(
            id=str(item.id),
            code=item.code,
            category=item.category,
            title=item.title,
            description=item.description,
            supports_mobile_service=item.supports_mobile_service,
            supports_emergency_service=item.supports_emergency_service,
            is_active=item.is_active,
            sort_order=item.sort_order,
            created_at=item.created_at,
            updated_at=item.updated_at,
        )

    def _build_provider_service_response(
        self,
        provider_service: ProviderService,
    ) -> ProviderServiceResponse:
        catalog_item = provider_service.service_catalog_item

        price_estimate_min = (
            float(provider_service.price_estimate_min)
            if provider_service.price_estimate_min is not None
            else None
        )
        price_estimate_max = (
            float(provider_service.price_estimate_max)
            if provider_service.price_estimate_max is not None
            else None
        )

        return ProviderServiceResponse(
            id=str(provider_service.id),
            provider_id=str(provider_service.provider_id),
            service_catalog_item_id=str(provider_service.service_catalog_item_id),
            service_code=catalog_item.code,
            service_category=catalog_item.category,
            catalog_title=catalog_item.title,
            catalog_description=catalog_item.description,
            custom_title=provider_service.custom_title,
            custom_description=provider_service.custom_description,
            effective_title=provider_service.effective_title,
            effective_description=provider_service.effective_description,
            price_estimate_min=price_estimate_min,
            price_estimate_max=price_estimate_max,
            estimated_duration_minutes=provider_service.estimated_duration_minutes,
            supports_mobile_service=catalog_item.supports_mobile_service,
            supports_emergency_service=catalog_item.supports_emergency_service,
            is_mobile_service_enabled=provider_service.is_mobile_service_enabled,
            is_emergency_service_enabled=provider_service.is_emergency_service_enabled,
            is_active=provider_service.is_active,
            created_at=provider_service.created_at,
            updated_at=provider_service.updated_at,
        )

    def _normalize_nullable_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None
```

### `app/services/evidences/__init__.py`

- Ruta relativa: `app/services/evidences/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/evidences/models.py`

- Ruta relativa: `app/services/evidences/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentEvidence(Base):
    __tablename__ = "incident_evidences"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    uploaded_by_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    evidence_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    original_filename: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stored_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_extension: Mapped[str | None] = mapped_column(String(20), nullable=True)
    mime_type: Mapped[str | None] = mapped_column(String(120), nullable=True)
    file_size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    text_content_snapshot: Mapped[str | None] = mapped_column(Text, nullable=True)

    storage_provider: Mapped[str] = mapped_column(String(30), nullable=False, default="local", index=True)
    storage_bucket: Mapped[str | None] = mapped_column(String(255), nullable=True)
    storage_object_key: Mapped[str | None] = mapped_column(Text, nullable=True)
    public_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    absolute_file_path: Mapped[str | None] = mapped_column(Text, nullable=True)

    audio_processing_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    audio_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    transcript_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript_language_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    transcript_confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    transcript_segments_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    audio_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    audio_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    image_processing_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    image_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    image_labels_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    image_detections_json: Mapped[list | None] = mapped_column(JSON, nullable=True)
    image_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    image_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    incident = relationship("Incident", lazy="selectin")
    uploaded_by_user = relationship("User", lazy="selectin")
```

### `app/services/evidences/repository.py`

- Ruta relativa: `app/services/evidences/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class EvidencesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_evidence(self, evidence: IncidentEvidence) -> IncidentEvidence:
        self.db.add(evidence)
        self.db.commit()
        self.db.refresh(evidence)
        return evidence

    def get_evidence_by_id(self, evidence_id: str) -> IncidentEvidence | None:
        query: Select[tuple[IncidentEvidence]] = select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_evidences_by_incident_id(self, incident_id: str) -> list[IncidentEvidence]:
        query: Select[tuple[IncidentEvidence]] = (
            select(IncidentEvidence)
            .where(IncidentEvidence.incident_id == incident_id)
            .order_by(IncidentEvidence.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())
```

### `app/services/evidences/router.py`

- Ruta relativa: `app/services/evidences/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session, get_storage_service
from app.core.security import require_roles
from app.integrations.storage.base import StorageService
from app.services.auth.models import User
from app.services.evidences.repository import EvidencesRepository
from app.services.evidences.schemas import CreateTextEvidenceRequest
from app.services.evidences.service import EvidencesService

router = APIRouter(prefix="/evidences", tags=["Evidences"])


@router.post("/client/incidents/{incident_id}/files")
async def upload_incident_file_evidence_as_client(
    incident_id: str,
    evidence_type: str = Form(...),
    description: str | None = Form(default=None),
    file: UploadFile = File(...),
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = await service.upload_incident_file_evidence_as_client(
        current_user=current_user,
        incident_id=incident_id,
        evidence_type=evidence_type,
        description=description,
        upload_file=file,
    )

    return success_response(
        message="Incident file evidence uploaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/text")
def create_incident_text_evidence_as_client(
    incident_id: str,
    payload: CreateTextEvidenceRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.create_incident_text_evidence_as_client(
        current_user=current_user,
        incident_id=incident_id,
        payload=payload,
    )

    return success_response(
        message="Incident text evidence created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/incidents/{incident_id}")
def list_client_incident_evidences(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_client_incident_evidences(current_user, incident_id)

    return success_response(
        message="Client incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/incidents/{incident_id}")
def list_provider_incident_evidences(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_provider_incident_evidences(current_user, incident_id)

    return success_response(
        message="Provider incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/platform/incidents/{incident_id}")
def list_platform_incident_evidences(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
) -> dict:
    service = EvidencesService(EvidencesRepository(db), storage_service)
    result = service.list_platform_incident_evidences(incident_id)

    return success_response(
        message="Platform incident evidences loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/{evidence_id}/download")
def download_evidence(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT, ROLE_PROVIDER_ADMIN, ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    storage_service: StorageService = Depends(get_storage_service),
):
    service = EvidencesService(EvidencesRepository(db), storage_service)

    user_role_codes = {role.code for role in current_user.roles}

    if ROLE_PLATFORM_ADMIN in user_role_codes:
        return service.download_evidence_as_platform(evidence_id)

    if ROLE_PROVIDER_ADMIN in user_role_codes:
        return service.download_evidence_as_provider(current_user, evidence_id)

    return service.download_evidence_as_client(current_user, evidence_id)
```

### `app/services/evidences/schemas.py`

- Ruta relativa: `app/services/evidences/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class EvidenceUploaderResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class IncidentEvidenceResponse(BaseModel):
    id: str
    incident_id: str
    uploaded_by_user_id: str | None = None
    evidence_type: str
    original_filename: str | None = None
    stored_filename: str
    file_extension: str | None = None
    mime_type: str | None = None
    file_size_bytes: int | None = None
    description: str | None = None
    text_content_snapshot: str | None = None

    storage_provider: str
    storage_bucket: str | None = None
    storage_object_key: str | None = None
    public_url: str | None = None
    download_url: str

    audio_processing_status: str
    audio_provider_name: str | None = None
    transcript_text: str | None = None
    transcript_language_code: str | None = None
    transcript_confidence: float | None = None
    transcript_segments_json: list[dict] | list | None = None
    audio_processed_at: datetime | None = None
    audio_error_message: str | None = None

    image_processing_status: str
    image_provider_name: str | None = None
    image_labels_json: list[str] | list | None = None
    image_detections_json: list[dict] | list | None = None
    image_summary: str | None = None
    image_processed_at: datetime | None = None
    image_error_message: str | None = None

    created_at: datetime
    updated_at: datetime
    uploaded_by_user: EvidenceUploaderResponse | None = None


class CreateTextEvidenceRequest(BaseModel):
    description: str | None = None
    text_content: str = Field(min_length=1)
    evidence_type: Literal["TEXT"] = "TEXT"
```

### `app/services/evidences/service.py`

- Ruta relativa: `app/services/evidences/service.py`
- Nombre de archivo: `service.py`

```python
from pathlib import Path

from fastapi import UploadFile
from fastapi.responses import FileResponse, RedirectResponse, Response

from app.common.constants import (
    EVIDENCE_TYPE_AUDIO,
    EVIDENCE_TYPE_IMAGE,
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_NOT_REQUESTED,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.core.config import settings
from app.integrations.factory import build_storage_service_by_name
from app.integrations.storage.base import StorageService
from app.services.auth.models import User
from app.services.evidences.models import IncidentEvidence
from app.services.evidences.repository import EvidencesRepository
from app.services.evidences.schemas import (
    CreateTextEvidenceRequest,
    EvidenceUploaderResponse,
    IncidentEvidenceResponse,
)
from app.services.jobs.dispatcher import PipelineDispatcher


class EvidencesService:
    def __init__(
        self,
        repository: EvidencesRepository,
        storage_service: StorageService,
    ) -> None:
        self.repository = repository
        self.storage_service = storage_service
        self.dispatcher = PipelineDispatcher(repository.db)

    async def upload_incident_file_evidence_as_client(
        self,
        current_user: User,
        incident_id: str,
        evidence_type: str,
        description: str | None,
        upload_file: UploadFile,
    ) -> IncidentEvidenceResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        return await self._create_file_evidence(
            incident_id=incident_id,
            uploaded_by_user=current_user,
            evidence_type=evidence_type,
            description=description,
            upload_file=upload_file,
        )

    def create_incident_text_evidence_as_client(
        self,
        current_user: User,
        incident_id: str,
        payload: CreateTextEvidenceRequest,
    ) -> IncidentEvidenceResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        storage_result = self.storage_service.save_text_content(
            incident_id=incident_id,
            text_content=payload.text_content,
        )

        file_extension = self._extract_file_extension(
            original_filename="text_evidence.txt",
            stored_filename=storage_result.stored_filename,
        )

        evidence = IncidentEvidence(
            incident_id=incident.id,
            uploaded_by_user_id=current_user.id,
            evidence_type=EVIDENCE_TYPE_TEXT,
            original_filename="text_evidence.txt",
            stored_filename=storage_result.stored_filename,
            file_extension=file_extension,
            mime_type=storage_result.mime_type,
            file_size_bytes=storage_result.file_size_bytes,
            description=payload.description.strip() if payload.description else None,
            text_content_snapshot=payload.text_content.strip(),
            storage_provider=storage_result.storage_provider,
            storage_bucket=storage_result.storage_bucket,
            storage_object_key=storage_result.storage_object_key,
            public_url=storage_result.public_url,
            absolute_file_path=storage_result.absolute_file_path,
            audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
            image_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        )

        created_evidence = self.repository.create_evidence(evidence)

        self.dispatcher.dispatch_for_new_evidence(
            evidence=created_evidence,
            requested_by_user_id=str(current_user.id),
        )

        return self._build_evidence_response(created_evidence)

    def list_client_incident_evidences(self, current_user: User, incident_id: str) -> list[IncidentEvidenceResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def list_provider_incident_evidences(self, current_user: User, incident_id: str) -> list[IncidentEvidenceResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def list_platform_incident_evidences(self, incident_id: str) -> list[IncidentEvidenceResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        evidences = self.repository.list_evidences_by_incident_id(incident_id)
        return [self._build_evidence_response(evidence) for evidence in evidences]

    def download_evidence_as_client(self, current_user: User, evidence_id: str) -> Response:
        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        incident = self.repository.get_incident_by_id(str(evidence.incident_id))
        if incident is None:
            raise NotFoundException("Incident not found for this evidence.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This evidence does not belong to the authenticated client.")

        return self._build_download_response(evidence)

    def download_evidence_as_provider(self, current_user: User, evidence_id: str) -> Response:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        incident = self.repository.get_incident_by_id(str(evidence.incident_id))
        if incident is None:
            raise NotFoundException("Incident not found for this evidence.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This evidence does not belong to your provider.")

        return self._build_download_response(evidence)

    def download_evidence_as_platform(self, evidence_id: str) -> Response:
        evidence = self.repository.get_evidence_by_id(evidence_id)
        if evidence is None:
            raise NotFoundException("Evidence not found.")

        return self._build_download_response(evidence)

    async def _create_file_evidence(
        self,
        incident_id: str,
        uploaded_by_user: User,
        evidence_type: str,
        description: str | None,
        upload_file: UploadFile,
    ) -> IncidentEvidenceResponse:
        normalized_type = evidence_type.strip().upper()

        if normalized_type not in (EVIDENCE_TYPE_IMAGE, EVIDENCE_TYPE_AUDIO):
            raise ConflictException("Only IMAGE or AUDIO file evidences are allowed in this endpoint.")

        storage_result = await self.storage_service.save_uploaded_file(
            incident_id=incident_id,
            upload_file=upload_file,
        )

        file_extension = self._extract_file_extension(
            original_filename=upload_file.filename,
            stored_filename=storage_result.stored_filename,
        )

        evidence = IncidentEvidence(
            incident_id=incident_id,
            uploaded_by_user_id=uploaded_by_user.id,
            evidence_type=normalized_type,
            original_filename=upload_file.filename,
            stored_filename=storage_result.stored_filename,
            file_extension=file_extension,
            mime_type=storage_result.mime_type,
            file_size_bytes=storage_result.file_size_bytes,
            description=description.strip() if description else None,
            text_content_snapshot=None,
            storage_provider=storage_result.storage_provider,
            storage_bucket=storage_result.storage_bucket,
            storage_object_key=storage_result.storage_object_key,
            public_url=storage_result.public_url,
            absolute_file_path=storage_result.absolute_file_path,
            audio_processing_status=(
                PROCESSING_STATUS_NOT_REQUESTED if normalized_type != EVIDENCE_TYPE_AUDIO else PROCESSING_STATUS_NOT_REQUESTED
            ),
            image_processing_status=(
                PROCESSING_STATUS_NOT_REQUESTED if normalized_type != EVIDENCE_TYPE_IMAGE else PROCESSING_STATUS_NOT_REQUESTED
            ),
        )

        created_evidence = self.repository.create_evidence(evidence)

        self.dispatcher.dispatch_for_new_evidence(
            evidence=created_evidence,
            requested_by_user_id=str(uploaded_by_user.id),
        )

        return self._build_evidence_response(created_evidence)

    def _build_download_response(self, evidence: IncidentEvidence) -> Response:
        storage_service = build_storage_service_by_name(evidence.storage_provider or "local")

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        if descriptor.kind == "signed_url":
            return RedirectResponse(
                url=descriptor.download_url,
                status_code=307,
            )

        return FileResponse(
            path=descriptor.absolute_file_path,
            media_type=descriptor.media_type or "application/octet-stream",
            filename=descriptor.filename,
        )

    def _build_evidence_response(self, evidence: IncidentEvidence) -> IncidentEvidenceResponse:
        uploaded_by_user_payload = None

        if evidence.uploaded_by_user is not None:
            uploaded_user = evidence.uploaded_by_user
            uploaded_by_user_payload = EvidenceUploaderResponse(
                id=str(uploaded_user.id),
                email=uploaded_user.email,
                first_name=uploaded_user.first_name,
                last_name=uploaded_user.last_name,
                full_name=uploaded_user.full_name,
            )

        return IncidentEvidenceResponse(
            id=str(evidence.id),
            incident_id=str(evidence.incident_id),
            uploaded_by_user_id=str(evidence.uploaded_by_user_id) if evidence.uploaded_by_user_id else None,
            evidence_type=evidence.evidence_type,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            file_extension=evidence.file_extension,
            mime_type=evidence.mime_type,
            file_size_bytes=evidence.file_size_bytes,
            description=evidence.description,
            text_content_snapshot=evidence.text_content_snapshot,
            storage_provider=evidence.storage_provider,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            download_url=f"{settings.api_v1_prefix}/evidences/{evidence.id}/download",
            audio_processing_status=evidence.audio_processing_status,
            audio_provider_name=evidence.audio_provider_name,
            transcript_text=evidence.transcript_text,
            transcript_language_code=evidence.transcript_language_code,
            transcript_confidence=evidence.transcript_confidence,
            transcript_segments_json=evidence.transcript_segments_json,
            audio_processed_at=evidence.audio_processed_at,
            audio_error_message=evidence.audio_error_message,
            image_processing_status=evidence.image_processing_status,
            image_provider_name=evidence.image_provider_name,
            image_labels_json=evidence.image_labels_json,
            image_detections_json=evidence.image_detections_json,
            image_summary=evidence.image_summary,
            image_processed_at=evidence.image_processed_at,
            image_error_message=evidence.image_error_message,
            created_at=evidence.created_at,
            updated_at=evidence.updated_at,
            uploaded_by_user=uploaded_by_user_payload,
        )

    def _extract_file_extension(
        self,
        original_filename: str | None,
        stored_filename: str,
    ) -> str | None:
        original_extension = Path(original_filename).suffix.lower() if original_filename else ""
        if original_extension:
            return original_extension

        stored_extension = Path(stored_filename).suffix.lower()
        return stored_extension or None
```

### `app/services/incidents/__init__.py`

- Ruta relativa: `app/services/incidents/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/incidents/models.py`

- Ruta relativa: `app/services/incidents/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    client_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    vehicle_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vehicles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    assigned_technician_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("technicians.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    priority: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    reported_category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    client_contact_phone_snapshot: Mapped[str | None] = mapped_column(String(30), nullable=True)

    incident_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    incident_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    address_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)

    estimated_price_min: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    estimated_price_max: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)

    ai_summary_status: Mapped[str] = mapped_column(String(30), nullable=False, default="NOT_REQUESTED", index=True)
    summary_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    structured_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    suggested_category: Mapped[str | None] = mapped_column(String(50), nullable=True)
    suggested_priority: Mapped[str | None] = mapped_column(String(30), nullable=True)
    requires_more_information: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    summary_processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    summary_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    dispatch_mode: Mapped[str | None] = mapped_column(String(30), nullable=True)

    responder_last_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    responder_last_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    responder_last_source_type: Mapped[str | None] = mapped_column(String(30), nullable=True)
    responder_last_recorded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    route_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    route_distance_meters: Mapped[float | None] = mapped_column(Float, nullable=True)
    route_duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    route_eta_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    route_polyline: Mapped[str | None] = mapped_column(Text, nullable=True)
    route_last_calculated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    route_error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    requested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    assigned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    en_route_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    arrived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    client_user = relationship("User", lazy="selectin")
    vehicle = relationship("Vehicle", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    assigned_technician = relationship(
        "Technician",
        lazy="selectin",
        foreign_keys="Incident.assigned_technician_id",
    )
```

### `app/services/incidents/repository.py`

- Ruta relativa: `app/services/incidents/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.incidents.models import Incident
from app.services.providers.models import Provider
from app.services.vehicles.models import Vehicle


class IncidentsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_vehicle_by_id(self, vehicle_id: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.id == vehicle_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_incident(self, incident: Incident) -> Incident:
        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)
        return incident

    def save_incident(self, incident: Incident) -> Incident:
        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)
        return incident

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_incidents_by_client_user_id(self, client_user_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.client_user_id == client_user_id)
            .order_by(Incident.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_incidents_by_provider_id(self, provider_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.provider_id == provider_id)
            .order_by(Incident.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_all_incidents(self, limit: int = 50, offset: int = 0) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .order_by(Incident.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())
```

### `app/services/incidents/router.py`

- Ruta relativa: `app/services/incidents/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.incidents.repository import IncidentsRepository
from app.services.incidents.schemas import CreateIncidentRequest, UpdateOwnPendingIncidentRequest
from app.services.incidents.service import IncidentsService

router = APIRouter(prefix="/incidents", tags=["Incidents"])


@router.post("")
def create_own_incident(
    payload: CreateIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.create_own_incident(current_user, payload)

    return success_response(
        message="Incident created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me")
def list_own_incidents(
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_own_incidents(current_user)

    return success_response(
        message="Own incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/me/{incident_id}")
def get_own_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_own_incident(current_user, incident_id)

    return success_response(
        message="Own incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/{incident_id}")
def update_own_pending_incident(
    incident_id: str,
    payload: UpdateOwnPendingIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.update_own_pending_incident(current_user, incident_id, payload)

    return success_response(
        message="Own incident updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/me/{incident_id}/cancel")
def cancel_own_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.cancel_own_incident(current_user, incident_id)

    return success_response(
        message="Own incident cancelled successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_all_incidents(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_all_incidents(limit=limit, offset=offset)

    return success_response(
        message="Incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{incident_id}")
def get_incident_by_id_for_platform(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_incident_by_id_for_platform(incident_id)

    return success_response(
        message="Incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/me")
def list_provider_incidents(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.list_provider_incidents(current_user)

    return success_response(
        message="Provider incidents loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/provider/me/{incident_id}")
def get_provider_incident(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = IncidentsService(IncidentsRepository(db))
    result = service.get_provider_incident(current_user, incident_id)

    return success_response(
        message="Provider incident loaded successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/incidents/schemas.py`

- Ruta relativa: `app/services/incidents/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class IncidentVehicleSummaryResponse(BaseModel):
    id: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    year: int | None = None
    color: str | None = None


class IncidentProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    contact_phone: str | None = None
    city: str | None = None
    is_available: bool
    average_rating: float


class IncidentTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class IncidentClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentResponse(BaseModel):
    id: str
    client_user_id: str
    vehicle_id: str
    provider_id: str | None = None
    assigned_technician_id: str | None = None
    dispatch_mode: str | None = None

    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    client_contact_phone_snapshot: str | None = None
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = None
    estimated_price_min: float | None = None
    estimated_price_max: float | None = None

    ai_summary_status: str
    summary_provider_name: str | None = None
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool
    summary_processed_at: datetime | None = None
    summary_error_message: str | None = None

    responder_last_latitude: float | None = None
    responder_last_longitude: float | None = None
    responder_last_source_type: str | None = None
    responder_last_recorded_at: datetime | None = None

    route_provider_name: str | None = None
    route_distance_meters: float | None = None
    route_distance_km: float | None = None
    route_duration_seconds: int | None = None
    route_eta_seconds: int | None = None
    route_eta_minutes: int | None = None
    route_polyline: str | None = None
    route_last_calculated_at: datetime | None = None
    route_error_message: str | None = None

    requested_at: datetime
    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    vehicle: IncidentVehicleSummaryResponse
    client_user: IncidentClientSummaryResponse
    provider: IncidentProviderSummaryResponse | None = None
    assigned_technician: IncidentTechnicianSummaryResponse | None = None


class CreateIncidentRequest(BaseModel):
    vehicle_id: str
    reported_category: Literal[
        "BATTERY",
        "TIRE",
        "ACCIDENT",
        "ENGINE",
        "LOCKOUT",
        "OVERHEATING",
        "OTHER",
        "UNCERTAIN",
    ] = "OTHER"
    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = "MEDIUM"
    title: str = Field(min_length=3, max_length=150)
    description: str = Field(min_length=5)
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = Field(default=None, max_length=255)


class UpdateOwnPendingIncidentRequest(BaseModel):
    reported_category: Literal[
        "BATTERY",
        "TIRE",
        "ACCIDENT",
        "ENGINE",
        "LOCKOUT",
        "OVERHEATING",
        "OTHER",
        "UNCERTAIN",
    ] | None = None
    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] | None = None
    title: str | None = Field(default=None, min_length=3, max_length=150)
    description: str | None = Field(default=None, min_length=5)
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = Field(default=None, max_length=255)
```

### `app/services/incidents/service.py`

- Ruta relativa: `app/services/incidents/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone

from app.common.constants import (
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_IN_REVIEW,
    INCIDENT_STATUS_PENDING,
    PROCESSING_STATUS_NOT_REQUESTED,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.incidents.repository import IncidentsRepository
from app.services.incidents.schemas import (
    CreateIncidentRequest,
    IncidentClientSummaryResponse,
    IncidentProviderSummaryResponse,
    IncidentResponse,
    IncidentTechnicianSummaryResponse,
    IncidentVehicleSummaryResponse,
    UpdateOwnPendingIncidentRequest,
)


class IncidentsService:
    def __init__(self, repository: IncidentsRepository) -> None:
        self.repository = repository

    def create_own_incident(
        self,
        current_user: User,
        payload: CreateIncidentRequest,
    ) -> IncidentResponse:
        vehicle = self.repository.get_vehicle_by_id(payload.vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        if not vehicle.is_active:
            raise ConflictException("The selected vehicle is inactive.")

        new_incident = Incident(
            client_user_id=current_user.id,
            vehicle_id=vehicle.id,
            provider_id=None,
            assigned_technician_id=None,
            dispatch_mode=None,
            status=INCIDENT_STATUS_PENDING,
            priority=payload.priority,
            reported_category=payload.reported_category,
            title=payload.title.strip(),
            description=payload.description.strip(),
            client_contact_phone_snapshot=current_user.phone_number,
            incident_latitude=payload.incident_latitude,
            incident_longitude=payload.incident_longitude,
            address_reference=payload.address_reference.strip() if payload.address_reference else None,
            estimated_price_min=None,
            estimated_price_max=None,
            ai_summary_status=PROCESSING_STATUS_NOT_REQUESTED,
            summary_provider_name=None,
            structured_summary=None,
            suggested_category=None,
            suggested_priority=None,
            requires_more_information=False,
            summary_processed_at=None,
            summary_error_message=None,
            responder_last_latitude=None,
            responder_last_longitude=None,
            responder_last_source_type=None,
            responder_last_recorded_at=None,
            route_provider_name=None,
            route_distance_meters=None,
            route_duration_seconds=None,
            route_eta_seconds=None,
            route_polyline=None,
            route_last_calculated_at=None,
            route_error_message=None,
        )

        created_incident = self.repository.create_incident(new_incident)
        return self._build_incident_response(created_incident)

    def list_own_incidents(self, current_user: User) -> list[IncidentResponse]:
        incidents = self.repository.list_incidents_by_client_user_id(str(current_user.id))
        return [self._build_incident_response(item) for item in incidents]

    def get_own_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        return self._build_incident_response(incident)

    def update_own_pending_incident(
        self,
        current_user: User,
        incident_id: str,
        payload: UpdateOwnPendingIncidentRequest,
    ) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        if incident.status not in (INCIDENT_STATUS_PENDING, INCIDENT_STATUS_IN_REVIEW):
            raise ConflictException("Only pending or in-review incidents can be updated by the client.")

        if payload.reported_category is not None:
            incident.reported_category = payload.reported_category

        if payload.priority is not None:
            incident.priority = payload.priority

        if payload.title is not None:
            incident.title = payload.title.strip()

        if payload.description is not None:
            incident.description = payload.description.strip()

        if payload.incident_latitude is not None:
            incident.incident_latitude = payload.incident_latitude

        if payload.incident_longitude is not None:
            incident.incident_longitude = payload.incident_longitude

        if payload.address_reference is not None:
            cleaned_value = payload.address_reference.strip()
            incident.address_reference = cleaned_value or None

        updated_incident = self.repository.save_incident(incident)
        return self._build_incident_response(updated_incident)

    def cancel_own_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated user.")

        if incident.status not in (INCIDENT_STATUS_PENDING, INCIDENT_STATUS_IN_REVIEW):
            raise ConflictException("Only pending or in-review incidents can be cancelled by the client.")

        incident.status = INCIDENT_STATUS_CANCELLED
        incident.cancelled_at = datetime.now(timezone.utc)

        updated_incident = self.repository.save_incident(incident)
        return self._build_incident_response(updated_incident)

    def list_all_incidents(self, limit: int = 50, offset: int = 0) -> list[IncidentResponse]:
        incidents = self.repository.list_all_incidents(limit=limit, offset=offset)
        return [self._build_incident_response(item) for item in incidents]

    def get_incident_by_id_for_platform(self, incident_id: str) -> IncidentResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_incident_response(incident)

    def list_provider_incidents(self, current_user: User) -> list[IncidentResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incidents = self.repository.list_incidents_by_provider_id(str(provider.id))
        return [self._build_incident_response(item) for item in incidents]

    def get_provider_incident(self, current_user: User, incident_id: str) -> IncidentResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_incident_response(incident)

    def _build_incident_response(self, incident: Incident) -> IncidentResponse:
        vehicle_payload = IncidentVehicleSummaryResponse(
            id=str(incident.vehicle.id),
            plate_number=incident.vehicle.plate_number,
            vehicle_type=incident.vehicle.vehicle_type,
            brand=incident.vehicle.brand,
            model=incident.vehicle.model,
            year=incident.vehicle.year,
            color=incident.vehicle.color,
        )

        client_payload = IncidentClientSummaryResponse(
            id=str(incident.client_user.id),
            email=incident.client_user.email,
            first_name=incident.client_user.first_name,
            last_name=incident.client_user.last_name,
            full_name=incident.client_user.full_name,
            phone_number=incident.client_user.phone_number,
        )

        provider_payload = None
        if incident.provider is not None:
            provider_payload = IncidentProviderSummaryResponse(
                id=str(incident.provider.id),
                provider_type=incident.provider.provider_type,
                business_name=incident.provider.business_name,
                contact_phone=incident.provider.contact_phone,
                city=incident.provider.city,
                is_available=incident.provider.is_available,
                average_rating=incident.provider.average_rating,
            )

        assigned_technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            assigned_technician_payload = IncidentTechnicianSummaryResponse(
                id=str(technician.id),
                provider_id=str(technician.provider_id),
                first_name=technician.first_name,
                last_name=technician.last_name,
                full_name=technician.full_name,
                phone_number=technician.phone_number,
                specialty=technician.specialty,
                is_active=technician.is_active,
                is_available=technician.is_available,
            )

        estimated_price_min = (
            float(incident.estimated_price_min)
            if incident.estimated_price_min is not None
            else None
        )
        estimated_price_max = (
            float(incident.estimated_price_max)
            if incident.estimated_price_max is not None
            else None
        )

        route_distance_km = (
            round(incident.route_distance_meters / 1000.0, 2)
            if incident.route_distance_meters is not None
            else None
        )
        route_eta_minutes = (
            int(round(incident.route_eta_seconds / 60))
            if incident.route_eta_seconds is not None
            else None
        )

        return IncidentResponse(
            id=str(incident.id),
            client_user_id=str(incident.client_user_id),
            vehicle_id=str(incident.vehicle_id),
            provider_id=str(incident.provider_id) if incident.provider_id is not None else None,
            assigned_technician_id=(
                str(incident.assigned_technician_id)
                if incident.assigned_technician_id is not None
                else None
            ),
            dispatch_mode=incident.dispatch_mode,
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            client_contact_phone_snapshot=incident.client_contact_phone_snapshot,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            estimated_price_min=estimated_price_min,
            estimated_price_max=estimated_price_max,
            ai_summary_status=incident.ai_summary_status,
            summary_provider_name=incident.summary_provider_name,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
            summary_processed_at=incident.summary_processed_at,
            summary_error_message=incident.summary_error_message,
            responder_last_latitude=incident.responder_last_latitude,
            responder_last_longitude=incident.responder_last_longitude,
            responder_last_source_type=incident.responder_last_source_type,
            responder_last_recorded_at=incident.responder_last_recorded_at,
            route_provider_name=incident.route_provider_name,
            route_distance_meters=incident.route_distance_meters,
            route_distance_km=route_distance_km,
            route_duration_seconds=incident.route_duration_seconds,
            route_eta_seconds=incident.route_eta_seconds,
            route_eta_minutes=route_eta_minutes,
            route_polyline=incident.route_polyline,
            route_last_calculated_at=incident.route_last_calculated_at,
            route_error_message=incident.route_error_message,
            requested_at=incident.requested_at,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            created_at=incident.created_at,
            updated_at=incident.updated_at,
            vehicle=vehicle_payload,
            client_user=client_payload,
            provider=provider_payload,
            assigned_technician=assigned_technician_payload,
        )
```

### `app/services/jobs/__init__.py`

- Ruta relativa: `app/services/jobs/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/jobs/dispatcher.py`

- Ruta relativa: `app/services/jobs/dispatcher.py`
- Nombre de archivo: `dispatcher.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_AUDIO_TRANSCRIPTION,
    BACKGROUND_JOB_TYPE_IMAGE_ANALYSIS,
    BACKGROUND_JOB_TYPE_INCIDENT_SUMMARY,
    CELERY_QUEUE_AUDIO,
    CELERY_QUEUE_IMAGE,
    CELERY_QUEUE_SUMMARY,
    EVIDENCE_TYPE_AUDIO,
    EVIDENCE_TYPE_IMAGE,
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_PENDING,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob


class PipelineDispatcher:
    def __init__(self, db: Session) -> None:
        self.db = db

    def dispatch_for_new_evidence(
        self,
        evidence: IncidentEvidence,
        requested_by_user_id: str | None,
    ) -> list[BackgroundJob]:
        created_jobs: list[BackgroundJob] = []

        if evidence.evidence_type == EVIDENCE_TYPE_AUDIO:
            created_jobs.append(
                self.enqueue_audio_transcription_job(
                    requested_by_user_id=requested_by_user_id,
                    evidence_id=str(evidence.id),
                    enqueue_reason="new_audio_evidence_uploaded",
                )
            )
            return created_jobs

        if evidence.evidence_type == EVIDENCE_TYPE_IMAGE:
            created_jobs.append(
                self.enqueue_image_analysis_job(
                    requested_by_user_id=requested_by_user_id,
                    evidence_id=str(evidence.id),
                    enqueue_reason="new_image_evidence_uploaded",
                )
            )
            return created_jobs

        if evidence.evidence_type == EVIDENCE_TYPE_TEXT:
            created_jobs.append(
                self.enqueue_incident_summary_job(
                    requested_by_user_id=requested_by_user_id,
                    incident_id=str(evidence.incident_id),
                    enqueue_reason="new_text_evidence_uploaded",
                )
            )
            return created_jobs

        return created_jobs

    def enqueue_audio_transcription_job(
        self,
        requested_by_user_id: str | None,
        evidence_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        evidence = self._get_evidence_or_raise(evidence_id)

        if evidence.evidence_type != EVIDENCE_TYPE_AUDIO:
            raise ConflictException("The selected evidence is not an AUDIO evidence.")

        evidence.audio_processing_status = PROCESSING_STATUS_PENDING
        evidence.audio_provider_name = None
        evidence.transcript_text = None
        evidence.transcript_language_code = None
        evidence.transcript_confidence = None
        evidence.transcript_segments_json = None
        evidence.audio_processed_at = None
        evidence.audio_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_AUDIO_TRANSCRIPTION,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_AUDIO,
            entity_type="INCIDENT_EVIDENCE",
            entity_id=evidence_id,
            payload_json={
                "evidence_id": evidence_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(evidence)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import audio_transcription_task

        async_result = audio_transcription_task.apply_async(
            args=[str(job.id), evidence_id],
            queue=CELERY_QUEUE_AUDIO,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def enqueue_image_analysis_job(
        self,
        requested_by_user_id: str | None,
        evidence_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        evidence = self._get_evidence_or_raise(evidence_id)

        if evidence.evidence_type != EVIDENCE_TYPE_IMAGE:
            raise ConflictException("The selected evidence is not an IMAGE evidence.")

        evidence.image_processing_status = PROCESSING_STATUS_PENDING
        evidence.image_provider_name = None
        evidence.image_labels_json = None
        evidence.image_detections_json = None
        evidence.image_summary = None
        evidence.image_processed_at = None
        evidence.image_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_IMAGE_ANALYSIS,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_IMAGE,
            entity_type="INCIDENT_EVIDENCE",
            entity_id=evidence_id,
            payload_json={
                "evidence_id": evidence_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(evidence)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import image_analysis_task

        async_result = image_analysis_task.apply_async(
            args=[str(job.id), evidence_id],
            queue=CELERY_QUEUE_IMAGE,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def enqueue_incident_summary_job(
        self,
        requested_by_user_id: str | None,
        incident_id: str,
        enqueue_reason: str = "manual",
    ) -> BackgroundJob:
        incident = self._get_incident_or_raise(incident_id)

        incident.ai_summary_status = PROCESSING_STATUS_PENDING
        incident.summary_provider_name = None
        incident.structured_summary = None
        incident.suggested_category = None
        incident.suggested_priority = None
        incident.requires_more_information = False
        incident.summary_processed_at = None
        incident.summary_error_message = None

        job = BackgroundJob(
            requested_by_user_id=requested_by_user_id,
            job_type=BACKGROUND_JOB_TYPE_INCIDENT_SUMMARY,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_SUMMARY,
            entity_type="INCIDENT",
            entity_id=incident_id,
            payload_json={
                "incident_id": incident_id,
                "enqueue_reason": enqueue_reason,
            },
        )

        self.db.add(incident)
        self.db.add(job)
        self.db.flush()

        from app.tasks.task_definitions import incident_summary_task

        async_result = incident_summary_task.apply_async(
            args=[str(job.id), incident_id],
            queue=CELERY_QUEUE_SUMMARY,
        )

        job.celery_task_id = async_result.id
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    def _get_evidence_or_raise(self, evidence_id: str) -> IncidentEvidence:
        evidence = self.db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        return evidence

    def _get_incident_or_raise(self, incident_id: str) -> Incident:
        incident = self.db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            raise NotFoundException("Incident not found.")

        return incident
```

### `app/services/jobs/models.py`

- Ruta relativa: `app/services/jobs/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class BackgroundJob(Base):
    __tablename__ = "background_jobs"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    requested_by_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    job_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    queue_name: Mapped[str] = mapped_column(String(50), nullable=False)

    celery_task_id: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    entity_type: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
    entity_id: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)

    payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    result_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    attempts_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    requested_by_user = relationship("User", lazy="selectin")
```

### `app/services/jobs/repository.py`

- Ruta relativa: `app/services/jobs/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob


class JobsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def save_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def get_job_by_id(self, job_id: str) -> BackgroundJob | None:
        query: Select[tuple[BackgroundJob]] = select(BackgroundJob).where(BackgroundJob.id == job_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_job_by_celery_task_id(self, celery_task_id: str) -> BackgroundJob | None:
        query: Select[tuple[BackgroundJob]] = (
            select(BackgroundJob).where(BackgroundJob.celery_task_id == celery_task_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_jobs(self, limit: int = 50, offset: int = 0) -> list[BackgroundJob]:
        query: Select[tuple[BackgroundJob]] = (
            select(BackgroundJob)
            .order_by(BackgroundJob.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def incident_exists(self, incident_id: str) -> bool:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none() is not None

    def evidence_exists(self, evidence_id: str) -> bool:
        query: Select[tuple[IncidentEvidence]] = select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        return self.db.execute(query).scalar_one_or_none() is not None
```

### `app/services/jobs/router.py`

- Ruta relativa: `app/services/jobs/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.jobs.repository import JobsRepository
from app.services.jobs.schemas import DemoJobEnqueueRequest
from app.services.jobs.service import JobsService

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/demo/enqueue")
def enqueue_demo_job(
    payload: DemoJobEnqueueRequest,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_demo_job(current_user, payload)

    return success_response(
        message="Demo background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/evidences/{evidence_id}/audio-transcription/enqueue")
def enqueue_audio_transcription_job(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_audio_transcription_job(current_user, evidence_id)

    return success_response(
        message="Audio transcription background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/evidences/{evidence_id}/image-analysis/enqueue")
def enqueue_image_analysis_job(
    evidence_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_image_analysis_job(current_user, evidence_id)

    return success_response(
        message="Image analysis background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/incidents/{incident_id}/summary/enqueue")
def enqueue_incident_summary_job(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.enqueue_incident_summary_job(current_user, incident_id)

    return success_response(
        message="Incident summary background job enqueued successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_jobs(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.list_jobs(limit=limit, offset=offset)

    return success_response(
        message="Background jobs loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{job_id}")
def get_job_by_id(
    job_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = JobsService(JobsRepository(db))
    result = service.get_job_by_id(job_id)

    return success_response(
        message="Background job loaded successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/jobs/schemas.py`

- Ruta relativa: `app/services/jobs/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel, Field


class BackgroundJobRequestedByUserResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class BackgroundJobResponse(BaseModel):
    id: str
    requested_by_user_id: str | None = None
    job_type: str
    status: str
    provider_name: str | None = None
    queue_name: str
    celery_task_id: str | None = None
    entity_type: str | None = None
    entity_id: str | None = None
    payload_json: dict | None = None
    result_json: dict | None = None
    error_message: str | None = None
    attempts_count: int
    started_at: datetime | None = None
    finished_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
    requested_by_user: BackgroundJobRequestedByUserResponse | None = None


class DemoJobEnqueueRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    countdown_seconds: int = Field(default=0, ge=0, le=30)
```

### `app/services/jobs/service.py`

- Ruta relativa: `app/services/jobs/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_DEMO,
    CELERY_QUEUE_DEFAULT,
)
from app.common.exceptions import NotFoundException
from app.services.auth.models import User
from app.services.jobs.dispatcher import PipelineDispatcher
from app.services.jobs.models import BackgroundJob
from app.services.jobs.repository import JobsRepository
from app.services.jobs.schemas import (
    BackgroundJobRequestedByUserResponse,
    BackgroundJobResponse,
    DemoJobEnqueueRequest,
)
from app.tasks.task_definitions import demo_echo_task


class JobsService:
    def __init__(self, repository: JobsRepository) -> None:
        self.repository = repository
        self.dispatcher = PipelineDispatcher(repository.db)

    def enqueue_demo_job(
        self,
        current_user: User,
        payload: DemoJobEnqueueRequest,
    ) -> BackgroundJobResponse:
        job = BackgroundJob(
            requested_by_user_id=current_user.id,
            job_type=BACKGROUND_JOB_TYPE_DEMO,
            status=BACKGROUND_JOB_STATUS_PENDING,
            provider_name="celery",
            queue_name=CELERY_QUEUE_DEFAULT,
            entity_type=None,
            entity_id=None,
            payload_json={
                "message": payload.message,
                "countdown_seconds": payload.countdown_seconds,
            },
        )

        created_job = self.repository.create_job(job)

        async_result = demo_echo_task.apply_async(
            args=[str(created_job.id), payload.message],
            countdown=payload.countdown_seconds,
            queue=CELERY_QUEUE_DEFAULT,
        )

        created_job.celery_task_id = async_result.id
        updated_job = self.repository.save_job(created_job)

        return self._build_job_response(updated_job)

    def enqueue_audio_transcription_job(
        self,
        current_user: User,
        evidence_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_audio_transcription_job(
            requested_by_user_id=str(current_user.id),
            evidence_id=evidence_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def enqueue_image_analysis_job(
        self,
        current_user: User,
        evidence_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_image_analysis_job(
            requested_by_user_id=str(current_user.id),
            evidence_id=evidence_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def enqueue_incident_summary_job(
        self,
        current_user: User,
        incident_id: str,
    ) -> BackgroundJobResponse:
        created_job = self.dispatcher.enqueue_incident_summary_job(
            requested_by_user_id=str(current_user.id),
            incident_id=incident_id,
            enqueue_reason="manual_platform_enqueue",
        )
        return self._build_job_response(created_job)

    def list_jobs(self, limit: int = 50, offset: int = 0) -> list[BackgroundJobResponse]:
        jobs = self.repository.list_jobs(limit=limit, offset=offset)
        return [self._build_job_response(job) for job in jobs]

    def get_job_by_id(self, job_id: str) -> BackgroundJobResponse:
        job = self.repository.get_job_by_id(job_id)
        if job is None:
            raise NotFoundException("Background job not found.")

        return self._build_job_response(job)

    def _build_job_response(self, job: BackgroundJob) -> BackgroundJobResponse:
        requested_by_user_payload = None

        if job.requested_by_user is not None:
            user = job.requested_by_user
            requested_by_user_payload = BackgroundJobRequestedByUserResponse(
                id=str(user.id),
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                full_name=user.full_name,
            )

        return BackgroundJobResponse(
            id=str(job.id),
            requested_by_user_id=str(job.requested_by_user_id) if job.requested_by_user_id else None,
            job_type=job.job_type,
            status=job.status,
            provider_name=job.provider_name,
            queue_name=job.queue_name,
            celery_task_id=job.celery_task_id,
            entity_type=job.entity_type,
            entity_id=job.entity_id,
            payload_json=job.payload_json,
            result_json=job.result_json,
            error_message=job.error_message,
            attempts_count=job.attempts_count,
            started_at=job.started_at,
            finished_at=job.finished_at,
            created_at=job.created_at,
            updated_at=job.updated_at,
            requested_by_user=requested_by_user_payload,
        )
```

### `app/services/notifications/__init__.py`

- Ruta relativa: `app/services/notifications/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/notifications/dispatcher.py`

- Ruta relativa: `app/services/notifications/dispatcher.py`
- Nombre de archivo: `dispatcher.py`

```python
from app.common.constants import (
    BACKGROUND_JOB_STATUS_PENDING,
    BACKGROUND_JOB_TYPE_PUSH_NOTIFICATION,
    CELERY_QUEUE_PUSH,
    PUSH_DELIVERY_STATUS_PENDING,
)
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery
from app.services.notifications.repository import NotificationsRepository


class PushNotificationDispatcher:
    def __init__(self, db) -> None:
        self.repository = NotificationsRepository(db)
        self.db = db

    def enqueue_event_for_user_ids(
        self,
        *,
        requested_by_user_id: str | None,
        incident_id: str | None,
        event_code: str,
        recipient_user_ids: list[str],
        title: str,
        body: str,
        data: dict[str, str] | None = None,
    ) -> list[BackgroundJob]:
        active_tokens = self.repository.list_active_user_device_tokens_by_user_ids(recipient_user_ids)
        if not active_tokens:
            return []

        normalized_data = {
            str(key): str(value)
            for key, value in (data or {}).items()
            if value is not None
        }

        try:
            created_jobs: list[BackgroundJob] = []

            for device_token in active_tokens:
                job = BackgroundJob(
                    requested_by_user_id=requested_by_user_id,
                    job_type=BACKGROUND_JOB_TYPE_PUSH_NOTIFICATION,
                    status=BACKGROUND_JOB_STATUS_PENDING,
                    provider_name="celery",
                    queue_name=CELERY_QUEUE_PUSH,
                    entity_type="PUSH_NOTIFICATION_DELIVERY",
                    entity_id=None,
                    payload_json={
                        "event_code": event_code,
                        "incident_id": incident_id,
                        "recipient_user_id": str(device_token.user_id),
                        "user_device_token_id": str(device_token.id),
                        "title": title,
                        "body": body,
                        "data": normalized_data,
                    },
                )
                self.repository.create_background_job(job)

                delivery = PushNotificationDelivery(
                    background_job_id=job.id,
                    incident_id=incident_id,
                    recipient_user_id=device_token.user_id,
                    user_device_token_id=device_token.id,
                    provider_name=None,
                    event_code=event_code,
                    title=title,
                    body=body,
                    data_json=normalized_data or None,
                    status=PUSH_DELIVERY_STATUS_PENDING,
                    provider_message_id=None,
                    error_message=None,
                    sent_at=None,
                )
                self.repository.create_delivery(delivery)

                job.entity_id = str(delivery.id)
                self.repository.save(job)

                from app.tasks.task_definitions import push_notification_task

                async_result = push_notification_task.apply_async(
                    args=[str(job.id), str(delivery.id)],
                    queue=CELERY_QUEUE_PUSH,
                )

                job.celery_task_id = async_result.id
                self.repository.save(job)
                created_jobs.append(job)

            self.repository.commit()

            for job in created_jobs:
                self.repository.refresh(job)

            return created_jobs
        except Exception:
            self.repository.rollback()
            raise
```

### `app/services/notifications/models.py`

- Ruta relativa: `app/services/notifications/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, JSON, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class UserDeviceToken(Base):
    __tablename__ = "user_device_tokens"
    __table_args__ = (
        UniqueConstraint("device_token", name="uq_user_device_tokens_device_token"),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    device_token: Mapped[str] = mapped_column(String(512), nullable=False)
    device_platform: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    device_label: Mapped[str | None] = mapped_column(String(120), nullable=True)
    app_role: Mapped[str | None] = mapped_column(String(30), nullable=True)
    push_provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    user = relationship("User", lazy="selectin")


class PushNotificationDelivery(Base):
    __tablename__ = "push_notification_deliveries"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    background_job_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("background_jobs.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    incident_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    recipient_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    user_device_token_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("user_device_tokens.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    provider_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    event_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    data_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    provider_message_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    sent_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    recipient_user = relationship("User", foreign_keys=[recipient_user_id], lazy="selectin")
    user_device_token = relationship("UserDeviceToken", lazy="selectin")
    background_job = relationship("BackgroundJob", lazy="selectin")
    incident = relationship("Incident", lazy="selectin")
```

### `app/services/notifications/repository.py`

- Ruta relativa: `app/services/notifications/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.auth.models import User
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery, UserDeviceToken
from app.services.providers.models import Provider


class NotificationsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_user_device_token_by_token(self, device_token: str) -> UserDeviceToken | None:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken).where(UserDeviceToken.device_token == device_token)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_user_device_token_by_id(self, device_token_id: str) -> UserDeviceToken | None:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken).where(UserDeviceToken.id == device_token_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_active_user_device_tokens_by_user_id(self, user_id: str) -> list[UserDeviceToken]:
        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken)
            .where(
                UserDeviceToken.user_id == user_id,
                UserDeviceToken.is_active.is_(True),
            )
            .order_by(UserDeviceToken.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_active_user_device_tokens_by_user_ids(self, user_ids: list[str]) -> list[UserDeviceToken]:
        if not user_ids:
            return []

        query: Select[tuple[UserDeviceToken]] = (
            select(UserDeviceToken)
            .where(
                UserDeviceToken.user_id.in_(user_ids),
                UserDeviceToken.is_active.is_(True),
            )
            .order_by(UserDeviceToken.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.assigned_technician),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_deliveries_by_incident_id(self, incident_id: str) -> list[PushNotificationDelivery]:
        query: Select[tuple[PushNotificationDelivery]] = (
            select(PushNotificationDelivery)
            .options(
                selectinload(PushNotificationDelivery.recipient_user),
                selectinload(PushNotificationDelivery.user_device_token),
                selectinload(PushNotificationDelivery.background_job),
            )
            .where(PushNotificationDelivery.incident_id == incident_id)
            .order_by(PushNotificationDelivery.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_background_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.flush()
        return job

    def create_delivery(self, delivery: PushNotificationDelivery) -> PushNotificationDelivery:
        self.db.add(delivery)
        self.db.flush()
        return delivery

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/notifications/router.py`

- Ruta relativa: `app/services/notifications/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.notifications.repository import NotificationsRepository
from app.services.notifications.schemas import (
    PlatformSendTestPushRequest,
    RegisterDeviceTokenRequest,
)
from app.services.notifications.service import NotificationsService

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/me/devices/register")
def register_my_device_token(
    payload: RegisterDeviceTokenRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.register_my_device_token(current_user, payload)

    return success_response(
        message="Device token registered successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/devices")
def list_my_device_tokens(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.list_my_device_tokens(current_user)

    return success_response(
        message="Device tokens loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )

@router.delete("/me/devices/{device_token_id}")
def deactivate_my_device_token(
    device_token_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.deactivate_my_device_token(current_user, device_token_id)

    return success_response(
        message="Device token deactivated successfully.",
        data=result.model_dump(mode="json"),
    )

@router.post("/platform/users/{user_id}/test")
def send_platform_test_push(
    user_id: str,
    payload: PlatformSendTestPushRequest,
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.send_platform_test_push(current_user, user_id, payload)

    return success_response(
        message="Platform test push notification enqueued successfully.",
        data=result.model_dump(mode="json"),
    )

@router.get("/platform/incidents/{incident_id}/deliveries")
def list_platform_incident_deliveries(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = NotificationsService(NotificationsRepository(db))
    result = service.list_platform_incident_deliveries(incident_id)

    return success_response(
        message="Incident notification deliveries loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
```

### `app/services/notifications/schemas.py`

- Ruta relativa: `app/services/notifications/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from app.common.constants import (
    DEVICE_PLATFORM_ANDROID,
    DEVICE_PLATFORM_IOS,
    DEVICE_PLATFORM_WEB,
)


class RegisterDeviceTokenRequest(BaseModel):
    device_token: str = Field(min_length=20, max_length=512)
    device_platform: Literal[
        DEVICE_PLATFORM_ANDROID,
        DEVICE_PLATFORM_IOS,
        DEVICE_PLATFORM_WEB,
    ]
    device_label: str | None = Field(default=None, max_length=120)
    app_role: str | None = Field(default=None, max_length=30)


class UserDeviceTokenResponse(BaseModel):
    id: str
    user_id: str
    device_platform: str
    device_label: str | None = None
    app_role: str | None = None
    push_provider_name: str | None = None
    is_active: bool
    last_seen_at: datetime
    created_at: datetime
    updated_at: datetime


class PlatformSendTestPushRequest(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    body: str = Field(min_length=2, max_length=1000)
    data: dict[str, str] = Field(default_factory=dict)
    incident_id: str | None = None


class NotificationDispatchSummaryResponse(BaseModel):
    event_code: str
    incident_id: str | None = None
    target_user_id: str
    active_device_tokens_count: int
    enqueued_jobs_count: int


class NotificationRecipientUserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str


class NotificationDeliveryResponse(BaseModel):
    id: str
    background_job_id: str | None = None
    incident_id: str | None = None
    recipient_user_id: str | None = None
    user_device_token_id: str | None = None
    provider_name: str | None = None
    event_code: str
    title: str
    body: str
    data_json: dict | None = None
    status: str
    provider_message_id: str | None = None
    error_message: str | None = None
    sent_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
    recipient_user: NotificationRecipientUserResponse | None = None
```

### `app/services/notifications/service.py`

- Ruta relativa: `app/services/notifications/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone

from app.common.constants import (
    PUSH_EVENT_TEST,
)
from app.common.exceptions import ForbiddenException, NotFoundException
from app.core.config import settings
from app.services.auth.models import User
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.services.notifications.models import PushNotificationDelivery, UserDeviceToken
from app.services.notifications.repository import NotificationsRepository
from app.services.notifications.schemas import (
    NotificationDeliveryResponse,
    NotificationDispatchSummaryResponse,
    NotificationRecipientUserResponse,
    PlatformSendTestPushRequest,
    RegisterDeviceTokenRequest,
    UserDeviceTokenResponse,
)


class NotificationsService:
    def __init__(self, repository: NotificationsRepository) -> None:
        self.repository = repository
        self.dispatcher = PushNotificationDispatcher(repository.db)

    def register_my_device_token(
        self,
        current_user: User,
        payload: RegisterDeviceTokenRequest,
    ) -> UserDeviceTokenResponse:
        existing_token = self.repository.get_user_device_token_by_token(payload.device_token)
        now = datetime.now(timezone.utc)

        if existing_token is None:
            token = UserDeviceToken(
                user_id=current_user.id,
                device_token=payload.device_token,
                device_platform=payload.device_platform,
                device_label=self._normalize_optional_text(payload.device_label),
                app_role=self._normalize_optional_text(payload.app_role),
                push_provider_name=settings.push_provider.lower(),
                is_active=True,
                last_seen_at=now,
            )
        else:
            token = existing_token
            token.user_id = current_user.id
            token.device_platform = payload.device_platform
            token.device_label = self._normalize_optional_text(payload.device_label)
            token.app_role = self._normalize_optional_text(payload.app_role)
            token.push_provider_name = settings.push_provider.lower()
            token.is_active = True
            token.last_seen_at = now

        try:
            self.repository.save(token)
            self.repository.commit()
            self.repository.refresh(token)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_device_token_response(token)

    def list_my_device_tokens(self, current_user: User) -> list[UserDeviceTokenResponse]:
        tokens = self.repository.list_active_user_device_tokens_by_user_id(str(current_user.id))
        return [self._build_device_token_response(item) for item in tokens]

    def deactivate_my_device_token(
        self,
        current_user: User,
        device_token_id: str,
    ) -> UserDeviceTokenResponse:
        token = self.repository.get_user_device_token_by_id(device_token_id)
        if token is None:
            raise NotFoundException("Device token not found.")

        if str(token.user_id) != str(current_user.id):
            raise ForbiddenException("This device token does not belong to the authenticated user.")

        token.is_active = False
        token.last_seen_at = datetime.now(timezone.utc)

        try:
            self.repository.save(token)
            self.repository.commit()
            self.repository.refresh(token)
        except Exception:
            self.repository.rollback()
            raise

        return self._build_device_token_response(token)

    def send_platform_test_push(
        self,
        current_user: User,
        user_id: str,
        payload: PlatformSendTestPushRequest,
    ) -> NotificationDispatchSummaryResponse:
        target_user = self.repository.get_user_by_id(user_id)
        if target_user is None:
            raise NotFoundException("Target user not found.")

        active_tokens = self.repository.list_active_user_device_tokens_by_user_id(user_id)
        created_jobs = self.dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=str(current_user.id),
            incident_id=payload.incident_id,
            event_code=PUSH_EVENT_TEST,
            recipient_user_ids=[user_id],
            title=payload.title.strip(),
            body=payload.body.strip(),
            data=payload.data,
        )

        return NotificationDispatchSummaryResponse(
            event_code=PUSH_EVENT_TEST,
            incident_id=payload.incident_id,
            target_user_id=str(target_user.id),
            active_device_tokens_count=len(active_tokens),
            enqueued_jobs_count=len(created_jobs),
        )

    def list_platform_incident_deliveries(
        self,
        incident_id: str,
    ) -> list[NotificationDeliveryResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        deliveries = self.repository.list_deliveries_by_incident_id(incident_id)
        return [self._build_delivery_response(item) for item in deliveries]

    def _build_device_token_response(self, token: UserDeviceToken) -> UserDeviceTokenResponse:
        return UserDeviceTokenResponse(
            id=str(token.id),
            user_id=str(token.user_id),
            device_platform=token.device_platform,
            device_label=token.device_label,
            app_role=token.app_role,
            push_provider_name=token.push_provider_name,
            is_active=token.is_active,
            last_seen_at=token.last_seen_at,
            created_at=token.created_at,
            updated_at=token.updated_at,
        )

    def _build_delivery_response(
        self,
        delivery: PushNotificationDelivery,
    ) -> NotificationDeliveryResponse:
        recipient_user_payload = None
        if delivery.recipient_user is not None:
            recipient_user = delivery.recipient_user
            recipient_user_payload = NotificationRecipientUserResponse(
                id=str(recipient_user.id),
                email=recipient_user.email,
                first_name=recipient_user.first_name,
                last_name=recipient_user.last_name,
                full_name=recipient_user.full_name,
            )

        return NotificationDeliveryResponse(
            id=str(delivery.id),
            background_job_id=(
                str(delivery.background_job_id) if delivery.background_job_id is not None else None
            ),
            incident_id=str(delivery.incident_id) if delivery.incident_id is not None else None,
            recipient_user_id=(
                str(delivery.recipient_user_id) if delivery.recipient_user_id is not None else None
            ),
            user_device_token_id=(
                str(delivery.user_device_token_id)
                if delivery.user_device_token_id is not None
                else None
            ),
            provider_name=delivery.provider_name,
            event_code=delivery.event_code,
            title=delivery.title,
            body=delivery.body,
            data_json=delivery.data_json,
            status=delivery.status,
            provider_message_id=delivery.provider_message_id,
            error_message=delivery.error_message,
            sent_at=delivery.sent_at,
            created_at=delivery.created_at,
            updated_at=delivery.updated_at,
            recipient_user=recipient_user_payload,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None
```

### `app/services/operations/__init__.py`

- Ruta relativa: `app/services/operations/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/operations/models.py`

- Ruta relativa: `app/services/operations/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentOperationEvent(Base):
    __tablename__ = "incident_operation_events"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    technician_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("technicians.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    actor_user_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    event_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    from_status: Mapped[str | None] = mapped_column(String(30), nullable=True)
    to_status: Mapped[str | None] = mapped_column(String(30), nullable=True)

    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    technician = relationship("Technician", lazy="selectin")
    actor_user = relationship("User", lazy="selectin")
```

### `app/services/operations/repository.py`

- Ruta relativa: `app/services/operations/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.incidents.models import Incident
from app.services.operations.models import IncidentOperationEvent
from app.services.providers.models import Provider, Technician


class OperationsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.technicians),
            )
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_id_for_update(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .where(Provider.id == provider_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id_for_update(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_technician_by_id_for_update(self, technician_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.id == technician_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_active_incidents(self, provider_id: str) -> list[Incident]:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.vehicle),
                selectinload(Incident.provider),
                selectinload(Incident.assigned_technician),
            )
            .where(
                Incident.provider_id == provider_id,
                Incident.status.in_(["ASSIGNED", "EN_ROUTE", "ON_SITE", "IN_PROGRESS"]),
            )
            .order_by(Incident.assigned_at.asc(), Incident.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_operation_events_by_incident_id(self, incident_id: str) -> list[IncidentOperationEvent]:
        query: Select[tuple[IncidentOperationEvent]] = (
            select(IncidentOperationEvent)
            .options(
                selectinload(IncidentOperationEvent.actor_user),
                selectinload(IncidentOperationEvent.technician),
                selectinload(IncidentOperationEvent.provider).selectinload(Provider.owner_user),
            )
            .where(IncidentOperationEvent.incident_id == incident_id)
            .order_by(IncidentOperationEvent.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_event(self, event: IncidentOperationEvent) -> IncidentOperationEvent:
        self.db.add(event)
        self.db.flush()
        return event

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/operations/router.py`

- Ruta relativa: `app/services/operations/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.operations.repository import OperationsRepository
from app.services.operations.schemas import (
    CompleteIncidentRequest,
    DispatchIncidentRequest,
    OperationNoteRequest,
)
from app.services.operations.service import OperationsService

router = APIRouter(prefix="/operations", tags=["Operations"])


@router.get("/provider/me/active")
def list_my_active_operations(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_my_active_operations(current_user)

    return success_response(
        message="Active provider operations loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/provider/incidents/{incident_id}/state")
def get_my_operation_state(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.get_my_operation_state(current_user, incident_id)

    return success_response(
        message="Provider operation state loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/dispatch")
def dispatch_my_incident(
    incident_id: str,
    payload: DispatchIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.dispatch_my_incident(current_user, incident_id, payload)

    return success_response(
        message="Incident dispatched successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/arrive")
def mark_my_arrival(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.mark_my_arrival(current_user, incident_id, payload)

    return success_response(
        message="Incident marked as arrived successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/start")
def start_my_service(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.start_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service started successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/complete")
def complete_my_service(
    incident_id: str,
    payload: CompleteIncidentRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.complete_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service completed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/cancel")
def cancel_my_service(
    incident_id: str,
    payload: OperationNoteRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.cancel_my_service(current_user, incident_id, payload)

    return success_response(
        message="Incident service cancelled successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/history")
def list_my_operation_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_my_operation_history(current_user, incident_id)

    return success_response(
        message="Provider operation history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/platform/incidents/{incident_id}/history")
def list_platform_operation_history(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = OperationsService(OperationsRepository(db))
    result = service.list_platform_operation_history(incident_id)

    return success_response(
        message="Platform operation history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
```

### `app/services/operations/schemas.py`

- Ruta relativa: `app/services/operations/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel, Field


class OperationTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class OperationClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentOperationStateResponse(BaseModel):
    incident_id: str
    provider_id: str | None = None
    assigned_technician_id: str | None = None
    dispatch_mode: str | None = None

    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    client_contact_phone_snapshot: str | None = None
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    address_reference: str | None = None

    ai_summary_status: str
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool

    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    client_user: OperationClientSummaryResponse
    assigned_technician: OperationTechnicianSummaryResponse | None = None


class DispatchIncidentRequest(BaseModel):
    technician_id: str | None = None
    note: str | None = Field(default=None, max_length=1000)


class OperationNoteRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)


class CompleteIncidentRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)
    completion_summary: str | None = Field(default=None, max_length=3000)


class OperationEventActorResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class IncidentOperationEventResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str | None = None
    technician_id: str | None = None
    actor_user_id: str | None = None
    event_type: str
    from_status: str | None = None
    to_status: str | None = None
    note: str | None = None
    payload_json: dict | None = None
    created_at: datetime
    actor_user: OperationEventActorResponse | None = None
    technician: OperationTechnicianSummaryResponse | None = None
```

### `app/services/operations/service.py`

- Ruta relativa: `app/services/operations/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone

from app.common.constants import (
    DISPATCH_MODE_PROVIDER_SELF,
    DISPATCH_MODE_TECHNICIAN,
    INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
    INCIDENT_OPERATION_EVENT_DISPATCHED,
    INCIDENT_OPERATION_EVENT_SERVICE_CANCELLED,
    INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
    INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_CANCELLED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    PROVIDER_TYPE_WORKSHOP,
    PUSH_EVENT_INCIDENT_CANCELLED,
    PUSH_EVENT_INCIDENT_COMPLETED,
    PUSH_EVENT_PROVIDER_ARRIVED,
    PUSH_EVENT_PROVIDER_EN_ROUTE,
    PUSH_EVENT_TECHNICIAN_ASSIGNED,
    AUDIT_EVENT_INCIDENT_ARRIVED,
    AUDIT_EVENT_INCIDENT_CANCELLED,
    AUDIT_EVENT_INCIDENT_COMPLETED,
    AUDIT_EVENT_INCIDENT_DISPATCHED,


)
from app.services.notifications.dispatcher import PushNotificationDispatcher
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.operations.models import IncidentOperationEvent
from app.services.operations.repository import OperationsRepository
from app.services.operations.schemas import (
    CompleteIncidentRequest,
    DispatchIncidentRequest,
    IncidentOperationEventResponse,
    IncidentOperationStateResponse,
    OperationClientSummaryResponse,
    OperationEventActorResponse,
    OperationNoteRequest,
    OperationTechnicianSummaryResponse,
)
from app.services.billing.repository import BillingRepository
from app.services.billing.service import BillingService



class OperationsService:
    def __init__(self, repository: OperationsRepository) -> None:
        self.repository = repository

    def list_my_active_operations(self, current_user: User) -> list[IncidentOperationStateResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incidents = self.repository.list_provider_active_incidents(str(provider.id))
        return [self._build_operation_state_response(item) for item in incidents]

    def get_my_operation_state(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_operation_state_response(incident)

    def dispatch_my_incident(
        self,
        current_user: User,
        incident_id: str,
        payload: DispatchIncidentRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status != INCIDENT_STATUS_ASSIGNED:
                raise ConflictException("Only assigned incidents can be dispatched.")

            assigned_technician = None
            dispatch_mode = DISPATCH_MODE_PROVIDER_SELF

            if locked_provider.provider_type == PROVIDER_TYPE_WORKSHOP:
                if not payload.technician_id:
                    raise ConflictException("A technician is required to dispatch a workshop incident.")

                assigned_technician = self.repository.get_technician_by_id_for_update(payload.technician_id)
                if assigned_technician is None:
                    raise NotFoundException("Technician not found.")

                if str(assigned_technician.provider_id) != str(locked_provider.id):
                    raise ForbiddenException("This technician does not belong to your provider.")

                if not assigned_technician.is_active:
                    raise ConflictException("The selected technician is inactive.")

                if not assigned_technician.is_available:
                    raise ConflictException("The selected technician is not available.")

                assigned_technician.is_available = False
                dispatch_mode = DISPATCH_MODE_TECHNICIAN
                locked_incident.assigned_technician_id = assigned_technician.id
                self.repository.save(assigned_technician)
            else:
                if payload.technician_id:
                    raise ConflictException("Independent mechanics cannot dispatch using a technician_id.")
                locked_incident.assigned_technician_id = None

            previous_status = locked_incident.status
            locked_incident.dispatch_mode = dispatch_mode
            locked_incident.status = INCIDENT_STATUS_EN_ROUTE
            locked_incident.en_route_at = now

            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=assigned_technician.id if assigned_technician is not None else None,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_DISPATCHED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json={
                        "dispatch_mode": dispatch_mode,
                        "assigned_technician_id": (
                            str(assigned_technician.id)
                            if assigned_technician is not None
                            else None
                        ),
                    },
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")
        
        self._enqueue_notification_safely(
        lambda: self._enqueue_dispatch_notification(incident_id)
        )

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_DISPATCHED,
        payload_json={
            "dispatch_mode": incident.dispatch_mode,
            "assigned_technician_id": str(incident.assigned_technician_id) if incident.assigned_technician_id else None,
            "status": incident.status,
        },
    )


        return self._build_operation_state_response(incident)

    def mark_my_arrival(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status != INCIDENT_STATUS_EN_ROUTE:
                raise ConflictException("Only incidents en route can be marked as arrived.")

            previous_status = locked_incident.status
            locked_incident.status = INCIDENT_STATUS_ON_SITE
            locked_incident.arrived_at = now
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        self._enqueue_notification_safely(
        lambda: self._enqueue_arrival_notification(incident_id)
        )

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_ARRIVED,
        payload_json={
            "status": incident.status,
            "arrived_at": incident.arrived_at.isoformat() if incident.arrived_at else None,
        },
    )


        return self._build_operation_state_response(incident)

    def start_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (INCIDENT_STATUS_EN_ROUTE, INCIDENT_STATUS_ON_SITE):
                raise ConflictException(
                    "Only incidents en route or on site can be started."
                )

            previous_status = locked_incident.status
            if locked_incident.arrived_at is None:
                locked_incident.arrived_at = now

            if locked_incident.started_at is None:
                locked_incident.started_at = now

            locked_incident.status = INCIDENT_STATUS_IN_PROGRESS
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_operation_state_response(incident)

    def complete_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: CompleteIncidentRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (INCIDENT_STATUS_ON_SITE, INCIDENT_STATUS_IN_PROGRESS):
                raise ConflictException(
                    "Only incidents on site or in progress can be completed."
                )

            assigned_technician = None
            if locked_incident.assigned_technician_id is not None:
                assigned_technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )

            previous_status = locked_incident.status

            if locked_incident.arrived_at is None:
                locked_incident.arrived_at = now

            if locked_incident.started_at is None:
                locked_incident.started_at = now

            locked_incident.status = INCIDENT_STATUS_COMPLETED
            locked_incident.completed_at = now

            if assigned_technician is not None and assigned_technician.is_active:
                assigned_technician.is_available = True
                self.repository.save(assigned_technician)

            locked_provider.current_active_services = max(
                locked_provider.current_active_services - 1,
                0,
            )

            self.repository.save(locked_provider)
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json={
                        "completion_summary": self._normalize_optional_text(payload.completion_summary),
                    },
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        self._enqueue_notification_safely(
        lambda: self._enqueue_completion_notification(incident_id)
        )


        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_COMPLETED,
        payload_json={
            "status": incident.status,
            "completed_at": incident.completed_at.isoformat() if incident.completed_at else None,
        },
    )

        return self._build_operation_state_response(incident)

    def cancel_my_service(
        self,
        current_user: User,
        incident_id: str,
        payload: OperationNoteRequest,
    ) -> IncidentOperationStateResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_provider = self.repository.get_provider_by_id_for_update(str(provider.id))
            if locked_provider is None:
                raise NotFoundException("Provider not found.")

            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(locked_provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException(
                    "Only assigned or active incidents can be cancelled by the provider."
                )

            assigned_technician = None
            if locked_incident.assigned_technician_id is not None:
                assigned_technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )

            previous_status = locked_incident.status
            locked_incident.status = INCIDENT_STATUS_CANCELLED
            locked_incident.cancelled_at = now

            if assigned_technician is not None and assigned_technician.is_active:
                assigned_technician.is_available = True
                self.repository.save(assigned_technician)

            locked_provider.current_active_services = max(
                locked_provider.current_active_services - 1,
                0,
            )

            self.repository.save(locked_provider)
            self.repository.save(locked_incident)

            self.repository.create_event(
                IncidentOperationEvent(
                    incident_id=locked_incident.id,
                    provider_id=locked_provider.id,
                    technician_id=locked_incident.assigned_technician_id,
                    actor_user_id=current_user.id,
                    event_type=INCIDENT_OPERATION_EVENT_SERVICE_CANCELLED,
                    from_status=previous_status,
                    to_status=locked_incident.status,
                    note=self._normalize_optional_text(payload.note),
                    payload_json=None,
                )
            )

            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")


        self._enqueue_notification_safely(
        lambda: self._enqueue_cancellation_notification(incident_id)
        )

        self._sync_billing_cancellation_safely(incident_id)

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=str(incident.id),
        provider_id=str(incident.provider_id) if incident.provider_id else None,
        event_type=AUDIT_EVENT_INCIDENT_CANCELLED,
        payload_json={
            "status": incident.status,
            "cancelled_at": incident.cancelled_at.isoformat() if incident.cancelled_at else None,
        },
    )

        return self._build_operation_state_response(incident)

    def list_my_operation_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[IncidentOperationEventResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        events = self.repository.list_operation_events_by_incident_id(incident_id)
        return [self._build_event_response(item) for item in events]

    def list_platform_operation_history(
        self,
        incident_id: str,
    ) -> list[IncidentOperationEventResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        events = self.repository.list_operation_events_by_incident_id(incident_id)
        return [self._build_event_response(item) for item in events]

    def _build_operation_state_response(self, incident) -> IncidentOperationStateResponse:
        client_user = incident.client_user

        assigned_technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            assigned_technician_payload = OperationTechnicianSummaryResponse(
                id=str(technician.id),
                provider_id=str(technician.provider_id),
                first_name=technician.first_name,
                last_name=technician.last_name,
                full_name=technician.full_name,
                phone_number=technician.phone_number,
                specialty=technician.specialty,
                is_active=technician.is_active,
                is_available=technician.is_available,
            )

        client_payload = OperationClientSummaryResponse(
            id=str(client_user.id),
            email=client_user.email,
            first_name=client_user.first_name,
            last_name=client_user.last_name,
            full_name=client_user.full_name,
            phone_number=client_user.phone_number,
        )

        return IncidentOperationStateResponse(
            incident_id=str(incident.id),
            provider_id=str(incident.provider_id) if incident.provider_id else None,
            assigned_technician_id=(
                str(incident.assigned_technician_id)
                if incident.assigned_technician_id is not None
                else None
            ),
            dispatch_mode=incident.dispatch_mode,
            status=incident.status,
            priority=incident.priority,
            reported_category=incident.reported_category,
            title=incident.title,
            description=incident.description,
            client_contact_phone_snapshot=incident.client_contact_phone_snapshot,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            address_reference=incident.address_reference,
            ai_summary_status=incident.ai_summary_status,
            structured_summary=incident.structured_summary,
            suggested_category=incident.suggested_category,
            suggested_priority=incident.suggested_priority,
            requires_more_information=incident.requires_more_information,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            client_user=client_payload,
            assigned_technician=assigned_technician_payload,
        )

    def _build_event_response(self, event: IncidentOperationEvent) -> IncidentOperationEventResponse:
        actor_payload = None
        if event.actor_user is not None:
            actor_user = event.actor_user
            actor_payload = OperationEventActorResponse(
                id=str(actor_user.id),
                email=actor_user.email,
                first_name=actor_user.first_name,
                last_name=actor_user.last_name,
                full_name=actor_user.full_name,
            )

        technician_payload = None
        if event.technician is not None:
            technician = event.technician
            technician_payload = OperationTechnicianSummaryResponse(
                id=str(technician.id),
                provider_id=str(technician.provider_id),
                first_name=technician.first_name,
                last_name=technician.last_name,
                full_name=technician.full_name,
                phone_number=technician.phone_number,
                specialty=technician.specialty,
                is_active=technician.is_active,
                is_available=technician.is_available,
            )

        return IncidentOperationEventResponse(
            id=str(event.id),
            incident_id=str(event.incident_id),
            provider_id=str(event.provider_id) if event.provider_id else None,
            technician_id=str(event.technician_id) if event.technician_id else None,
            actor_user_id=str(event.actor_user_id) if event.actor_user_id else None,
            event_type=event.event_type,
            from_status=event.from_status,
            to_status=event.to_status,
            note=event.note,
            payload_json=event.payload_json,
            created_at=event.created_at,
            actor_user=actor_payload,
            technician=technician_payload,
        )

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None

        cleaned_value = value.strip()
        return cleaned_value or None


    def _enqueue_dispatch_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)

        if incident.dispatch_mode == DISPATCH_MODE_TECHNICIAN and incident.assigned_technician is not None:
            dispatcher.enqueue_event_for_user_ids(
                requested_by_user_id=None,
                incident_id=incident_id,
                event_code=PUSH_EVENT_TECHNICIAN_ASSIGNED,
                recipient_user_ids=[str(incident.client_user_id)],
                title="Técnico asignado",
                body=f"{incident.assigned_technician.full_name} fue asignado y ya va en camino.",
                data={
                "event_code": PUSH_EVENT_TECHNICIAN_ASSIGNED,
                "incident_id": str(incident.id),
                "provider_id": str(incident.provider_id),
                "technician_id": str(incident.assigned_technician_id),
                "technician_name": incident.assigned_technician.full_name,
                "status": incident.status,
                },
            )
            return

        dispatcher.enqueue_event_for_user_ids(
        requested_by_user_id=None,
        incident_id=incident_id,
        event_code=PUSH_EVENT_PROVIDER_EN_ROUTE,
        recipient_user_ids=[str(incident.client_user_id)],
        title="Ayuda en camino",
        body=f"{incident.provider.business_name} ya va en camino hacia tu ubicación.",
        data={
            "event_code": PUSH_EVENT_PROVIDER_EN_ROUTE,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_arrival_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_PROVIDER_ARRIVED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Proveedor en el lugar",
            body=f"{incident.provider.business_name} llegó al punto del incidente.",
            data={
            "event_code": PUSH_EVENT_PROVIDER_ARRIVED,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_completion_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_COMPLETED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Servicio finalizado",
            body=f"{incident.provider.business_name} finalizó la atención de tu incidente.",
            data={
            "event_code": PUSH_EVENT_INCIDENT_COMPLETED,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_cancellation_notification(self, incident_id: str) -> None:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None or incident.provider is None:
            return

        dispatcher = PushNotificationDispatcher(self.repository.db)
        dispatcher.enqueue_event_for_user_ids(
            requested_by_user_id=None,
            incident_id=incident_id,
            event_code=PUSH_EVENT_INCIDENT_CANCELLED,
            recipient_user_ids=[str(incident.client_user_id)],
            title="Servicio cancelado",
            body=f"{incident.provider.business_name} canceló la atención del incidente.",
            data={
            "event_code": PUSH_EVENT_INCIDENT_CANCELLED,
            "incident_id": str(incident.id),
            "provider_id": str(incident.provider_id),
            "provider_name": incident.provider.business_name,
            "status": incident.status,
            },
        )


    def _enqueue_notification_safely(self, callback) -> None:
        try:
            callback()
        except Exception:
            return

    def _sync_billing_cancellation_safely(self, incident_id: str) -> None:
        try:
            billing_service = BillingService(BillingRepository(self.repository.db))
            billing_service.cancel_billing_due_to_incident_cancellation(incident_id)
        except Exception:
            return


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type="INCIDENT",
                entity_id=incident_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return
```

### `app/services/providers/__init__.py`

- Ruta relativa: `app/services/providers/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/providers/models.py`

- Ruta relativa: `app/services/providers/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    owner_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        unique=True,
        nullable=False,
    )

    provider_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    business_name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    legal_name: Mapped[str | None] = mapped_column(String(180), nullable=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    contact_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    contact_phone: Mapped[str | None] = mapped_column(String(30), nullable=True)

    city: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)

    base_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    base_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    max_concurrent_services: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    current_active_services: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    average_rating: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    owner_user = relationship("User", lazy="selectin")
    technicians: Mapped[list["Technician"]] = relationship(
        back_populates="provider",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    provider_services: Mapped[list["ProviderService"]] = relationship(
        back_populates="provider",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    @property
    def available_capacity(self) -> int:
        available = self.max_concurrent_services - self.current_active_services
        return max(available, 0)


class Technician(Base):
    __tablename__ = "technicians"
    __table_args__ = (
        UniqueConstraint("provider_id", "phone_number", name="uq_technician_provider_phone"),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(30), nullable=True)

    specialty: Mapped[str | None] = mapped_column(String(120), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    current_latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    current_longitude: Mapped[float | None] = mapped_column(Float, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    provider: Mapped[Provider] = relationship(back_populates="technicians", lazy="selectin")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()
```

### `app/services/providers/repository.py`

- Ruta relativa: `app/services/providers/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import Role, User
from app.services.providers.models import Provider, Technician


class ProvidersRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_role_by_code(self, role_code: str) -> Role | None:
        query: Select[tuple[Role]] = select(Role).where(Role.code == role_code)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_provider(self, provider: Provider) -> Provider:
        self.db.add(provider)
        self.db.commit()
        self.db.refresh(provider)
        return provider

    def save_provider(self, provider: Provider) -> Provider:
        self.db.add(provider)
        self.db.commit()
        self.db.refresh(provider)
        return provider

    def list_providers(self, limit: int = 50, offset: int = 0) -> list[Provider]:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .order_by(Provider.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.id == provider_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_technician(self, technician: Technician) -> Technician:
        self.db.add(technician)
        self.db.commit()
        self.db.refresh(technician)
        return technician

    def save_technician(self, technician: Technician) -> Technician:
        self.db.add(technician)
        self.db.commit()
        self.db.refresh(technician)
        return technician

    def list_technicians_by_provider_id(self, provider_id: str) -> list[Technician]:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.provider_id == provider_id)
            .order_by(Technician.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_technician_by_id(self, technician_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = select(Technician).where(Technician.id == technician_id)
        return self.db.execute(query).scalar_one_or_none()
```

### `app/services/providers/router.py`

- Ruta relativa: `app/services/providers/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.providers.repository import ProvidersRepository
from app.services.providers.schemas import (
    CreateTechnicianRequest,
    ProviderOnboardingRequest,
    UpdateOwnProviderRequest,
    UpdateProviderOperationsRequest,
    UpdateTechnicianRequest,
)
from app.services.providers.service import ProvidersService

router = APIRouter(prefix="/providers", tags=["Providers"])


@router.post("/onboarding")
def onboard_provider(
    payload: ProviderOnboardingRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.onboard_provider(payload)

    return success_response(
        message="Provider and provider admin user created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_providers(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_providers(limit=limit, offset=offset)

    return success_response(
        message="Providers loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{provider_id}")
def get_provider_by_id(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.get_provider_by_id(provider_id)

    return success_response(
        message="Provider loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{provider_id}/operations")
def update_provider_operations(
    provider_id: str,
    payload: UpdateProviderOperationsRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_provider_operations(provider_id, payload)

    return success_response(
        message="Provider operations updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/profile")
def get_my_provider(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.get_my_provider(current_user)

    return success_response(
        message="Own provider profile loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/profile")
def update_my_provider(
    payload: UpdateOwnProviderRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_my_provider(current_user, payload)

    return success_response(
        message="Own provider profile updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/me/technicians")
def list_my_technicians(
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_my_technicians(current_user)

    return success_response(
        message="Own provider technicians loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/me/technicians")
def create_my_technician(
    payload: CreateTechnicianRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.create_my_technician(current_user, payload)

    return success_response(
        message="Technician created successfully for own provider.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/technicians/{technician_id}")
def update_my_technician(
    technician_id: str,
    payload: UpdateTechnicianRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_my_technician(current_user, technician_id, payload)

    return success_response(
        message="Technician updated successfully for own provider.",
        data=result.model_dump(mode="json"),
    )


@router.get("/{provider_id}/technicians")
def list_provider_technicians(
    provider_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.list_provider_technicians(provider_id)

    return success_response(
        message="Provider technicians loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.post("/{provider_id}/technicians")
def create_provider_technician(
    provider_id: str,
    payload: CreateTechnicianRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.create_provider_technician(provider_id, payload)

    return success_response(
        message="Technician created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{provider_id}/technicians/{technician_id}")
def update_provider_technician(
    provider_id: str,
    technician_id: str,
    payload: UpdateTechnicianRequest,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = ProvidersService(ProvidersRepository(db))
    result = service.update_provider_technician(provider_id, technician_id, payload)

    return success_response(
        message="Technician updated successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/providers/schemas.py`

- Ruta relativa: `app/services/providers/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ProviderOwnerResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool


class ProviderConfiguredServiceSummaryResponse(BaseModel):
    id: str
    service_catalog_item_id: str
    code: str
    category: str
    title: str
    price_estimate_min: float | None = None
    price_estimate_max: float | None = None
    estimated_duration_minutes: int | None = None
    is_mobile_service_enabled: bool
    is_emergency_service_enabled: bool
    is_active: bool


class TechnicianResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool
    current_latitude: float | None = None
    current_longitude: float | None = None
    created_at: datetime
    updated_at: datetime


class ProviderResponse(BaseModel):
    id: str
    owner_user_id: str
    provider_type: str
    business_name: str
    legal_name: str | None = None
    description: str | None = None
    contact_email: str | None = None
    contact_phone: str | None = None
    city: str | None = None
    address: str | None = None
    base_latitude: float | None = None
    base_longitude: float | None = None
    is_active: bool
    is_available: bool
    max_concurrent_services: int
    current_active_services: int
    available_capacity: int
    average_rating: float
    owner_user: ProviderOwnerResponse
    technicians_count: int
    available_technicians_count: int
    configured_services_count: int
    active_services_count: int
    active_services: list[ProviderConfiguredServiceSummaryResponse]
    created_at: datetime
    updated_at: datetime


class CreateProviderAdminUserRequest(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)


class CreateProviderProfileRequest(BaseModel):
    provider_type: Literal["INDEPENDENT_MECHANIC", "WORKSHOP"]
    business_name: str = Field(min_length=2, max_length=150)
    legal_name: str | None = Field(default=None, max_length=180)
    description: str | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=30)
    city: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=255)
    base_latitude: float | None = None
    base_longitude: float | None = None
    max_concurrent_services: int = Field(default=1, ge=1, le=100)


class ProviderOnboardingRequest(BaseModel):
    admin_user: CreateProviderAdminUserRequest
    provider: CreateProviderProfileRequest


class UpdateOwnProviderRequest(BaseModel):
    business_name: str | None = Field(default=None, min_length=2, max_length=150)
    legal_name: str | None = Field(default=None, max_length=180)
    description: str | None = None
    contact_email: str | None = Field(default=None, max_length=255)
    contact_phone: str | None = Field(default=None, max_length=30)
    city: str | None = Field(default=None, max_length=100)
    address: str | None = Field(default=None, max_length=255)
    base_latitude: float | None = None
    base_longitude: float | None = None
    is_available: bool | None = None
    max_concurrent_services: int | None = Field(default=None, ge=1, le=100)


class UpdateProviderOperationsRequest(BaseModel):
    is_active: bool | None = None
    is_available: bool | None = None
    max_concurrent_services: int | None = Field(default=None, ge=1, le=100)
    current_active_services: int | None = Field(default=None, ge=0, le=100)


class CreateTechnicianRequest(BaseModel):
    first_name: str = Field(min_length=2, max_length=120)
    last_name: str = Field(min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    specialty: str | None = Field(default=None, max_length=120)
    is_available: bool = True
    current_latitude: float | None = None
    current_longitude: float | None = None


class UpdateTechnicianRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=2, max_length=120)
    last_name: str | None = Field(default=None, min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
    specialty: str | None = Field(default=None, max_length=120)
    is_active: bool | None = None
    is_available: bool | None = None
    current_latitude: float | None = None
    current_longitude: float | None = None
```

### `app/services/providers/service.py`

- Ruta relativa: `app/services/providers/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.constants import (
    PROVIDER_TYPE_INDEPENDENT_MECHANIC,
    PROVIDER_TYPE_WORKSHOP,
    ROLE_PROVIDER_ADMIN,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.core.security import hash_password
from app.services.auth.models import User
from app.services.providers.models import Provider, Technician
from app.services.providers.repository import ProvidersRepository
from app.services.providers.schemas import (
    CreateTechnicianRequest,
    ProviderConfiguredServiceSummaryResponse,
    ProviderOnboardingRequest,
    ProviderOwnerResponse,
    ProviderResponse,
    TechnicianResponse,
    UpdateOwnProviderRequest,
    UpdateProviderOperationsRequest,
    UpdateTechnicianRequest,
)


class ProvidersService:
    def __init__(self, repository: ProvidersRepository) -> None:
        self.repository = repository

    def onboard_provider(self, payload: ProviderOnboardingRequest) -> ProviderResponse:
        normalized_email = payload.admin_user.email.strip().lower()

        existing_user = self.repository.get_user_by_email(normalized_email)
        if existing_user is not None:
            raise ConflictException("A user with this email already exists.")

        provider_admin_role = self.repository.get_role_by_code(ROLE_PROVIDER_ADMIN)
        if provider_admin_role is None:
            raise NotFoundException("PROVIDER_ADMIN role was not found.")

        provider_type = payload.provider.provider_type.strip().upper()
        if provider_type not in (
            PROVIDER_TYPE_INDEPENDENT_MECHANIC,
            PROVIDER_TYPE_WORKSHOP,
        ):
            raise ConflictException("Invalid provider type.")

        new_owner_user = User(
            email=normalized_email,
            password_hash=hash_password(payload.admin_user.password),
            first_name=payload.admin_user.first_name.strip(),
            last_name=payload.admin_user.last_name.strip(),
            phone_number=payload.admin_user.phone_number.strip() if payload.admin_user.phone_number else None,
            is_active=True,
            is_superuser=False,
            roles=[provider_admin_role],
        )

        created_owner_user = self.repository.create_user(new_owner_user)

        new_provider = Provider(
            owner_user_id=created_owner_user.id,
            provider_type=provider_type,
            business_name=payload.provider.business_name.strip(),
            legal_name=payload.provider.legal_name.strip() if payload.provider.legal_name else None,
            description=payload.provider.description.strip() if payload.provider.description else None,
            contact_email=payload.provider.contact_email.strip().lower() if payload.provider.contact_email else None,
            contact_phone=payload.provider.contact_phone.strip() if payload.provider.contact_phone else None,
            city=payload.provider.city.strip() if payload.provider.city else None,
            address=payload.provider.address.strip() if payload.provider.address else None,
            base_latitude=payload.provider.base_latitude,
            base_longitude=payload.provider.base_longitude,
            is_active=True,
            is_available=True,
            max_concurrent_services=payload.provider.max_concurrent_services,
            current_active_services=0,
            average_rating=0.0,
        )

        created_provider = self.repository.create_provider(new_provider)
        return self._build_provider_response(created_provider)

    def list_providers(self, limit: int = 50, offset: int = 0) -> list[ProviderResponse]:
        providers = self.repository.list_providers(limit=limit, offset=offset)
        return [self._build_provider_response(provider) for provider in providers]

    def get_provider_by_id(self, provider_id: str) -> ProviderResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        return self._build_provider_response(provider)

    def get_my_provider(self, current_user: User) -> ProviderResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        return self._build_provider_response(provider)

    def update_my_provider(self, current_user: User, payload: UpdateOwnProviderRequest) -> ProviderResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        if payload.business_name is not None:
            provider.business_name = payload.business_name.strip()

        if payload.legal_name is not None:
            cleaned_value = payload.legal_name.strip()
            provider.legal_name = cleaned_value or None

        if payload.description is not None:
            cleaned_value = payload.description.strip()
            provider.description = cleaned_value or None

        if payload.contact_email is not None:
            cleaned_value = payload.contact_email.strip().lower()
            provider.contact_email = cleaned_value or None

        if payload.contact_phone is not None:
            cleaned_value = payload.contact_phone.strip()
            provider.contact_phone = cleaned_value or None

        if payload.city is not None:
            cleaned_value = payload.city.strip()
            provider.city = cleaned_value or None

        if payload.address is not None:
            cleaned_value = payload.address.strip()
            provider.address = cleaned_value or None

        if payload.base_latitude is not None:
            provider.base_latitude = payload.base_latitude

        if payload.base_longitude is not None:
            provider.base_longitude = payload.base_longitude

        if payload.is_available is not None:
            provider.is_available = payload.is_available

        if payload.max_concurrent_services is not None:
            provider.max_concurrent_services = payload.max_concurrent_services

        if provider.current_active_services > provider.max_concurrent_services:
            raise ConflictException(
                "Current active services cannot be greater than max concurrent services."
            )

        updated_provider = self.repository.save_provider(provider)
        return self._build_provider_response(updated_provider)

    def update_provider_operations(
        self,
        provider_id: str,
        payload: UpdateProviderOperationsRequest,
    ) -> ProviderResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        if payload.is_active is not None:
            provider.is_active = payload.is_active

        if payload.is_available is not None:
            provider.is_available = payload.is_available

        if payload.max_concurrent_services is not None:
            provider.max_concurrent_services = payload.max_concurrent_services

        if payload.current_active_services is not None:
            provider.current_active_services = payload.current_active_services

        if provider.current_active_services > provider.max_concurrent_services:
            raise ConflictException(
                "Current active services cannot be greater than max concurrent services."
            )

        updated_provider = self.repository.save_provider(provider)
        return self._build_provider_response(updated_provider)

    def list_my_technicians(self, current_user: User) -> list[TechnicianResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        technicians = self.repository.list_technicians_by_provider_id(str(provider.id))
        return [self._build_technician_response(item) for item in technicians]

    def list_provider_technicians(self, provider_id: str) -> list[TechnicianResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        technicians = self.repository.list_technicians_by_provider_id(provider_id)
        return [self._build_technician_response(item) for item in technicians]

    def create_my_technician(
        self,
        current_user: User,
        payload: CreateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        new_technician = Technician(
            provider_id=provider.id,
            first_name=payload.first_name.strip(),
            last_name=payload.last_name.strip(),
            phone_number=payload.phone_number.strip() if payload.phone_number else None,
            specialty=payload.specialty.strip() if payload.specialty else None,
            is_active=True,
            is_available=payload.is_available,
            current_latitude=payload.current_latitude,
            current_longitude=payload.current_longitude,
        )

        created_technician = self.repository.create_technician(new_technician)
        return self._build_technician_response(created_technician)

    def create_provider_technician(
        self,
        provider_id: str,
        payload: CreateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        new_technician = Technician(
            provider_id=provider.id,
            first_name=payload.first_name.strip(),
            last_name=payload.last_name.strip(),
            phone_number=payload.phone_number.strip() if payload.phone_number else None,
            specialty=payload.specialty.strip() if payload.specialty else None,
            is_active=True,
            is_available=payload.is_available,
            current_latitude=payload.current_latitude,
            current_longitude=payload.current_longitude,
        )

        created_technician = self.repository.create_technician(new_technician)
        return self._build_technician_response(created_technician)

    def update_my_technician(
        self,
        current_user: User,
        technician_id: str,
        payload: UpdateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        technician = self.repository.get_technician_by_id(technician_id)
        if technician is None:
            raise NotFoundException("Technician not found.")

        if str(technician.provider_id) != str(provider.id):
            raise ForbiddenException("This technician does not belong to your provider.")

        updated_technician = self._apply_technician_changes(technician, payload)
        saved_technician = self.repository.save_technician(updated_technician)
        return self._build_technician_response(saved_technician)

    def update_provider_technician(
        self,
        provider_id: str,
        technician_id: str,
        payload: UpdateTechnicianRequest,
    ) -> TechnicianResponse:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        technician = self.repository.get_technician_by_id(technician_id)
        if technician is None:
            raise NotFoundException("Technician not found.")

        if str(technician.provider_id) != str(provider.id):
            raise ConflictException("Technician does not belong to the selected provider.")

        updated_technician = self._apply_technician_changes(technician, payload)
        saved_technician = self.repository.save_technician(updated_technician)
        return self._build_technician_response(saved_technician)

    def _apply_technician_changes(
        self,
        technician: Technician,
        payload: UpdateTechnicianRequest,
    ) -> Technician:
        if payload.first_name is not None:
            technician.first_name = payload.first_name.strip()

        if payload.last_name is not None:
            technician.last_name = payload.last_name.strip()

        if payload.phone_number is not None:
            cleaned_value = payload.phone_number.strip()
            technician.phone_number = cleaned_value or None

        if payload.specialty is not None:
            cleaned_value = payload.specialty.strip()
            technician.specialty = cleaned_value or None

        if payload.is_active is not None:
            technician.is_active = payload.is_active

        if payload.is_available is not None:
            technician.is_available = payload.is_available

        if payload.current_latitude is not None:
            technician.current_latitude = payload.current_latitude

        if payload.current_longitude is not None:
            technician.current_longitude = payload.current_longitude

        return technician

    def _build_provider_response(self, provider: Provider) -> ProviderResponse:
        owner_user = provider.owner_user

        technicians = list(provider.technicians)
        available_technicians_count = sum(
            1 for technician in technicians if technician.is_available and technician.is_active
        )

        active_provider_services = []
        for provider_service in provider.provider_services:
            catalog_item = provider_service.service_catalog_item
            if not provider_service.is_active:
                continue
            if catalog_item is None or not catalog_item.is_active:
                continue

            price_estimate_min = (
                float(provider_service.price_estimate_min)
                if provider_service.price_estimate_min is not None
                else None
            )
            price_estimate_max = (
                float(provider_service.price_estimate_max)
                if provider_service.price_estimate_max is not None
                else None
            )

            active_provider_services.append(
                ProviderConfiguredServiceSummaryResponse(
                    id=str(provider_service.id),
                    service_catalog_item_id=str(provider_service.service_catalog_item_id),
                    code=catalog_item.code,
                    category=catalog_item.category,
                    title=provider_service.effective_title,
                    price_estimate_min=price_estimate_min,
                    price_estimate_max=price_estimate_max,
                    estimated_duration_minutes=provider_service.estimated_duration_minutes,
                    is_mobile_service_enabled=provider_service.is_mobile_service_enabled,
                    is_emergency_service_enabled=provider_service.is_emergency_service_enabled,
                    is_active=provider_service.is_active,
                )
            )

        owner_payload = ProviderOwnerResponse(
            id=str(owner_user.id),
            email=owner_user.email,
            first_name=owner_user.first_name,
            last_name=owner_user.last_name,
            full_name=owner_user.full_name,
            phone_number=owner_user.phone_number,
            is_active=owner_user.is_active,
        )

        return ProviderResponse(
            id=str(provider.id),
            owner_user_id=str(provider.owner_user_id),
            provider_type=provider.provider_type,
            business_name=provider.business_name,
            legal_name=provider.legal_name,
            description=provider.description,
            contact_email=provider.contact_email,
            contact_phone=provider.contact_phone,
            city=provider.city,
            address=provider.address,
            base_latitude=provider.base_latitude,
            base_longitude=provider.base_longitude,
            is_active=provider.is_active,
            is_available=provider.is_available,
            max_concurrent_services=provider.max_concurrent_services,
            current_active_services=provider.current_active_services,
            available_capacity=provider.available_capacity,
            average_rating=provider.average_rating,
            owner_user=owner_payload,
            technicians_count=len(technicians),
            available_technicians_count=available_technicians_count,
            configured_services_count=len(provider.provider_services),
            active_services_count=len(active_provider_services),
            active_services=active_provider_services,
            created_at=provider.created_at,
            updated_at=provider.updated_at,
        )

    def _build_technician_response(self, technician: Technician) -> TechnicianResponse:
        return TechnicianResponse(
            id=str(technician.id),
            provider_id=str(technician.provider_id),
            first_name=technician.first_name,
            last_name=technician.last_name,
            full_name=technician.full_name,
            phone_number=technician.phone_number,
            specialty=technician.specialty,
            is_active=technician.is_active,
            is_available=technician.is_available,
            current_latitude=technician.current_latitude,
            current_longitude=technician.current_longitude,
            created_at=technician.created_at,
            updated_at=technician.updated_at,
        )
```

### `app/services/subscriptions/__init__.py`

- Ruta relativa: `app/services/subscriptions/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/subscriptions/models.py`

- Ruta relativa: `app/services/subscriptions/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ProviderSubscriptionPlan(Base):
    __tablename__ = "provider_subscription_plans"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    code: Mapped[str] = mapped_column(String(60), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    billing_period: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    price_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=False, default="BOB", server_default="BOB")

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    auto_renews: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    provider = relationship("Provider", lazy="selectin")
    coverages = relationship(
        "ProviderSubscriptionPlanCoverage",
        back_populates="plan",
        lazy="selectin",
        cascade="all, delete-orphan",
    )


class ProviderSubscriptionPlanCoverage(Base):
    __tablename__ = "provider_subscription_plan_coverages"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    plan_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plans.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    service_catalog_item_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    incident_category: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)

    coverage_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    coverage_value: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    max_coverage_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    waiting_period_days: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    max_applications_per_subscription: Mapped[int | None] = mapped_column(Integer, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    plan = relationship("ProviderSubscriptionPlan", back_populates="coverages", lazy="selectin")
    service_catalog_item = relationship("ServiceCatalogItem", lazy="selectin")


class ClientPlanSubscription(Base):
    __tablename__ = "client_plan_subscriptions"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    client_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    plan_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plans.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    external_reference: Mapped[str | None] = mapped_column(String(120), nullable=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    client_user = relationship("User", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    plan = relationship("ProviderSubscriptionPlan", lazy="selectin")


class IncidentSubscriptionApplication(Base):
    __tablename__ = "incident_subscription_applications"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    incident_billing_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incident_billings.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    client_plan_subscription_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("client_plan_subscriptions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    plan_coverage_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("provider_subscription_plan_coverages.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    matched_service_catalog_item_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("service_catalog_items.id", ondelete="SET NULL"),
        nullable=True,
    )

    matched_incident_category: Mapped[str | None] = mapped_column(String(50), nullable=True)
    coverage_type: Mapped[str] = mapped_column(String(30), nullable=False)
    coverage_value: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    original_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    coverage_applied_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    client_payable_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    snapshot_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    applied_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    incident_billing = relationship("IncidentBilling", lazy="selectin")
    client_plan_subscription = relationship("ClientPlanSubscription", lazy="selectin")
    plan_coverage = relationship("ProviderSubscriptionPlanCoverage", lazy="selectin")
    matched_service_catalog_item = relationship("ServiceCatalogItem", lazy="selectin")
```

### `app/services/subscriptions/repository.py`

- Ruta relativa: `app/services/subscriptions/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload

from app.services.billing.models import IncidentBilling
from app.services.catalog.models import ServiceCatalogItem
from app.services.incidents.models import Incident
from app.services.providers.models import Provider
from app.services.subscriptions.models import (
    ClientPlanSubscription,
    IncidentSubscriptionApplication,
    ProviderSubscriptionPlan,
    ProviderSubscriptionPlanCoverage,
)


class SubscriptionsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_provider_by_id(self, provider_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
            .where(Provider.id == provider_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(selectinload(Provider.owner_user))
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_provider_plans(self, provider_id: str, include_inactive: bool = False) -> list[ProviderSubscriptionPlan]:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .options(
                selectinload(ProviderSubscriptionPlan.provider).selectinload(Provider.owner_user),
                selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ProviderSubscriptionPlan.provider_id == provider_id)
            .order_by(ProviderSubscriptionPlan.created_at.asc())
        )

        if not include_inactive:
            query = query.where(ProviderSubscriptionPlan.is_active.is_(True))

        return list(self.db.execute(query).scalars().all())

    def get_plan_by_id(self, plan_id: str) -> ProviderSubscriptionPlan | None:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .options(
                selectinload(ProviderSubscriptionPlan.provider).selectinload(Provider.owner_user),
                selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ProviderSubscriptionPlan.id == plan_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_by_id_for_update(self, plan_id: str) -> ProviderSubscriptionPlan | None:
        query: Select[tuple[ProviderSubscriptionPlan]] = (
            select(ProviderSubscriptionPlan)
            .where(ProviderSubscriptionPlan.id == plan_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_service_catalog_item_by_id(self, service_catalog_item_id: str) -> ServiceCatalogItem | None:
        query: Select[tuple[ServiceCatalogItem]] = (
            select(ServiceCatalogItem).where(ServiceCatalogItem.id == service_catalog_item_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_coverage_by_id(self, coverage_id: str) -> ProviderSubscriptionPlanCoverage | None:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .options(
                selectinload(ProviderSubscriptionPlanCoverage.plan).selectinload(
                    ProviderSubscriptionPlan.provider
                ),
                selectinload(ProviderSubscriptionPlanCoverage.service_catalog_item),
            )
            .where(ProviderSubscriptionPlanCoverage.id == coverage_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_plan_coverage_by_id_for_update(self, coverage_id: str) -> ProviderSubscriptionPlanCoverage | None:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .where(ProviderSubscriptionPlanCoverage.id == coverage_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_plan_coverages(self, plan_id: str) -> list[ProviderSubscriptionPlanCoverage]:
        query: Select[tuple[ProviderSubscriptionPlanCoverage]] = (
            select(ProviderSubscriptionPlanCoverage)
            .options(selectinload(ProviderSubscriptionPlanCoverage.service_catalog_item))
            .where(ProviderSubscriptionPlanCoverage.plan_id == plan_id)
            .order_by(ProviderSubscriptionPlanCoverage.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_available_provider_plans_for_client(self, provider_id: str) -> list[ProviderSubscriptionPlan]:
        return self.list_provider_plans(provider_id=provider_id, include_inactive=False)

    def list_client_subscriptions(self, client_user_id: str) -> list[ClientPlanSubscription]:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .options(
                selectinload(ClientPlanSubscription.provider).selectinload(Provider.owner_user),
                selectinload(ClientPlanSubscription.plan).selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(ClientPlanSubscription.client_user_id == client_user_id)
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_active_subscription_for_client_and_plan(
        self,
        client_user_id: str,
        plan_id: str,
    ) -> ClientPlanSubscription | None:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .where(
                ClientPlanSubscription.client_user_id == client_user_id,
                ClientPlanSubscription.plan_id == plan_id,
                ClientPlanSubscription.status == "ACTIVE",
            )
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_active_subscriptions_for_client_and_provider(
        self,
        client_user_id: str,
        provider_id: str,
    ) -> list[ClientPlanSubscription]:
        query: Select[tuple[ClientPlanSubscription]] = (
            select(ClientPlanSubscription)
            .options(
                selectinload(ClientPlanSubscription.plan).selectinload(ProviderSubscriptionPlan.coverages).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
                selectinload(ClientPlanSubscription.provider).selectinload(Provider.owner_user),
            )
            .where(
                ClientPlanSubscription.client_user_id == client_user_id,
                ClientPlanSubscription.provider_id == provider_id,
                ClientPlanSubscription.status == "ACTIVE",
            )
            .order_by(ClientPlanSubscription.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.vehicle),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_billing_by_incident_id(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling).where(IncidentBilling.incident_id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_billing_by_incident_id_for_update(self, incident_id: str) -> IncidentBilling | None:
        query: Select[tuple[IncidentBilling]] = (
            select(IncidentBilling)
            .where(IncidentBilling.incident_id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_incident_applications(self, incident_id: str) -> list[IncidentSubscriptionApplication]:
        query: Select[tuple[IncidentSubscriptionApplication]] = (
            select(IncidentSubscriptionApplication)
            .options(
                selectinload(IncidentSubscriptionApplication.client_plan_subscription).selectinload(
                    ClientPlanSubscription.plan
                ),
                selectinload(IncidentSubscriptionApplication.plan_coverage).selectinload(
                    ProviderSubscriptionPlanCoverage.service_catalog_item
                ),
            )
            .where(IncidentSubscriptionApplication.incident_id == incident_id)
            .order_by(IncidentSubscriptionApplication.applied_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def list_incident_applications_for_update(self, incident_id: str) -> list[IncidentSubscriptionApplication]:
        query: Select[tuple[IncidentSubscriptionApplication]] = (
            select(IncidentSubscriptionApplication)
            .where(
                IncidentSubscriptionApplication.incident_id == incident_id,
                IncidentSubscriptionApplication.status == "APPLIED",
            )
            .with_for_update()
        )
        return list(self.db.execute(query).scalars().all())

    def count_applied_coverage_usages(
        self,
        subscription_id: str,
        coverage_id: str,
    ) -> int:
        query = (
            select(func.count(IncidentSubscriptionApplication.id))
            .where(
                IncidentSubscriptionApplication.client_plan_subscription_id == subscription_id,
                IncidentSubscriptionApplication.plan_coverage_id == coverage_id,
                IncidentSubscriptionApplication.status == "APPLIED",
            )
        )
        return int(self.db.execute(query).scalar_one() or 0)

    def save(self, entity) -> None:
        self.db.add(entity)

    def flush(self) -> None:
        self.db.flush()

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/subscriptions/router.py`

- Ruta relativa: `app/services/subscriptions/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.subscriptions.repository import SubscriptionsRepository
from app.services.subscriptions.schemas import (
    ClientSubscribeToPlanRequest,
    ProviderPlanCoverageUpsertRequest,
    ProviderPlanUpsertRequest,
)
from app.services.subscriptions.service import SubscriptionsService

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


@router.get("/provider/me/plans")
def list_my_provider_plans(
    include_inactive: bool = Query(default=False),
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_my_provider_plans(current_user, include_inactive=include_inactive)

    return success_response(
        message="Provider subscription plans loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result), "include_inactive": include_inactive},
    )


@router.post("/provider/me/plans")
def create_my_provider_plan(
    payload: ProviderPlanUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.create_my_provider_plan(current_user, payload)

    return success_response(
        message="Provider subscription plan created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.put("/provider/me/plans/{plan_id}")
def update_my_provider_plan(
    plan_id: str,
    payload: ProviderPlanUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.update_my_provider_plan(current_user, plan_id, payload)

    return success_response(
        message="Provider subscription plan updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/me/plans/{plan_id}/coverages")
def upsert_my_provider_plan_coverage(
    plan_id: str,
    payload: ProviderPlanCoverageUpsertRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.upsert_my_provider_plan_coverage(current_user, plan_id, payload)

    return success_response(
        message="Provider plan coverage configured successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/providers/{provider_id}/plans")
def list_provider_plans_for_client(
    provider_id: str,
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_provider_plans_for_client(provider_id)

    return success_response(
        message="Provider available plans loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.post("/client/plans/{plan_id}/subscribe")
def subscribe_client_to_plan(
    plan_id: str,
    payload: ClientSubscribeToPlanRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.subscribe_client_to_plan(current_user, plan_id, payload)

    return success_response(
        message="Client subscribed to plan successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/me/subscriptions")
def list_my_client_subscriptions(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_my_client_subscriptions(current_user)

    return success_response(
        message="Client subscriptions loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/client/incidents/{incident_id}/coverage-preview")
def preview_applicable_coverage_for_incident(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.preview_applicable_coverage_for_incident(current_user, incident_id)

    return success_response(
        message="Applicable incident coverage preview loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/client/incidents/{incident_id}/apply-coverage")
def apply_best_coverage_for_incident(
    incident_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.apply_best_coverage_for_incident(current_user, incident_id)

    return success_response(
        message="Incident subscription coverage applied successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/applications")
def list_platform_incident_subscription_applications(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SubscriptionsService(SubscriptionsRepository(db))
    result = service.list_platform_incident_subscription_applications(incident_id)

    return success_response(
        message="Incident subscription applications loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
```

### `app/services/subscriptions/schemas.py`

- Ruta relativa: `app/services/subscriptions/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from pydantic import BaseModel, Field


class ProviderPlanUpsertRequest(BaseModel):
    code: str = Field(min_length=2, max_length=60)
    name: str = Field(min_length=2, max_length=150)
    description: str | None = Field(default=None, max_length=2000)
    billing_period: str
    price_amount: float = Field(gt=0)
    currency_code: str = Field(default="BOB", min_length=3, max_length=10)
    is_active: bool = True
    auto_renews: bool = False


class ProviderPlanCoverageUpsertRequest(BaseModel):
    coverage_id: str | None = None
    service_catalog_item_id: str | None = None
    incident_category: str | None = None
    coverage_type: str
    coverage_value: float = Field(gt=0)
    max_coverage_amount: float | None = Field(default=None, gt=0)
    waiting_period_days: int = Field(default=0, ge=0)
    max_applications_per_subscription: int | None = Field(default=None, ge=1)
    is_active: bool = True


class ClientSubscribeToPlanRequest(BaseModel):
    external_reference: str | None = Field(default=None, max_length=120)
    note: str | None = Field(default=None, max_length=1000)


class SubscriptionUserSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class SubscriptionProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    owner_user: SubscriptionUserSummaryResponse | None = None


class ProviderPlanCoverageResponse(BaseModel):
    id: str
    plan_id: str
    service_catalog_item_id: str | None = None
    service_catalog_item_code: str | None = None
    service_catalog_item_title: str | None = None
    incident_category: str | None = None
    coverage_type: str
    coverage_value: float
    max_coverage_amount: float | None = None
    waiting_period_days: int
    max_applications_per_subscription: int | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class ProviderPlanResponse(BaseModel):
    id: str
    provider_id: str
    code: str
    name: str
    description: str | None = None
    billing_period: str
    price_amount: float
    currency_code: str
    is_active: bool
    auto_renews: bool
    created_at: datetime
    updated_at: datetime
    provider: SubscriptionProviderSummaryResponse | None = None
    coverages: list[ProviderPlanCoverageResponse]


class ClientPlanSubscriptionResponse(BaseModel):
    id: str
    client_user_id: str
    provider_id: str
    plan_id: str
    status: str
    started_at: datetime
    expires_at: datetime
    cancelled_at: datetime | None = None
    external_reference: str | None = None
    note: str | None = None
    created_at: datetime
    updated_at: datetime
    provider: SubscriptionProviderSummaryResponse | None = None
    plan: ProviderPlanResponse


class IncidentCoveragePreviewResponse(BaseModel):
    incident_id: str
    billing_amount_basis: float
    matched_incident_category: str
    has_applicable_coverage: bool
    client_plan_subscription_id: str | None = None
    plan_id: str | None = None
    plan_name: str | None = None
    plan_coverage_id: str | None = None
    coverage_type: str | None = None
    coverage_value: float | None = None
    coverage_applied_amount: float | None = None
    client_payable_amount: float | None = None
    rationale: dict | None = None


class IncidentSubscriptionApplicationResponse(BaseModel):
    id: str
    incident_id: str
    incident_billing_id: str | None = None
    client_plan_subscription_id: str
    plan_coverage_id: str
    matched_service_catalog_item_id: str | None = None
    matched_incident_category: str | None = None
    coverage_type: str
    coverage_value: float
    original_amount: float
    coverage_applied_amount: float
    client_payable_amount: float
    status: str
    snapshot_json: dict | None = None
    applied_at: datetime
    updated_at: datetime
```

### `app/services/subscriptions/service.py`

- Ruta relativa: `app/services/subscriptions/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP

from app.common.constants import (
    DEFAULT_CURRENCY_CODE,
    INCIDENT_STATUS_CANCELLED,
    PLAN_BILLING_PERIOD_ANNUAL,
    PLAN_BILLING_PERIOD_MONTHLY,
    PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
    PLAN_COVERAGE_TYPE_FULL,
    PLAN_COVERAGE_TYPE_PERCENTAGE,
    SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
    SUBSCRIPTION_APPLICATION_STATUS_VOIDED,
    SUBSCRIPTION_STATUS_ACTIVE,
    SUBSCRIPTION_STATUS_CANCELLED,
    AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
    AUDIT_EVENT_COVERAGE_APPLIED,
    AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,

)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.subscriptions.models import (
    ClientPlanSubscription,
    IncidentSubscriptionApplication,
    ProviderSubscriptionPlan,
    ProviderSubscriptionPlanCoverage,
)
from app.services.subscriptions.repository import SubscriptionsRepository
from app.services.subscriptions.schemas import (
    ClientPlanSubscriptionResponse,
    ClientSubscribeToPlanRequest,
    IncidentCoveragePreviewResponse,
    IncidentSubscriptionApplicationResponse,
    ProviderPlanCoverageResponse,
    ProviderPlanCoverageUpsertRequest,
    ProviderPlanResponse,
    ProviderPlanUpsertRequest,
    SubscriptionProviderSummaryResponse,
    SubscriptionUserSummaryResponse,
)
from app.services.audit.dispatcher import AuditEventDispatcher

MONEY_QUANTIZER = Decimal("0.01")


class SubscriptionsService:
    def __init__(self, repository: SubscriptionsRepository) -> None:
        self.repository = repository

    # ---------------------------
    # Provider plans
    # ---------------------------

    def list_my_provider_plans(
        self,
        current_user: User,
        include_inactive: bool = False,
    ) -> list[ProviderPlanResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        plans = self.repository.list_provider_plans(str(provider.id), include_inactive=include_inactive)
        return [self._build_plan_response(item) for item in plans]

    def create_my_provider_plan(
        self,
        current_user: User,
        payload: ProviderPlanUpsertRequest,
    ) -> ProviderPlanResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        billing_period = payload.billing_period.strip().upper()
        if billing_period not in (PLAN_BILLING_PERIOD_MONTHLY, PLAN_BILLING_PERIOD_ANNUAL):
            raise ConflictException("Unsupported billing_period. Use MONTHLY or ANNUAL.")

        plan = ProviderSubscriptionPlan(
            provider_id=provider.id,
            code=payload.code.strip().upper(),
            name=payload.name.strip(),
            description=self._normalize_optional_text(payload.description),
            billing_period=billing_period,
            price_amount=self._to_money_decimal(payload.price_amount),
            currency_code=payload.currency_code.strip().upper() if payload.currency_code else DEFAULT_CURRENCY_CODE,
            is_active=payload.is_active,
            auto_renews=payload.auto_renews,
        )

        try:
            self.repository.save(plan)
            self.repository.commit()
            self.repository.refresh(plan)
        except Exception:
            self.repository.rollback()
            raise

        plan = self.repository.get_plan_by_id(str(plan.id))
        if plan is None:
            raise NotFoundException("Plan not found after creation.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=None,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,
        entity_type="SUBSCRIPTION_PLAN",
        entity_id=str(plan.id),
        payload_json={
            "code": plan.code,
            "billing_period": plan.billing_period,
            "price_amount": float(plan.price_amount),
            "currency_code": plan.currency_code,
            "is_active": plan.is_active,
        },
    )


        return self._build_plan_response(plan)

    def update_my_provider_plan(
        self,
        current_user: User,
        plan_id: str,
        payload: ProviderPlanUpsertRequest,
    ) -> ProviderPlanResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            plan = self.repository.get_plan_by_id_for_update(plan_id)
            if plan is None:
                raise NotFoundException("Provider subscription plan not found.")

            if str(plan.provider_id) != str(provider.id):
                raise ForbiddenException("This plan does not belong to your provider.")

            billing_period = payload.billing_period.strip().upper()
            if billing_period not in (PLAN_BILLING_PERIOD_MONTHLY, PLAN_BILLING_PERIOD_ANNUAL):
                raise ConflictException("Unsupported billing_period. Use MONTHLY or ANNUAL.")

            plan.code = payload.code.strip().upper()
            plan.name = payload.name.strip()
            plan.description = self._normalize_optional_text(payload.description)
            plan.billing_period = billing_period
            plan.price_amount = self._to_money_decimal(payload.price_amount)
            plan.currency_code = payload.currency_code.strip().upper() if payload.currency_code else DEFAULT_CURRENCY_CODE
            plan.is_active = payload.is_active
            plan.auto_renews = payload.auto_renews

            self.repository.save(plan)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        plan = self.repository.get_plan_by_id(plan_id)
        if plan is None:
            raise NotFoundException("Provider subscription plan not found after update.")

        return self._build_plan_response(plan)

    def upsert_my_provider_plan_coverage(
        self,
        current_user: User,
        plan_id: str,
        payload: ProviderPlanCoverageUpsertRequest,
    ) -> ProviderPlanCoverageResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        coverage_type = payload.coverage_type.strip().upper()
        if coverage_type not in (
            PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
            PLAN_COVERAGE_TYPE_PERCENTAGE,
            PLAN_COVERAGE_TYPE_FULL,
        ):
            raise ConflictException("Unsupported coverage_type.")

        if payload.service_catalog_item_id is None and payload.incident_category is None:
            raise ConflictException(
                "At least one matching rule is required: service_catalog_item_id or incident_category."
            )

        service_catalog_item = None
        if payload.service_catalog_item_id is not None:
            service_catalog_item = self.repository.get_service_catalog_item_by_id(payload.service_catalog_item_id)
            if service_catalog_item is None:
                raise NotFoundException("Service catalog item not found.")

        try:
            plan = self.repository.get_plan_by_id_for_update(plan_id)
            if plan is None:
                raise NotFoundException("Provider subscription plan not found.")

            if str(plan.provider_id) != str(provider.id):
                raise ForbiddenException("This plan does not belong to your provider.")

            if payload.coverage_id:
                coverage = self.repository.get_plan_coverage_by_id_for_update(payload.coverage_id)
                if coverage is None:
                    raise NotFoundException("Plan coverage not found.")
                if str(coverage.plan_id) != str(plan.id):
                    raise ForbiddenException("This coverage rule does not belong to the selected plan.")
            else:
                coverage = ProviderSubscriptionPlanCoverage(
                    plan_id=plan.id,
                    service_catalog_item_id=None,
                    incident_category=None,
                    coverage_type=coverage_type,
                    coverage_value=self._to_money_decimal(payload.coverage_value),
                    max_coverage_amount=None,
                    waiting_period_days=payload.waiting_period_days,
                    max_applications_per_subscription=payload.max_applications_per_subscription,
                    is_active=payload.is_active,
                )

            coverage.service_catalog_item_id = payload.service_catalog_item_id
            coverage.incident_category = (
                payload.incident_category.strip().upper() if payload.incident_category else None
            )
            coverage.coverage_type = coverage_type
            coverage.coverage_value = self._to_money_decimal(payload.coverage_value)
            coverage.max_coverage_amount = (
                self._to_money_decimal(payload.max_coverage_amount)
                if payload.max_coverage_amount is not None
                else None
            )
            coverage.waiting_period_days = payload.waiting_period_days
            coverage.max_applications_per_subscription = payload.max_applications_per_subscription
            coverage.is_active = payload.is_active

            self.repository.save(coverage)
            self.repository.commit()
            self.repository.refresh(coverage)
        except Exception:
            self.repository.rollback()
            raise

        coverage = self.repository.get_plan_coverage_by_id(str(coverage.id))
        if coverage is None:
            raise NotFoundException("Plan coverage not found after upsert.")

        return self._build_coverage_response(coverage)

    def list_provider_plans_for_client(self, provider_id: str) -> list[ProviderPlanResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        plans = self.repository.list_available_provider_plans_for_client(provider_id)
        return [self._build_plan_response(item) for item in plans]

    # ---------------------------
    # Client subscriptions
    # ---------------------------

    def subscribe_client_to_plan(
        self,
        current_user: User,
        plan_id: str,
        payload: ClientSubscribeToPlanRequest,
    ) -> ClientPlanSubscriptionResponse:
        plan = self.repository.get_plan_by_id(plan_id)
        if plan is None:
            raise NotFoundException("Provider subscription plan not found.")

        if not plan.is_active:
            raise ConflictException("This plan is not currently active.")

        existing_subscription = self.repository.get_active_subscription_for_client_and_plan(
            client_user_id=str(current_user.id),
            plan_id=plan_id,
        )
        if existing_subscription is not None and existing_subscription.expires_at > datetime.now(timezone.utc):
            raise ConflictException("The client already has an active subscription for this plan.")

        started_at = datetime.now(timezone.utc)
        expires_at = self._calculate_expiration(
            started_at=started_at,
            billing_period=plan.billing_period,
        )

        subscription = ClientPlanSubscription(
            client_user_id=current_user.id,
            provider_id=plan.provider_id,
            plan_id=plan.id,
            status=SUBSCRIPTION_STATUS_ACTIVE,
            started_at=started_at,
            expires_at=expires_at,
            cancelled_at=None,
            external_reference=self._normalize_optional_text(payload.external_reference),
            note=self._normalize_optional_text(payload.note),
        )

        try:
            self.repository.save(subscription)
            self.repository.commit()
            self.repository.refresh(subscription)
        except Exception:
            self.repository.rollback()
            raise

        subscriptions = self.repository.list_client_subscriptions(str(current_user.id))
        created = next((item for item in subscriptions if str(item.id) == str(subscription.id)), None)
        if created is None:
            raise NotFoundException("Subscription not found after creation.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=None,
        provider_id=str(plan.provider_id),
        event_type=AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
        entity_type="CLIENT_PLAN_SUBSCRIPTION",
        entity_id=str(subscription.id),
        payload_json={
            "plan_id": str(plan.id),
            "started_at": subscription.started_at.isoformat(),
            "expires_at": subscription.expires_at.isoformat(),
            "status": subscription.status,
        },
    )


        return self._build_client_subscription_response(created)

    def list_my_client_subscriptions(self, current_user: User) -> list[ClientPlanSubscriptionResponse]:
        subscriptions = self.repository.list_client_subscriptions(str(current_user.id))

        now = datetime.now(timezone.utc)
        updated_any = False

        for item in subscriptions:
            if item.status == SUBSCRIPTION_STATUS_ACTIVE and item.expires_at <= now:
                item.status = "EXPIRED"
                self.repository.save(item)
                updated_any = True

        if updated_any:
            self.repository.commit()
            subscriptions = self.repository.list_client_subscriptions(str(current_user.id))

        return [self._build_client_subscription_response(item) for item in subscriptions]

    # ---------------------------
    # Coverage preview / apply
    # ---------------------------

    def preview_applicable_coverage_for_incident(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentCoveragePreviewResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        if incident.provider_id is None:
            raise ConflictException("This incident does not yet have an assigned provider.")

        if incident.status == INCIDENT_STATUS_CANCELLED:
            raise ConflictException("Cancelled incidents cannot use subscription coverage.")

        billing = self.repository.get_incident_billing_by_incident_id(incident_id)
        if billing is None:
            raise ConflictException("This incident does not yet have billing information.")

        amount_basis = self._resolve_billing_amount_basis(billing)
        used_category = self._resolve_incident_category(incident)

        active_subscriptions = self.repository.list_active_subscriptions_for_client_and_provider(
            client_user_id=str(current_user.id),
            provider_id=str(incident.provider_id),
        )

        best_option = self._find_best_coverage_option(
            incident=incident,
            billing=billing,
            active_subscriptions=active_subscriptions,
            amount_basis=amount_basis,
            used_category=used_category,
        )

        if best_option is None:
            return IncidentCoveragePreviewResponse(
                incident_id=incident_id,
                billing_amount_basis=float(amount_basis),
                matched_incident_category=used_category,
                has_applicable_coverage=False,
                rationale={
                    "reason": "No active subscription with applicable coverage was found for this incident."
                },
            )

        return IncidentCoveragePreviewResponse(
            incident_id=incident_id,
            billing_amount_basis=float(amount_basis),
            matched_incident_category=used_category,
            has_applicable_coverage=True,
            client_plan_subscription_id=str(best_option["subscription"].id),
            plan_id=str(best_option["plan"].id),
            plan_name=best_option["plan"].name,
            plan_coverage_id=str(best_option["coverage"].id),
            coverage_type=best_option["coverage"].coverage_type,
            coverage_value=float(best_option["coverage"].coverage_value),
            coverage_applied_amount=float(best_option["coverage_applied_amount"]),
            client_payable_amount=float(best_option["client_payable_amount"]),
            rationale=best_option["rationale"],
        )

    def apply_best_coverage_for_incident(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentSubscriptionApplicationResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        if incident.provider_id is None:
            raise ConflictException("This incident does not yet have an assigned provider.")

        if incident.status == INCIDENT_STATUS_CANCELLED:
            raise ConflictException("Cancelled incidents cannot use subscription coverage.")

        try:
            billing = self.repository.get_incident_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not yet have billing information.")

            if billing.final_price_amount is None:
                raise ConflictException(
                    "Coverage can only be applied after the provider finalizes the service price."
                )

            active_subscriptions = self.repository.list_active_subscriptions_for_client_and_provider(
                client_user_id=str(current_user.id),
                provider_id=str(incident.provider_id),
            )

            used_category = self._resolve_incident_category(incident)

            best_option = self._find_best_coverage_option(
                incident=incident,
                billing=billing,
                active_subscriptions=active_subscriptions,
                amount_basis=billing.final_price_amount,
                used_category=used_category,
            )

            if best_option is None:
                raise ConflictException("No applicable subscription coverage was found for this incident.")

            previous_applications = self.repository.list_incident_applications_for_update(incident_id)
            for previous in previous_applications:
                previous.status = SUBSCRIPTION_APPLICATION_STATUS_VOIDED
                self.repository.save(previous)

            application = IncidentSubscriptionApplication(
                incident_id=incident.id,
                incident_billing_id=billing.id,
                client_plan_subscription_id=best_option["subscription"].id,
                plan_coverage_id=best_option["coverage"].id,
                matched_service_catalog_item_id=best_option["matched_service_catalog_item_id"],
                matched_incident_category=used_category,
                coverage_type=best_option["coverage"].coverage_type,
                coverage_value=best_option["coverage"].coverage_value,
                original_amount=billing.final_price_amount,
                coverage_applied_amount=best_option["coverage_applied_amount"],
                client_payable_amount=best_option["client_payable_amount"],
                status=SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
                snapshot_json=best_option["rationale"],
            )

            billing.client_plan_subscription_id = best_option["subscription"].id
            billing.plan_coverage_id = best_option["coverage"].id
            billing.coverage_applied_amount = best_option["coverage_applied_amount"]
            billing.client_payable_amount = best_option["client_payable_amount"]

            self.repository.save(application)
            self.repository.save(billing)
            self.repository.commit()
            self.repository.refresh(application)
        except Exception:
            self.repository.rollback()
            raise

        applications = self.repository.list_incident_applications(incident_id)
        applied = next(
            (
                item
                for item in applications
                if str(item.id) == str(application.id)
            ),
            None,
        )
        if applied is None:
            raise NotFoundException("Incident subscription application not found after apply.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(incident.provider_id),
        event_type=AUDIT_EVENT_COVERAGE_APPLIED,
        entity_type="INCIDENT_SUBSCRIPTION_APPLICATION",
        entity_id=str(application.id),
        payload_json={
            "client_plan_subscription_id": str(application.client_plan_subscription_id),
            "plan_coverage_id": str(application.plan_coverage_id),
            "coverage_applied_amount": float(application.coverage_applied_amount),
            "client_payable_amount": float(application.client_payable_amount),
        },
    )


        return self._build_application_response(applied)

    def list_platform_incident_subscription_applications(
        self,
        incident_id: str,
    ) -> list[IncidentSubscriptionApplicationResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        items = self.repository.list_incident_applications(incident_id)
        return [self._build_application_response(item) for item in items]

    # ---------------------------
    # Internal helpers
    # ---------------------------

    def _find_best_coverage_option(
        self,
        *,
        incident,
        billing,
        active_subscriptions: list[ClientPlanSubscription],
        amount_basis: Decimal,
        used_category: str,
    ) -> dict | None:
        now = datetime.now(timezone.utc)
        best_option = None

        for subscription in active_subscriptions:
            if subscription.status != SUBSCRIPTION_STATUS_ACTIVE:
                continue
            if subscription.expires_at <= now:
                continue

            plan = subscription.plan
            if plan is None or not plan.is_active:
                continue

            for coverage in plan.coverages:
                if not coverage.is_active:
                    continue

                waiting_limit = subscription.started_at + timedelta(days=coverage.waiting_period_days)
                if waiting_limit > now:
                    continue

                current_usage_count = self.repository.count_applied_coverage_usages(
                    subscription_id=str(subscription.id),
                    coverage_id=str(coverage.id),
                )
                if (
                    coverage.max_applications_per_subscription is not None
                    and current_usage_count >= coverage.max_applications_per_subscription
                ):
                    continue

                matched_service_catalog_item_id = None

                if coverage.service_catalog_item is not None:
                    if coverage.service_catalog_item.category != used_category:
                        continue
                    matched_service_catalog_item_id = coverage.service_catalog_item.id
                elif coverage.incident_category is not None:
                    if coverage.incident_category != used_category:
                        continue

                coverage_applied_amount = self._calculate_coverage_amount(
                    amount_basis=amount_basis,
                    coverage=coverage,
                )
                if coverage_applied_amount <= Decimal("0.00"):
                    continue

                client_payable_amount = (amount_basis - coverage_applied_amount).quantize(
                    MONEY_QUANTIZER,
                    rounding=ROUND_HALF_UP,
                )

                candidate = {
                    "subscription": subscription,
                    "plan": plan,
                    "coverage": coverage,
                    "matched_service_catalog_item_id": matched_service_catalog_item_id,
                    "coverage_applied_amount": coverage_applied_amount,
                    "client_payable_amount": client_payable_amount,
                    "rationale": {
                        "used_category": used_category,
                        "matched_rule_scope": (
                            "SERVICE_CATEGORY"
                            if coverage.service_catalog_item_id is not None
                            else "INCIDENT_CATEGORY"
                            if coverage.incident_category is not None
                            else "GLOBAL"
                        ),
                        "waiting_period_days": coverage.waiting_period_days,
                        "current_usage_count": current_usage_count,
                        "max_applications_per_subscription": coverage.max_applications_per_subscription,
                        "amount_basis": float(amount_basis),
                    },
                }

                if best_option is None:
                    best_option = candidate
                    continue

                if candidate["coverage_applied_amount"] > best_option["coverage_applied_amount"]:
                    best_option = candidate

        return best_option

    def _calculate_coverage_amount(
        self,
        *,
        amount_basis: Decimal,
        coverage: ProviderSubscriptionPlanCoverage,
    ) -> Decimal:
        if coverage.coverage_type == PLAN_COVERAGE_TYPE_FULL:
            applied_amount = amount_basis
        elif coverage.coverage_type == PLAN_COVERAGE_TYPE_FIXED_AMOUNT:
            applied_amount = min(amount_basis, coverage.coverage_value)
        elif coverage.coverage_type == PLAN_COVERAGE_TYPE_PERCENTAGE:
            applied_amount = (
                amount_basis * coverage.coverage_value / Decimal("100")
            ).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)
        else:
            raise ConflictException("Unsupported coverage_type.")

        if coverage.max_coverage_amount is not None:
            applied_amount = min(applied_amount, coverage.max_coverage_amount)

        if applied_amount < Decimal("0.00"):
            applied_amount = Decimal("0.00")

        if applied_amount > amount_basis:
            applied_amount = amount_basis

        return applied_amount.quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _resolve_billing_amount_basis(self, billing) -> Decimal:
        if billing.final_price_amount is not None:
            return billing.final_price_amount

        if billing.estimated_price_max is not None:
            return billing.estimated_price_max

        if billing.estimated_price_min is not None:
            return billing.estimated_price_min

        raise ConflictException("This incident still does not have an estimated or final billing amount.")

    def _resolve_incident_category(self, incident) -> str:
        if incident.suggested_category:
            return incident.suggested_category.strip().upper()
        return incident.reported_category.strip().upper()

    def _calculate_expiration(self, *, started_at: datetime, billing_period: str) -> datetime:
        if billing_period == PLAN_BILLING_PERIOD_MONTHLY:
            return started_at + timedelta(days=30)

        if billing_period == PLAN_BILLING_PERIOD_ANNUAL:
            return started_at + timedelta(days=365)

        raise ConflictException("Unsupported billing period.")

    def _build_plan_response(self, plan: ProviderSubscriptionPlan) -> ProviderPlanResponse:
        provider_payload = None
        if plan.provider is not None:
            owner_payload = None
            if plan.provider.owner_user is not None:
                owner = plan.provider.owner_user
                owner_payload = SubscriptionUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = SubscriptionProviderSummaryResponse(
                id=str(plan.provider.id),
                provider_type=plan.provider.provider_type,
                business_name=plan.provider.business_name,
                owner_user=owner_payload,
            )

        return ProviderPlanResponse(
            id=str(plan.id),
            provider_id=str(plan.provider_id),
            code=plan.code,
            name=plan.name,
            description=plan.description,
            billing_period=plan.billing_period,
            price_amount=float(plan.price_amount),
            currency_code=plan.currency_code,
            is_active=plan.is_active,
            auto_renews=plan.auto_renews,
            created_at=plan.created_at,
            updated_at=plan.updated_at,
            provider=provider_payload,
            coverages=[self._build_coverage_response(item) for item in plan.coverages],
        )

    def _build_coverage_response(
        self,
        coverage: ProviderSubscriptionPlanCoverage,
    ) -> ProviderPlanCoverageResponse:
        service_item = coverage.service_catalog_item
        return ProviderPlanCoverageResponse(
            id=str(coverage.id),
            plan_id=str(coverage.plan_id),
            service_catalog_item_id=(
                str(coverage.service_catalog_item_id) if coverage.service_catalog_item_id else None
            ),
            service_catalog_item_code=service_item.code if service_item is not None else None,
            service_catalog_item_title=service_item.title if service_item is not None else None,
            incident_category=coverage.incident_category,
            coverage_type=coverage.coverage_type,
            coverage_value=float(coverage.coverage_value),
            max_coverage_amount=float(coverage.max_coverage_amount) if coverage.max_coverage_amount is not None else None,
            waiting_period_days=coverage.waiting_period_days,
            max_applications_per_subscription=coverage.max_applications_per_subscription,
            is_active=coverage.is_active,
            created_at=coverage.created_at,
            updated_at=coverage.updated_at,
        )

    def _build_client_subscription_response(
        self,
        subscription: ClientPlanSubscription,
    ) -> ClientPlanSubscriptionResponse:
        provider_payload = None
        if subscription.provider is not None:
            owner_payload = None
            if subscription.provider.owner_user is not None:
                owner = subscription.provider.owner_user
                owner_payload = SubscriptionUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = SubscriptionProviderSummaryResponse(
                id=str(subscription.provider.id),
                provider_type=subscription.provider.provider_type,
                business_name=subscription.provider.business_name,
                owner_user=owner_payload,
            )

        return ClientPlanSubscriptionResponse(
            id=str(subscription.id),
            client_user_id=str(subscription.client_user_id),
            provider_id=str(subscription.provider_id),
            plan_id=str(subscription.plan_id),
            status=subscription.status,
            started_at=subscription.started_at,
            expires_at=subscription.expires_at,
            cancelled_at=subscription.cancelled_at,
            external_reference=subscription.external_reference,
            note=subscription.note,
            created_at=subscription.created_at,
            updated_at=subscription.updated_at,
            provider=provider_payload,
            plan=self._build_plan_response(subscription.plan),
        )

    def _build_application_response(
        self,
        application: IncidentSubscriptionApplication,
    ) -> IncidentSubscriptionApplicationResponse:
        return IncidentSubscriptionApplicationResponse(
            id=str(application.id),
            incident_id=str(application.incident_id),
            incident_billing_id=(
                str(application.incident_billing_id) if application.incident_billing_id else None
            ),
            client_plan_subscription_id=str(application.client_plan_subscription_id),
            plan_coverage_id=str(application.plan_coverage_id),
            matched_service_catalog_item_id=(
                str(application.matched_service_catalog_item_id)
                if application.matched_service_catalog_item_id
                else None
            ),
            matched_incident_category=application.matched_incident_category,
            coverage_type=application.coverage_type,
            coverage_value=float(application.coverage_value),
            original_amount=float(application.original_amount),
            coverage_applied_amount=float(application.coverage_applied_amount),
            client_payable_amount=float(application.client_payable_amount),
            status=application.status,
            snapshot_json=application.snapshot_json,
            applied_at=application.applied_at,
            updated_at=application.updated_at,
        )

    def _to_money_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type=entity_type,
                entity_id=entity_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return
```

### `app/services/system/__init__.py`

- Ruta relativa: `app/services/system/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/system/repository.py`

- Ruta relativa: `app/services/system/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.services.audit.models import AuditLog
from app.services.billing.models import IncidentBilling
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery
from app.services.providers.models import Provider, Technician
from app.services.subscriptions.models import ClientPlanSubscription


class SystemRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incidents_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(Incident.status, func.count(Incident.id))
            .group_by(Incident.status)
            .order_by(Incident.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_background_jobs_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(BackgroundJob.status, func.count(BackgroundJob.id))
            .group_by(BackgroundJob.status)
            .order_by(BackgroundJob.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_push_deliveries_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(PushNotificationDelivery.status, func.count(PushNotificationDelivery.id))
            .group_by(PushNotificationDelivery.status)
            .order_by(PushNotificationDelivery.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_provider_summary(self) -> dict:
        total = int(self.db.execute(select(func.count(Provider.id))).scalar_one() or 0)
        active = int(
            self.db.execute(
                select(func.count(Provider.id)).where(Provider.is_active.is_(True))
            ).scalar_one()
            or 0
        )
        available = int(
            self.db.execute(
                select(func.count(Provider.id)).where(
                    Provider.is_active.is_(True),
                    Provider.is_available.is_(True),
                )
            ).scalar_one()
            or 0
        )

        total_capacity = int(
            self.db.execute(select(func.coalesce(func.sum(Provider.max_concurrent_services), 0))).scalar_one() or 0
        )
        active_services = int(
            self.db.execute(select(func.coalesce(func.sum(Provider.current_active_services), 0))).scalar_one() or 0
        )

        return {
            "total": total,
            "active": active,
            "available": available,
            "total_capacity": total_capacity,
            "current_active_services": active_services,
        }

    def get_technician_summary(self) -> dict:
        total = int(self.db.execute(select(func.count(Technician.id))).scalar_one() or 0)
        active = int(
            self.db.execute(
                select(func.count(Technician.id)).where(Technician.is_active.is_(True))
            ).scalar_one()
            or 0
        )
        available = int(
            self.db.execute(
                select(func.count(Technician.id)).where(
                    Technician.is_active.is_(True),
                    Technician.is_available.is_(True),
                )
            ).scalar_one()
            or 0
        )

        return {
            "total": total,
            "active": active,
            "available": available,
        }

    def get_financial_summary(self) -> dict:
        row = self.db.execute(
            select(
                func.coalesce(func.sum(IncidentBilling.final_price_amount), 0),
                func.coalesce(
                    func.sum(
                        func.case(
                            (IncidentBilling.payment_status == "PAID", func.coalesce(IncidentBilling.client_payable_amount, IncidentBilling.final_price_amount)),
                            else_=0,
                        )
                    ),
                    0,
                ),
                func.coalesce(func.sum(IncidentBilling.platform_commission_amount), 0),
                func.coalesce(func.sum(IncidentBilling.provider_net_amount), 0),
                func.coalesce(func.sum(IncidentBilling.client_payable_amount), 0),
            )
        ).one()

        return {
            "total_service_value": float(row[0] or 0),
            "total_paid_value": float(row[1] or 0),
            "total_platform_commission": float(row[2] or 0),
            "total_provider_net_amount": float(row[3] or 0),
            "total_client_payable_amount": float(row[4] or 0),
        }

    def get_subscription_summary(self) -> dict[str, int]:
        rows = self.db.execute(
            select(ClientPlanSubscription.status, func.count(ClientPlanSubscription.id))
            .group_by(ClientPlanSubscription.status)
            .order_by(ClientPlanSubscription.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_audit_events_last_24h_count(self) -> int:
        value = self.db.execute(
            select(func.count(AuditLog.id)).where(
                AuditLog.created_at >= func.now() - func.cast("24 hours", type_=func.interval())
            )
        ).scalar_one()
        return int(value or 0)

    def get_average_assignment_seconds(self) -> float | None:
        value = self.db.execute(
            select(
                func.avg(
                    func.extract("epoch", Incident.assigned_at) - func.extract("epoch", Incident.requested_at)
                )
            ).where(
                Incident.assigned_at.is_not(None),
                Incident.requested_at.is_not(None),
            )
        ).scalar_one()
        return float(value) if value is not None else None

    def get_average_completion_seconds(self) -> float | None:
        value = self.db.execute(
            select(
                func.avg(
                    func.extract("epoch", Incident.completed_at) - func.extract("epoch", Incident.requested_at)
                )
            ).where(
                Incident.completed_at.is_not(None),
                Incident.requested_at.is_not(None),
            )
        ).scalar_one()
        return float(value) if value is not None else None
```

### `app/services/system/router.py`

- Ruta relativa: `app/services/system/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import (
    get_ai_provider,
    get_db_session,
    get_llm_provider,
    get_push_provider,
    get_routing_provider,
    get_speech_to_text_provider,
    get_vision_provider,
)
from app.core.security import require_roles
from app.integrations.ai.base import IncidentAIProvider
from app.integrations.llm.base import IncidentSummaryProvider
from app.integrations.push.base import PushNotificationProvider
from app.integrations.routing.base import RoutingProvider
from app.integrations.speech_to_text.base import SpeechToTextProvider
from app.integrations.vision.base import VisionAnalysisProvider
from app.services.auth.models import User
from app.services.system.service import SystemService

router = APIRouter(prefix="/system", tags=["System"])


@router.get("/health")
def health(db: Session = Depends(get_db_session)) -> dict:
    service = SystemService(db)
    payload = service.build_health_payload()

    return success_response(
        message="API is running correctly.",
        data=payload.model_dump(mode="json"),
    )


@router.get("/readiness")
def readiness(db: Session = Depends(get_db_session)) -> dict:
    service = SystemService(db)
    payload = service.build_readiness_payload()

    return success_response(
        message="API dependencies are ready.",
        data=payload.model_dump(mode="json"),
    )


@router.get("/info")
def info(
    ai_provider: IncidentAIProvider = Depends(get_ai_provider),
    speech_to_text_provider: SpeechToTextProvider = Depends(get_speech_to_text_provider),
    vision_provider: VisionAnalysisProvider = Depends(get_vision_provider),
    llm_provider: IncidentSummaryProvider = Depends(get_llm_provider),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
    push_provider: PushNotificationProvider = Depends(get_push_provider),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SystemService(db)
    payload = service.build_app_info_payload(
        ai_provider_name=ai_provider.provider_name,
        speech_to_text_provider_name=speech_to_text_provider.provider_name,
        vision_provider_name=vision_provider.provider_name,
        llm_provider_name=llm_provider.provider_name,
        routing_provider_name=routing_provider.provider_name,
        push_provider_name=push_provider.provider_name,
    )

    return success_response(
        message="Application information loaded successfully.",
        data=payload.model_dump(mode="json"),
    )


@router.get("/platform/metrics")
def platform_metrics(
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SystemService(db)
    payload = service.get_platform_metrics_overview()

    return success_response(
        message="Platform metrics loaded successfully.",
        data=payload.model_dump(mode="json"),
    )


@router.post("/platform/metrics/snapshot")
def create_metrics_snapshot(
    current_user: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = SystemService(db)
    payload = service.create_metrics_snapshot(str(current_user.id))

    return success_response(
        message="Metrics snapshot created successfully.",
        data=payload,
    )
```

### `app/services/system/schemas.py`

- Ruta relativa: `app/services/system/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel


class HealthPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    status: str
    timestamp: datetime


class ReadinessComponentPayload(BaseModel):
    name: str
    status: str
    detail: str


class ReadinessPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    status: str
    components: list[ReadinessComponentPayload]
    timestamp: datetime


class AppInfoPayload(BaseModel):
    app_name: str
    version: str
    environment: str
    api_prefix: str
    docs_enabled: bool
    docs_url: str | None = None
    ai_provider: str
    storage_provider: str
    speech_to_text_provider: str
    vision_provider: str
    llm_provider: str
    routing_provider: str
    push_provider: str
    trusted_hosts: list[str]
    security_headers_enabled: bool
    https_redirect_enabled: bool
    audit_http_enabled: bool
    timestamp: datetime


class SystemMetricsPayload(BaseModel):
    incidents_by_status: dict[str, int]
    background_jobs_by_status: dict[str, int]
    push_deliveries_by_status: dict[str, int]
    providers: dict
    technicians: dict
    financial: dict
    subscriptions_by_status: dict[str, int]
    average_assignment_seconds: float | None = None
    average_completion_seconds: float | None = None
    audit_events_last_24h: int
    timestamp: datetime
```

### `app/services/system/service.py`

- Ruta relativa: `app/services/system/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone
from pathlib import Path

import redis
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.common.exceptions import ServiceUnavailableException
from app.core.config import settings
from app.services.audit.repository import AuditRepository
from app.services.audit.service import AuditService
from app.services.system.repository import SystemRepository
from app.services.system.schemas import (
    AppInfoPayload,
    HealthPayload,
    ReadinessComponentPayload,
    ReadinessPayload,
    SystemMetricsPayload,
)


class SystemService:
    def __init__(self, db) -> None:
        self.db = db
        self.repository = SystemRepository(db)
        self.audit_service = AuditService(AuditRepository(db))

    def build_health_payload(self) -> HealthPayload:
        return HealthPayload(
            app_name=settings.app_name,
            version=settings.app_version,
            environment=settings.env_mode,
            status="ok",
            timestamp=datetime.now(timezone.utc),
        )

    def build_readiness_payload(self) -> ReadinessPayload:
        components: list[ReadinessComponentPayload] = []

        db_status = "ready"
        try:
            self.db.execute(text("SELECT 1"))
        except SQLAlchemyError as exc:
            db_status = "error"
            components.append(
                ReadinessComponentPayload(
                    name="database",
                    status="error",
                    detail=f"Database readiness failed: {str(exc)}",
                )
            )
        else:
            components.append(
                ReadinessComponentPayload(
                    name="database",
                    status="ready",
                    detail="PostgreSQL connection check succeeded.",
                )
            )

        redis_status = "ready"
        try:
            redis_client = redis.Redis.from_url(settings.redis_url)
            redis_client.ping()
        except redis.RedisError as exc:
            redis_status = "error"
            components.append(
                ReadinessComponentPayload(
                    name="redis",
                    status="error",
                    detail=f"Redis readiness failed: {str(exc)}",
                )
            )
        else:
            components.append(
                ReadinessComponentPayload(
                    name="redis",
                    status="ready",
                    detail="Redis ping succeeded.",
                )
            )

        storage_status, storage_detail = self._check_storage_readiness()
        components.append(
            ReadinessComponentPayload(
                name="storage",
                status=storage_status,
                detail=storage_detail,
            )
        )

        components.append(
            ReadinessComponentPayload(
                name="integrations",
                status="ready",
                detail=(
                    f"speech_to_text={settings.speech_to_text_provider}, "
                    f"vision={settings.vision_provider}, "
                    f"llm={settings.llm_provider}, "
                    f"routing={settings.routing_provider}, "
                    f"push={settings.push_provider}"
                ),
            )
        )

        overall_status = "ready" if all(item.status == "ready" for item in components) else "degraded"

        if overall_status != "ready":
            raise ServiceUnavailableException("Application dependencies are not ready.")

        return ReadinessPayload(
            app_name=settings.app_name,
            version=settings.app_version,
            environment=settings.env_mode,
            status=overall_status,
            components=components,
            timestamp=datetime.now(timezone.utc),
        )

    def build_app_info_payload(
        self,
        *,
        ai_provider_name: str,
        speech_to_text_provider_name: str,
        vision_provider_name: str,
        llm_provider_name: str,
        routing_provider_name: str,
        push_provider_name: str,
    ) -> AppInfoPayload:
        return AppInfoPayload(
            app_name=settings.app_name,
            version=settings.app_version,
            environment=settings.env_mode,
            api_prefix=settings.api_v1_prefix,
            docs_enabled=settings.docs_enabled,
            docs_url="/docs" if settings.docs_enabled else None,
            ai_provider=ai_provider_name,
            storage_provider=settings.storage_provider,
            speech_to_text_provider=speech_to_text_provider_name,
            vision_provider=vision_provider_name,
            llm_provider=llm_provider_name,
            routing_provider=routing_provider_name,
            push_provider=push_provider_name,
            trusted_hosts=settings.trusted_hosts_list,
            security_headers_enabled=settings.security_headers_enabled,
            https_redirect_enabled=settings.https_redirect_enabled,
            audit_http_enabled=settings.audit_http_enabled,
            timestamp=datetime.now(timezone.utc),
        )

    def get_platform_metrics_overview(self) -> SystemMetricsPayload:
        incidents_by_status = self.repository.get_incidents_by_status()
        jobs_by_status = self.repository.get_background_jobs_by_status()
        push_deliveries_by_status = self.repository.get_push_deliveries_by_status()
        provider_summary = self.repository.get_provider_summary()
        technician_summary = self.repository.get_technician_summary()
        financial_summary = self.repository.get_financial_summary()
        subscriptions_by_status = self.repository.get_subscription_summary()

        return SystemMetricsPayload(
            incidents_by_status=incidents_by_status,
            background_jobs_by_status=jobs_by_status,
            push_deliveries_by_status=push_deliveries_by_status,
            providers=provider_summary,
            technicians=technician_summary,
            financial=financial_summary,
            subscriptions_by_status=subscriptions_by_status,
            average_assignment_seconds=self.repository.get_average_assignment_seconds(),
            average_completion_seconds=self.repository.get_average_completion_seconds(),
            audit_events_last_24h=self.repository.get_audit_events_last_24h_count(),
            timestamp=datetime.now(timezone.utc),
        )

    def create_metrics_snapshot(self, captured_by_user_id: str | None) -> dict:
        payload = self.get_platform_metrics_overview().model_dump(mode="json")
        snapshot = self.audit_service.create_metric_snapshot(
            captured_by_user_id=captured_by_user_id,
            snapshot_type="OVERVIEW",
            payload_json=payload,
        )
        return snapshot.model_dump(mode="json")

    def _check_storage_readiness(self) -> tuple[str, str]:
        if settings.storage_provider.lower() == "local":
            try:
                root = Path(settings.local_storage_root).resolve()
                root.mkdir(parents=True, exist_ok=True)

                healthcheck_file = root / ".healthcheck_write_test"
                healthcheck_file.write_text("ok", encoding="utf-8")
                healthcheck_file.unlink(missing_ok=True)

                return "ready", f"Local storage path is writable: {root}"
            except Exception as exc:
                return "error", f"Local storage is not writable: {str(exc)}"

        if settings.storage_provider.lower() == "s3":
            if not settings.s3_bucket_name:
                return "error", "S3 storage provider is selected but S3_BUCKET_NAME is missing."
            return "ready", f"S3 storage is configured for bucket {settings.s3_bucket_name}."

        return "ready", f"Storage provider {settings.storage_provider} is configured."
```

### `app/services/tracking/__init__.py`

- Ruta relativa: `app/services/tracking/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/tracking/models.py`

- Ruta relativa: `app/services/tracking/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class IncidentResponderLocationPing(Base):
    __tablename__ = "incident_responder_location_pings"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    incident_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("providers.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    technician_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("technicians.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    source_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    accuracy_meters: Mapped[float | None] = mapped_column(Float, nullable=True)

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    incident = relationship("Incident", lazy="selectin")
    provider = relationship("Provider", lazy="selectin")
    technician = relationship("Technician", lazy="selectin")
```

### `app/services/tracking/repository.py`

- Ruta relativa: `app/services/tracking/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session, selectinload

from app.services.incidents.models import Incident
from app.services.providers.models import Provider, Technician
from app.services.tracking.models import IncidentResponderLocationPing


class TrackingRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = (
            select(Provider)
            .options(
                selectinload(Provider.owner_user),
                selectinload(Provider.technicians),
            )
            .where(Provider.owner_user_id == owner_user_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .options(
                selectinload(Incident.client_user),
                selectinload(Incident.provider).selectinload(Provider.owner_user),
                selectinload(Incident.assigned_technician),
                selectinload(Incident.vehicle),
            )
            .where(Incident.id == incident_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_incident_by_id_for_update(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = (
            select(Incident)
            .where(Incident.id == incident_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def get_technician_by_id_for_update(self, technician_id: str) -> Technician | None:
        query: Select[tuple[Technician]] = (
            select(Technician)
            .where(Technician.id == technician_id)
            .with_for_update()
        )
        return self.db.execute(query).scalar_one_or_none()

    def create_ping(
        self,
        ping: IncidentResponderLocationPing,
    ) -> IncidentResponderLocationPing:
        self.db.add(ping)
        self.db.flush()
        return ping

    def list_pings_by_incident_id(
        self,
        incident_id: str,
    ) -> list[IncidentResponderLocationPing]:
        query: Select[tuple[IncidentResponderLocationPing]] = (
            select(IncidentResponderLocationPing)
            .options(
                selectinload(IncidentResponderLocationPing.provider).selectinload(Provider.owner_user),
                selectinload(IncidentResponderLocationPing.technician),
            )
            .where(IncidentResponderLocationPing.incident_id == incident_id)
            .order_by(IncidentResponderLocationPing.recorded_at.asc(), IncidentResponderLocationPing.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, entity) -> None:
        self.db.add(entity)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(self, entity) -> None:
        self.db.refresh(entity)
```

### `app/services/tracking/router.py`

- Ruta relativa: `app/services/tracking/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT, ROLE_PLATFORM_ADMIN, ROLE_PROVIDER_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session, get_routing_provider
from app.core.security import require_roles
from app.integrations.routing.base import RoutingProvider
from app.services.auth.models import User
from app.services.tracking.repository import TrackingRepository
from app.services.tracking.schemas import LocationPingRequest
from app.services.tracking.service import TrackingService

router = APIRouter(prefix="/tracking", tags=["Tracking"])


@router.post("/provider/incidents/{incident_id}/location")
def report_my_location(
    incident_id: str,
    payload: LocationPingRequest,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.report_my_location(current_user, incident_id, payload)

    return success_response(
        message="Responder location reported successfully.",
        data=result.model_dump(mode="json"),
    )


@router.post("/provider/incidents/{incident_id}/refresh-route")
def refresh_my_route(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.refresh_my_route(current_user, incident_id)

    return success_response(
        message="Route refreshed successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/live")
def get_provider_live_tracking(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_provider_live_tracking(current_user, incident_id)

    return success_response(
        message="Provider live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/provider/incidents/{incident_id}/history")
def list_provider_tracking_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_PROVIDER_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_provider_tracking_history(current_user, incident_id)

    return success_response(
        message="Provider tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/client/incidents/{incident_id}/live")
def get_client_live_tracking(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_client_live_tracking(current_user, incident_id)

    return success_response(
        message="Client live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/client/incidents/{incident_id}/history")
def list_client_tracking_history(
    incident_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_client_tracking_history(current_user, incident_id)

    return success_response(
        message="Client tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )


@router.get("/platform/incidents/{incident_id}/live")
def get_platform_live_tracking(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.get_platform_live_tracking(incident_id)

    return success_response(
        message="Platform live tracking loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("/platform/incidents/{incident_id}/history")
def list_platform_tracking_history(
    incident_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
    routing_provider: RoutingProvider = Depends(get_routing_provider),
) -> dict:
    service = TrackingService(TrackingRepository(db), routing_provider)
    result = service.list_platform_tracking_history(incident_id)

    return success_response(
        message="Platform tracking history loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={"count": len(result)},
    )
```

### `app/services/tracking/schemas.py`

- Ruta relativa: `app/services/tracking/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime

from pydantic import BaseModel, Field


class IncidentTrackingProviderSummaryResponse(BaseModel):
    id: str
    provider_type: str
    business_name: str
    contact_phone: str | None = None
    city: str | None = None
    average_rating: float


class IncidentTrackingTechnicianSummaryResponse(BaseModel):
    id: str
    provider_id: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    specialty: str | None = None
    is_active: bool
    is_available: bool


class IncidentTrackingClientSummaryResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None


class IncidentTrackingRouteResponse(BaseModel):
    provider_name: str | None = None
    distance_meters: float | None = None
    distance_km: float | None = None
    duration_seconds: int | None = None
    eta_seconds: int | None = None
    eta_minutes: int | None = None
    polyline: str | None = None
    last_calculated_at: datetime | None = None
    error_message: str | None = None


class IncidentTrackingResponderPositionResponse(BaseModel):
    latitude: float | None = None
    longitude: float | None = None
    source_type: str | None = None
    recorded_at: datetime | None = None


class IncidentLiveTrackingResponse(BaseModel):
    incident_id: str
    status: str
    priority: str
    title: str
    description: str
    address_reference: str | None = None
    incident_latitude: float | None = None
    incident_longitude: float | None = None
    assigned_at: datetime | None = None
    en_route_at: datetime | None = None
    arrived_at: datetime | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    cancelled_at: datetime | None = None

    provider: IncidentTrackingProviderSummaryResponse | None = None
    assigned_technician: IncidentTrackingTechnicianSummaryResponse | None = None
    client_user: IncidentTrackingClientSummaryResponse

    responder_position: IncidentTrackingResponderPositionResponse
    route: IncidentTrackingRouteResponse


class LocationPingRequest(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    accuracy_meters: float | None = Field(default=None, ge=0)
    technician_id: str | None = None


class TrackingHistoryItemResponse(BaseModel):
    id: str
    incident_id: str
    provider_id: str | None = None
    technician_id: str | None = None
    source_type: str
    latitude: float
    longitude: float
    accuracy_meters: float | None = None
    recorded_at: datetime
    provider_business_name: str | None = None
    technician_full_name: str | None = None
```

### `app/services/tracking/service.py`

- Ruta relativa: `app/services/tracking/service.py`
- Nombre de archivo: `service.py`

```python
from datetime import datetime, timezone

from app.common.constants import (
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    PROVIDER_TYPE_WORKSHOP,
    TRACKING_SOURCE_PROVIDER_SELF,
    TRACKING_SOURCE_TECHNICIAN,
)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.integrations.routing.base import RouteCalculationRequest, RoutingProvider
from app.integrations.routing.null_provider import NullRoutingProvider
from app.services.auth.models import User
from app.services.tracking.models import IncidentResponderLocationPing
from app.services.tracking.repository import TrackingRepository
from app.services.tracking.schemas import (
    IncidentLiveTrackingResponse,
    IncidentTrackingClientSummaryResponse,
    IncidentTrackingProviderSummaryResponse,
    IncidentTrackingResponderPositionResponse,
    IncidentTrackingRouteResponse,
    IncidentTrackingTechnicianSummaryResponse,
    LocationPingRequest,
    TrackingHistoryItemResponse,
)


class TrackingService:
    def __init__(
        self,
        repository: TrackingRepository,
        routing_provider: RoutingProvider,
    ) -> None:
        self.repository = repository
        self.routing_provider = routing_provider

    def report_my_location(
        self,
        current_user: User,
        incident_id: str,
        payload: LocationPingRequest,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        now = datetime.now(timezone.utc)

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException("Tracking is only available for assigned or active incidents.")

            source_type = TRACKING_SOURCE_PROVIDER_SELF
            technician = None

            if provider.provider_type == PROVIDER_TYPE_WORKSHOP and locked_incident.assigned_technician_id is not None:
                technician = self.repository.get_technician_by_id_for_update(
                    str(locked_incident.assigned_technician_id)
                )
                if technician is None:
                    raise NotFoundException("Assigned technician not found.")

                if payload.technician_id and str(payload.technician_id) != str(technician.id):
                    raise ForbiddenException("The provided technician_id does not match the incident technician.")

                technician.current_latitude = payload.latitude
                technician.current_longitude = payload.longitude
                self.repository.save(technician)
                source_type = TRACKING_SOURCE_TECHNICIAN
            else:
                if payload.technician_id:
                    raise ConflictException("Independent providers cannot report location using technician_id.")

            ping = IncidentResponderLocationPing(
                incident_id=locked_incident.id,
                provider_id=provider.id,
                technician_id=technician.id if technician is not None else None,
                source_type=source_type,
                latitude=payload.latitude,
                longitude=payload.longitude,
                accuracy_meters=payload.accuracy_meters,
                recorded_at=now,
            )

            self.repository.create_ping(ping)

            locked_incident.responder_last_latitude = payload.latitude
            locked_incident.responder_last_longitude = payload.longitude
            locked_incident.responder_last_source_type = source_type
            locked_incident.responder_last_recorded_at = now

            self._apply_route_calculation(
                incident=locked_incident,
                origin_latitude=payload.latitude,
                origin_longitude=payload.longitude,
            )

            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def refresh_my_route(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            locked_incident = self.repository.get_incident_by_id_for_update(incident_id)
            if locked_incident is None:
                raise NotFoundException("Incident not found.")

            if locked_incident.provider_id is None or str(locked_incident.provider_id) != str(provider.id):
                raise ForbiddenException("This incident does not belong to your provider.")

            if locked_incident.status not in (
                INCIDENT_STATUS_ASSIGNED,
                INCIDENT_STATUS_EN_ROUTE,
                INCIDENT_STATUS_ON_SITE,
                INCIDENT_STATUS_IN_PROGRESS,
            ):
                raise ConflictException("Route refresh is only available for assigned or active incidents.")

            origin_latitude, origin_longitude = self._resolve_origin_coordinates(
                incident=locked_incident,
                provider=provider,
            )

            self._apply_route_calculation(
                incident=locked_incident,
                origin_latitude=origin_latitude,
                origin_longitude=origin_longitude,
            )

            self.repository.save(locked_incident)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def get_provider_live_tracking(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        return self._build_live_response(incident)

    def get_client_live_tracking(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        return self._build_live_response(incident)

    def get_platform_live_tracking(
        self,
        incident_id: str,
    ) -> IncidentLiveTrackingResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        return self._build_live_response(incident)

    def list_provider_tracking_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if incident.provider_id is None or str(incident.provider_id) != str(provider.id):
            raise ForbiddenException("This incident does not belong to your provider.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def list_client_tracking_history(
        self,
        current_user: User,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def list_platform_tracking_history(
        self,
        incident_id: str,
    ) -> list[TrackingHistoryItemResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        pings = self.repository.list_pings_by_incident_id(incident_id)
        return [self._build_history_item(item) for item in pings]

    def _resolve_origin_coordinates(self, incident, provider) -> tuple[float, float]:
        if incident.responder_last_latitude is not None and incident.responder_last_longitude is not None:
            return incident.responder_last_latitude, incident.responder_last_longitude

        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            if technician.current_latitude is not None and technician.current_longitude is not None:
                return technician.current_latitude, technician.current_longitude

        if provider.base_latitude is not None and provider.base_longitude is not None:
            return provider.base_latitude, provider.base_longitude

        raise ConflictException("No origin coordinates are available to calculate the route.")

    def _apply_route_calculation(
        self,
        incident,
        origin_latitude: float,
        origin_longitude: float,
    ) -> None:
        if incident.incident_latitude is None or incident.incident_longitude is None:
            raise ConflictException("The incident does not have coordinates to calculate a route.")

        route_request = RouteCalculationRequest(
            origin_latitude=origin_latitude,
            origin_longitude=origin_longitude,
            destination_latitude=incident.incident_latitude,
            destination_longitude=incident.incident_longitude,
            profile=None,
        )

        try:
            route_result = self.routing_provider.calculate_route(route_request)
            incident.route_error_message = None
            incident.route_provider_name = self.routing_provider.provider_name
        except Exception as exc:
            fallback_provider = NullRoutingProvider()
            route_result = fallback_provider.calculate_route(route_request)
            incident.route_error_message = f"Primary routing provider failed: {str(exc)}"
            incident.route_provider_name = fallback_provider.provider_name

        incident.route_distance_meters = route_result.distance_meters
        incident.route_duration_seconds = route_result.duration_seconds
        incident.route_eta_seconds = route_result.duration_seconds
        incident.route_polyline = route_result.polyline
        incident.route_last_calculated_at = datetime.now(timezone.utc)

    def _build_live_response(self, incident) -> IncidentLiveTrackingResponse:
        provider_payload = None
        if incident.provider is not None:
            provider = incident.provider
            provider_payload = IncidentTrackingProviderSummaryResponse(
                id=str(provider.id),
                provider_type=provider.provider_type,
                business_name=provider.business_name,
                contact_phone=provider.contact_phone,
                city=provider.city,
                average_rating=provider.average_rating,
            )

        technician_payload = None
        if incident.assigned_technician is not None:
            technician = incident.assigned_technician
            technician_payload = IncidentTrackingTechnicianSummaryResponse(
                id=str(technician.id),
                provider_id=str(technician.provider_id),
                first_name=technician.first_name,
                last_name=technician.last_name,
                full_name=technician.full_name,
                phone_number=technician.phone_number,
                specialty=technician.specialty,
                is_active=technician.is_active,
                is_available=technician.is_available,
            )

        client_user = incident.client_user
        client_payload = IncidentTrackingClientSummaryResponse(
            id=str(client_user.id),
            email=client_user.email,
            first_name=client_user.first_name,
            last_name=client_user.last_name,
            full_name=client_user.full_name,
            phone_number=client_user.phone_number,
        )

        route_distance_km = (
            round(incident.route_distance_meters / 1000.0, 2)
            if incident.route_distance_meters is not None
            else None
        )
        eta_minutes = (
            int(round(incident.route_eta_seconds / 60))
            if incident.route_eta_seconds is not None
            else None
        )

        return IncidentLiveTrackingResponse(
            incident_id=str(incident.id),
            status=incident.status,
            priority=incident.priority,
            title=incident.title,
            description=incident.description,
            address_reference=incident.address_reference,
            incident_latitude=incident.incident_latitude,
            incident_longitude=incident.incident_longitude,
            assigned_at=incident.assigned_at,
            en_route_at=incident.en_route_at,
            arrived_at=incident.arrived_at,
            started_at=incident.started_at,
            completed_at=incident.completed_at,
            cancelled_at=incident.cancelled_at,
            provider=provider_payload,
            assigned_technician=technician_payload,
            client_user=client_payload,
            responder_position=IncidentTrackingResponderPositionResponse(
                latitude=incident.responder_last_latitude,
                longitude=incident.responder_last_longitude,
                source_type=incident.responder_last_source_type,
                recorded_at=incident.responder_last_recorded_at,
            ),
            route=IncidentTrackingRouteResponse(
                provider_name=incident.route_provider_name,
                distance_meters=incident.route_distance_meters,
                distance_km=route_distance_km,
                duration_seconds=incident.route_duration_seconds,
                eta_seconds=incident.route_eta_seconds,
                eta_minutes=eta_minutes,
                polyline=incident.route_polyline,
                last_calculated_at=incident.route_last_calculated_at,
                error_message=incident.route_error_message,
            ),
        )

    def _build_history_item(self, ping: IncidentResponderLocationPing) -> TrackingHistoryItemResponse:
        provider_business_name = ping.provider.business_name if ping.provider is not None else None
        technician_full_name = ping.technician.full_name if ping.technician is not None else None

        return TrackingHistoryItemResponse(
            id=str(ping.id),
            incident_id=str(ping.incident_id),
            provider_id=str(ping.provider_id) if ping.provider_id else None,
            technician_id=str(ping.technician_id) if ping.technician_id else None,
            source_type=ping.source_type,
            latitude=ping.latitude,
            longitude=ping.longitude,
            accuracy_meters=ping.accuracy_meters,
            recorded_at=ping.recorded_at,
            provider_business_name=provider_business_name,
            technician_full_name=technician_full_name,
        )
```

### `app/services/users/__init__.py`

- Ruta relativa: `app/services/users/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/users/repository.py`

- Ruta relativa: `app/services/users/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.auth.models import User


class UsersRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_id(self, user_id: str) -> User | None:
        query: Select[tuple[User]] = select(User).where(User.id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_users(self, limit: int = 50, offset: int = 0) -> list[User]:
        query: Select[tuple[User]] = (
            select(User)
            .order_by(User.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
```

### `app/services/users/router.py`

- Ruta relativa: `app/services/users/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.common.constants import ROLE_PLATFORM_ADMIN
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import get_current_active_user, require_roles
from app.services.auth.models import User
from app.services.users.repository import UsersRepository
from app.services.users.schemas import UpdateOwnProfileRequest
from app.services.users.service import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me/profile")
def get_own_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.get_own_profile(current_user)

    return success_response(
        message="Own profile loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/me/profile")
def update_own_profile(
    payload: UpdateOwnProfileRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.update_own_profile(current_user, payload)

    return success_response(
        message="Own profile updated successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_users(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.list_users(limit=limit, offset=offset)

    return success_response(
        message="Users loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "limit": limit,
            "offset": offset,
            "count": len(result),
        },
    )


@router.get("/{user_id}")
def get_user_by_id(
    user_id: str,
    _: User = Depends(require_roles(ROLE_PLATFORM_ADMIN)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = UsersService(UsersRepository(db))
    result = service.get_user_by_id(user_id)

    return success_response(
        message="User loaded successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/users/schemas.py`

- Ruta relativa: `app/services/users/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from pydantic import BaseModel, Field


class UserRoleItemResponse(BaseModel):
    id: str
    code: str
    name: str
    description: str | None = None


class UserProfileResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    full_name: str
    phone_number: str | None = None
    is_active: bool
    is_superuser: bool
    role_codes: list[str]
    roles: list[UserRoleItemResponse]
    created_at: datetime
    updated_at: datetime


class UpdateOwnProfileRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=2, max_length=120)
    last_name: str | None = Field(default=None, min_length=2, max_length=120)
    phone_number: str | None = Field(default=None, max_length=30)
```

### `app/services/users/service.py`

- Ruta relativa: `app/services/users/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.exceptions import NotFoundException
from app.services.auth.models import User
from app.services.users.repository import UsersRepository
from app.services.users.schemas import (
    UpdateOwnProfileRequest,
    UserProfileResponse,
    UserRoleItemResponse,
)


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def get_own_profile(self, current_user: User) -> UserProfileResponse:
        return self._build_profile_response(current_user)

    def update_own_profile(
        self,
        current_user: User,
        payload: UpdateOwnProfileRequest,
    ) -> UserProfileResponse:
        if payload.first_name is not None:
            current_user.first_name = payload.first_name.strip()

        if payload.last_name is not None:
            current_user.last_name = payload.last_name.strip()

        if payload.phone_number is not None:
            cleaned_phone = payload.phone_number.strip()
            current_user.phone_number = cleaned_phone or None

        updated_user = self.repository.save(current_user)
        return self._build_profile_response(updated_user)

    def get_user_by_id(self, user_id: str) -> UserProfileResponse:
        user = self.repository.get_user_by_id(user_id)
        if user is None:
            raise NotFoundException("User not found.")

        return self._build_profile_response(user)

    def list_users(self, limit: int = 50, offset: int = 0) -> list[UserProfileResponse]:
        users = self.repository.list_users(limit=limit, offset=offset)
        return [self._build_profile_response(user) for user in users]

    def _build_profile_response(self, user: User) -> UserProfileResponse:
        role_items = [
            UserRoleItemResponse(
                id=str(role.id),
                code=role.code,
                name=role.name,
                description=role.description,
            )
            for role in sorted(user.roles, key=lambda item: item.code)
        ]

        role_codes = [role.code for role in role_items]

        return UserProfileResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            full_name=user.full_name,
            phone_number=user.phone_number,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            role_codes=role_codes,
            roles=role_items,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
```

### `app/services/vehicles/__init__.py`

- Ruta relativa: `app/services/vehicles/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/services/vehicles/models.py`

- Ruta relativa: `app/services/vehicles/models.py`
- Nombre de archivo: `models.py`

```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    owner_user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    plate_number: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    vehicle_type: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    brand: Mapped[str] = mapped_column(String(80), nullable=False)
    model: Mapped[str] = mapped_column(String(80), nullable=False)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    color: Mapped[str | None] = mapped_column(String(50), nullable=True)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    owner_user = relationship("User", lazy="selectin")
```

### `app/services/vehicles/repository.py`

- Ruta relativa: `app/services/vehicles/repository.py`
- Nombre de archivo: `repository.py`

```python
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.vehicles.models import Vehicle


class VehiclesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_vehicle_by_id(self, vehicle_id: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.id == vehicle_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_vehicle_by_plate_number(self, plate_number: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.plate_number == plate_number)
        return self.db.execute(query).scalar_one_or_none()

    def list_vehicles_by_owner_user_id(self, owner_user_id: str) -> list[Vehicle]:
        query: Select[tuple[Vehicle]] = (
            select(Vehicle)
            .where(Vehicle.owner_user_id == owner_user_id)
            .order_by(Vehicle.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle

    def save_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle
```

### `app/services/vehicles/router.py`

- Ruta relativa: `app/services/vehicles/router.py`
- Nombre de archivo: `router.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.vehicles.repository import VehiclesRepository
from app.services.vehicles.schemas import CreateVehicleRequest, UpdateOwnVehicleRequest
from app.services.vehicles.service import VehiclesService

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("")
def create_own_vehicle(
    payload: CreateVehicleRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.create_own_vehicle(current_user, payload)

    return success_response(
        message="Vehicle created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_own_vehicles(
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.list_own_vehicles(current_user)

    return success_response(
        message="Vehicles loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/{vehicle_id}")
def get_own_vehicle(
    vehicle_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.get_own_vehicle(current_user, vehicle_id)

    return success_response(
        message="Vehicle loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{vehicle_id}")
def update_own_vehicle(
    vehicle_id: str,
    payload: UpdateOwnVehicleRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.update_own_vehicle(current_user, vehicle_id, payload)

    return success_response(
        message="Vehicle updated successfully.",
        data=result.model_dump(mode="json"),
    )
```

### `app/services/vehicles/schemas.py`

- Ruta relativa: `app/services/vehicles/schemas.py`
- Nombre de archivo: `schemas.py`

```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class VehicleResponse(BaseModel):
    id: str
    owner_user_id: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    year: int | None = None
    color: str | None = None
    notes: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class CreateVehicleRequest(BaseModel):
    plate_number: str = Field(min_length=3, max_length=20)
    vehicle_type: Literal["CAR", "MOTORCYCLE", "TRUCK", "VAN", "OTHER"]
    brand: str = Field(min_length=2, max_length=80)
    model: str = Field(min_length=1, max_length=80)
    year: int | None = Field(default=None, ge=1950, le=2100)
    color: str | None = Field(default=None, max_length=50)
    notes: str | None = None


class UpdateOwnVehicleRequest(BaseModel):
    vehicle_type: Literal["CAR", "MOTORCYCLE", "TRUCK", "VAN", "OTHER"] | None = None
    brand: str | None = Field(default=None, min_length=2, max_length=80)
    model: str | None = Field(default=None, min_length=1, max_length=80)
    year: int | None = Field(default=None, ge=1950, le=2100)
    color: str | None = Field(default=None, max_length=50)
    notes: str | None = None
    is_active: bool | None = None
```

### `app/services/vehicles/service.py`

- Ruta relativa: `app/services/vehicles/service.py`
- Nombre de archivo: `service.py`

```python
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.vehicles.models import Vehicle
from app.services.vehicles.repository import VehiclesRepository
from app.services.vehicles.schemas import CreateVehicleRequest, UpdateOwnVehicleRequest, VehicleResponse


class VehiclesService:
    def __init__(self, repository: VehiclesRepository) -> None:
        self.repository = repository

    def create_own_vehicle(self, current_user: User, payload: CreateVehicleRequest) -> VehicleResponse:
        normalized_plate_number = payload.plate_number.strip().upper()

        existing_vehicle = self.repository.get_vehicle_by_plate_number(normalized_plate_number)
        if existing_vehicle is not None:
            raise ConflictException("A vehicle with this plate number already exists.")

        new_vehicle = Vehicle(
            owner_user_id=current_user.id,
            plate_number=normalized_plate_number,
            vehicle_type=payload.vehicle_type,
            brand=payload.brand.strip(),
            model=payload.model.strip(),
            year=payload.year,
            color=payload.color.strip() if payload.color else None,
            notes=payload.notes.strip() if payload.notes else None,
            is_active=True,
        )

        created_vehicle = self.repository.create_vehicle(new_vehicle)
        return self._build_vehicle_response(created_vehicle)

    def list_own_vehicles(self, current_user: User) -> list[VehicleResponse]:
        vehicles = self.repository.list_vehicles_by_owner_user_id(str(current_user.id))
        return [self._build_vehicle_response(vehicle) for vehicle in vehicles]

    def get_own_vehicle(self, current_user: User, vehicle_id: str) -> VehicleResponse:
        vehicle = self.repository.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        return self._build_vehicle_response(vehicle)

    def update_own_vehicle(
        self,
        current_user: User,
        vehicle_id: str,
        payload: UpdateOwnVehicleRequest,
    ) -> VehicleResponse:
        vehicle = self.repository.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        if payload.vehicle_type is not None:
            vehicle.vehicle_type = payload.vehicle_type

        if payload.brand is not None:
            vehicle.brand = payload.brand.strip()

        if payload.model is not None:
            vehicle.model = payload.model.strip()

        if payload.year is not None:
            vehicle.year = payload.year

        if payload.color is not None:
            cleaned_value = payload.color.strip()
            vehicle.color = cleaned_value or None

        if payload.notes is not None:
            cleaned_value = payload.notes.strip()
            vehicle.notes = cleaned_value or None

        if payload.is_active is not None:
            vehicle.is_active = payload.is_active

        updated_vehicle = self.repository.save_vehicle(vehicle)
        return self._build_vehicle_response(updated_vehicle)

    def _build_vehicle_response(self, vehicle: Vehicle) -> VehicleResponse:
        return VehicleResponse(
            id=str(vehicle.id),
            owner_user_id=str(vehicle.owner_user_id),
            plate_number=vehicle.plate_number,
            vehicle_type=vehicle.vehicle_type,
            brand=vehicle.brand,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            notes=vehicle.notes,
            is_active=vehicle.is_active,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at,
        )
```

### `app/tasks/__init__.py`

- Ruta relativa: `app/tasks/__init__.py`
- Nombre de archivo: `__init__.py`

```python

```

### `app/tasks/celery_app.py`

- Ruta relativa: `app/tasks/celery_app.py`
- Nombre de archivo: `celery_app.py`

```python
from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "mechanic_api",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=["app.tasks.task_definitions"],
)

celery_app.conf.update(
    task_default_queue=settings.celery_default_queue,
    task_track_started=True,
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_routes={
        "jobs.demo_echo_task": {"queue": "default"},
        "jobs.audio_transcription_task": {"queue": "audio"},
        "jobs.image_analysis_task": {"queue": "image"},
        "jobs.incident_summary_task": {"queue": "summary"},
        "jobs.push_notification_task": {"queue": "push"},
    },
)
```

### `app/tasks/job_runtime.py`

- Ruta relativa: `app/tasks/job_runtime.py`
- Nombre de archivo: `job_runtime.py`

```python
from dataclasses import asdict
from datetime import datetime, timezone

from app.common.constants import (
    BACKGROUND_JOB_STATUS_FAILED,
    BACKGROUND_JOB_STATUS_RUNNING,
    BACKGROUND_JOB_STATUS_SUCCEEDED,
)
from app.core.database import SessionLocal
from app.services.jobs.repository import JobsRepository


def mark_job_running(job_id: str, celery_task_id: str | None = None) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_RUNNING
        job.celery_task_id = celery_task_id or job.celery_task_id
        job.started_at = datetime.now(timezone.utc)
        job.finished_at = None
        job.error_message = None
        job.attempts_count += 1

        repository.save_job(job)
    finally:
        db.close()


def mark_job_succeeded(job_id: str, result_payload: dict | object | None = None) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_SUCCEEDED
        job.finished_at = datetime.now(timezone.utc)
        job.error_message = None

        if result_payload is None:
            job.result_json = None
        elif isinstance(result_payload, dict):
            job.result_json = result_payload
        else:
            job.result_json = asdict(result_payload)

        repository.save_job(job)
    finally:
        db.close()


def mark_job_failed(job_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        repository = JobsRepository(db)
        job = repository.get_job_by_id(job_id)
        if job is None:
            return

        job.status = BACKGROUND_JOB_STATUS_FAILED
        job.error_message = error_message
        job.finished_at = datetime.now(timezone.utc)

        repository.save_job(job)
    finally:
        db.close()
```

### `app/tasks/notification_runtime.py`

- Ruta relativa: `app/tasks/notification_runtime.py`
- Nombre de archivo: `notification_runtime.py`

```python
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.common.constants import (
    PUSH_DELIVERY_STATUS_FAILED,
    PUSH_DELIVERY_STATUS_RUNNING,
    PUSH_DELIVERY_STATUS_SUCCEEDED,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.core.database import SessionLocal
from app.services.notifications.models import PushNotificationDelivery


def build_push_notification_delivery_context(delivery_id: str) -> dict:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery)
            .options(selectinload(PushNotificationDelivery.user_device_token))
            .where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            raise NotFoundException("Push notification delivery not found.")

        device_token = delivery.user_device_token
        if device_token is None:
            raise ConflictException("Push notification delivery does not have a device token.")

        if not device_token.is_active:
            raise ConflictException("The target device token is inactive.")

        return {
            "delivery_id": str(delivery.id),
            "recipient_token": device_token.device_token,
            "title": delivery.title,
            "body": delivery.body,
            "data": delivery.data_json or {},
        }
    finally:
        db.close()


def mark_delivery_running(delivery_id: str) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery).where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_RUNNING
        delivery.error_message = None

        db.add(delivery)
        db.commit()
    finally:
        db.close()


def mark_delivery_succeeded(
    delivery_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery).where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_SUCCEEDED
        delivery.provider_name = provider_name
        delivery.provider_message_id = result_payload.get("provider_message_id")
        delivery.error_message = None
        delivery.sent_at = datetime.now(timezone.utc)

        db.add(delivery)
        db.commit()
    finally:
        db.close()


def mark_delivery_failed(
    delivery_id: str,
    provider_name: str | None,
    error_message: str,
    deactivate_device: bool = False,
) -> None:
    db = SessionLocal()
    try:
        delivery = db.execute(
            select(PushNotificationDelivery)
            .options(selectinload(PushNotificationDelivery.user_device_token))
            .where(PushNotificationDelivery.id == delivery_id)
        ).scalar_one_or_none()

        if delivery is None:
            return

        delivery.status = PUSH_DELIVERY_STATUS_FAILED
        delivery.provider_name = provider_name
        delivery.error_message = error_message
        delivery.sent_at = datetime.now(timezone.utc)

        if deactivate_device and delivery.user_device_token is not None:
            delivery.user_device_token.is_active = False
            delivery.user_device_token.last_seen_at = datetime.now(timezone.utc)
            db.add(delivery.user_device_token)

        db.add(delivery)
        db.commit()
    finally:
        db.close()
```

### `app/tasks/pipeline_runtime.py`

- Ruta relativa: `app/tasks/pipeline_runtime.py`
- Nombre de archivo: `pipeline_runtime.py`

```python
from datetime import datetime, timezone

from sqlalchemy import select

from app.common.constants import (
    EVIDENCE_TYPE_TEXT,
    PROCESSING_STATUS_FAILED,
    PROCESSING_STATUS_RUNNING,
    PROCESSING_STATUS_SUCCEEDED,
)
from app.common.exceptions import ConflictException, NotFoundException
from app.core.database import SessionLocal
from app.integrations.factory import build_storage_service_by_name
from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident


def build_audio_evidence_processing_context(evidence_id: str) -> dict:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        storage_service = build_storage_service_by_name(evidence.storage_provider)

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        return {
            "evidence_id": str(evidence.id),
            "incident_id": str(evidence.incident_id),
            "audio_file_path": descriptor.absolute_file_path if descriptor.kind == "local_file" else None,
            "source_url": descriptor.download_url if descriptor.kind == "signed_url" else None,
        }
    finally:
        db.close()


def build_image_evidence_processing_context(evidence_id: str) -> dict:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            raise NotFoundException("Evidence not found.")

        storage_service = build_storage_service_by_name(evidence.storage_provider)

        descriptor = storage_service.build_download_descriptor(
            absolute_file_path=evidence.absolute_file_path,
            storage_bucket=evidence.storage_bucket,
            storage_object_key=evidence.storage_object_key,
            public_url=evidence.public_url,
            original_filename=evidence.original_filename,
            stored_filename=evidence.stored_filename,
            mime_type=evidence.mime_type,
        )

        return {
            "evidence_id": str(evidence.id),
            "incident_id": str(evidence.incident_id),
            "image_file_path": descriptor.absolute_file_path if descriptor.kind == "local_file" else None,
            "source_url": descriptor.download_url if descriptor.kind == "signed_url" else None,
        }
    finally:
        db.close()


def build_incident_summary_request_data(incident_id: str) -> dict:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            raise NotFoundException("Incident not found.")

        evidences = list(
            db.execute(
                select(IncidentEvidence)
                .where(IncidentEvidence.incident_id == incident_id)
                .order_by(IncidentEvidence.created_at.asc())
            ).scalars().all()
        )

        additional_texts = [
            evidence.text_content_snapshot.strip()
            for evidence in evidences
            if evidence.evidence_type == EVIDENCE_TYPE_TEXT and evidence.text_content_snapshot
        ]

        successful_transcripts = [
            evidence.transcript_text.strip()
            for evidence in evidences
            if evidence.transcript_text and evidence.audio_processing_status == PROCESSING_STATUS_SUCCEEDED
        ]

        successful_image_summaries = [
            evidence.image_summary.strip()
            for evidence in evidences
            if evidence.image_summary and evidence.image_processing_status == PROCESSING_STATUS_SUCCEEDED
        ]

        user_text_sections = [
            f"Título reportado: {incident.title}",
            f"Descripción reportada: {incident.description}",
        ]

        if additional_texts:
            user_text_sections.append(
                "Texto adicional del cliente:\n- " + "\n- ".join(additional_texts)
            )

        return {
            "incident_id": str(incident.id),
            "user_text": "\n\n".join(user_text_sections).strip() or None,
            "transcript_text": "\n\n".join(successful_transcripts).strip() or None,
            "image_analysis_summary": "\n\n".join(successful_image_summaries).strip() or None,
        }
    finally:
        db.close()


def mark_audio_processing_running(evidence_id: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_RUNNING
        evidence.audio_error_message = None
        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_audio_processing_succeeded(
    evidence_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_SUCCEEDED
        evidence.audio_provider_name = provider_name
        evidence.transcript_text = result_payload.get("transcript_text")
        evidence.transcript_language_code = result_payload.get("language_code")
        evidence.transcript_confidence = result_payload.get("confidence")
        evidence.transcript_segments_json = result_payload.get("segments")
        evidence.audio_processed_at = datetime.now(timezone.utc)
        evidence.audio_error_message = None

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_audio_processing_failed(evidence_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.audio_processing_status = PROCESSING_STATUS_FAILED
        evidence.audio_error_message = error_message
        evidence.audio_processed_at = datetime.now(timezone.utc)

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_running(evidence_id: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_RUNNING
        evidence.image_error_message = None
        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_succeeded(
    evidence_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_SUCCEEDED
        evidence.image_provider_name = provider_name
        evidence.image_labels_json = result_payload.get("labels")
        evidence.image_detections_json = result_payload.get("detections")
        evidence.image_summary = result_payload.get("summary")
        evidence.image_processed_at = datetime.now(timezone.utc)
        evidence.image_error_message = None

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_image_processing_failed(evidence_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        evidence = db.execute(
            select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        ).scalar_one_or_none()

        if evidence is None:
            return

        evidence.image_processing_status = PROCESSING_STATUS_FAILED
        evidence.image_error_message = error_message
        evidence.image_processed_at = datetime.now(timezone.utc)

        db.add(evidence)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_running(incident_id: str) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_RUNNING
        incident.summary_error_message = None

        db.add(incident)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_succeeded(
    incident_id: str,
    provider_name: str,
    result_payload: dict,
) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_SUCCEEDED
        incident.summary_provider_name = provider_name
        incident.structured_summary = result_payload.get("structured_summary")
        incident.suggested_category = result_payload.get("suggested_category")
        incident.suggested_priority = result_payload.get("suggested_priority")
        incident.requires_more_information = bool(
            result_payload.get("requires_more_information", False)
        )
        incident.summary_processed_at = datetime.now(timezone.utc)
        incident.summary_error_message = None

        db.add(incident)
        db.commit()
    finally:
        db.close()


def mark_incident_summary_failed(incident_id: str, error_message: str) -> None:
    db = SessionLocal()
    try:
        incident = db.execute(
            select(Incident).where(Incident.id == incident_id)
        ).scalar_one_or_none()

        if incident is None:
            return

        incident.ai_summary_status = PROCESSING_STATUS_FAILED
        incident.summary_error_message = error_message
        incident.summary_processed_at = datetime.now(timezone.utc)

        db.add(incident)
        db.commit()
    finally:
        db.close()
```

### `app/tasks/task_definitions.py`

- Ruta relativa: `app/tasks/task_definitions.py`
- Nombre de archivo: `task_definitions.py`

```python
import time
from dataclasses import asdict

from app.core.database import SessionLocal
from app.integrations.factory import (
    build_llm_provider,
    build_push_provider,
    build_speech_to_text_provider,
    build_vision_provider,
)
from app.integrations.llm.base import IncidentSummaryRequest
from app.integrations.push.base import PushNotificationRequest
from app.integrations.speech_to_text.base import AudioTranscriptionRequest
from app.integrations.vision.base import ImageAnalysisRequest
from app.services.jobs.dispatcher import PipelineDispatcher
from app.tasks.celery_app import celery_app
from app.tasks.job_runtime import mark_job_failed, mark_job_running, mark_job_succeeded
from app.tasks.notification_runtime import (
    build_push_notification_delivery_context,
    mark_delivery_failed,
    mark_delivery_running,
    mark_delivery_succeeded,
)
from app.tasks.pipeline_runtime import (
    build_audio_evidence_processing_context,
    build_image_evidence_processing_context,
    build_incident_summary_request_data,
    mark_audio_processing_failed,
    mark_audio_processing_running,
    mark_audio_processing_succeeded,
    mark_image_processing_failed,
    mark_image_processing_running,
    mark_image_processing_succeeded,
    mark_incident_summary_failed,
    mark_incident_summary_running,
    mark_incident_summary_succeeded,
)


@celery_app.task(bind=True, name="jobs.demo_echo_task")
def demo_echo_task(self, job_id: str, message: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        time.sleep(2)

        result = {
            "message": message,
            "worker_task_id": self.request.id,
            "info": "Demo background task finished successfully.",
        }

        mark_job_succeeded(job_id, result)
        return result
    except Exception as exc:
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.audio_transcription_task")
def audio_transcription_task(self, job_id: str, evidence_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_audio_processing_running(evidence_id)

        context = build_audio_evidence_processing_context(evidence_id)

        provider = build_speech_to_text_provider()
        result = provider.transcribe_audio(
            AudioTranscriptionRequest(
                evidence_id=evidence_id,
                audio_file_path=context["audio_file_path"],
                source_url=context["source_url"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = context["incident_id"]

        mark_audio_processing_succeeded(
            evidence_id=evidence_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        try:
            db = SessionLocal()
            try:
                dispatcher = PipelineDispatcher(db)
                summary_job = dispatcher.enqueue_incident_summary_job(
                    requested_by_user_id=None,
                    incident_id=context["incident_id"],
                    enqueue_reason="audio_transcription_succeeded",
                )
                result_payload["followup_incident_summary_job_id"] = str(summary_job.id)
            finally:
                db.close()
        except Exception as followup_exc:
            result_payload["followup_incident_summary_enqueue_error"] = str(followup_exc)

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_audio_processing_failed(evidence_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.image_analysis_task")
def image_analysis_task(self, job_id: str, evidence_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_image_processing_running(evidence_id)

        context = build_image_evidence_processing_context(evidence_id)

        provider = build_vision_provider()
        result = provider.analyze_image(
            ImageAnalysisRequest(
                evidence_id=evidence_id,
                image_file_path=context["image_file_path"],
                source_url=context["source_url"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = context["incident_id"]

        mark_image_processing_succeeded(
            evidence_id=evidence_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        try:
            db = SessionLocal()
            try:
                dispatcher = PipelineDispatcher(db)
                summary_job = dispatcher.enqueue_incident_summary_job(
                    requested_by_user_id=None,
                    incident_id=context["incident_id"],
                    enqueue_reason="image_analysis_succeeded",
                )
                result_payload["followup_incident_summary_job_id"] = str(summary_job.id)
            finally:
                db.close()
        except Exception as followup_exc:
            result_payload["followup_incident_summary_enqueue_error"] = str(followup_exc)

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_image_processing_failed(evidence_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.incident_summary_task")
def incident_summary_task(self, job_id: str, incident_id: str) -> dict:
    try:
        mark_job_running(job_id, self.request.id)
        mark_incident_summary_running(incident_id)

        request_payload = build_incident_summary_request_data(incident_id)

        provider = build_llm_provider()
        result = provider.summarize_incident(
            IncidentSummaryRequest(
                incident_id=incident_id,
                user_text=request_payload["user_text"],
                transcript_text=request_payload["transcript_text"],
                image_analysis_summary=request_payload["image_analysis_summary"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["incident_id"] = incident_id

        mark_incident_summary_succeeded(
            incident_id=incident_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )

        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        mark_incident_summary_failed(incident_id, str(exc))
        mark_job_failed(job_id, str(exc))
        raise


@celery_app.task(bind=True, name="jobs.push_notification_task")
def push_notification_task(self, job_id: str, delivery_id: str) -> dict:
    provider_name = None

    try:
        mark_job_running(job_id, self.request.id)
        mark_delivery_running(delivery_id)

        context = build_push_notification_delivery_context(delivery_id)

        provider = build_push_provider()
        provider_name = provider.provider_name

        result = provider.send_push_notification(
            PushNotificationRequest(
                recipient_token=context["recipient_token"],
                title=context["title"],
                body=context["body"],
                data=context["data"],
            )
        )

        result_payload = asdict(result)
        result_payload["provider_name"] = provider.provider_name
        result_payload["delivery_id"] = delivery_id

        if not result.accepted:
            error_message = (
                result_payload.get("error_message")
                or "Push notification provider did not accept the message."
            )
            deactivate_device = _should_deactivate_device(error_message)
            mark_delivery_failed(
                delivery_id=delivery_id,
                provider_name=provider.provider_name,
                error_message=error_message,
                deactivate_device=deactivate_device,
            )
            mark_job_failed(job_id, error_message)
            return result_payload

        mark_delivery_succeeded(
            delivery_id=delivery_id,
            provider_name=provider.provider_name,
            result_payload=result_payload,
        )
        mark_job_succeeded(job_id, result_payload)
        return result_payload
    except Exception as exc:
        error_message = str(exc)
        deactivate_device = _should_deactivate_device(error_message)
        mark_delivery_failed(
            delivery_id=delivery_id,
            provider_name=provider_name,
            error_message=error_message,
            deactivate_device=deactivate_device,
        )
        mark_job_failed(job_id, error_message)
        raise


def _should_deactivate_device(error_message: str) -> bool:
    normalized_error = error_message.lower()
    return (
        "not registered" in normalized_error
        or "registration token is not a valid fcm registration token" in normalized_error
        or "requested entity was not found" in normalized_error
        or "unregistered" in normalized_error
    )
```

### `Dockerfile.dev`

- Ruta relativa: `Dockerfile.dev`
- Nombre de archivo: `Dockerfile.dev`

```text
FROM python:3.12-slim

# Prevents Python from generating .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Ensures logs are shown immediately in Docker.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies commonly needed for PostgreSQL drivers
# and some Python packages with native extensions.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/scripts/start.sh && chmod +x /app/scripts/start_worker.sh

EXPOSE 8000

CMD ["/app/scripts/start.sh"]
```

### `Dockerfile.prod`

- Ruta relativa: `Dockerfile.prod`
- Nombre de archivo: `Dockerfile.prod`

```text

```

### `requirements.txt`

- Ruta relativa: `requirements.txt`
- Nombre de archivo: `requirements.txt`

```text
fastapi>=0.115,<1.0
uvicorn[standard]>=0.30,<1.0
sqlalchemy>=2.0,<3.0
psycopg[binary]>=3.2,<4.0
alembic>=1.14,<2.0
pydantic-settings>=2.6,<3.0
PyJWT>=2.9,<3.0
pwdlib[argon2]>=0.2,<1.0
python-multipart>=0.0.9,<1.0
celery[redis]>=5.4,<6.0
redis>=5.0,<6.0
boto3>=1.35,<2.0
faster-whisper>=1.1,<2.0
ultralytics-opencv-headless>=8.4,<9.0
firebase-admin>=6.5,<7.0
```

### `scripts/start.sh`

- Ruta relativa: `scripts/start.sh`
- Nombre de archivo: `start.sh`

```bash
#!/bin/sh
set -e

echo "Waiting for PostgreSQL at ${POSTGRES_SERV}:${POSTGRES_PORT}..."
while ! nc -z "${POSTGRES_SERV}" "${POSTGRES_PORT}"; do
  sleep 1
done

echo "Waiting for Redis at ${REDIS_HOST}:${REDIS_PORT}..."
while ! nc -z "${REDIS_HOST}" "${REDIS_PORT}"; do
  sleep 1
done

echo "PostgreSQL and Redis are ready."
echo "Running migrations..."

alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### `scripts/start_worker.sh`

- Ruta relativa: `scripts/start_worker.sh`
- Nombre de archivo: `start_worker.sh`

```bash
#!/bin/sh
set -e

echo "Waiting for PostgreSQL at ${POSTGRES_SERV}:${POSTGRES_PORT}..."
while ! nc -z "${POSTGRES_SERV}" "${POSTGRES_PORT}"; do
  sleep 1
done

echo "Waiting for Redis at ${REDIS_HOST}:${REDIS_PORT}..."
while ! nc -z "${REDIS_HOST}" "${REDIS_PORT}"; do
  sleep 1
done

echo "Starting Celery worker..."
exec celery -A app.tasks.celery_app.celery_app worker --loglevel=info -Q default,audio,image,summary,push
```
