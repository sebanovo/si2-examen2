import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from app.common.exceptions import ConflictException, ServiceUnavailableException
from app.core.config import settings
from app.integrations.routing.base import RouteCalculationRequest, RouteCalculationResult


class GraphHopperRoutingProvider:
    provider_name = "graphhopper"

    def __init__(self) -> None:
        self.api_key = settings.graphhopper_api_key
        self.api_base_url = settings.graphhopper_api_base_url.rstrip("/")
        self.default_profile = settings.graphhopper_profile
        self.timeout_seconds = settings.graphhopper_timeout_seconds
        self.points_encoded = settings.graphhopper_points_encoded

        if not self.api_key:
            raise ConflictException(
                "GraphHopper provider is selected but GRAPHHOPPER_API_KEY is not configured."
            )

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        profile = request.profile or self.default_profile

        query_params = [
            ("point", f"{request.origin_latitude},{request.origin_longitude}"),
            ("point", f"{request.destination_latitude},{request.destination_longitude}"),
            ("profile", profile),
            ("instructions", "false"),
            ("calc_points", "true"),
            ("points_encoded", "true" if self.points_encoded else "false"),
            ("key", self.api_key),
        ]

        url = f"{self.api_base_url}/route?{urlencode(query_params)}"

        try:
            with urlopen(url, timeout=self.timeout_seconds) as response:
                response_body = response.read().decode("utf-8")

            payload = json.loads(response_body)
            paths = payload.get("paths") or []
            if not paths:
                raise ServiceUnavailableException("GraphHopper response did not contain paths.")

            path = paths[0]
            distance_meters = path.get("distance")
            duration_millis = path.get("time")
            polyline = path.get("points")

            return RouteCalculationResult(
                distance_meters=float(distance_meters) if distance_meters is not None else None,
                duration_seconds=int(duration_millis / 1000) if duration_millis is not None else None,
                polyline=polyline if isinstance(polyline, str) else None,
                raw_response={
                    "provider": self.provider_name,
                    "profile": profile,
                    "raw_path": path,
                },
            )
        except HTTPError as exc:
            try:
                error_body = exc.read().decode("utf-8")
            except Exception:
                error_body = str(exc)

            raise ServiceUnavailableException(
                f"GraphHopper request failed with HTTP {exc.code}: {error_body}"
            ) from exc
        except URLError as exc:
            raise ServiceUnavailableException(
                f"GraphHopper request failed: {str(exc.reason)}"
            ) from exc
