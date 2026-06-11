from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class EvidenceUploaderResponse(BaseModel):
    id: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None


class IncidentEvidenceResponse(BaseModel):
    id: str
    incident_id: str
    uploaded_by_user_id: str | None = None
    evidence_type: str
    original_filename: str | None = None
    stored_filename: str
    file_extension: str | None = None
    mime_type: str | None = None
    file_size_bytes: int | None = None
    description: str | None = None
    text_content_snapshot: str | None = None

    storage_provider: str
    storage_bucket: str | None = None
    storage_object_key: str | None = None
    public_url: str | None = None
    download_url: str

    audio_processing_status: str
    audio_provider_name: str | None = None
    transcript_text: str | None = None
    transcript_language_code: str | None = None
    transcript_confidence: float | None = None
    transcript_segments_json: list[dict] | list | None = None
    audio_processed_at: datetime | None = None
    audio_error_message: str | None = None

    image_processing_status: str
    image_provider_name: str | None = None
    image_labels_json: list[str] | list | None = None
    image_detections_json: list[dict] | list | None = None
    image_summary: str | None = None
    image_processed_at: datetime | None = None
    image_error_message: str | None = None

    created_at: datetime
    updated_at: datetime
    uploaded_by_user: EvidenceUploaderResponse | None = None


class CreateTextEvidenceRequest(BaseModel):
    description: str | None = None
    text_content: str = Field(min_length=1)
    evidence_type: Literal["TEXT"] = "TEXT"
