import logging
import os
import tempfile
import threading
from pathlib import Path
from statistics import mean
from typing import Any
from urllib.parse import urlparse
from urllib.request import urlopen

from faster_whisper import WhisperModel

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.speech_to_text.base import (
    AudioTranscriptionRequest,
    AudioTranscriptionResult,
)

logger = logging.getLogger(__name__)


class FasterWhisperSpeechToTextProvider:
    provider_name = "faster_whisper"

    _model_cache: dict[tuple[str, str, str], WhisperModel] = {}
    _model_cache_lock = threading.Lock()

    def __init__(self) -> None:
        self.model_size = settings.faster_whisper_model_size
        self.device = settings.faster_whisper_device
        self.compute_type = settings.faster_whisper_compute_type
        self.beam_size = settings.faster_whisper_beam_size
        self.vad_filter = settings.faster_whisper_vad_filter
        self.word_timestamps = settings.faster_whisper_word_timestamps
        self.condition_on_previous_text = settings.faster_whisper_condition_on_previous_text
        self.language = settings.faster_whisper_language
        self.download_timeout_seconds = settings.faster_whisper_download_timeout_seconds

    def transcribe_audio(
        self,
        request: AudioTranscriptionRequest,
    ) -> AudioTranscriptionResult:
        audio_source_path, cleanup_path = self._resolve_audio_source(request)

        try:
            model = self._get_or_create_model()

            transcribe_kwargs: dict[str, Any] = {
                "beam_size": self.beam_size,
                "vad_filter": self.vad_filter,
                "word_timestamps": self.word_timestamps,
                "condition_on_previous_text": self.condition_on_previous_text,
                "task": "transcribe",
            }

            language_hint = request.language_hint or self.language
            if language_hint:
                transcribe_kwargs["language"] = language_hint

            segments, info = model.transcribe(audio_source_path, **transcribe_kwargs)
            segment_items = []
            transcript_parts: list[str] = []
            word_probabilities: list[float] = []

            for index, segment in enumerate(list(segments), start=1):
                cleaned_text = (segment.text or "").strip()
                if cleaned_text:
                    transcript_parts.append(cleaned_text)

                segment_words = []
                if getattr(segment, "words", None):
                    for word in segment.words:
                        probability = getattr(word, "probability", None)
                        if probability is not None:
                            word_probabilities.append(float(probability))

                        segment_words.append(
                            {
                                "start": getattr(word, "start", None),
                                "end": getattr(word, "end", None),
                                "word": getattr(word, "word", None),
                                "probability": probability,
                            }
                        )

                segment_items.append(
                    {
                        "segment_index": index,
                        "seek": getattr(segment, "seek", None),
                        "start": getattr(segment, "start", None),
                        "end": getattr(segment, "end", None),
                        "text": cleaned_text,
                        "avg_logprob": getattr(segment, "avg_logprob", None),
                        "no_speech_prob": getattr(segment, "no_speech_prob", None),
                        "compression_ratio": getattr(segment, "compression_ratio", None),
                        "words": segment_words,
                    }
                )

            transcript_text = "\n".join(part for part in transcript_parts if part).strip() or None
            transcript_confidence = (
                float(mean(word_probabilities))
                if word_probabilities
                else float(getattr(info, "language_probability", 0.0) or 0.0)
            )

            raw_response = {
                "provider": self.provider_name,
                "model_size": self.model_size,
                "device": self.device,
                "compute_type": self.compute_type,
                "beam_size": self.beam_size,
                "vad_filter": self.vad_filter,
                "word_timestamps": self.word_timestamps,
                "detected_language": getattr(info, "language", None),
                "language_probability": getattr(info, "language_probability", None),
                "duration": getattr(info, "duration", None),
                "duration_after_vad": getattr(info, "duration_after_vad", None),
            }

            return AudioTranscriptionResult(
                transcript_text=transcript_text,
                language_code=getattr(info, "language", None),
                confidence=transcript_confidence,
                segments=segment_items,
                raw_response=raw_response,
            )
        except Exception as exc:
            logger.exception("faster-whisper transcription failed for evidence_id=%s", request.evidence_id)
            raise ServiceUnavailableException(
                f"Speech-to-text provider failed: {str(exc)}"
            ) from exc
        finally:
            if cleanup_path and os.path.exists(cleanup_path):
                try:
                    os.remove(cleanup_path)
                except OSError:
                    logger.warning("Temporary audio file could not be removed: %s", cleanup_path)

    def _get_or_create_model(self) -> WhisperModel:
        cache_key = (self.model_size, self.device, self.compute_type)

        with self._model_cache_lock:
            existing_model = self._model_cache.get(cache_key)
            if existing_model is not None:
                return existing_model

            logger.info(
                "Loading faster-whisper model size=%s device=%s compute_type=%s",
                self.model_size,
                self.device,
                self.compute_type,
            )
            model = WhisperModel(
                self.model_size,
                device=self.device,
                compute_type=self.compute_type,
            )
            self._model_cache[cache_key] = model
            return model

    def _resolve_audio_source(
        self,
        request: AudioTranscriptionRequest,
    ) -> tuple[str, str | None]:
        if request.audio_file_path:
            audio_path = Path(request.audio_file_path).resolve()
            if not audio_path.exists():
                raise ConflictException("Audio file path does not exist for transcription.")
            return str(audio_path), None

        if request.source_url:
            temporary_file_path = self._download_remote_audio_to_tempfile(request.source_url)
            return temporary_file_path, temporary_file_path

        raise ConflictException("No audio source was provided for transcription.")

    def _download_remote_audio_to_tempfile(self, source_url: str) -> str:
        suffix = self._infer_suffix_from_url(source_url)

        with urlopen(source_url, timeout=self.download_timeout_seconds) as response:
            file_bytes = response.read()

        if not file_bytes:
            raise ConflictException("Remote audio source is empty.")

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temporary_file:
            temporary_file.write(file_bytes)
            temporary_file.flush()
            return temporary_file.name

    def _infer_suffix_from_url(self, source_url: str) -> str:
        parsed_url = urlparse(source_url)
        suffix = Path(parsed_url.path).suffix.lower()
        return suffix or ".audio"
