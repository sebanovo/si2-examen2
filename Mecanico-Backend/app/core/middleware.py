import time
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.core.config import settings
from app.core.security import decode_access_token
from app.services.audit.dispatcher import AuditEventDispatcher


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get(settings.request_id_header_name) or str(uuid4())
        request.state.request_id = request_id
        start_time = time.perf_counter()

        response = await call_next(request)

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        response.headers[settings.request_id_header_name] = request_id
        response.headers[settings.response_time_header_name] = str(elapsed_ms)

        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if not settings.security_headers_enabled:
            return response

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

        if settings.https_redirect_enabled:
            response.headers["Strict-Transport-Security"] = (
                f"max-age={settings.hsts_max_age_seconds}; includeSubDomains"
            )

        return response


class AuditHttpMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if not settings.audit_http_enabled:
            return response

        normalized_path = request.url.path
        if request.method.upper() not in settings.audit_http_methods_list:
            return response

        if any(normalized_path.startswith(path) for path in settings.audit_excluded_paths_list):
            return response

        actor_user_id = self._extract_actor_user_id(request)
        request_id = getattr(request.state, "request_id", None)

        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=None,
                provider_id=None,
                request_id=request_id,
                event_scope="HTTP",
                event_type="HTTP_REQUEST",
                entity_type="ROUTE",
                entity_id=normalized_path,
                http_method=request.method.upper(),
                route_path=normalized_path,
                ip_address=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                status_code=response.status_code,
                outcome="SUCCESS" if response.status_code < 400 else "ERROR",
                payload_json={
                    "query_param_keys": sorted(list(request.query_params.keys())),
                    "response_time_ms": response.headers.get(settings.response_time_header_name),
                },
            )
        except Exception:
            return response

        return response

    def _extract_actor_user_id(self, request: Request) -> str | None:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return None

        if not authorization_header.lower().startswith("bearer "):
            return None

        token = authorization_header.split(" ", 1)[1].strip()
        if not token:
            return None

        try:
            payload = decode_access_token(token)
        except Exception:
            return None

        user_id = payload.get("sub")
        return str(user_id) if user_id else None
