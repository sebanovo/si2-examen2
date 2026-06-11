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