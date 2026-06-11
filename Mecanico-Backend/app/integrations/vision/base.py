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