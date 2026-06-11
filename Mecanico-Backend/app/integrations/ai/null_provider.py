from app.integrations.ai.base import (
    AIIncidentAnalysisRequest,
    AIIncidentAnalysisResult,
)


class NullIncidentAIProvider:
    provider_name = "null"

    def analyze_incident(
        self,
        request: AIIncidentAnalysisRequest,
    ) -> AIIncidentAnalysisResult:
        return AIIncidentAnalysisResult(
            category="unknown",
            summary=(
                "No AI provider has been configured yet. "
                "This is a placeholder adapter prepared for future integration."
            ),
            confidence=0.0,
            requires_more_information=True,
            raw_response={
                "provider": self.provider_name,
                "incident_id": request.incident_id,
            },
        )