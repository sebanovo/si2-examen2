from collections.abc import Mapping
from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from pydantic import BaseModel, ConfigDict, Field


class ApiResponse(BaseModel):
    success: bool = Field(default=True, description="Indica si la operación fue exitosa.")
    message: str = Field(description="Mensaje legible para mostrar o registrar en el frontend.")
    data: Any | None = Field(default=None, description="Payload principal de la respuesta.")
    meta: dict[str, Any] | None = Field(
        default=None,
        description="Metadatos de paginación, conteos o trazabilidad.",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Operation completed successfully.",
                "data": {"id": "uuid-value"},
                "meta": {"request_id": "req_01HZX9Y9K2"},
            }
        }
    )


class ApiErrorBody(BaseModel):
    code: str = Field(description="Código estable del error para manejo programático.")
    details: list[Any] | None = Field(
        default=None,
        description="Detalle adicional del error, especialmente validaciones 422.",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "code": "validation_error",
                "details": [
                    {
                        "type": "missing",
                        "loc": ["body", "email"],
                        "msg": "Field required",
                        "input": {},
                    }
                ],
            }
        }
    )


class ApiErrorResponse(BaseModel):
    success: bool = Field(default=False, description="Siempre false para respuestas de error.")
    message: str = Field(description="Mensaje legible del error.")
    error: ApiErrorBody = Field(description="Código y detalle del error.")
    meta: dict[str, Any] | None = Field(
        default=None,
        description="Metadatos de trazabilidad. Incluye request_id cuando está disponible.",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "message": "Validation error.",
                "error": {
                    "code": "validation_error",
                    "details": [
                        {
                            "type": "missing",
                            "loc": ["body", "email"],
                            "msg": "Field required",
                            "input": {},
                        }
                    ],
                },
                "meta": {"request_id": "req_01HZX9Y9K2"},
            }
        }
    )


API_DESCRIPTION = """
Backend FastAPI para una plataforma inteligente de atención de emergencias vehiculares.

La API usa JSON y un formato de respuesta estable para que Angular pueda consumirla de forma uniforme:

```json
{
  "success": true,
  "message": "string",
  "data": {},
  "meta": {}
}
```

Los errores siguen la misma envoltura, con un objeto `error`:

```json
{
  "success": false,
  "message": "string",
  "error": {
    "code": "string",
    "details": []
  },
  "meta": {
    "request_id": "string"
  }
}
```

Autenticación:

- Usa el botón **Authorize** de Swagger con un Bearer Token JWT.
- El header enviado por Angular debe ser `Authorization: Bearer <access_token>`.
- Endpoints públicos como registro, login, health, readiness e info no requieren token.

Enums relevantes:

- Roles: `CLIENT`, `PROVIDER_ADMIN`, `TECHNICIAN`, `PLATFORM_ADMIN`.
- Estados de incidente: `PENDING`, `IN_REVIEW`, `PUBLISHED`, `ASSIGNED`, `EN_ROUTE`, `ON_SITE`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED`.
- Prioridades: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.
- Categorías: `BATTERY`, `TIRE`, `ACCIDENT`, `ENGINE`, `LOCKOUT`, `OVERHEATING`, `OTHER`, `UNCERTAIN`.
- Estados de pago: `PENDING_PRICING`, `ESTIMATED`, `PENDING_PAYMENT`, `PAID`, `CANCELLED`.
- Plataformas de dispositivo: `ANDROID`, `IOS`, `WEB`.
"""


OPENAPI_TAGS = [
    {"name": "Root", "description": "Punto de entrada con enlaces base de la API."},
    {"name": "System", "description": "Salud, readiness, información del sistema y métricas."},
    {"name": "Auth", "description": "Registro, login y perfil del usuario autenticado."},
    {"name": "Users", "description": "Perfil propio y administración de usuarios."},
    {"name": "Providers", "description": "Onboarding, perfil, disponibilidad y técnicos de talleres o mecánicos."},
    {"name": "Catalog", "description": "Catálogo de servicios y configuración de servicios ofrecidos."},
    {"name": "Vehicles", "description": "Vehículos del cliente autenticado."},
    {"name": "Incidents", "description": "Creación, consulta y ciclo inicial de incidentes vehiculares."},
    {"name": "Evidences", "description": "Evidencias de incidentes: imágenes, audio, texto y descarga."},
    {"name": "Jobs", "description": "Trabajos asíncronos de IA, transcripción, visión y resumen."},
    {"name": "Assignment", "description": "Publicación de incidentes y gestión de candidatos proveedores."},
    {"name": "Operations", "description": "Despacho, avance operativo, cierre e historial del servicio."},
    {"name": "Tracking", "description": "Ubicación, rutas, ETA y tracking en vivo o histórico."},
    {"name": "Notifications", "description": "Tokens de dispositivo, pruebas push y entregas de notificaciones."},
    {"name": "Billing", "description": "Estimaciones, checkout, precios finales y estado de pago."},
    {"name": "Subscriptions", "description": "Planes, coberturas, suscripciones y aplicación de cobertura."},
    {"name": "Audit", "description": "Logs de auditoría y snapshots de métricas para administración."},
]


