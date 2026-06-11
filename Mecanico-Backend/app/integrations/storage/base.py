from dataclasses import dataclass
from typing import Protocol

from fastapi import UploadFile


@dataclass(slots=True)
class StoredObjectMetadata:
    storage_provider: str
    stored_filename: str
    mime_type: str | None
    file_size_bytes: int
    absolute_file_path: str | None = None
    storage_bucket: str | None = None
    storage_object_key: str | None = None
    public_url: str | None = None


@dataclass(slots=True)
class StorageDownloadDescriptor:
    kind: str  # local_file | signed_url
    filename: str
    media_type: str | None = None
    absolute_file_path: str | None = None
    download_url: str | None = None


class StorageService(Protocol):
    provider_name: str

    async def save_uploaded_file(
        self,
        incident_id: str,
        upload_file: UploadFile,
    ) -> StoredObjectMetadata:
        ...

    def save_text_content(
        self,
        incident_id: str,
        text_content: str,
    ) -> StoredObjectMetadata:
        ...

    def build_download_descriptor(
        self,
        *,
        absolute_file_path: str | None,
        storage_bucket: str | None,
        storage_object_key: str | None,
        public_url: str | None,
        original_filename: str | None,
        stored_filename: str,
        mime_type: str | None,
    ) -> StorageDownloadDescriptor:
        ...
