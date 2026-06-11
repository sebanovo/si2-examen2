from app.integrations.speech_to_text.base import (
    AudioTranscriptionRequest,
    AudioTranscriptionResult,
)


class NullSpeechToTextProvider:
    provider_name = "null"

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        return AudioTranscriptionResult(
            transcript_text=(
                "No speech-to-text provider has been configured yet. "
                "This is a placeholder transcription result."
            ),
            language_code="unknown",
            confidence=0.0,
            segments=[],
            raw_response={
                "provider": self.provider_name,
                "evidence_id": request.evidence_id,
            },
        )