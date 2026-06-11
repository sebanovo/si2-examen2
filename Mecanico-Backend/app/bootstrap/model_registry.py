"""
Registro central de modelos SQLAlchemy.

Este archivo importa todos los modelos para que SQLAlchemy pueda resolver
relaciones declaradas con strings, por ejemplo relationship("ProviderService").
"""

from app.services.auth import models as auth_models  # noqa: F401
from app.services.catalog import models as catalog_models  # noqa: F401
from app.services.providers import models as providers_models  # noqa: F401
from app.services.vehicles import models as vehicles_models  # noqa: F401
from app.services.incidents import models as incidents_models  # noqa: F401
from app.services.evidences import models as evidences_models  # noqa: F401
from app.services.assignment import models as assignment_models  # noqa: F401
from app.services.operations import models as operations_models  # noqa: F401
from app.services.tracking import models as tracking_models  # noqa: F401
from app.services.billing import models as billing_models  # noqa: F401
from app.services.subscriptions import models as subscriptions_models  # noqa: F401
from app.services.jobs import models as jobs_models  # noqa: F401
from app.services.notifications import models as notifications_models  # noqa: F401
from app.services.ratings import models as ratings_models  # noqa: F401
from app.services.audit import models as audit_models  # noqa: F401