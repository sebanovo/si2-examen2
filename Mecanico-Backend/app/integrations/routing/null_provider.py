import math

from app.core.config import settings
from app.integrations.routing.base import RouteCalculationRequest, RouteCalculationResult


class NullRoutingProvider:
    provider_name = "null_haversine"

    def calculate_route(
        self,
        request: RouteCalculationRequest,
    ) -> RouteCalculationResult:
        distance_meters = self._haversine_distance_meters(
            request.origin_latitude,
            request.origin_longitude,
            request.destination_latitude,
            request.destination_longitude,
        )

        average_speed_kmh = max(settings.fallback_routing_average_speed_kmh, 1)
        duration_seconds = int((distance_meters / 1000.0) / average_speed_kmh * 3600)

        return RouteCalculationResult(
            distance_meters=round(distance_meters, 2),
            duration_seconds=max(duration_seconds, 0),
            polyline=None,
            raw_response={
                "provider": self.provider_name,
                "approximation": "haversine",
                "average_speed_kmh": average_speed_kmh,
            },
        )

    def _haversine_distance_meters(
        self,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float,
    ) -> float:
        earth_radius_m = 6371000.0

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2) ** 2
            + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return earth_radius_m * c
