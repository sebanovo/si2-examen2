from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.bootstrap.seed import seed_initial_platform_admin
from app.common.exceptions import register_exception_handlers
from app.common.openapi import API_DESCRIPTION, OPENAPI_TAGS, configure_openapi
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
from app.services.ratings.router import router as ratings_router
from app.services.subscriptions.router import router as subscriptions_router
from app.services.system.router import router as system_router
from app.services.tracking.router import router as tracking_router
from app.services.technician_mobile.router import router as technician_mobile_router
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
        title="Mechanic System Emergency Assistance API",
        version=settings.app_version,
        summary="API backend para atención inteligente de emergencias vehiculares.",
        description=API_DESCRIPTION,
        contact={
            "name": "Mechanic System Backend Team",
            "email": "backend@mechanic.local",
        },
        openapi_tags=OPENAPI_TAGS,
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
    application.include_router(ratings_router, prefix=settings.api_v1_prefix)
    application.include_router(catalog_router, prefix=settings.api_v1_prefix)
    application.include_router(vehicles_router, prefix=settings.api_v1_prefix)
    application.include_router(incidents_router, prefix=settings.api_v1_prefix)
    application.include_router(evidences_router, prefix=settings.api_v1_prefix)
    application.include_router(jobs_router, prefix=settings.api_v1_prefix)
    application.include_router(assignment_router, prefix=settings.api_v1_prefix)
    application.include_router(operations_router, prefix=settings.api_v1_prefix)
    application.include_router(tracking_router, prefix=settings.api_v1_prefix)
    application.include_router(technician_mobile_router, prefix=settings.api_v1_prefix)
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

    configure_openapi(application)

    return application


app = create_application()
application = app
