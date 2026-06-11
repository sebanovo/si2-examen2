from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class IncidentSummaryRequest:
    incident_id: str
    user_text: str | None = None
    transcript_text: str | None = None
    image_analysis_summary: str | None = None


@dataclass(slots=True)
class IncidentSummaryResult:
    structured_summary: str | None = None
    suggested_category: str | None = None
    suggested_priority: str | None = None
    requires_more_information: bool = False
    raw_response: dict[str, Any] = field(default_factory=dict)


class IncidentSummaryProvider(Protocol):
    provider_name: str

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        ...