ERROR_EXAMPLES: dict[int, dict[str, Any]] = {
    400: {"success": False, "message": "Invalid request.", "error": {"code": "app_error"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
    401: {"success": False, "message": "Bearer token is required.", "error": {"code": "unauthorized"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
    403: {"success": False, "message": "You do not have the required role to access this resource.", "error": {"code": "forbidden"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
    404: {"success": False, "message": "Resource not found.", "error": {"code": "not_found"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
    409: {"success": False, "message": "Resource already exists.", "error": {"code": "conflict"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
    422: ApiErrorResponse.model_config["json_schema_extra"]["example"],
    500: {"success": False, "message": "Internal server error.", "error": {"code": "internal_server_error"}, "meta": {"request_id": "req_01HZX9Y9K2"}},
}


ERROR_DESCRIPTIONS = {
    400: "Solicitud inválida o regla de negocio no satisfecha.",
    401: "No autenticado. Enviar `Authorization: Bearer <token>`.",
    403: "Autenticado, pero sin rol suficiente para este recurso.",
    404: "Recurso no encontrado.",
    409: "Conflicto con el estado actual del recurso.",
    422: "Error de validación de payload, path o query params.",
    500: "Error inesperado del servidor.",
}


SUCCESS_EXAMPLES: dict[str, dict[str, Any]] = {
    "auth_user": {
        "success": True,
        "message": "User registered successfully.",
        "data": {
            "id": "usr_123",
            "email": "cliente@example.com",
            "first_name": "Brayan",
            "last_name": "Rojas",
            "full_name": "Brayan Rojas",
            "phone_number": "70000001",
            "is_active": True,
            "is_superuser": False,
            "role_codes": ["CLIENT"],
            "roles": [{"id": "role_client", "code": "CLIENT", "name": "Client"}],
            "created_at": "2026-04-27T12:00:00Z",
            "updated_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "auth_login": {
        "success": True,
        "message": "Login completed successfully.",
        "data": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer",
            "expires_in_minutes": 60,
            "user": {
                "id": "usr_123",
                "email": "cliente@example.com",
                "first_name": "Brayan",
                "last_name": "Rojas",
                "full_name": "Brayan Rojas",
                "role_codes": ["CLIENT"],
                "roles": [{"id": "role_client", "code": "CLIENT", "name": "Client"}],
                "is_active": True,
                "is_superuser": False,
                "created_at": "2026-04-27T12:00:00Z",
                "updated_at": "2026-04-27T12:00:00Z",
            },
        },
        "meta": None,
    },
    "vehicle": {
        "success": True,
        "message": "Vehicle loaded successfully.",
        "data": {
            "id": "veh_123",
            "owner_user_id": "usr_123",
            "plate_number": "ABC123",
            "vehicle_type": "CAR",
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2018,
            "color": "Blanco",
            "notes": "Vehículo familiar",
            "is_active": True,
            "created_at": "2026-04-27T12:00:00Z",
            "updated_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "incident": {
        "success": True,
        "message": "Incident loaded successfully.",
        "data": {
            "id": "inc_123",
            "status": "PENDING",
            "priority": "HIGH",
            "category": "TIRE",
            "description": "Llanta reventada en avenida principal.",
            "latitude": -17.7833,
            "longitude": -63.1821,
            "address": "Av. Cristo Redentor, Santa Cruz",
            "vehicle_id": "veh_123",
            "created_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "list": {
        "success": True,
        "message": "Resources loaded successfully.",
        "data": [],
        "meta": {"limit": 50, "offset": 0, "count": 0},
    },
    "provider": {
        "success": True,
        "message": "Provider loaded successfully.",
        "data": {
            "id": "prv_123",
            "business_name": "Taller Central",
            "provider_type": "WORKSHOP",
            "city": "Santa Cruz",
            "is_available": True,
            "max_concurrent_services": 3,
        },
        "meta": None,
    },
    "evidence": {
        "success": True,
        "message": "Incident file evidence uploaded successfully.",
        "data": {
            "id": "evd_123",
            "incident_id": "inc_123",
            "evidence_type": "IMAGE",
            "description": "Foto de la llanta dañada",
            "mime_type": "image/jpeg",
            "created_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "job": {
        "success": True,
        "message": "Background job enqueued successfully.",
        "data": {
            "id": "job_123",
            "job_type": "IMAGE_ANALYSIS",
            "status": "PENDING",
            "queue_name": "image",
            "created_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "assignment": {
        "success": True,
        "message": "Assignment candidate accepted successfully.",
        "data": {
            "candidate_id": "cand_123",
            "incident_id": "inc_123",
            "status": "ACCEPTED",
        },
        "meta": None,
    },
    "operation": {
        "success": True,
        "message": "Incident operation state loaded successfully.",
        "data": {
            "incident_id": "inc_123",
            "status": "EN_ROUTE",
            "assigned_provider_id": "prv_123",
            "assigned_technician_id": "tech_123",
        },
        "meta": None,
    },
    "tracking": {
        "success": True,
        "message": "Incident live tracking loaded successfully.",
        "data": {
            "incident_id": "inc_123",
            "responder_position": {"latitude": -17.78, "longitude": -63.18},
            "eta_minutes": 18,
            "distance_meters": 6200,
        },
        "meta": None,
    },
    "notification": {
        "success": True,
        "message": "Device token registered successfully.",
        "data": {
            "id": "dev_123",
            "platform": "ANDROID",
            "is_active": True,
            "created_at": "2026-04-27T12:00:00Z",
        },
        "meta": None,
    },
    "billing": {
        "success": True,
        "message": "Client incident billing loaded successfully.",
        "data": {
            "incident_id": "inc_123",
            "currency_code": "BOB",
            "estimated_amount": "120.00",
            "final_amount": None,
            "payment_status": "ESTIMATED",
        },
        "meta": None,
    },
    "subscription": {
        "success": True,
        "message": "Provider subscription plan loaded successfully.",
        "data": {
            "id": "plan_123",
            "name": "Auxilio mensual",
            "price_amount": "49.00",
            "billing_period": "MONTHLY",
            "is_active": True,
        },
        "meta": None,
    },
    "system": {
        "success": True,
        "message": "API is running correctly.",
        "data": {"status": "ok", "environment": "development"},
        "meta": None,
    },
}


REQUEST_EXAMPLES: dict[str, dict[str, Any]] = {
    "register_client": {
        "summary": "Registrar cliente",
        "value": {
            "account_type": "CLIENT",
            "email": "cliente@example.com",
            "password": "Cliente12345",
            "first_name": "Brayan",
            "last_name": "Rojas",
            "phone_number": "70000001",
        },
    },
    "register_provider": {
        "summary": "Registrar taller o mecánico independiente",
        "value": {
            "account_type": "WORKSHOP",
            "email": "taller@example.com",
            "password": "Taller12345",
            "first_name": "Ana",
            "last_name": "Mendez",
            "phone_number": "70000002",
            "provider_profile": {
                "business_name": "Taller Central",
                "legal_name": "Taller Central SRL",
                "description": "Auxilio mecánico y taller integral.",
                "contact_email": "contacto@tallercentral.bo",
                "contact_phone": "70000003",
                "city": "Santa Cruz",
                "address": "Av. Principal 123",
                "base_latitude": -17.7833,
                "base_longitude": -63.1821,
                "max_concurrent_services": 3,
            },
        },
    },
    "login": {
        "summary": "Login",
        "value": {"email": "cliente@example.com", "password": "Cliente12345"},
    },
    "vehicle_create": {
        "summary": "Crear vehículo",
        "value": {
            "plate_number": "ABC123",
            "vehicle_type": "CAR",
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2018,
            "color": "Blanco",
            "notes": "Vehículo familiar",
        },
    },
    "incident_create": {
        "summary": "Crear incidente",
        "value": {
            "vehicle_id": "veh_123",
            "category": "TIRE",
            "priority": "HIGH",
            "description": "Llanta reventada en avenida principal.",
            "latitude": -17.7833,
            "longitude": -63.1821,
            "address": "Av. Cristo Redentor, Santa Cruz",
        },
    },
    "text_evidence": {
        "summary": "Registrar evidencia textual",
        "value": {"evidence_type": "TEXT", "description": "El vehículo no puede avanzar."},
    },
    "provider_operations": {
        "summary": "Actualizar disponibilidad operativa",
        "value": {"is_available": True, "max_concurrent_services": 3},
    },
    "technician": {
        "summary": "Crear o actualizar técnico",
        "value": {
            "first_name": "Luis",
            "last_name": "Perez",
            "phone_number": "70000004",
            "is_active": True,
        },
    },
    "provider_service": {
        "summary": "Configurar servicio ofrecido",
        "value": {
            "service_catalog_item_id": "svc_123",
            "is_enabled": True,
            "base_price": "80.00",
            "emergency_surcharge": "25.00",
        },
    },
    "demo_job": {"summary": "Ejecutar job demo", "value": {"message": "ping"}},
    "dispatch": {
        "summary": "Despachar técnico",
        "value": {"dispatch_mode": "TECHNICIAN", "technician_id": "tech_123", "notes": "Sale desde el taller."},
    },
    "operation_note": {"summary": "Nota operativa", "value": {"notes": "Cliente confirmado por llamada."}},
    "complete": {"summary": "Completar servicio", "value": {"notes": "Servicio completado sin novedades."}},
    "location": {"summary": "Registrar ubicación", "value": {"latitude": -17.78, "longitude": -63.18, "source": "TECHNICIAN"}},
    "device": {
        "summary": "Registrar device token",
        "value": {"platform": "ANDROID", "token": "fcm-token-example", "device_name": "Pixel 8"},
    },
    "test_push": {
        "summary": "Enviar notificación de prueba",
        "value": {"title": "Prueba", "body": "Notificación de prueba desde plataforma."},
    },
    "estimate": {
        "summary": "Estimar precio",
        "value": {"estimated_amount": "120.00", "currency_code": "BOB", "notes": "Incluye movilidad."},
    },
    "finalize": {
        "summary": "Finalizar precio",
        "value": {"final_amount": "135.00", "currency_code": "BOB", "notes": "Incluye repuesto menor."},
    },
    "mark_paid": {
        "summary": "Marcar pago",
        "value": {"payment_method": "QR", "payment_reference": "QR-001"},
    },
    "checkout": {
        "summary": "Preview de checkout",
        "value": {"payment_method": "QR"},
    },
    "plan": {
        "summary": "Crear plan",
        "value": {
            "name": "Auxilio mensual",
            "description": "Cobertura mensual para auxilio vehicular.",
            "price_amount": "49.00",
            "currency_code": "BOB",
            "billing_period": "MONTHLY",
            "is_active": True,
        },
    },
    "coverage": {
        "summary": "Crear cobertura",
        "value": {
            "service_catalog_item_id": "svc_123",
            "coverage_type": "PERCENTAGE",
            "coverage_value": "50.00",
            "max_uses_per_period": 2,
        },
    },
    "subscribe": {
        "summary": "Suscribir cliente",
        "value": {"payment_method": "QR", "payment_reference": "SUB-001"},
    },
}


SCHEMA_EXAMPLES: dict[str, dict[str, Any]] = {
    "RegisterRequest": REQUEST_EXAMPLES["register_client"]["value"],
    "RegisterProviderProfileRequest": REQUEST_EXAMPLES["register_provider"]["value"]["provider_profile"],
    "LoginRequest": REQUEST_EXAMPLES["login"]["value"],
    "CreateVehicleRequest": REQUEST_EXAMPLES["vehicle_create"]["value"],
    "UpdateOwnVehicleRequest": {
        "vehicle_type": "CAR",
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2019,
        "color": "Gris",
        "notes": "Actualizado desde Angular",
        "is_active": True,
    },
    "CreateIncidentRequest": REQUEST_EXAMPLES["incident_create"]["value"],
    "UpdateOwnPendingIncidentRequest": {
        "category": "ENGINE",
        "priority": "MEDIUM",
        "description": "El motor perdió potencia y necesito asistencia.",
        "latitude": -17.785,
        "longitude": -63.18,
        "address": "Segundo anillo, Santa Cruz",
    },
    "CreateTextEvidenceRequest": REQUEST_EXAMPLES["text_evidence"]["value"],
    "ProviderOnboardingRequest": REQUEST_EXAMPLES["register_provider"]["value"],
    "CreateTechnicianRequest": REQUEST_EXAMPLES["technician"]["value"],
    "UpdateTechnicianRequest": REQUEST_EXAMPLES["technician"]["value"],
    "UpdateProviderOperationsRequest": REQUEST_EXAMPLES["provider_operations"]["value"],
    "UpsertProviderServiceRequest": REQUEST_EXAMPLES["provider_service"]["value"],
    "UpdateProviderServiceRequest": REQUEST_EXAMPLES["provider_service"]["value"],
    "DemoJobEnqueueRequest": REQUEST_EXAMPLES["demo_job"]["value"],
    "DispatchIncidentRequest": REQUEST_EXAMPLES["dispatch"]["value"],
    "OperationNoteRequest": REQUEST_EXAMPLES["operation_note"]["value"],
    "CompleteIncidentRequest": REQUEST_EXAMPLES["complete"]["value"],
    "LocationPingRequest": REQUEST_EXAMPLES["location"]["value"],
    "RegisterDeviceTokenRequest": REQUEST_EXAMPLES["device"]["value"],
    "PlatformSendTestPushRequest": REQUEST_EXAMPLES["test_push"]["value"],
    "ProviderEstimateIncidentPricingRequest": REQUEST_EXAMPLES["estimate"]["value"],
    "ProviderFinalizeIncidentPricingRequest": REQUEST_EXAMPLES["finalize"]["value"],
    "ClientCheckoutPreviewRequest": REQUEST_EXAMPLES["checkout"]["value"],
    "ClientMarkIncidentPaidRequest": REQUEST_EXAMPLES["mark_paid"]["value"],
    "ProviderPlanUpsertRequest": REQUEST_EXAMPLES["plan"]["value"],
    "ProviderPlanCoverageUpsertRequest": REQUEST_EXAMPLES["coverage"]["value"],
    "ClientSubscribeToPlanRequest": REQUEST_EXAMPLES["subscribe"]["value"],
    "AccessTokenResponse": SUCCESS_EXAMPLES["auth_login"]["data"],
    "AuthenticatedUserResponse": SUCCESS_EXAMPLES["auth_user"]["data"],
    "VehicleResponse": SUCCESS_EXAMPLES["vehicle"]["data"],
    "IncidentResponse": SUCCESS_EXAMPLES["incident"]["data"],
    "IncidentEvidenceResponse": SUCCESS_EXAMPLES["evidence"]["data"],
    "BackgroundJobResponse": SUCCESS_EXAMPLES["job"]["data"],
    "AssignmentCandidateResponse": {
        "id": "cand_123",
        "incident_id": "inc_123",
        "provider_id": "prv_123",
        "status": "AVAILABLE",
        "score": "0.92",
        "distance_meters": 6200,
        "eta_minutes": 18,
    },
    "AssignmentPublishResponse": {
        "incident_id": "inc_123",
        "published": True,
        "generated_candidates_count": 4,
    },
    "AssignmentActionResponse": SUCCESS_EXAMPLES["assignment"]["data"],
    "IncidentOperationStateResponse": SUCCESS_EXAMPLES["operation"]["data"],
    "IncidentOperationEventResponse": {
        "id": "evt_123",
        "incident_id": "inc_123",
        "event_type": "SERVICE_STARTED",
        "notes": "Servicio iniciado",
        "created_at": "2026-04-27T12:00:00Z",
    },
    "IncidentLiveTrackingResponse": SUCCESS_EXAMPLES["tracking"]["data"],
    "TrackingHistoryItemResponse": {
        "id": "trk_123",
        "incident_id": "inc_123",
        "latitude": -17.78,
        "longitude": -63.18,
        "source": "TECHNICIAN",
        "created_at": "2026-04-27T12:00:00Z",
    },
    "UserDeviceTokenResponse": SUCCESS_EXAMPLES["notification"]["data"],
    "NotificationDeliveryResponse": {
        "id": "del_123",
        "incident_id": "inc_123",
        "status": "SUCCEEDED",
        "event_type": "INCIDENT_ACCEPTED",
        "created_at": "2026-04-27T12:00:00Z",
    },
    "IncidentBillingResponse": SUCCESS_EXAMPLES["billing"]["data"],
    "BillingCheckoutPreviewResponse": {
        "incident_id": "inc_123",
        "amount": "135.00",
        "currency_code": "BOB",
        "payment_method": "QR",
        "expires_at": "2026-04-27T12:15:00Z",
    },
    "ProviderPlanResponse": SUCCESS_EXAMPLES["subscription"]["data"],
    "ProviderPlanCoverageResponse": REQUEST_EXAMPLES["coverage"]["value"],
    "ClientPlanSubscriptionResponse": {
        "id": "sub_123",
        "client_user_id": "usr_123",
        "plan_id": "plan_123",
        "status": "ACTIVE",
        "started_at": "2026-04-27T12:00:00Z",
    },
    "IncidentCoveragePreviewResponse": {
        "incident_id": "inc_123",
        "coverage_applies": True,
        "covered_amount": "60.00",
        "remaining_amount": "75.00",
    },
    "IncidentSubscriptionApplicationResponse": {
        "id": "app_123",
        "incident_id": "inc_123",
        "subscription_id": "sub_123",
        "status": "APPLIED",
        "covered_amount": "60.00",
    },
    "AuditLogResponse": {
        "id": "aud_123",
        "event_type": "HTTP_REQUEST",
        "outcome": "SUCCESS",
        "method": "POST",
        "path": "/api/incidents",
        "status_code": 200,
        "created_at": "2026-04-27T12:00:00Z",
    },
    "MetricSnapshotResponse": {
        "id": "met_123",
        "payload": {"active_incidents": 8, "completed_incidents": 42},
        "created_at": "2026-04-27T12:00:00Z",
    },
}


ENUM_FIELD_DESCRIPTIONS = {
    "account_type": "Tipo de cuenta: `CLIENT`, `INDEPENDENT_MECHANIC`, `WORKSHOP`.",
    "role_codes": "Roles del usuario: `CLIENT`, `PROVIDER_ADMIN`, `TECHNICIAN`, `PLATFORM_ADMIN`.",
    "status": "Estado según el contexto. Incidentes: `PENDING`, `IN_REVIEW`, `PUBLISHED`, `ASSIGNED`, `EN_ROUTE`, `ON_SITE`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED`.",
    "priority": "Prioridad del incidente: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.",
    "category": "Categoría del incidente: `BATTERY`, `TIRE`, `ACCIDENT`, `ENGINE`, `LOCKOUT`, `OVERHEATING`, `OTHER`, `UNCERTAIN`.",
    "payment_status": "Estado de pago: `PENDING_PRICING`, `ESTIMATED`, `PENDING_PAYMENT`, `PAID`, `CANCELLED`.",
    "platform": "Plataforma del dispositivo: `ANDROID`, `IOS`, `WEB`.",
    "vehicle_type": "Tipo de vehículo: `CAR`, `MOTORCYCLE`, `TRUCK`, `VAN`, `OTHER`.",
    "evidence_type": "Tipo de evidencia: `IMAGE`, `AUDIO`, `TEXT`.",
    "job_type": "Tipo de job: `DEMO`, `AUDIO_TRANSCRIPTION`, `IMAGE_ANALYSIS`, `INCIDENT_SUMMARY`, `PUSH_NOTIFICATION`.",
    "dispatch_mode": "Modo de despacho: `PROVIDER_SELF` o `TECHNICIAN`.",
    "source": "Origen del tracking: `PROVIDER_SELF` o `TECHNICIAN`.",
    "billing_period": "Periodo de cobro del plan: `MONTHLY` o `ANNUAL`.",
    "coverage_type": "Tipo de cobertura: `FIXED_AMOUNT`, `PERCENTAGE` o `FULL`.",
}


ENDPOINT_DOCS: dict[str, dict[str, Any]] = {
    "root": {"summary": "Estado inicial de la API", "description": "Devuelve información base y URLs principales para descubrir el backend.", "response": "system", "public": True},
    "health": {"summary": "Health check", "description": "Verifica que la API esté levantada y pueda responder. Útil para Docker, monitoreo y frontend.", "response": "system", "public": True},
    "readiness": {"summary": "Readiness check", "description": "Verifica dependencias necesarias para operar, como la base de datos.", "response": "system", "public": True},
    "info": {"summary": "Información del sistema", "description": "Devuelve configuración visible de proveedores integrados y datos generales de la API.", "response": "system", "public": True},
    "platform_metrics": {"summary": "Consultar métricas de plataforma", "description": "Vista administrativa de métricas operativas agregadas.", "response": "system"},
    "create_metrics_snapshot": {"summary": "Crear snapshot de métricas", "description": "Persiste una captura administrativa de métricas para auditoría o reportes.", "response": "system"},
    "register": {"summary": "Registrar usuario", "description": "Crea cuentas cliente, mecánico independiente o taller. Para proveedores se puede enviar `provider_profile`.", "request_examples": ["register_client", "register_provider"], "response": "auth_user", "public": True},
    "login": {"summary": "Iniciar sesión", "description": "Autentica credenciales y devuelve un JWT para usar en el header Authorization de Angular.", "request_examples": ["login"], "response": "auth_login", "public": True},
    "get_authenticated_user_profile": {"summary": "Obtener usuario actual", "description": "Devuelve el perfil y roles del usuario autenticado con Bearer JWT.", "response": "auth_user"},
    "get_own_profile": {"summary": "Ver mi perfil", "description": "Consulta el perfil editable del usuario autenticado.", "response": "auth_user"},
    "update_own_profile": {"summary": "Actualizar mi perfil", "description": "Actualiza campos personales del usuario autenticado.", "response": "auth_user"},
    "list_users": {"summary": "Listar usuarios", "description": "Listado administrativo paginado de usuarios registrados.", "response": "list"},
    "get_user_by_id": {"summary": "Ver usuario por ID", "description": "Consulta administrativa de un usuario específico.", "response": "auth_user"},
    "onboard_provider": {"summary": "Registrar taller o proveedor", "description": "Crea proveedor y usuario administrador del proveedor desde plataforma.", "request_examples": ["register_provider"], "response": "provider"},
    "list_providers": {"summary": "Listar proveedores", "description": "Listado administrativo paginado de talleres y mecánicos independientes.", "response": "list"},
    "get_provider_by_id": {"summary": "Ver proveedor por ID", "description": "Consulta administrativa del perfil de un proveedor.", "response": "provider"},
    "update_provider_operations": {"summary": "Actualizar disponibilidad de proveedor", "description": "Permite a plataforma ajustar disponibilidad y capacidad operativa del proveedor.", "request_examples": ["provider_operations"], "response": "provider"},
    "get_my_provider": {"summary": "Ver mi perfil de proveedor", "description": "Consulta el perfil del taller o mecánico asociado al admin autenticado.", "response": "provider"},
    "update_my_provider": {"summary": "Actualizar mi perfil de proveedor", "description": "Actualiza datos comerciales y operativos del proveedor autenticado.", "response": "provider"},
    "list_my_technicians": {"summary": "Listar mis técnicos", "description": "Lista técnicos asociados al proveedor autenticado.", "response": "list"},
    "create_my_technician": {"summary": "Crear técnico propio", "description": "Registra un técnico para el proveedor autenticado.", "request_examples": ["technician"], "response": "provider"},
    "update_my_technician": {"summary": "Actualizar técnico propio", "description": "Actualiza datos o estado de un técnico del proveedor autenticado.", "request_examples": ["technician"], "response": "provider"},
    "list_provider_technicians": {"summary": "Listar técnicos de proveedor", "description": "Listado administrativo de técnicos de un proveedor específico.", "response": "list"},
    "create_provider_technician": {"summary": "Crear técnico para proveedor", "description": "Crea un técnico para un proveedor desde plataforma.", "request_examples": ["technician"], "response": "provider"},
    "update_provider_technician": {"summary": "Actualizar técnico de proveedor", "description": "Actualiza un técnico específico desde plataforma.", "request_examples": ["technician"], "response": "provider"},
    "create_service_catalog_item": {"summary": "Crear servicio de catálogo", "description": "Crea un tipo de servicio disponible para configurar proveedores.", "response": "system"},
    "list_service_catalog_items": {"summary": "Listar catálogo de servicios", "description": "Lista servicios base como batería, llantas, grúa o diagnóstico.", "response": "list"},
    "get_service_catalog_item_by_id": {"summary": "Ver servicio de catálogo", "description": "Consulta detalle de un servicio base.", "response": "system"},
    "update_service_catalog_item": {"summary": "Actualizar servicio de catálogo", "description": "Actualiza definición de un servicio base desde plataforma.", "response": "system"},
    "list_provider_services_for_platform": {"summary": "Listar servicios de proveedor", "description": "Consulta administrativa de servicios configurados por un proveedor.", "response": "list"},
    "list_my_catalog_with_configuration": {"summary": "Ver catálogo con mi configuración", "description": "Devuelve servicios base junto con la configuración del proveedor autenticado.", "response": "list"},
    "list_my_provider_services": {"summary": "Listar mis servicios ofrecidos", "description": "Lista servicios activos y precios del proveedor autenticado.", "response": "list"},
    "upsert_my_provider_service": {"summary": "Configurar servicio ofrecido", "description": "Crea o actualiza la configuración de un servicio ofrecido por el proveedor.", "request_examples": ["provider_service"], "response": "provider"},
    "update_my_provider_service": {"summary": "Actualizar servicio ofrecido", "description": "Actualiza precio, disponibilidad o flags de un servicio del proveedor.", "request_examples": ["provider_service"], "response": "provider"},
    "create_own_vehicle": {"summary": "Crear vehículo", "description": "Registra un vehículo para el cliente autenticado.", "request_examples": ["vehicle_create"], "response": "vehicle"},
    "list_own_vehicles": {"summary": "Listar mis vehículos", "description": "Lista vehículos activos o históricos del cliente autenticado.", "response": "list"},
    "get_own_vehicle": {"summary": "Ver mi vehículo", "description": "Consulta detalle de un vehículo perteneciente al cliente autenticado.", "response": "vehicle"},
    "update_own_vehicle": {"summary": "Actualizar mi vehículo", "description": "Actualiza datos de un vehículo del cliente autenticado.", "request_examples": ["vehicle_create"], "response": "vehicle"},
    "create_own_incident": {"summary": "Crear incidente", "description": "Registra una emergencia vehicular para el cliente autenticado.", "request_examples": ["incident_create"], "response": "incident"},
    "list_own_incidents": {"summary": "Listar mis incidentes", "description": "Lista incidentes del cliente autenticado.", "response": "list"},
    "get_own_incident": {"summary": "Ver detalle de mi incidente", "description": "Consulta detalle de un incidente del cliente autenticado.", "response": "incident"},
    "update_own_pending_incident": {"summary": "Actualizar incidente pendiente", "description": "Permite editar un incidente propio mientras siga en estado editable.", "request_examples": ["incident_create"], "response": "incident"},
    "cancel_own_incident": {"summary": "Cancelar incidente", "description": "Cancela un incidente propio cuando el estado lo permite.", "response": "incident"},
    "list_all_incidents": {"summary": "Listar incidentes de plataforma", "description": "Listado administrativo paginado de incidentes.", "response": "list"},
    "get_incident_by_id_for_platform": {"summary": "Ver incidente por ID", "description": "Consulta administrativa de un incidente específico.", "response": "incident"},
    "list_provider_incidents": {"summary": "Listar incidentes del proveedor", "description": "Lista incidentes asignados o visibles para el proveedor autenticado.", "response": "list"},
    "get_provider_incident": {"summary": "Ver incidente del proveedor", "description": "Consulta detalle de un incidente asociado al proveedor autenticado.", "response": "incident"},
    "upload_incident_file_evidence_as_client": {"summary": "Subir imagen o audio", "description": "Carga evidencia multipart para un incidente del cliente. `evidence_type` suele ser `IMAGE` o `AUDIO`.", "response": "evidence"},
    "create_incident_text_evidence_as_client": {"summary": "Registrar evidencia textual", "description": "Agrega una evidencia de tipo texto al incidente del cliente.", "request_examples": ["text_evidence"], "response": "evidence"},
    "list_client_incident_evidences": {"summary": "Listar evidencias del cliente", "description": "Lista evidencias de un incidente perteneciente al cliente autenticado.", "response": "list"},
    "list_provider_incident_evidences": {"summary": "Listar evidencias para proveedor", "description": "Lista evidencias visibles para el proveedor asignado o autorizado.", "response": "list"},
    "list_platform_incident_evidences": {"summary": "Listar evidencias de plataforma", "description": "Lista administrativa de evidencias de un incidente.", "response": "list"},
    "download_evidence": {"summary": "Descargar evidencia", "description": "Devuelve o redirige al archivo de evidencia autorizado para el rol autenticado.", "response": "evidence"},
    "enqueue_demo_job": {"summary": "Ejecutar job demo", "description": "Encola un job de prueba para validar workers.", "request_examples": ["demo_job"], "response": "job"},
    "enqueue_audio_transcription_job": {"summary": "Ejecutar transcripción", "description": "Encola transcripción de audio para una evidencia.", "response": "job"},
    "enqueue_image_analysis_job": {"summary": "Ejecutar análisis de imagen", "description": "Encola análisis de visión para una evidencia de imagen.", "response": "job"},
    "enqueue_incident_summary_job": {"summary": "Ejecutar resumen de incidente", "description": "Encola generación de resumen inteligente para un incidente.", "response": "job"},
    "list_jobs": {"summary": "Listar jobs", "description": "Listado paginado de trabajos asíncronos.", "response": "list"},
    "get_job_by_id": {"summary": "Consultar estado de job", "description": "Consulta estado, tipo, resultado o error de un job asíncrono.", "response": "job"},
    "publish_incident_for_assignment": {"summary": "Publicar incidente", "description": "Publica un incidente para generar candidatos de asignación.", "response": "assignment"},
    "list_platform_candidates_for_incident": {"summary": "Listar candidatos de incidente", "description": "Lista candidatos generados para un incidente desde plataforma.", "response": "list"},
    "list_my_available_candidates": {"summary": "Listar candidatos disponibles", "description": "Lista oportunidades disponibles para el proveedor autenticado.", "response": "list"},
    "get_my_available_candidate": {"summary": "Ver candidato disponible", "description": "Consulta detalle de una oportunidad para aceptar o rechazar.", "response": "assignment"},
    "accept_my_candidate": {"summary": "Aceptar candidato", "description": "El proveedor acepta atender el incidente propuesto.", "response": "assignment"},
    "reject_my_candidate": {"summary": "Rechazar candidato", "description": "El proveedor rechaza la oportunidad de asignación.", "response": "assignment"},
    "list_my_active_operations": {"summary": "Listar operaciones activas", "description": "Lista servicios en curso del proveedor autenticado.", "response": "list"},
    "get_my_operation_state": {"summary": "Ver estado operativo", "description": "Consulta estado operativo actual de un incidente del proveedor.", "response": "operation"},
    "dispatch_my_incident": {"summary": "Despachar técnico", "description": "Asigna despacho propio o técnico y cambia el flujo operativo a en camino.", "request_examples": ["dispatch"], "response": "operation"},
    "mark_my_arrival": {"summary": "Marcar llegada", "description": "Marca llegada al sitio del incidente.", "request_examples": ["operation_note"], "response": "operation"},
    "start_my_service": {"summary": "Iniciar servicio", "description": "Marca inicio de atención mecánica.", "request_examples": ["operation_note"], "response": "operation"},
    "complete_my_service": {"summary": "Completar servicio", "description": "Finaliza el servicio y registra notas de cierre.", "request_examples": ["complete"], "response": "operation"},
    "cancel_my_service": {"summary": "Cancelar servicio", "description": "Cancela la atención desde el proveedor cuando corresponde.", "request_examples": ["operation_note"], "response": "operation"},
    "list_my_operation_history": {"summary": "Ver historial operativo", "description": "Lista eventos operativos de un incidente del proveedor.", "response": "list"},
    "list_platform_operation_history": {"summary": "Ver historial operativo plataforma", "description": "Lista administrativa de eventos operativos de un incidente.", "response": "list"},
    "report_my_location": {"summary": "Registrar ubicación", "description": "Registra ubicación actual del proveedor o técnico para tracking.", "request_examples": ["location"], "response": "tracking"},
    "refresh_my_route": {"summary": "Calcular ruta y ETA", "description": "Actualiza ruta y ETA hacia el incidente con el proveedor configurado.", "response": "tracking"},
    "get_provider_live_tracking": {"summary": "Consultar tracking proveedor", "description": "Tracking en vivo visible para el proveedor autenticado.", "response": "tracking"},
    "list_provider_tracking_history": {"summary": "Historial tracking proveedor", "description": "Historial de ubicaciones de un incidente para el proveedor.", "response": "list"},
    "get_client_live_tracking": {"summary": "Consultar tracking del incidente", "description": "Tracking en vivo para el cliente dueño del incidente.", "response": "tracking"},
    "list_client_tracking_history": {"summary": "Historial tracking cliente", "description": "Historial de ubicaciones visible para el cliente.", "response": "list"},
    "get_platform_live_tracking": {"summary": "Tracking plataforma", "description": "Tracking en vivo administrativo de un incidente.", "response": "tracking"},
    "list_platform_tracking_history": {"summary": "Historial tracking plataforma", "description": "Historial administrativo de ubicaciones de un incidente.", "response": "list"},
    "register_my_device_token": {"summary": "Registrar device token", "description": "Registra o actualiza token FCM/APNS/Web Push del usuario autenticado.", "request_examples": ["device"], "response": "notification"},
    "list_my_device_tokens": {"summary": "Listar mis device tokens", "description": "Lista dispositivos registrados del usuario autenticado.", "response": "list"},
    "deactivate_my_device_token": {"summary": "Desactivar device token", "description": "Desactiva un token de dispositivo del usuario autenticado.", "response": "notification"},
    "send_platform_test_push": {"summary": "Enviar notificación de prueba", "description": "Envía una notificación de prueba a un usuario desde plataforma.", "request_examples": ["test_push"], "response": "notification"},
    "list_platform_incident_deliveries": {"summary": "Listar entregas de notificación", "description": "Lista entregas push asociadas a un incidente.", "response": "list"},
    "get_my_client_incident_billing": {"summary": "Obtener facturación del incidente", "description": "Consulta facturación del incidente para el cliente autenticado.", "response": "billing"},
    "create_client_checkout_preview": {"summary": "Preview de checkout", "description": "Genera vista previa de checkout para el cliente.", "request_examples": ["checkout"], "response": "billing"},
    "mark_client_incident_as_paid": {"summary": "Marcar pago", "description": "Marca pago de incidente desde el cliente cuando corresponde.", "request_examples": ["mark_paid"], "response": "billing"},
    "get_my_provider_incident_billing": {"summary": "Ver facturación proveedor", "description": "Consulta facturación de un incidente atendido por el proveedor.", "response": "billing"},
    "upsert_provider_incident_estimate": {"summary": "Estimar precio", "description": "Crea o actualiza estimación de precio del incidente.", "request_examples": ["estimate"], "response": "billing"},
    "finalize_provider_incident_pricing": {"summary": "Finalizar precio", "description": "Define el precio final del servicio para pago.", "request_examples": ["finalize"], "response": "billing"},
    "get_platform_incident_billing": {"summary": "Ver facturación plataforma", "description": "Consulta administrativa de facturación de un incidente.", "response": "billing"},
    "list_my_provider_plans": {"summary": "Listar mis planes", "description": "Lista planes de suscripción creados por el proveedor.", "response": "list"},
    "create_my_provider_plan": {"summary": "Crear plan", "description": "Crea un plan de suscripción del proveedor autenticado.", "request_examples": ["plan"], "response": "subscription"},
    "update_my_provider_plan": {"summary": "Actualizar plan", "description": "Actualiza precio, nombre, periodo o estado de un plan.", "request_examples": ["plan"], "response": "subscription"},
    "upsert_my_provider_plan_coverage": {"summary": "Crear cobertura", "description": "Crea o actualiza cobertura de un servicio dentro de un plan.", "request_examples": ["coverage"], "response": "subscription"},
    "list_provider_plans_for_client": {"summary": "Listar planes de proveedor", "description": "Lista planes disponibles de un proveedor para clientes.", "response": "list"},
    "subscribe_client_to_plan": {"summary": "Suscribir cliente", "description": "Suscribe al cliente autenticado a un plan de proveedor.", "request_examples": ["subscribe"], "response": "subscription"},
    "list_my_client_subscriptions": {"summary": "Listar mis suscripciones", "description": "Lista suscripciones del cliente autenticado.", "response": "list"},
    "preview_applicable_coverage_for_incident": {"summary": "Previsualizar cobertura", "description": "Calcula cobertura aplicable para un incidente antes de aplicarla.", "response": "subscription"},
    "apply_best_coverage_for_incident": {"summary": "Aplicar cobertura a incidente", "description": "Aplica la mejor cobertura disponible al incidente del cliente.", "response": "subscription"},
    "list_platform_incident_subscription_applications": {"summary": "Listar aplicaciones de cobertura", "description": "Lista aplicaciones de suscripción/cobertura de un incidente.", "response": "list"},
    "list_audit_logs": {"summary": "Listar logs de auditoría", "description": "Listado paginado y filtrable de eventos de auditoría.", "response": "list"},
    "list_metric_snapshots": {"summary": "Consultar métricas históricas", "description": "Lista snapshots de métricas capturados por la plataforma.", "response": "list"},
}


def configure_openapi(application: FastAPI) -> None:
    def custom_openapi() -> dict[str, Any]:
        if application.openapi_schema:
            return application.openapi_schema

        schema = get_openapi(
            title=application.title,
            version=application.version,
            description=application.description,
            routes=application.routes,
            tags=application.openapi_tags,
        )

        components = schema.setdefault("components", {})
        schemas = components.setdefault("schemas", {})
        _register_component_schema(schemas, "ApiResponse", ApiResponse)
        _register_component_schema(schemas, "ApiErrorResponse", ApiErrorResponse)
        components["securitySchemes"] = {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "JWT obtenido desde `/api/auth/login`. Usar: `Bearer <access_token>`.",
            }
        }
        _apply_schema_examples_and_enum_descriptions(schemas)

        route_by_path_method = _build_route_index(application)

        for path, path_item in schema.get("paths", {}).items():
            if not isinstance(path_item, Mapping):
                continue

            for method, operation in path_item.items():
                if method not in {"get", "post", "put", "patch", "delete"}:
                    continue

                route = route_by_path_method.get((path, method.upper()))
                endpoint_name = route.endpoint.__name__ if route else None
                docs = ENDPOINT_DOCS.get(endpoint_name or "", {})
                is_public = bool(docs.get("public"))

                operation["summary"] = docs.get("summary") or _fallback_summary(method, path)
                operation["description"] = docs.get("description") or _fallback_description(method, path)
                operation["tags"] = operation.get("tags") or [_tag_from_path(path)]
                operation["security"] = [] if is_public else [{"BearerAuth": []}]

                _apply_common_responses(operation, protected=not is_public, has_path_param="{" in path)
                _apply_success_example(operation, docs.get("response", _response_key_from_tag(operation["tags"][0])))
                _apply_request_examples(operation, docs.get("request_examples", []))

        application.openapi_schema = schema
        return application.openapi_schema

    application.openapi = custom_openapi


def _build_route_index(application: FastAPI) -> dict[tuple[str, str], APIRoute]:
    index: dict[tuple[str, str], APIRoute] = {}
    for route in application.routes:
        if not isinstance(route, APIRoute):
            continue
        for method in route.methods or []:
            if method in {"HEAD", "OPTIONS"}:
                continue
            index[(route.path_format, method)] = route
    return index


def _fallback_summary(method: str, path: str) -> str:
    resource = path.rstrip("/").split("/")[-1] or "API"
    resource = resource.replace("{", "").replace("}", "").replace("-", " ").replace("_", " ")
    action = {
        "get": "Consultar",
        "post": "Crear o ejecutar",
        "put": "Reemplazar",
        "patch": "Actualizar",
        "delete": "Eliminar",
    }.get(method, "Operar")
    return f"{action} {resource}".strip().capitalize()


def _fallback_description(method: str, path: str) -> str:
    return (
        f"Endpoint `{method.upper()} {path}`. "
        "Devuelve la envoltura estándar `{ success, message, data, meta }` o un error documentado."
    )


def _tag_from_path(path: str) -> str:
    parts = [part for part in path.split("/") if part]
    if len(parts) >= 2 and parts[0] == "api":
        return parts[1].replace("-", " ").title()
    return "Root"


def _response_key_from_tag(tag: str) -> str:
    return {
        "Auth": "auth_user",
        "Vehicles": "vehicle",
        "Providers": "provider",
        "Incidents": "incident",
        "Evidences": "evidence",
        "Jobs": "job",
        "Assignment": "assignment",
        "Operations": "operation",
        "Tracking": "tracking",
        "Notifications": "notification",
        "Billing": "billing",
        "Subscriptions": "subscription",
        "System": "system",
    }.get(tag, "list")


def _apply_common_responses(operation: dict[str, Any], protected: bool, has_path_param: bool) -> None:
    responses = operation.setdefault("responses", {})
    default_success_code = next((code for code in responses if str(code).startswith("2")), "200")
    responses.setdefault(default_success_code, {})
    responses[default_success_code].setdefault("description", "Operación exitosa.")

    status_codes = [400, 409, 422, 500]
    if protected:
        status_codes.extend([401, 403])
    if has_path_param:
        status_codes.append(404)

    for status_code in sorted(set(status_codes)):
        responses[str(status_code)] = {
            "description": ERROR_DESCRIPTIONS[status_code],
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/ApiErrorResponse"},
                    "example": ERROR_EXAMPLES[status_code],
                }
            },
        }


def _apply_success_example(operation: dict[str, Any], response_key: str) -> None:
    example = SUCCESS_EXAMPLES.get(response_key, SUCCESS_EXAMPLES["list"])
    responses = operation.setdefault("responses", {})
    success_code = next((code for code in responses if str(code).startswith("2")), "200")
    success_response = responses.setdefault(success_code, {"description": "Operación exitosa."})
    content = success_response.setdefault("content", {}).setdefault("application/json", {})
    content.setdefault("schema", {"$ref": "#/components/schemas/ApiResponse"})
    content["example"] = example


def _apply_request_examples(operation: dict[str, Any], example_keys: list[str]) -> None:
    if not example_keys or "requestBody" not in operation:
        return

    request_body = operation["requestBody"]
    content = request_body.get("content", {})
    media_type = "application/json" if "application/json" in content else next(iter(content), None)
    if not media_type:
        return

    examples = {
        key: REQUEST_EXAMPLES[key]
        for key in example_keys
        if key in REQUEST_EXAMPLES
    }
    if examples:
        content[media_type]["examples"] = examples


def _apply_schema_examples_and_enum_descriptions(schemas: dict[str, Any]) -> None:
    for schema_name, example in SCHEMA_EXAMPLES.items():
        schema = schemas.get(schema_name)
        if isinstance(schema, dict):
            schema.setdefault("example", example)

    for schema in schemas.values():
        if not isinstance(schema, dict):
            continue
        properties = schema.get("properties")
        if not isinstance(properties, dict):
            continue
        for field_name, description in ENUM_FIELD_DESCRIPTIONS.items():
            property_schema = properties.get(field_name)
            if isinstance(property_schema, dict):
                property_schema.setdefault("description", description)


def _register_component_schema(
    schemas: dict[str, Any],
    schema_name: str,
    model: type[BaseModel],
) -> None:
    model_schema = model.model_json_schema(ref_template="#/components/schemas/{model}")
    defs = model_schema.pop("$defs", {})
    schemas.update(defs)
    schemas[schema_name] = model_schema
