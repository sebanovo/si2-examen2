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
