from app.integrations.push.base import PushNotificationRequest, PushNotificationResult


class NullPushNotificationProvider:
    provider_name = "null"

    def send_push_notification(
        self,
        request: PushNotificationRequest,
    ) -> PushNotificationResult:
        return PushNotificationResult(
            accepted=False,
            provider_message_id=None,
            raw_response={
                "provider": self.provider_name,
                "recipient_token": request.recipient_token,
                "title": request.title,
            },
        )