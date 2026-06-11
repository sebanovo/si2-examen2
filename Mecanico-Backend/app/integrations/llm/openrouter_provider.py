import json
import logging
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.common.constants import (
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OTHER,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_UNCERTAIN,
    INCIDENT_PRIORITY_CRITICAL,
    INCIDENT_PRIORITY_HIGH,
    INCIDENT_PRIORITY_LOW,
    INCIDENT_PRIORITY_MEDIUM,
    PUBLIC_INCIDENT_CATEGORIES,
)
from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.llm.base import IncidentSummaryRequest, IncidentSummaryResult

logger = logging.getLogger(__name__)


class OpenRouterIncidentSummaryProvider:
    provider_name = "openrouter"

    def __init__(self) -> None:
        self.api_key = settings.openrouter_api_key
        self.base_url = settings.openrouter_api_base_url.rstrip("/")
        self.primary_model = settings.openrouter_model
        self.fallback_models = settings.openrouter_fallback_models_list
        self.temperature = settings.openrouter_temperature
        self.max_tokens = settings.openrouter_max_tokens
        self.site_url = settings.openrouter_http_referer
        self.site_title = settings.openrouter_x_title
        self.timeout_seconds = settings.openrouter_timeout_seconds

        if not self.api_key:
            raise ConflictException(
                "OpenRouter provider is selected but OPENROUTER_API_KEY is not configured."
            )

        if not self.primary_model:
            raise ConflictException(
                "OpenRouter provider is selected but OPENROUTER_MODEL is not configured."
            )

    def summarize_incident(
        self,
        request: IncidentSummaryRequest,
    ) -> IncidentSummaryResult:
        messages = self._build_messages(request)
        request_body = self._build_request_body(messages)

        try:
            raw_response = self._send_request(request_body)
            assistant_content = self._extract_assistant_content(raw_response)
            parsed_payload = self._parse_json_payload(assistant_content)
            normalized_payload = self._normalize_payload(parsed_payload, assistant_content)

            response_metadata = {
                "provider": self.provider_name,
                "api_base_url": self.base_url,
                "requested_model": self.primary_model,
                "fallback_models": self.fallback_models,
                "response_id": raw_response.get("id"),
                "response_model": raw_response.get("model"),
                "usage": raw_response.get("usage"),
                "raw_message_content": assistant_content,
            }

            return IncidentSummaryResult(
                structured_summary=normalized_payload["structured_summary"],
                suggested_category=normalized_payload["suggested_category"],
                suggested_priority=normalized_payload["suggested_priority"],
                requires_more_information=normalized_payload["requires_more_information"],
                raw_response=response_metadata,
            )
        except (HTTPError, URLError) as exc:
            logger.exception(
                "OpenRouter request failed for incident_id=%s",
                request.incident_id,
            )
            raise ServiceUnavailableException(
                f"OpenRouter request failed: {self._build_network_error_message(exc)}"
            ) from exc
        except Exception as exc:
            logger.exception(
                "OpenRouter incident summary failed for incident_id=%s",
                request.incident_id,
            )
            raise ServiceUnavailableException(
                f"LLM provider failed: {str(exc)}"
            ) from exc

    def _build_messages(self, request: IncidentSummaryRequest) -> list[dict[str, str]]:
        allowed_categories = ", ".join(PUBLIC_INCIDENT_CATEGORIES)
        allowed_priorities = ", ".join(
            [
                INCIDENT_PRIORITY_LOW,
                INCIDENT_PRIORITY_MEDIUM,
                INCIDENT_PRIORITY_HIGH,
                INCIDENT_PRIORITY_CRITICAL,
            ]
        )

        system_prompt = f"""
You are an expert roadside assistance triage engine for a vehicular emergency platform.

Your task is to read multimodal incident information and produce a concise structured incident record.

Rules:
- Return ONLY valid JSON.
- Do not wrap the JSON in markdown.
- Do not include explanations outside the JSON.
- The JSON schema must be:
{{
  "structured_summary": "string",
  "suggested_category": "one of [{allowed_categories}]",
  "suggested_priority": "one of [{allowed_priorities}]",
  "requires_more_information": true or false
}}

Classification guidance:
- {INCIDENT_CATEGORY_BATTERY}: battery discharged, no ignition, dashboard/battery clues
- {INCIDENT_CATEGORY_TIRE}: flat tire, damaged tire, wheel issue
- {INCIDENT_CATEGORY_ACCIDENT}: visible crash, collision, impact scene, multiple vehicles, visible damage after a hit
- {INCIDENT_CATEGORY_ENGINE}: engine or mechanical failure without clear battery/tire/lockout specialization
- {INCIDENT_CATEGORY_LOCKOUT}: locked keys, door lock issue, inability to access vehicle
- {INCIDENT_CATEGORY_OVERHEATING}: overheating, steam, high temperature warnings
- {INCIDENT_CATEGORY_OTHER}: roadside assistance case that does not fit the above
- {INCIDENT_CATEGORY_UNCERTAIN}: insufficient or conflicting information

Priority guidance:
- {INCIDENT_PRIORITY_LOW}: low urgency, minor inconvenience, no safety signal
- {INCIDENT_PRIORITY_MEDIUM}: standard roadside assistance required
- {INCIDENT_PRIORITY_HIGH}: urgent roadside assistance, blocking situation, vulnerable location, or stronger risk
- {INCIDENT_PRIORITY_CRITICAL}: immediate danger, accident with possible injuries or high-risk scenario

Use requires_more_information=true when information is ambiguous, contradictory, too weak, or insufficient.
Make the summary practical for a workshop or mobile mechanic.
""".strip()

        user_sections = [
            f"Incident ID: {request.incident_id}",
            f"Client reported text:\n{request.user_text or 'N/A'}",
            f"Audio transcription:\n{request.transcript_text or 'N/A'}",
            f"Visual analysis summary:\n{request.image_analysis_summary or 'N/A'}",
        ]

        user_prompt = "\n\n".join(user_sections).strip()

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def _build_request_body(self, messages: list[dict[str, str]]) -> dict[str, Any]:
        request_body: dict[str, Any] = {
            "model": self.primary_model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stream": False,
        }

        if self.fallback_models:
            request_body["models"] = self.fallback_models

        return request_body

    def _send_request(self, request_body: dict[str, Any]) -> dict[str, Any]:
        payload_bytes = json.dumps(request_body).encode("utf-8")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if self.site_url:
            headers["HTTP-Referer"] = self.site_url

        if self.site_title:
            headers["X-OpenRouter-Title"] = self.site_title

        http_request = Request(
            url=f"{self.base_url}/chat/completions",
            data=payload_bytes,
            headers=headers,
            method="POST",
        )

        with urlopen(http_request, timeout=self.timeout_seconds) as response:
            response_body = response.read().decode("utf-8")

        return json.loads(response_body)

    def _extract_assistant_content(self, raw_response: dict[str, Any]) -> str:
        choices = raw_response.get("choices") or []
        if not choices:
            raise ServiceUnavailableException("OpenRouter response does not contain choices.")

        message = choices[0].get("message") or {}
        content = message.get("content")

        if isinstance(content, str):
            return content.strip()

        if isinstance(content, list):
            extracted_parts: list[str] = []
            for item in content:
                if isinstance(item, dict):
                    text_value = item.get("text")
                    if text_value:
                        extracted_parts.append(str(text_value))
                elif isinstance(item, str):
                    extracted_parts.append(item)

            merged_content = "\n".join(part.strip() for part in extracted_parts if part.strip()).strip()
            if merged_content:
                return merged_content

        raise ServiceUnavailableException("OpenRouter response does not contain message content.")

    def _parse_json_payload(self, assistant_content: str) -> dict[str, Any]:
        normalized_content = assistant_content.strip()

        if normalized_content.startswith("```"):
            normalized_content = self._strip_markdown_code_fence(normalized_content)

        try:
            return json.loads(normalized_content)
        except json.JSONDecodeError:
            extracted_json = self._extract_first_json_object(normalized_content)
            if extracted_json is None:
                raise
            return json.loads(extracted_json)

    def _normalize_payload(
        self,
        parsed_payload: dict[str, Any],
        raw_content: str,
    ) -> dict[str, Any]:
        structured_summary = self._normalize_summary(
            parsed_payload.get("structured_summary"),
            raw_content=raw_content,
        )

        suggested_category = self._normalize_category(
            parsed_payload.get("suggested_category")
        )

        suggested_priority = self._normalize_priority(
            parsed_payload.get("suggested_priority")
        )

        requires_more_information = self._normalize_requires_more_information(
            parsed_payload.get("requires_more_information"),
            suggested_category=suggested_category,
            structured_summary=structured_summary,
        )

        return {
            "structured_summary": structured_summary,
            "suggested_category": suggested_category,
            "suggested_priority": suggested_priority,
            "requires_more_information": requires_more_information,
        }

    def _normalize_summary(self, value: Any, raw_content: str) -> str:
        if isinstance(value, str):
            cleaned_value = value.strip()
            if cleaned_value:
                return cleaned_value

        fallback_summary = raw_content.strip()
        if fallback_summary:
            return fallback_summary[:4000]

        return "No se pudo generar un resumen estructurado del incidente."

    def _normalize_category(self, value: Any) -> str:
        if not isinstance(value, str):
            return INCIDENT_CATEGORY_UNCERTAIN

        normalized_value = value.strip().upper()
        if normalized_value in PUBLIC_INCIDENT_CATEGORIES:
            return normalized_value

        category_aliases = {
            "COLLISION": INCIDENT_CATEGORY_ACCIDENT,
            "CRASH": INCIDENT_CATEGORY_ACCIDENT,
            "CHOQUE": INCIDENT_CATEGORY_ACCIDENT,
            "FLAT_TIRE": INCIDENT_CATEGORY_TIRE,
            "TYRE": INCIDENT_CATEGORY_TIRE,
            "TIRE": INCIDENT_CATEGORY_TIRE,
            "BATTERY_ISSUE": INCIDENT_CATEGORY_BATTERY,
            "ENGINE_FAILURE": INCIDENT_CATEGORY_ENGINE,
            "OVERHEAT": INCIDENT_CATEGORY_OVERHEATING,
            "LOCKED_OUT": INCIDENT_CATEGORY_LOCKOUT,
            "UNKNOWN": INCIDENT_CATEGORY_UNCERTAIN,
        }

        return category_aliases.get(normalized_value, INCIDENT_CATEGORY_UNCERTAIN)

    def _normalize_priority(self, value: Any) -> str:
        allowed_priorities = {
            INCIDENT_PRIORITY_LOW,
            INCIDENT_PRIORITY_MEDIUM,
            INCIDENT_PRIORITY_HIGH,
            INCIDENT_PRIORITY_CRITICAL,
        }

        if not isinstance(value, str):
            return INCIDENT_PRIORITY_MEDIUM

        normalized_value = value.strip().upper()
        if normalized_value in allowed_priorities:
            return normalized_value

        priority_aliases = {
            "NORMAL": INCIDENT_PRIORITY_MEDIUM,
            "URGENT": INCIDENT_PRIORITY_HIGH,
            "VERY_HIGH": INCIDENT_PRIORITY_HIGH,
            "EMERGENCY": INCIDENT_PRIORITY_CRITICAL,
        }

        return priority_aliases.get(normalized_value, INCIDENT_PRIORITY_MEDIUM)

    def _normalize_requires_more_information(
        self,
        value: Any,
        suggested_category: str,
        structured_summary: str,
    ) -> bool:
        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            normalized_value = value.strip().lower()
            if normalized_value in {"true", "yes", "1"}:
                return True
            if normalized_value in {"false", "no", "0"}:
                return False

        if suggested_category == INCIDENT_CATEGORY_UNCERTAIN:
            return True

        if not structured_summary or len(structured_summary.strip()) < 20:
            return True

        return False

    def _strip_markdown_code_fence(self, content: str) -> str:
        stripped = content.strip()

        if stripped.startswith("```json"):
            stripped = stripped[len("```json"):].strip()
        elif stripped.startswith("```"):
            stripped = stripped[len("```"):].strip()

        if stripped.endswith("```"):
            stripped = stripped[:-3].strip()

        return stripped

    def _extract_first_json_object(self, content: str) -> str | None:
        start_index = content.find("{")
        end_index = content.rfind("}")

        if start_index == -1 or end_index == -1 or end_index <= start_index:
            return None

        return content[start_index : end_index + 1]

    def _build_network_error_message(self, exc: HTTPError | URLError) -> str:
        if isinstance(exc, HTTPError):
            try:
                response_body = exc.read().decode("utf-8")
            except Exception:
                response_body = ""

            if response_body:
                return f"HTTP {exc.code}: {response_body}"

            return f"HTTP {exc.code}: {exc.reason}"

        return str(exc.reason)
