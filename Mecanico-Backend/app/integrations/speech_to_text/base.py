from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class AudioTranscriptionRequest:
    evidence_id: str
    audio_file_path: str | None = None
    source_url: str | None = None
    language_hint: str | None = None


@dataclass(slots=True)
class AudioTranscriptionResult:
    transcript_text: str | None = None
    language_code: str | None = None
    confidence: float | None = None
    segments: list[dict[str, Any]] = field(default_factory=list)
    raw_response: dict[str, Any] = field(default_factory=dict)


class SpeechToTextProvider(Protocol):
    provider_name: str

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        ...