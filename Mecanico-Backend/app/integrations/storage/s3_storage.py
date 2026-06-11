import mimetypes
from pathlib import Path
from uuid import uuid4

import boto3
from botocore.client import BaseClient

from fastapi import UploadFile

from app.common.exceptions import ConflictException
from app.core.config import settings
from app.integrations.storage.base import (
    StorageDownloadDescriptor,
    StorageService,
    StoredObjectMetadata,
)


class S3StorageService(StorageService):
    provider_name = "s3"

    def __init__(self) -> None:
        self.bucket_name = settings.s3_bucket_name
        self.region = settings.s3_region
        self.endpoint_url = settings.s3_endpoint_url
        self.public_base_url = settings.s3_public_base_url
        self.presigned_expiration_seconds = settings.s3_presigned_url_expiration_seconds

        self.client: BaseClient = boto3.client(
            "s3",
            region_name=self.region,
            aws_access_key_id=settings.s3_access_key_id,
            aws_secret_access_key=settings.s3_secret_access_key,
            endpoint_url=self.endpoint_url,
        )

    async def save_uploaded_file(
        self,
        incident_id: str,
        upload_file: UploadFile,
    ) -> StoredObjectMetadata:
        self._ensure_bucket_name()

        file_bytes = await upload_file.read()

        if not file_bytes:
            raise ConflictException("Uploaded file is empty.")

        if len(file_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Uploaded file exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        original_filename = upload_file.filename or "uploaded_file"
        safe_extension = Path(original_filename).suffix.lower()
        generated_filename = f"{uuid4().hex}{safe_extension}"
        object_key = self._build_object_key(incident_id, generated_filename)
        mime_type = upload_file.content_type or self.guess_mime_type(original_filename)

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=object_key,
            Body=file_bytes,
            ContentType=mime_type or "application/octet-stream",
        )

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type=mime_type,
            file_size_bytes=len(file_bytes),
            absolute_file_path=None,
            storage_bucket=self.bucket_name,
            storage_object_key=object_key,
            public_url=self._build_public_url(object_key),
        )

    def save_text_content(
        self,
        incident_id: str,
        text_content: str,
    ) -> StoredObjectMetadata:
        self._ensure_bucket_name()

        cleaned_text = text_content.strip()

        if not cleaned_text:
            raise ConflictException("Text evidence cannot be empty.")

        text_bytes = cleaned_text.encode("utf-8")

        if len(text_bytes) > settings.max_upload_size_bytes:
            raise ConflictException(
                f"Text evidence exceeds the maximum allowed size of {settings.max_upload_size_bytes} bytes."
            )

        generated_filename = f"{uuid4().hex}.txt"
        object_key = self._build_object_key(incident_id, generated_filename)

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=object_key,
            Body=text_bytes,
            ContentType="text/plain",
        )

        return StoredObjectMetadata(
            storage_provider=self.provider_name,
            stored_filename=generated_filename,
            mime_type="text/plain",
            file_size_bytes=len(text_bytes),
            absolute_file_path=None,
            storage_bucket=self.bucket_name,
            storage_object_key=object_key,
            public_url=self._build_public_url(object_key),
        )

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
        bucket_name = storage_bucket or self.bucket_name

        if not bucket_name:
            raise ConflictException("S3 evidence does not contain a bucket reference.")

        if not storage_object_key:
            raise ConflictException("S3 evidence does not contain an object key.")

        filename = original_filename or stored_filename

        params = {
            "Bucket": bucket_name,
            "Key": storage_object_key,
            "ResponseContentDisposition": f'attachment; filename="{filename}"',
        }

        if mime_type:
            params["ResponseContentType"] = mime_type

        signed_url = self.client.generate_presigned_url(
            ClientMethod="get_object",
            Params=params,
            ExpiresIn=self.presigned_expiration_seconds,
        )

        return StorageDownloadDescriptor(
            kind="signed_url",
            filename=filename,
            media_type=mime_type or "application/octet-stream",
            absolute_file_path=None,
            download_url=signed_url,
        )

    def _build_object_key(self, incident_id: str, filename: str) -> str:
        return f"incidents/{incident_id}/{filename}"

    def _ensure_bucket_name(self) -> None:
        if not self.bucket_name:
            raise ConflictException(
                "S3 storage provider is selected but S3_BUCKET_NAME is not configured."
            )

    def _build_public_url(self, object_key: str) -> str | None:
        if not self.public_base_url:
            return None

        return f"{self.public_base_url.rstrip('/')}/{object_key}"

    def guess_mime_type(self, filename: str) -> str:
        guessed_type, _ = mimetypes.guess_type(filename)
        return guessed_type or "application/octet-stream"
