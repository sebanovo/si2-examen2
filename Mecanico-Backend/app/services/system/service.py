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
