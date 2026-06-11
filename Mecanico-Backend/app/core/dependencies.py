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
