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
