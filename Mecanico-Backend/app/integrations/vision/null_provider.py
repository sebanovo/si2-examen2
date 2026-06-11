from app.integrations.vision.base import ImageAnalysisRequest, ImageAnalysisResult


class NullVisionAnalysisProvider:
    provider_name = "null"

    def analyze_image(
        self,
        request: ImageAnalysisRequest,
    ) -> ImageAnalysisResult:
        return ImageAnalysisResult(
            labels=["unknown"],
            detections=[],
            summary=(
                "No vision provider has been configured yet. "
                "This is a placeholder image analysis result."
            ),
            raw_response={
                "provider": self.provider_name,
                "evidence_id": request.evidence_id,
            },
        )