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
from app.services.ratings import models as ratings_models  # noqa: F401
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
