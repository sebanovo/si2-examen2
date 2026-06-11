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
