from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class RouteCalculationRequest:
    origin_latitude: float
    origin_longitude: float
    destination_latitude: float
    destination_longitude: float
    profile: str | None = None


@dataclass(slots=True)
class RouteCalculationResult:
    distance_meters: float | None
    duration_seconds: int | None
    polyline: str | None
    raw_response: dict | None = None


class RoutingProvider(Protocol):
    provider_name: str

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        ...
