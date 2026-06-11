from app.integrations.llm.base import IncidentSummaryRequest, IncidentSummaryResult


class NullIncidentSummaryProvider:
    provider_name = "null"

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        return IncidentSummaryResult(
            structured_summary=(
                "No LLM provider has been configured yet. "
                "This is a placeholder incident summary."
            ),
            suggested_category="UNCERTAIN",
            suggested_priority="MEDIUM",
            requires_more_information=True,
            raw_response={
                "provider": self.provider_name,
                "incident_id": request.incident_id,
            },
        )