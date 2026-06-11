import json
import threading

import firebase_admin
from firebase_admin import credentials, messaging

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.push.base import PushNotificationRequest, PushNotificationResult


class FirebaseFcmPushNotificationProvider:
    provider_name = "firebase_fcm"

    _firebase_app = None
    _firebase_app_lock = threading.Lock()

    def __init__(self) -> None:
        if not settings.firebase_project_id and not settings.firebase_service_account_json_normalized:
            raise ConflictException(
                "Firebase FCM provider is selected but Firebase credentials are not configured."
            )

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        firebase_app = self._get_or_initialize_app()

        normalized_data = {
            str(key): str(value)
            for key, value in (request.data or {}).items()
            if value is not None
        }

        message = messaging.Message(
            token=request.recipient_token,
            notification=messaging.Notification(
                title=request.title,
                body=request.body,
            ),
            data=normalized_data or None,
        )

        try:
            provider_message_id = messaging.send(message, app=firebase_app)

            return PushNotificationResult(
                accepted=True,
                provider_message_id=provider_message_id,
                raw_response={
                    "provider": self.provider_name,
                    "project_id": settings.firebase_project_id,
                    "device_token_suffix": request.recipient_token[-12:],
                    "data_keys": sorted(normalized_data.keys()),
                },
            )
        except Exception as exc:
            raise ServiceUnavailableException(
                f"Firebase FCM push failed: {str(exc)}"
            ) from exc

    def _get_or_initialize_app(self):
        existing_app = self.__class__._firebase_app
        if existing_app is not None:
            return existing_app

        with self.__class__._firebase_app_lock:
            existing_app = self.__class__._firebase_app
            if existing_app is not None:
                return existing_app

            credential_info = self._build_credential_info()
            firebase_credential = credentials.Certificate(credential_info)

            options = {}
            project_id = credential_info.get("project_id") or settings.firebase_project_id
            if project_id:
                options["projectId"] = project_id

            self.__class__._firebase_app = firebase_admin.initialize_app(
                credential=firebase_credential,
                options=options or None,
            )
            return self.__class__._firebase_app

    def _build_credential_info(self) -> dict:
        raw_service_account_json = settings.firebase_service_account_json_normalized
        if raw_service_account_json:
            try:
                credential_info = json.loads(raw_service_account_json)
            except json.JSONDecodeError as exc:
                raise ConflictException(
                    "FIREBASE_SERVICE_ACCOUNT_JSON is not valid JSON."
                ) from exc

            private_key = credential_info.get("private_key")
            if isinstance(private_key, str):
                credential_info["private_key"] = private_key.replace("\\n", "\n")

            return credential_info

        private_key = settings.firebase_private_key_normalized
        if not private_key:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_PRIVATE_KEY is not configured."
            )

        if not settings.firebase_client_email:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_CLIENT_EMAIL is not configured."
            )

        project_id = settings.firebase_project_id
        if not project_id:
            raise ConflictException(
                "Firebase FCM provider is selected but FIREBASE_PROJECT_ID is not configured."
            )

        return {
            "type": settings.firebase_service_account_type,
            "project_id": project_id,
            "private_key_id": settings.firebase_private_key_id or "env",
            "private_key": private_key,
            "client_email": settings.firebase_client_email,
            "client_id": settings.firebase_client_id or "env",
            "token_uri": settings.firebase_token_uri,
        }
