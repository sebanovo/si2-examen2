import logging
from collections.abc import Callable
from dataclasses import dataclass
from decimal import Decimal
from typing import Any
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session, configure_mappers

import app.bootstrap.model_registry  # noqa: F401

from app.common.constants import (
    INITIAL_SERVICE_CATALOG_ITEMS,
    PROVIDER_TYPE_INDEPENDENT_MECHANIC,
    PROVIDER_TYPE_WORKSHOP,
    ROLE_CLIENT,
    ROLE_PLATFORM_ADMIN,
    ROLE_PROVIDER_ADMIN,
    ROLE_TECHNICIAN,
    EVIDENCE_TYPE_AUDIO,
    EVIDENCE_TYPE_IMAGE,
    EVIDENCE_TYPE_TEXT,
    INCIDENT_CATEGORY_ACCIDENT,
    INCIDENT_CATEGORY_BATTERY,
    INCIDENT_CATEGORY_ENGINE,
    INCIDENT_CATEGORY_LOCKOUT,
    INCIDENT_CATEGORY_OVERHEATING,
    INCIDENT_CATEGORY_TIRE,
    INCIDENT_CATEGORY_UNCERTAIN,
    INCIDENT_PRIORITY_HIGH,
    INCIDENT_PRIORITY_MEDIUM,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_REVIEW,
    INCIDENT_STATUS_PENDING,
    INCIDENT_STATUS_PUBLISHED,
    PROCESSING_STATUS_NOT_REQUESTED,
    PROCESSING_STATUS_SUCCEEDED,
    ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
    ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
    ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
    DISPATCH_MODE_TECHNICIAN,
    INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
    INCIDENT_OPERATION_EVENT_DISPATCHED,
    INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
    INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
    INCIDENT_STATUS_ASSIGNED,
    INCIDENT_STATUS_COMPLETED,
    INCIDENT_STATUS_EN_ROUTE,
    INCIDENT_STATUS_IN_PROGRESS,
    INCIDENT_STATUS_ON_SITE,
    TRACKING_SOURCE_TECHNICIAN,
    
)
from app.core.database import SessionLocal
from app.core.logging_config import configure_logging
from app.core.security import hash_password
from app.services.auth.models import Role, User
from app.services.catalog.models import ProviderService, ServiceCatalogItem
from app.services.providers.models import Provider, Technician
from app.services.vehicles.models import Vehicle
from app.services.incidents.models import Incident
from app.services.evidences.models import IncidentEvidence
from app.services.assignment.models import IncidentAssignmentCandidate
from app.services.operations.models import IncidentOperationEvent
from app.services.tracking.models import IncidentResponderLocationPing
from app.bootstrap.demo_seed_step_05 import (
    seed_step_05_billing_subscriptions_notifications_and_audit,
)
from app.bootstrap.demo_seed_step_06_technician_mobile import (
    seed_step_06_technician_mobile_users,
)

logger = logging.getLogger(__name__)

DEMO_PASSWORD = "Demo12345"


@dataclass(frozen=True)
class RoleSeed:
    code: str
    name: str
    description: str


@dataclass(frozen=True)
class UserSeed:
    email: str
    password: str
    first_name: str
    last_name: str
    phone_number: str | None
    role_code: str
    is_superuser: bool = False


@dataclass(frozen=True)
class ProviderSeed:
    owner_email: str
    provider_type: str
    business_name: str
    legal_name: str | None
    description: str | None
    contact_email: str | None
    contact_phone: str | None
    city: str | None
    address: str | None
    base_latitude: float | None
    base_longitude: float | None
    is_active: bool
    is_available: bool
    max_concurrent_services: int
    current_active_services: int
    average_rating: float


@dataclass(frozen=True)
class TechnicianSeed:
    provider_owner_email: str
    first_name: str
    last_name: str
    phone_number: str
    specialty: str | None
    is_active: bool
    is_available: bool
    current_latitude: float | None
    current_longitude: float | None


@dataclass(frozen=True)
class VehicleSeed:
    owner_email: str
    plate_number: str
    vehicle_type: str
    brand: str
    model: str
    year: int | None
    color: str | None
    notes: str | None
    is_active: bool


@dataclass(frozen=True)
class ProviderServiceSeed:
    provider_owner_email: str
    service_code: str
    custom_title: str | None
    custom_description: str | None
    price_estimate_min: Decimal | None
    price_estimate_max: Decimal | None
    estimated_duration_minutes: int | None
    is_mobile_service_enabled: bool
    is_emergency_service_enabled: bool
    is_active: bool

@dataclass(frozen=True)
class IncidentSeed:
    demo_key: str
    client_email: str
    vehicle_plate_number: str
    provider_owner_email: str | None
    assigned_technician_phone: str | None
    status: str
    priority: str
    reported_category: str
    title: str
    description: str
    client_contact_phone_snapshot: str | None
    incident_latitude: float | None
    incident_longitude: float | None
    address_reference: str | None
    estimated_price_min: Decimal | None
    estimated_price_max: Decimal | None
    ai_summary_status: str
    summary_provider_name: str | None
    structured_summary: str | None
    suggested_category: str | None
    suggested_priority: str | None
    requires_more_information: bool


@dataclass(frozen=True)
class EvidenceSeed:
    incident_demo_key: str
    uploaded_by_email: str
    evidence_type: str
    original_filename: str | None
    stored_filename: str
    file_extension: str | None
    mime_type: str | None
    file_size_bytes: int | None
    description: str | None
    text_content_snapshot: str | None
    audio_processing_status: str
    audio_provider_name: str | None
    transcript_text: str | None
    transcript_language_code: str | None
    transcript_confidence: float | None
    image_processing_status: str
    image_provider_name: str | None
    image_labels_json: list | None
    image_detections_json: list | None
    image_summary: str | None

@dataclass(frozen=True)
class AssignmentCandidateSeed:
    incident_demo_key: str
    provider_owner_email: str
    status: str
    recommendation_rank: int
    score: float
    distance_km: float | None
    required_service_codes_json: list[str] | None
    matched_service_codes_json: list[str] | None
    rationale_json: dict | None
    provider_available_capacity_snapshot: int
    available_technicians_count_snapshot: int


@dataclass(frozen=True)
class OperationEventSeed:
    incident_demo_key: str
    provider_owner_email: str | None
    technician_phone: str | None
    actor_email: str | None
    event_type: str
    from_status: str | None
    to_status: str | None
    note: str | None
    payload_json: dict | None


@dataclass(frozen=True)
class TrackingPingSeed:
    incident_demo_key: str
    provider_owner_email: str
    technician_phone: str | None
    source_type: str
    latitude: float
    longitude: float
    accuracy_meters: float | None
    minutes_ago: int


SYSTEM_ROLES: tuple[RoleSeed, ...] = (
    RoleSeed(
        code=ROLE_CLIENT,
        name="Client",
        description="Cliente que solicita asistencia mecánica desde la aplicación móvil.",
    ),
    RoleSeed(
        code=ROLE_PROVIDER_ADMIN,
        name="Provider Admin",
        description="Administrador de taller o mecánico independiente que atiende solicitudes.",
    ),
    RoleSeed(
        code=ROLE_TECHNICIAN,
        name="Technician",
        description="Técnico asignado para asistir incidentes vehiculares.",
    ),
    RoleSeed(
        code=ROLE_PLATFORM_ADMIN,
        name="Platform Admin",
        description="Administrador general de la plataforma.",
    ),
)


DEMO_USERS: tuple[UserSeed, ...] = (
    UserSeed(
        email="admin@mechanic.local",
        password="Admin12345",
        first_name="Platform",
        last_name="Admin",
        phone_number="70000001",
        role_code=ROLE_PLATFORM_ADMIN,
        is_superuser=True,
    ),
    UserSeed(
        email="cliente.bateria@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Luis",
        last_name="Rivero",
        phone_number="70010001",
        role_code=ROLE_CLIENT,
    ),
    UserSeed(
        email="cliente.llanta@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="María",
        last_name="Gutiérrez",
        phone_number="70010002",
        role_code=ROLE_CLIENT,
    ),
    UserSeed(
        email="cliente.accidente@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Carlos",
        last_name="Mendoza",
        phone_number="70010003",
        role_code=ROLE_CLIENT,
    ),
    UserSeed(
        email="taller.norte@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Roxana",
        last_name="Suárez",
        phone_number="70020001",
        role_code=ROLE_PROVIDER_ADMIN,
    ),
    UserSeed(
        email="taller.express@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Miguel",
        last_name="Ortiz",
        phone_number="70020002",
        role_code=ROLE_PROVIDER_ADMIN,
    ),
    UserSeed(
        email="taller.gruas@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Fernando",
        last_name="Rojas",
        phone_number="70020003",
        role_code=ROLE_PROVIDER_ADMIN,
    ),
    UserSeed(
        email="mecanico.juan@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Juan",
        last_name="Paredes",
        phone_number="70020004",
        role_code=ROLE_PROVIDER_ADMIN,
    ),
    UserSeed(
        email="mecanico.carlos@mechanic.local",
        password=DEMO_PASSWORD,
        first_name="Carlos",
        last_name="Vargas",
        phone_number="70020005",
        role_code=ROLE_PROVIDER_ADMIN,
    ),
)


DEMO_PROVIDERS: tuple[ProviderSeed, ...] = (
    ProviderSeed(
        owner_email="taller.norte@mechanic.local",
        provider_type=PROVIDER_TYPE_WORKSHOP,
        business_name="Taller Rápido Norte",
        legal_name="Taller Rápido Norte S.R.L.",
        description=(
            "Taller especializado en auxilio de batería, llantas, diagnóstico "
            "mecánico básico y atención móvil dentro de la ciudad."
        ),
        contact_email="contacto@tallernorte.local",
        contact_phone="70030001",
        city="Santa Cruz de la Sierra",
        address="Av. Cristo Redentor, 4to Anillo",
        base_latitude=-17.7539,
        base_longitude=-63.1816,
        is_active=True,
        is_available=True,
        max_concurrent_services=3,
        current_active_services=0,
        average_rating=4.6,
    ),
    ProviderSeed(
        owner_email="taller.express@mechanic.local",
        provider_type=PROVIDER_TYPE_WORKSHOP,
        business_name="Taller Auxilio Express",
        legal_name="Auxilio Express S.R.L.",
        description=(
            "Taller con técnicos móviles para emergencias vehiculares, "
            "diagnóstico rápido y apoyo en carretera urbana."
        ),
        contact_email="contacto@auxilioexpress.local",
        contact_phone="70030002",
        city="Santa Cruz de la Sierra",
        address="Av. Banzer, entre 5to y 6to Anillo",
        base_latitude=-17.7386,
        base_longitude=-63.1732,
        is_active=True,
        is_available=True,
        max_concurrent_services=4,
        current_active_services=1,
        average_rating=4.4,
    ),
    ProviderSeed(
        owner_email="taller.gruas@mechanic.local",
        provider_type=PROVIDER_TYPE_WORKSHOP,
        business_name="Taller Grúas Santa Cruz",
        legal_name="Grúas Santa Cruz S.R.L.",
        description=(
            "Proveedor especializado en grúa, remolque, accidentes leves "
            "y traslado de vehículos averiados."
        ),
        contact_email="contacto@gruassantacruz.local",
        contact_phone="70030003",
        city="Santa Cruz de la Sierra",
        address="Doble vía La Guardia, km 7",
        base_latitude=-17.8245,
        base_longitude=-63.2071,
        is_active=True,
        is_available=True,
        max_concurrent_services=2,
        current_active_services=0,
        average_rating=4.8,
    ),
    ProviderSeed(
        owner_email="mecanico.juan@mechanic.local",
        provider_type=PROVIDER_TYPE_INDEPENDENT_MECHANIC,
        business_name="Mecánico Independiente Juan",
        legal_name=None,
        description=(
            "Mecánico independiente especializado en batería, llantas, "
            "diagnóstico rápido y auxilio a domicilio."
        ),
        contact_email="juan@mecanico.local",
        contact_phone="70030004",
        city="Santa Cruz de la Sierra",
        address="Zona Equipetrol Norte",
        base_latitude=-17.7597,
        base_longitude=-63.1962,
        is_active=True,
        is_available=True,
        max_concurrent_services=1,
        current_active_services=0,
        average_rating=4.2,
    ),
    ProviderSeed(
        owner_email="mecanico.carlos@mechanic.local",
        provider_type=PROVIDER_TYPE_INDEPENDENT_MECHANIC,
        business_name="Mecánico Independiente Carlos",
        legal_name=None,
        description=(
            "Mecánico independiente orientado a fallas de motor, "
            "sobrecalentamiento y atención básica de emergencia."
        ),
        contact_email="carlos@mecanico.local",
        contact_phone="70030005",
        city="Santa Cruz de la Sierra",
        address="Zona Villa Primero de Mayo",
        base_latitude=-17.7916,
        base_longitude=-63.1357,
        is_active=True,
        is_available=False,
        max_concurrent_services=1,
        current_active_services=1,
        average_rating=4.0,
    ),
)


DEMO_TECHNICIANS: tuple[TechnicianSeed, ...] = (
    TechnicianSeed(
        provider_owner_email="taller.norte@mechanic.local",
        first_name="Pedro",
        last_name="Salvatierra",
        phone_number="70100001",
        specialty="Batería y diagnóstico eléctrico",
        is_active=True,
        is_available=True,
        current_latitude=-17.7551,
        current_longitude=-63.1805,
    ),
    TechnicianSeed(
        provider_owner_email="taller.norte@mechanic.local",
        first_name="Ramiro",
        last_name="Flores",
        phone_number="70100002",
        specialty="Llanta y auxilio móvil",
        is_active=True,
        is_available=True,
        current_latitude=-17.7518,
        current_longitude=-63.1854,
    ),
    TechnicianSeed(
        provider_owner_email="taller.norte@mechanic.local",
        first_name="Silvia",
        last_name="Aguilera",
        phone_number="70100003",
        specialty="Motor y sobrecalentamiento",
        is_active=True,
        is_available=False,
        current_latitude=-17.7509,
        current_longitude=-63.1798,
    ),
    TechnicianSeed(
        provider_owner_email="taller.express@mechanic.local",
        first_name="Jorge",
        last_name="López",
        phone_number="70100004",
        specialty="Diagnóstico general",
        is_active=True,
        is_available=True,
        current_latitude=-17.7398,
        current_longitude=-63.1719,
    ),
    TechnicianSeed(
        provider_owner_email="taller.express@mechanic.local",
        first_name="Andrés",
        last_name="Mercado",
        phone_number="70100005",
        specialty="Batería y arranque",
        is_active=True,
        is_available=True,
        current_latitude=-17.7371,
        current_longitude=-63.1764,
    ),
    TechnicianSeed(
        provider_owner_email="taller.express@mechanic.local",
        first_name="Gabriel",
        last_name="Cuéllar",
        phone_number="70100006",
        specialty="Llanta y carretera urbana",
        is_active=True,
        is_available=False,
        current_latitude=-17.7422,
        current_longitude=-63.1701,
    ),
    TechnicianSeed(
        provider_owner_email="taller.express@mechanic.local",
        first_name="Daniela",
        last_name="Ribera",
        phone_number="70100007",
        specialty="Atención móvil integral",
        is_active=True,
        is_available=True,
        current_latitude=-17.7359,
        current_longitude=-63.1688,
    ),
    TechnicianSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        first_name="Marcelo",
        last_name="Vaca",
        phone_number="70100008",
        specialty="Grúa y remolque",
        is_active=True,
        is_available=True,
        current_latitude=-17.8235,
        current_longitude=-63.2059,
    ),
    TechnicianSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        first_name="Hugo",
        last_name="Justiniano",
        phone_number="70100009",
        specialty="Accidentes leves y traslado",
        is_active=True,
        is_available=True,
        current_latitude=-17.8261,
        current_longitude=-63.2084,
    ),
    TechnicianSeed(
        provider_owner_email="mecanico.juan@mechanic.local",
        first_name="Juan",
        last_name="Paredes",
        phone_number="70100010",
        specialty="Mecánica rápida a domicilio",
        is_active=True,
        is_available=True,
        current_latitude=-17.7597,
        current_longitude=-63.1962,
    ),
    TechnicianSeed(
        provider_owner_email="mecanico.carlos@mechanic.local",
        first_name="Carlos",
        last_name="Vargas",
        phone_number="70100011",
        specialty="Motor y refrigeración",
        is_active=True,
        is_available=False,
        current_latitude=-17.7916,
        current_longitude=-63.1357,
    ),
)


DEMO_VEHICLES: tuple[VehicleSeed, ...] = (
    VehicleSeed(
        owner_email="cliente.bateria@mechanic.local",
        plate_number="BAT123",
        vehicle_type="CAR",
        brand="Toyota",
        model="Corolla",
        year=2016,
        color="Blanco",
        notes="Vehículo usado para caso demo de batería descargada.",
        is_active=True,
    ),
    VehicleSeed(
        owner_email="cliente.bateria@mechanic.local",
        plate_number="MOT456",
        vehicle_type="MOTORCYCLE",
        brand="Honda",
        model="CB 190R",
        year=2020,
        color="Rojo",
        notes="Motocicleta secundaria del cliente demo.",
        is_active=True,
    ),
    VehicleSeed(
        owner_email="cliente.llanta@mechanic.local",
        plate_number="LLA789",
        vehicle_type="CAR",
        brand="Suzuki",
        model="Swift",
        year=2018,
        color="Azul",
        notes="Vehículo usado para caso demo de pinchazo de llanta.",
        is_active=True,
    ),
    VehicleSeed(
        owner_email="cliente.accidente@mechanic.local",
        plate_number="ACC321",
        vehicle_type="TRUCK",
        brand="Nissan",
        model="Frontier",
        year=2019,
        color="Gris",
        notes="Vehículo usado para caso demo de accidente leve.",
        is_active=True,
    ),
    VehicleSeed(
        owner_email="cliente.accidente@mechanic.local",
        plate_number="CAL654",
        vehicle_type="VAN",
        brand="Hyundai",
        model="Tucson",
        year=2017,
        color="Negro",
        notes="Vehículo usado para caso demo de sobrecalentamiento.",
        is_active=True,
    ),
)


DEMO_PROVIDER_SERVICES: tuple[ProviderServiceSeed, ...] = (
    ProviderServiceSeed(
        provider_owner_email="taller.norte@mechanic.local",
        service_code="BATTERY_JUMPSTART",
        custom_title="Auxilio de batería a domicilio",
        custom_description="Paso de corriente, revisión de bornes y diagnóstico básico de batería.",
        price_estimate_min=Decimal("50.00"),
        price_estimate_max=Decimal("90.00"),
        estimated_duration_minutes=30,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.norte@mechanic.local",
        service_code="TIRE_CHANGE",
        custom_title="Cambio de llanta urbano",
        custom_description="Cambio de llanta, revisión visual y apoyo en vía urbana.",
        price_estimate_min=Decimal("60.00"),
        price_estimate_max=Decimal("100.00"),
        estimated_duration_minutes=35,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.norte@mechanic.local",
        service_code="ENGINE_DIAGNOSTIC",
        custom_title="Diagnóstico mecánico básico",
        custom_description="Evaluación rápida de falla mecánica o eléctrica en sitio.",
        price_estimate_min=Decimal("80.00"),
        price_estimate_max=Decimal("150.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.norte@mechanic.local",
        service_code="OVERHEATING_ASSISTANCE",
        custom_title="Auxilio por sobrecalentamiento",
        custom_description="Revisión preliminar de temperatura, refrigerante y posibles fugas.",
        price_estimate_min=Decimal("70.00"),
        price_estimate_max=Decimal("140.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.express@mechanic.local",
        service_code="BATTERY_JUMPSTART",
        custom_title="Arranque rápido por batería",
        custom_description="Atención rápida para vehículos que no encienden.",
        price_estimate_min=Decimal("45.00"),
        price_estimate_max=Decimal("85.00"),
        estimated_duration_minutes=25,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.express@mechanic.local",
        service_code="TIRE_CHANGE",
        custom_title="Cambio o auxilio de llanta",
        custom_description="Atención móvil por pinchazo, llanta baja o rueda dañada.",
        price_estimate_min=Decimal("55.00"),
        price_estimate_max=Decimal("110.00"),
        estimated_duration_minutes=35,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.express@mechanic.local",
        service_code="LOCKOUT_ASSISTANCE",
        custom_title="Apertura por llave encerrada",
        custom_description="Apoyo básico cuando el cliente dejó la llave dentro del vehículo.",
        price_estimate_min=Decimal("80.00"),
        price_estimate_max=Decimal("160.00"),
        estimated_duration_minutes=40,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.express@mechanic.local",
        service_code="ENGINE_DIAGNOSTIC",
        custom_title="Diagnóstico express",
        custom_description="Revisión inicial de motor, arranque y fallas generales.",
        price_estimate_min=Decimal("90.00"),
        price_estimate_max=Decimal("180.00"),
        estimated_duration_minutes=50,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.express@mechanic.local",
        service_code="OVERHEATING_ASSISTANCE",
        custom_title="Revisión por calentamiento",
        custom_description="Atención preliminar para vehículos detenidos por temperatura alta.",
        price_estimate_min=Decimal("75.00"),
        price_estimate_max=Decimal("150.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        service_code="TOWING",
        custom_title="Servicio de grúa y remolque",
        custom_description="Traslado de vehículo averiado o inmovilizado.",
        price_estimate_min=Decimal("180.00"),
        price_estimate_max=Decimal("450.00"),
        estimated_duration_minutes=60,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        service_code="ACCIDENT_SUPPORT",
        custom_title="Atención inicial por choque leve",
        custom_description="Evaluación visual, apoyo en sitio y coordinación de traslado.",
        price_estimate_min=Decimal("150.00"),
        price_estimate_max=Decimal("350.00"),
        estimated_duration_minutes=70,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        service_code="ENGINE_DIAGNOSTIC",
        custom_title="Diagnóstico para traslado",
        custom_description="Evaluación para determinar si el vehículo requiere remolque.",
        price_estimate_min=Decimal("90.00"),
        price_estimate_max=Decimal("180.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="mecanico.juan@mechanic.local",
        service_code="BATTERY_JUMPSTART",
        custom_title="Paso de corriente independiente",
        custom_description="Atención rápida de batería descargada por mecánico independiente.",
        price_estimate_min=Decimal("40.00"),
        price_estimate_max=Decimal("80.00"),
        estimated_duration_minutes=25,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="mecanico.juan@mechanic.local",
        service_code="TIRE_CHANGE",
        custom_title="Cambio de llanta independiente",
        custom_description="Cambio básico de llanta y revisión visual.",
        price_estimate_min=Decimal("50.00"),
        price_estimate_max=Decimal("90.00"),
        estimated_duration_minutes=30,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="mecanico.juan@mechanic.local",
        service_code="ENGINE_DIAGNOSTIC",
        custom_title="Diagnóstico rápido independiente",
        custom_description="Diagnóstico básico de falla en sitio.",
        price_estimate_min=Decimal("70.00"),
        price_estimate_max=Decimal("130.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="mecanico.carlos@mechanic.local",
        service_code="ENGINE_DIAGNOSTIC",
        custom_title="Revisión de motor",
        custom_description="Diagnóstico inicial de fallas de motor.",
        price_estimate_min=Decimal("80.00"),
        price_estimate_max=Decimal("160.00"),
        estimated_duration_minutes=50,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
    ProviderServiceSeed(
        provider_owner_email="mecanico.carlos@mechanic.local",
        service_code="OVERHEATING_ASSISTANCE",
        custom_title="Auxilio de refrigeración",
        custom_description="Revisión de temperatura, fugas y refrigerante.",
        price_estimate_min=Decimal("70.00"),
        price_estimate_max=Decimal("140.00"),
        estimated_duration_minutes=45,
        is_mobile_service_enabled=True,
        is_emergency_service_enabled=True,
        is_active=True,
    ),
)

DEMO_INCIDENTS: tuple[IncidentSeed, ...] = (
    IncidentSeed(
        demo_key="INC_BATTERY_001",
        client_email="cliente.bateria@mechanic.local",
        vehicle_plate_number="BAT123",
        provider_owner_email=None,
        assigned_technician_phone=None,
        status=INCIDENT_STATUS_PUBLISHED,
        priority=INCIDENT_PRIORITY_MEDIUM,
        reported_category=INCIDENT_CATEGORY_BATTERY,
        title="Vehículo no enciende en estacionamiento",
        description=(
            "El cliente reporta que el vehículo no enciende. Indica que al girar la llave "
            "solo se escuchan clics y el tablero enciende débilmente."
        ),
        client_contact_phone_snapshot="70010001",
        incident_latitude=-17.7833,
        incident_longitude=-63.1821,
        address_reference="Estacionamiento de supermercado, zona centro",
        estimated_price_min=Decimal("50.00"),
        estimated_price_max=Decimal("90.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "Posible problema de batería descargada. El vehículo no enciende y el tablero "
            "presenta baja intensidad. Se recomienda auxilio de batería o revisión eléctrica básica."
        ),
        suggested_category=INCIDENT_CATEGORY_BATTERY,
        suggested_priority=INCIDENT_PRIORITY_MEDIUM,
        requires_more_information=False,
    ),
    IncidentSeed(
        demo_key="INC_TIRE_001",
        client_email="cliente.llanta@mechanic.local",
        vehicle_plate_number="LLA789",
        provider_owner_email=None,
        assigned_technician_phone=None,
        status=INCIDENT_STATUS_PUBLISHED,
        priority=INCIDENT_PRIORITY_MEDIUM,
        reported_category=INCIDENT_CATEGORY_TIRE,
        title="Pinchazo de llanta en carretera urbana",
        description=(
            "El cliente reporta que una llanta perdió aire rápidamente y el vehículo "
            "no puede continuar circulando con seguridad."
        ),
        client_contact_phone_snapshot="70010002",
        incident_latitude=-17.7609,
        incident_longitude=-63.2054,
        address_reference="Av. Banzer, cerca del 5to anillo",
        estimated_price_min=Decimal("55.00"),
        estimated_price_max=Decimal("110.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "Incidente compatible con pinchazo o daño de llanta. Se requiere servicio móvil "
            "de cambio de llanta o auxilio en vía urbana."
        ),
        suggested_category=INCIDENT_CATEGORY_TIRE,
        suggested_priority=INCIDENT_PRIORITY_MEDIUM,
        requires_more_information=False,
    ),
    IncidentSeed(
        demo_key="INC_ACCIDENT_001",
        client_email="cliente.accidente@mechanic.local",
        vehicle_plate_number="ACC321",
        provider_owner_email="taller.gruas@mechanic.local",
        assigned_technician_phone="70100008",
        status=INCIDENT_STATUS_ASSIGNED,
        priority=INCIDENT_PRIORITY_HIGH,
        reported_category=INCIDENT_CATEGORY_ACCIDENT,
        title="Choque leve con daño frontal",
        description=(
            "El cliente reporta un choque leve. El vehículo tiene daño frontal visible "
            "y posiblemente requiere remolque."
        ),
        client_contact_phone_snapshot="70010003",
        incident_latitude=-17.8121,
        incident_longitude=-63.1958,
        address_reference="Doble vía La Guardia, zona km 6",
        estimated_price_min=Decimal("180.00"),
        estimated_price_max=Decimal("450.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "Accidente leve con daño frontal visible. Se recomienda proveedor con capacidad "
            "de grúa o remolque y revisión inicial del daño."
        ),
        suggested_category=INCIDENT_CATEGORY_ACCIDENT,
        suggested_priority=INCIDENT_PRIORITY_HIGH,
        requires_more_information=False,
    ),
    IncidentSeed(
        demo_key="INC_OVERHEATING_001",
        client_email="cliente.accidente@mechanic.local",
        vehicle_plate_number="CAL654",
        provider_owner_email="taller.norte@mechanic.local",
        assigned_technician_phone="70100003",
        status=INCIDENT_STATUS_EN_ROUTE,
        priority=INCIDENT_PRIORITY_MEDIUM,
        reported_category=INCIDENT_CATEGORY_OVERHEATING,
        title="Vehículo detenido por sobrecalentamiento",
        description=(
            "El cliente indica que el indicador de temperatura subió al máximo y salió vapor "
            "del capó. Detuvo el vehículo por seguridad."
        ),
        client_contact_phone_snapshot="70010003",
        incident_latitude=-17.7894,
        incident_longitude=-63.1765,
        address_reference="Av. Cristo Redentor, cerca del 3er anillo",
        estimated_price_min=Decimal("70.00"),
        estimated_price_max=Decimal("140.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "Posible sobrecalentamiento del motor. Se recomienda revisión de refrigerante, "
            "fugas y sistema de enfriamiento antes de continuar la marcha."
        ),
        suggested_category=INCIDENT_CATEGORY_OVERHEATING,
        suggested_priority=INCIDENT_PRIORITY_MEDIUM,
        requires_more_information=False,
    ),
    IncidentSeed(
        demo_key="INC_LOCKOUT_001",
        client_email="cliente.bateria@mechanic.local",
        vehicle_plate_number="MOT456",
        provider_owner_email=None,
        assigned_technician_phone=None,
        status=INCIDENT_STATUS_IN_REVIEW,
        priority=INCIDENT_PRIORITY_MEDIUM,
        reported_category=INCIDENT_CATEGORY_LOCKOUT,
        title="Llave encerrada dentro del vehículo",
        description=(
            "El cliente indica que dejó la llave dentro del vehículo y no puede abrirlo. "
            "Solicita apoyo para apertura."
        ),
        client_contact_phone_snapshot="70010001",
        incident_latitude=-17.7712,
        incident_longitude=-63.1873,
        address_reference="Zona Equipetrol, parqueo privado",
        estimated_price_min=Decimal("80.00"),
        estimated_price_max=Decimal("160.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "Caso de llave encerrada o bloqueo de acceso. Se requiere servicio de apertura "
            "vehicular o asistencia de cerrajería automotriz."
        ),
        suggested_category=INCIDENT_CATEGORY_LOCKOUT,
        suggested_priority=INCIDENT_PRIORITY_MEDIUM,
        requires_more_information=False,
    ),
    IncidentSeed(
        demo_key="INC_UNCERTAIN_001",
        client_email="cliente.llanta@mechanic.local",
        vehicle_plate_number="LLA789",
        provider_owner_email=None,
        assigned_technician_phone=None,
        status=INCIDENT_STATUS_PENDING,
        priority=INCIDENT_PRIORITY_MEDIUM,
        reported_category=INCIDENT_CATEGORY_UNCERTAIN,
        title="Ruido extraño y pérdida de fuerza",
        description=(
            "El cliente reporta un ruido extraño y pérdida de fuerza, pero no logra identificar "
            "si el problema es motor, caja, llanta o batería."
        ),
        client_contact_phone_snapshot="70010002",
        incident_latitude=-17.7981,
        incident_longitude=-63.1642,
        address_reference="Zona Mutualista, avenida principal",
        estimated_price_min=Decimal("80.00"),
        estimated_price_max=Decimal("180.00"),
        ai_summary_status=PROCESSING_STATUS_SUCCEEDED,
        summary_provider_name="demo_openrouter",
        structured_summary=(
            "La información es ambigua. El síntoma principal es ruido extraño y pérdida "
            "de fuerza. Se requiere más información o revisión manual."
        ),
        suggested_category=INCIDENT_CATEGORY_UNCERTAIN,
        suggested_priority=INCIDENT_PRIORITY_MEDIUM,
        requires_more_information=True,
    ),
)

DEMO_EVIDENCES: tuple[EvidenceSeed, ...] = (
    EvidenceSeed(
        incident_demo_key="INC_BATTERY_001",
        uploaded_by_email="cliente.bateria@mechanic.local",
        evidence_type=EVIDENCE_TYPE_TEXT,
        original_filename="reporte_bateria.txt",
        stored_filename="demo_battery_text.txt",
        file_extension=".txt",
        mime_type="text/plain",
        file_size_bytes=180,
        description="Texto enviado por el cliente.",
        text_content_snapshot="Mi auto no enciende, solo hace clic y el tablero se ve débil.",
        audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        audio_provider_name=None,
        transcript_text=None,
        transcript_language_code=None,
        transcript_confidence=None,
        image_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        image_provider_name=None,
        image_labels_json=None,
        image_detections_json=None,
        image_summary=None,
    ),
    EvidenceSeed(
        incident_demo_key="INC_BATTERY_001",
        uploaded_by_email="cliente.bateria@mechanic.local",
        evidence_type=EVIDENCE_TYPE_AUDIO,
        original_filename="audio_bateria.m4a",
        stored_filename="demo_battery_audio.m4a",
        file_extension=".m4a",
        mime_type="audio/mp4",
        file_size_bytes=850000,
        description="Audio describiendo el problema de batería.",
        text_content_snapshot=None,
        audio_processing_status=PROCESSING_STATUS_SUCCEEDED,
        audio_provider_name="demo_faster_whisper",
        transcript_text="El auto no quiere encender, solo suena un clic y parece que la batería está baja.",
        transcript_language_code="es",
        transcript_confidence=0.93,
        image_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        image_provider_name=None,
        image_labels_json=None,
        image_detections_json=None,
        image_summary=None,
    ),
    EvidenceSeed(
        incident_demo_key="INC_BATTERY_001",
        uploaded_by_email="cliente.bateria@mechanic.local",
        evidence_type=EVIDENCE_TYPE_IMAGE,
        original_filename="tablero_bateria.jpg",
        stored_filename="demo_battery_dashboard.jpg",
        file_extension=".jpg",
        mime_type="image/jpeg",
        file_size_bytes=620000,
        description="Foto del tablero del vehículo.",
        text_content_snapshot=None,
        audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        audio_provider_name=None,
        transcript_text=None,
        transcript_language_code=None,
        transcript_confidence=None,
        image_processing_status=PROCESSING_STATUS_SUCCEEDED,
        image_provider_name="demo_yolo",
        image_labels_json=["dashboard", "battery_warning", "vehicle_interior"],
        image_detections_json=[
            {"label": "dashboard", "confidence": 0.88},
            {"label": "battery_warning", "confidence": 0.81},
        ],
        image_summary="La imagen parece mostrar el tablero del vehículo con posible indicador de batería.",
    ),
    EvidenceSeed(
        incident_demo_key="INC_TIRE_001",
        uploaded_by_email="cliente.llanta@mechanic.local",
        evidence_type=EVIDENCE_TYPE_IMAGE,
        original_filename="llanta_danada.jpg",
        stored_filename="demo_tire_damage.jpg",
        file_extension=".jpg",
        mime_type="image/jpeg",
        file_size_bytes=700000,
        description="Foto de la llanta dañada.",
        text_content_snapshot=None,
        audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        audio_provider_name=None,
        transcript_text=None,
        transcript_language_code=None,
        transcript_confidence=None,
        image_processing_status=PROCESSING_STATUS_SUCCEEDED,
        image_provider_name="demo_yolo",
        image_labels_json=["tire", "flat_tire", "vehicle_wheel"],
        image_detections_json=[
            {"label": "tire", "confidence": 0.91},
            {"label": "flat_tire", "confidence": 0.84},
        ],
        image_summary="La imagen sugiere una llanta desinflada o dañada.",
    ),
    EvidenceSeed(
        incident_demo_key="INC_ACCIDENT_001",
        uploaded_by_email="cliente.accidente@mechanic.local",
        evidence_type=EVIDENCE_TYPE_AUDIO,
        original_filename="audio_accidente.m4a",
        stored_filename="demo_accident_audio.m4a",
        file_extension=".m4a",
        mime_type="audio/mp4",
        file_size_bytes=920000,
        description="Audio indicando choque leve.",
        text_content_snapshot=None,
        audio_processing_status=PROCESSING_STATUS_SUCCEEDED,
        audio_provider_name="demo_faster_whisper",
        transcript_text="Tuve un choque leve, la parte delantera está golpeada y creo que necesito grúa.",
        transcript_language_code="es",
        transcript_confidence=0.95,
        image_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        image_provider_name=None,
        image_labels_json=None,
        image_detections_json=None,
        image_summary=None,
    ),
    EvidenceSeed(
        incident_demo_key="INC_ACCIDENT_001",
        uploaded_by_email="cliente.accidente@mechanic.local",
        evidence_type=EVIDENCE_TYPE_IMAGE,
        original_filename="choque_frontal.jpg",
        stored_filename="demo_accident_front.jpg",
        file_extension=".jpg",
        mime_type="image/jpeg",
        file_size_bytes=1150000,
        description="Foto del daño frontal.",
        text_content_snapshot=None,
        audio_processing_status=PROCESSING_STATUS_NOT_REQUESTED,
        audio_provider_name=None,
        transcript_text=None,
        transcript_language_code=None,
        transcript_confidence=None,
        image_processing_status=PROCESSING_STATUS_SUCCEEDED,
        image_provider_name="demo_yolo",
        image_labels_json=["car", "vehicle_damage", "front_damage"],
        image_detections_json=[
            {"label": "car", "confidence": 0.94},
            {"label": "vehicle_damage", "confidence": 0.86},
        ],
        image_summary="La imagen muestra posible daño frontal compatible con choque leve.",
    ),
)

DEMO_ASSIGNMENT_CANDIDATES: tuple[AssignmentCandidateSeed, ...] = (
    AssignmentCandidateSeed(
        incident_demo_key="INC_BATTERY_001",
        provider_owner_email="taller.norte@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
        recommendation_rank=1,
        score=92.5,
        distance_km=2.8,
        required_service_codes_json=["BATTERY_JUMPSTART"],
        matched_service_codes_json=["BATTERY_JUMPSTART"],
        rationale_json={
            "distance": "Proveedor cercano al incidente",
            "service_match": "Ofrece auxilio de batería",
            "capacity": "Tiene capacidad disponible",
            "rating": "Buena calificación promedio",
        },
        provider_available_capacity_snapshot=3,
        available_technicians_count_snapshot=2,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_BATTERY_001",
        provider_owner_email="mecanico.juan@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
        recommendation_rank=2,
        score=86.0,
        distance_km=3.6,
        required_service_codes_json=["BATTERY_JUMPSTART"],
        matched_service_codes_json=["BATTERY_JUMPSTART"],
        rationale_json={
            "distance": "Distancia aceptable",
            "service_match": "Mecánico independiente ofrece paso de corriente",
            "capacity": "Disponible",
        },
        provider_available_capacity_snapshot=1,
        available_technicians_count_snapshot=1,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_BATTERY_001",
        provider_owner_email="taller.express@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
        recommendation_rank=3,
        score=81.5,
        distance_km=5.1,
        required_service_codes_json=["BATTERY_JUMPSTART"],
        matched_service_codes_json=["BATTERY_JUMPSTART"],
        rationale_json={
            "distance": "Más alejado, pero disponible",
            "service_match": "Ofrece arranque rápido por batería",
        },
        provider_available_capacity_snapshot=3,
        available_technicians_count_snapshot=3,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_TIRE_001",
        provider_owner_email="taller.express@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
        recommendation_rank=1,
        score=90.0,
        distance_km=1.7,
        required_service_codes_json=["TIRE_CHANGE"],
        matched_service_codes_json=["TIRE_CHANGE"],
        rationale_json={
            "distance": "Muy cercano",
            "service_match": "Ofrece cambio o auxilio de llanta",
            "capacity": "Cuenta con técnicos disponibles",
        },
        provider_available_capacity_snapshot=3,
        available_technicians_count_snapshot=3,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_TIRE_001",
        provider_owner_email="taller.norte@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_AVAILABLE,
        recommendation_rank=2,
        score=84.0,
        distance_km=4.2,
        required_service_codes_json=["TIRE_CHANGE"],
        matched_service_codes_json=["TIRE_CHANGE"],
        rationale_json={
            "distance": "Distancia media",
            "service_match": "También ofrece cambio de llanta",
        },
        provider_available_capacity_snapshot=3,
        available_technicians_count_snapshot=2,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
        recommendation_rank=1,
        score=95.0,
        distance_km=2.2,
        required_service_codes_json=["TOWING", "ACCIDENT_SUPPORT"],
        matched_service_codes_json=["TOWING", "ACCIDENT_SUPPORT"],
        rationale_json={
            "distance": "Cercano al lugar del accidente",
            "service_match": "Especializado en grúa y accidentes leves",
            "rating": "Mejor calificación para este tipo de caso",
        },
        provider_available_capacity_snapshot=2,
        available_technicians_count_snapshot=2,
    ),
    AssignmentCandidateSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.express@mechanic.local",
        status=ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
        recommendation_rank=2,
        score=72.0,
        distance_km=7.8,
        required_service_codes_json=["TOWING", "ACCIDENT_SUPPORT"],
        matched_service_codes_json=[],
        rationale_json={
            "distance": "Más alejado",
            "service_match": "No especializado en grúa",
            "decision": "Rechazado para demo",
        },
        provider_available_capacity_snapshot=3,
        available_technicians_count_snapshot=3,
    ),
)

DEMO_OPERATION_EVENTS: tuple[OperationEventSeed, ...] = (
    OperationEventSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        technician_phone="70100008",
        actor_email="taller.gruas@mechanic.local",
        event_type=INCIDENT_OPERATION_EVENT_DISPATCHED,
        from_status=INCIDENT_STATUS_ASSIGNED,
        to_status=INCIDENT_STATUS_EN_ROUTE,
        note="Se despacha técnico con grúa hacia el punto del accidente.",
        payload_json={"dispatch_mode": DISPATCH_MODE_TECHNICIAN},
    ),
    OperationEventSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        technician_phone="70100003",
        actor_email="taller.norte@mechanic.local",
        event_type=INCIDENT_OPERATION_EVENT_DISPATCHED,
        from_status=INCIDENT_STATUS_ASSIGNED,
        to_status=INCIDENT_STATUS_EN_ROUTE,
        note="Técnico asignado se encuentra en camino para revisar sobrecalentamiento.",
        payload_json={"dispatch_mode": DISPATCH_MODE_TECHNICIAN},
    ),
    OperationEventSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        technician_phone="70100003",
        actor_email="taller.norte@mechanic.local",
        event_type=INCIDENT_OPERATION_EVENT_ARRIVED_ON_SITE,
        from_status=INCIDENT_STATUS_EN_ROUTE,
        to_status=INCIDENT_STATUS_ON_SITE,
        note="Técnico llegó al punto y está revisando el vehículo.",
        payload_json={"arrival_confirmed": True},
    ),
    OperationEventSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        technician_phone="70100003",
        actor_email="taller.norte@mechanic.local",
        event_type=INCIDENT_OPERATION_EVENT_SERVICE_STARTED,
        from_status=INCIDENT_STATUS_ON_SITE,
        to_status=INCIDENT_STATUS_IN_PROGRESS,
        note="Se inicia revisión del sistema de refrigeración.",
        payload_json={"work_started": True},
    ),
    OperationEventSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        technician_phone="70100008",
        actor_email="taller.gruas@mechanic.local",
        event_type=INCIDENT_OPERATION_EVENT_SERVICE_COMPLETED,
        from_status=INCIDENT_STATUS_IN_PROGRESS,
        to_status=INCIDENT_STATUS_COMPLETED,
        note="Servicio demo completado: vehículo trasladado al taller.",
        payload_json={"completed": True, "requires_follow_up": True},
    ),
)

DEMO_TRACKING_PINGS: tuple[TrackingPingSeed, ...] = (
    TrackingPingSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        technician_phone="70100008",
        source_type=TRACKING_SOURCE_TECHNICIAN,
        latitude=-17.8245,
        longitude=-63.2071,
        accuracy_meters=12.0,
        minutes_ago=18,
    ),
    TrackingPingSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        technician_phone="70100008",
        source_type=TRACKING_SOURCE_TECHNICIAN,
        latitude=-17.8201,
        longitude=-63.2038,
        accuracy_meters=10.0,
        minutes_ago=12,
    ),
    TrackingPingSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        technician_phone="70100008",
        source_type=TRACKING_SOURCE_TECHNICIAN,
        latitude=-17.8152,
        longitude=-63.1997,
        accuracy_meters=9.0,
        minutes_ago=6,
    ),
    TrackingPingSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        technician_phone="70100003",
        source_type=TRACKING_SOURCE_TECHNICIAN,
        latitude=-17.7539,
        longitude=-63.1816,
        accuracy_meters=11.0,
        minutes_ago=10,
    ),
    TrackingPingSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        technician_phone="70100003",
        source_type=TRACKING_SOURCE_TECHNICIAN,
        latitude=-17.7721,
        longitude=-63.1792,
        accuracy_meters=8.0,
        minutes_ago=5,
    ),
)


def seed_demo_data(db: Session) -> None:
    """
    Ejecuta todas las semillas demo disponibles.

    Cada fase es idempotente para poder ejecutarse varias veces sin duplicar datos.
    """

    logger.info("Starting complete demo seed process...")

    seed_steps: list[tuple[str, Callable[[Session], None]]] = [
        ("step_01_roles_users_and_providers", seed_step_01_roles_users_and_providers),
        ("step_02_technicians_vehicles_and_services", seed_step_02_technicians_vehicles_and_services),
        ("step_03_incidents_evidences_and_ai", seed_step_03_incidents_evidences_and_ai),
        ("step_04_assignment_operations_and_tracking", seed_step_04_assignment_operations_and_tracking),
        (
        "step_05_billing_subscriptions_notifications_and_audit",
        seed_step_05_billing_subscriptions_notifications_and_audit,
        ),
        (
            "step_06_technician_mobile_users",
            seed_step_06_technician_mobile_users,
        ),
        
    ]

    for step_name, step_function in seed_steps:
        logger.info("Running demo seed step: %s", step_name)
        step_function(db)
        db.flush()
        logger.info("Finished demo seed step: %s", step_name)

    db.commit()

    logger.info("Complete demo seed process finished successfully.")


def seed_step_01_roles_users_and_providers(db: Session) -> None:
    seed_roles(db)
    seed_users(db)
    seed_providers(db)


def seed_step_02_technicians_vehicles_and_services(db: Session) -> None:
    seed_technicians(db)
    seed_vehicles(db)
    seed_service_catalog_items(db)
    seed_provider_services(db)

def seed_step_03_incidents_evidences_and_ai(db: Session) -> None:
    seed_incidents(db)
    seed_evidences(db)

def seed_step_04_assignment_operations_and_tracking(db: Session) -> None:
    seed_assignment_candidates(db)
    seed_operation_events(db)
    seed_tracking_pings(db)
    update_demo_incident_tracking_snapshots(db)

def seed_roles(db: Session) -> None:
    for role_seed in SYSTEM_ROLES:
        role = get_role_by_code(db, role_seed.code)

        if role is None:
            role = Role(
                code=role_seed.code,
                name=role_seed.name,
                description=role_seed.description,
                is_system=True,
            )
            db.add(role)
            logger.info("Created role: %s", role_seed.code)
        else:
            role.name = role_seed.name
            role.description = role_seed.description
            role.is_system = True
            db.add(role)
            logger.info("Updated role: %s", role_seed.code)

    db.flush()


def seed_users(db: Session) -> None:
    for user_seed in DEMO_USERS:
        role = get_role_by_code(db, user_seed.role_code)
        if role is None:
            raise RuntimeError(f"Role {user_seed.role_code} was not found.")

        normalized_email = normalize_email(user_seed.email)
        user = get_user_by_email(db, normalized_email)

        if user is None:
            user = User(
                email=normalized_email,
                password_hash=hash_password(user_seed.password),
                first_name=user_seed.first_name.strip(),
                last_name=user_seed.last_name.strip(),
                phone_number=normalize_optional_text(user_seed.phone_number),
                is_active=True,
                is_superuser=user_seed.is_superuser,
                roles=[role],
            )
            db.add(user)
            logger.info("Created demo user: %s", normalized_email)
        else:
            user.password_hash = hash_password(user_seed.password)
            user.first_name = user_seed.first_name.strip()
            user.last_name = user_seed.last_name.strip()
            user.phone_number = normalize_optional_text(user_seed.phone_number)
            user.is_active = True
            user.is_superuser = user_seed.is_superuser

            ensure_user_has_role(user, role)

            db.add(user)
            logger.info("Updated demo user: %s", normalized_email)

    db.flush()


def seed_providers(db: Session) -> None:
    for provider_seed in DEMO_PROVIDERS:
        owner_email = normalize_email(provider_seed.owner_email)
        owner_user = get_user_by_email(db, owner_email)

        if owner_user is None:
            raise RuntimeError(
                f"Provider owner user {owner_email} was not found. "
                "Run seed_users before seed_providers."
            )

        provider = get_provider_by_owner_user_id(db, owner_user.id)

        if provider is None:
            provider = Provider(
                owner_user_id=owner_user.id,
                provider_type=provider_seed.provider_type,
                business_name=provider_seed.business_name,
                legal_name=provider_seed.legal_name,
                description=provider_seed.description,
                contact_email=provider_seed.contact_email,
                contact_phone=provider_seed.contact_phone,
                city=provider_seed.city,
                address=provider_seed.address,
                base_latitude=provider_seed.base_latitude,
                base_longitude=provider_seed.base_longitude,
                is_active=provider_seed.is_active,
                is_available=provider_seed.is_available,
                max_concurrent_services=provider_seed.max_concurrent_services,
                current_active_services=provider_seed.current_active_services,
                average_rating=provider_seed.average_rating,
            )
            db.add(provider)
            logger.info("Created demo provider: %s", provider_seed.business_name)
        else:
            provider.provider_type = provider_seed.provider_type
            provider.business_name = provider_seed.business_name
            provider.legal_name = provider_seed.legal_name
            provider.description = provider_seed.description
            provider.contact_email = provider_seed.contact_email
            provider.contact_phone = provider_seed.contact_phone
            provider.city = provider_seed.city
            provider.address = provider_seed.address
            provider.base_latitude = provider_seed.base_latitude
            provider.base_longitude = provider_seed.base_longitude
            provider.is_active = provider_seed.is_active
            provider.is_available = provider_seed.is_available
            provider.max_concurrent_services = provider_seed.max_concurrent_services
            provider.current_active_services = provider_seed.current_active_services
            provider.average_rating = provider_seed.average_rating

            db.add(provider)
            logger.info("Updated demo provider: %s", provider_seed.business_name)

    db.flush()


def seed_technicians(db: Session) -> None:
    for technician_seed in DEMO_TECHNICIANS:
        provider = get_provider_by_owner_email(db, technician_seed.provider_owner_email)

        if provider is None:
            raise RuntimeError(
                f"Provider linked to {technician_seed.provider_owner_email} was not found."
            )

        normalized_phone = technician_seed.phone_number.strip()
        technician = get_technician_by_provider_and_phone(
            db=db,
            provider_id=provider.id,
            phone_number=normalized_phone,
        )

        if technician is None:
            technician = Technician(
                provider_id=provider.id,
                first_name=technician_seed.first_name.strip(),
                last_name=technician_seed.last_name.strip(),
                phone_number=normalized_phone,
                specialty=normalize_optional_text(technician_seed.specialty),
                is_active=technician_seed.is_active,
                is_available=technician_seed.is_available,
                current_latitude=technician_seed.current_latitude,
                current_longitude=technician_seed.current_longitude,
            )
            db.add(technician)
            logger.info(
                "Created demo technician: %s %s",
                technician_seed.first_name,
                technician_seed.last_name,
            )
        else:
            technician.first_name = technician_seed.first_name.strip()
            technician.last_name = technician_seed.last_name.strip()
            technician.phone_number = normalized_phone
            technician.specialty = normalize_optional_text(technician_seed.specialty)
            technician.is_active = technician_seed.is_active
            technician.is_available = technician_seed.is_available
            technician.current_latitude = technician_seed.current_latitude
            technician.current_longitude = technician_seed.current_longitude

            db.add(technician)
            logger.info(
                "Updated demo technician: %s %s",
                technician_seed.first_name,
                technician_seed.last_name,
            )

    db.flush()


def seed_vehicles(db: Session) -> None:
    for vehicle_seed in DEMO_VEHICLES:
        owner = get_user_by_email(db, vehicle_seed.owner_email)

        if owner is None:
            raise RuntimeError(f"Vehicle owner {vehicle_seed.owner_email} was not found.")

        normalized_plate = vehicle_seed.plate_number.strip().upper()
        vehicle = get_vehicle_by_plate_number(db, normalized_plate)

        if vehicle is None:
            vehicle = Vehicle(
                owner_user_id=owner.id,
                plate_number=normalized_plate,
                vehicle_type=vehicle_seed.vehicle_type.strip().upper(),
                brand=vehicle_seed.brand.strip(),
                model=vehicle_seed.model.strip(),
                year=vehicle_seed.year,
                color=normalize_optional_text(vehicle_seed.color),
                notes=normalize_optional_text(vehicle_seed.notes),
                is_active=vehicle_seed.is_active,
            )
            db.add(vehicle)
            logger.info("Created demo vehicle: %s", normalized_plate)
        else:
            vehicle.owner_user_id = owner.id
            vehicle.plate_number = normalized_plate
            vehicle.vehicle_type = vehicle_seed.vehicle_type.strip().upper()
            vehicle.brand = vehicle_seed.brand.strip()
            vehicle.model = vehicle_seed.model.strip()
            vehicle.year = vehicle_seed.year
            vehicle.color = normalize_optional_text(vehicle_seed.color)
            vehicle.notes = normalize_optional_text(vehicle_seed.notes)
            vehicle.is_active = vehicle_seed.is_active

            db.add(vehicle)
            logger.info("Updated demo vehicle: %s", normalized_plate)

    db.flush()


def seed_service_catalog_items(db: Session) -> None:
    for item_seed in INITIAL_SERVICE_CATALOG_ITEMS:
        code = str(item_seed["code"]).strip().upper()
        item = get_service_catalog_item_by_code(db, code)

        if item is None:
            item = ServiceCatalogItem(
                code=code,
                category=str(item_seed["category"]).strip().upper(),
                title=str(item_seed["title"]).strip(),
                description=normalize_optional_text(str(item_seed.get("description") or "")),
                supports_mobile_service=bool(item_seed["supports_mobile_service"]),
                supports_emergency_service=bool(item_seed["supports_emergency_service"]),
                is_active=True,
                sort_order=int(item_seed["sort_order"]),
            )
            db.add(item)
            logger.info("Created service catalog item: %s", code)
        else:
            item.category = str(item_seed["category"]).strip().upper()
            item.title = str(item_seed["title"]).strip()
            item.description = normalize_optional_text(str(item_seed.get("description") or ""))
            item.supports_mobile_service = bool(item_seed["supports_mobile_service"])
            item.supports_emergency_service = bool(item_seed["supports_emergency_service"])
            item.is_active = True
            item.sort_order = int(item_seed["sort_order"])

            db.add(item)
            logger.info("Updated service catalog item: %s", code)

    db.flush()


def seed_provider_services(db: Session) -> None:
    for provider_service_seed in DEMO_PROVIDER_SERVICES:
        provider = get_provider_by_owner_email(db, provider_service_seed.provider_owner_email)
        if provider is None:
            raise RuntimeError(
                f"Provider linked to {provider_service_seed.provider_owner_email} was not found."
            )

        service_catalog_item = get_service_catalog_item_by_code(
            db,
            provider_service_seed.service_code,
        )
        if service_catalog_item is None:
            raise RuntimeError(
                f"Service catalog item {provider_service_seed.service_code} was not found."
            )

        provider_service = get_provider_service_by_provider_and_catalog_item(
            db=db,
            provider_id=provider.id,
            service_catalog_item_id=service_catalog_item.id,
        )

        if provider_service is None:
            provider_service = ProviderService(
                provider_id=provider.id,
                service_catalog_item_id=service_catalog_item.id,
                custom_title=normalize_optional_text(provider_service_seed.custom_title),
                custom_description=normalize_optional_text(provider_service_seed.custom_description),
                price_estimate_min=provider_service_seed.price_estimate_min,
                price_estimate_max=provider_service_seed.price_estimate_max,
                estimated_duration_minutes=provider_service_seed.estimated_duration_minutes,
                is_mobile_service_enabled=provider_service_seed.is_mobile_service_enabled,
                is_emergency_service_enabled=provider_service_seed.is_emergency_service_enabled,
                is_active=provider_service_seed.is_active,
            )
            db.add(provider_service)
            logger.info(
                "Created provider service: provider=%s service=%s",
                provider.business_name,
                provider_service_seed.service_code,
            )
        else:
            provider_service.custom_title = normalize_optional_text(provider_service_seed.custom_title)
            provider_service.custom_description = normalize_optional_text(
                provider_service_seed.custom_description
            )
            provider_service.price_estimate_min = provider_service_seed.price_estimate_min
            provider_service.price_estimate_max = provider_service_seed.price_estimate_max
            provider_service.estimated_duration_minutes = (
                provider_service_seed.estimated_duration_minutes
            )
            provider_service.is_mobile_service_enabled = (
                provider_service_seed.is_mobile_service_enabled
            )
            provider_service.is_emergency_service_enabled = (
                provider_service_seed.is_emergency_service_enabled
            )
            provider_service.is_active = provider_service_seed.is_active

            db.add(provider_service)
            logger.info(
                "Updated provider service: provider=%s service=%s",
                provider.business_name,
                provider_service_seed.service_code,
            )

    db.flush()


def get_role_by_code(db: Session, role_code: str) -> Role | None:
    query = select(Role).where(Role.code == role_code)
    return db.execute(query).scalar_one_or_none()


def get_user_by_email(db: Session, email: str) -> User | None:
    query = select(User).where(User.email == normalize_email(email))
    return db.execute(query).scalar_one_or_none()


def get_provider_by_owner_user_id(db: Session, owner_user_id: Any) -> Provider | None:
    query = select(Provider).where(Provider.owner_user_id == owner_user_id)
    return db.execute(query).scalar_one_or_none()


def get_provider_by_owner_email(db: Session, owner_email: str) -> Provider | None:
    owner_user = get_user_by_email(db, owner_email)
    if owner_user is None:
        return None

    return get_provider_by_owner_user_id(db, owner_user.id)


def get_technician_by_provider_and_phone(
    db: Session,
    provider_id: Any,
    phone_number: str,
) -> Technician | None:
    query = select(Technician).where(
        Technician.provider_id == provider_id,
        Technician.phone_number == phone_number,
    )
    return db.execute(query).scalar_one_or_none()


def get_vehicle_by_plate_number(db: Session, plate_number: str) -> Vehicle | None:
    query = select(Vehicle).where(Vehicle.plate_number == plate_number.strip().upper())
    return db.execute(query).scalar_one_or_none()


def get_service_catalog_item_by_code(
    db: Session,
    service_code: str,
) -> ServiceCatalogItem | None:
    query = select(ServiceCatalogItem).where(
        ServiceCatalogItem.code == service_code.strip().upper()
    )
    return db.execute(query).scalar_one_or_none()


def get_provider_service_by_provider_and_catalog_item(
    db: Session,
    provider_id: Any,
    service_catalog_item_id: Any,
) -> ProviderService | None:
    query = select(ProviderService).where(
        ProviderService.provider_id == provider_id,
        ProviderService.service_catalog_item_id == service_catalog_item_id,
    )
    return db.execute(query).scalar_one_or_none()


def ensure_user_has_role(user: User, role: Role) -> None:
    current_role_codes = {existing_role.code for existing_role in user.roles}

    if role.code not in current_role_codes:
        user.roles.append(role)


def normalize_email(email: str) -> str:
    return email.strip().lower()


def normalize_optional_text(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned_value = value.strip()
    return cleaned_value or None


def run() -> None:
    configure_logging()

    configure_mappers()

    db = SessionLocal()

    try:
        seed_demo_data(db)
    except Exception:
        db.rollback()
        logger.exception("Demo seed process failed.")
        raise
    finally:
        db.close()

def seed_step_02_technicians_vehicles_and_services(db: Session) -> None:
    seed_technicians(db)
    seed_vehicles(db)
    seed_service_catalog_items(db)
    seed_provider_services(db)

def seed_incidents(db: Session) -> None:
    processed_at = datetime.now(timezone.utc) - timedelta(minutes=20)

    for incident_seed in DEMO_INCIDENTS:
        client = get_user_by_email(db, incident_seed.client_email)
        if client is None:
            raise RuntimeError(f"Client {incident_seed.client_email} was not found.")

        vehicle = get_vehicle_by_plate_number(db, incident_seed.vehicle_plate_number)
        if vehicle is None:
            raise RuntimeError(f"Vehicle {incident_seed.vehicle_plate_number} was not found.")

        provider = None
        if incident_seed.provider_owner_email:
            provider = get_provider_by_owner_email(db, incident_seed.provider_owner_email)
            if provider is None:
                raise RuntimeError(
                    f"Provider linked to {incident_seed.provider_owner_email} was not found."
                )

        assigned_technician = None
        if provider is not None and incident_seed.assigned_technician_phone:
            assigned_technician = get_technician_by_provider_and_phone(
                db=db,
                provider_id=provider.id,
                phone_number=incident_seed.assigned_technician_phone,
            )
            if assigned_technician is None:
                raise RuntimeError(
                    f"Technician {incident_seed.assigned_technician_phone} was not found."
                )

        incident = get_incident_by_demo_key(db, incident_seed.demo_key)

        if incident is None:
            incident = Incident(
                client_user_id=client.id,
                vehicle_id=vehicle.id,
                provider_id=provider.id if provider else None,
                assigned_technician_id=assigned_technician.id if assigned_technician else None,
                status=incident_seed.status,
                priority=incident_seed.priority,
                reported_category=incident_seed.reported_category,
                title=f"[{incident_seed.demo_key}] {incident_seed.title}",
                description=incident_seed.description,
                client_contact_phone_snapshot=incident_seed.client_contact_phone_snapshot,
                incident_latitude=incident_seed.incident_latitude,
                incident_longitude=incident_seed.incident_longitude,
                address_reference=incident_seed.address_reference,
                estimated_price_min=incident_seed.estimated_price_min,
                estimated_price_max=incident_seed.estimated_price_max,
                ai_summary_status=incident_seed.ai_summary_status,
                summary_provider_name=incident_seed.summary_provider_name,
                structured_summary=incident_seed.structured_summary,
                suggested_category=incident_seed.suggested_category,
                suggested_priority=incident_seed.suggested_priority,
                requires_more_information=incident_seed.requires_more_information,
                summary_processed_at=processed_at,
            )
            db.add(incident)
            logger.info("Created demo incident: %s", incident_seed.demo_key)
        else:
            incident.client_user_id = client.id
            incident.vehicle_id = vehicle.id
            incident.provider_id = provider.id if provider else None
            incident.assigned_technician_id = assigned_technician.id if assigned_technician else None
            incident.status = incident_seed.status
            incident.priority = incident_seed.priority
            incident.reported_category = incident_seed.reported_category
            incident.title = f"[{incident_seed.demo_key}] {incident_seed.title}"
            incident.description = incident_seed.description
            incident.client_contact_phone_snapshot = incident_seed.client_contact_phone_snapshot
            incident.incident_latitude = incident_seed.incident_latitude
            incident.incident_longitude = incident_seed.incident_longitude
            incident.address_reference = incident_seed.address_reference
            incident.estimated_price_min = incident_seed.estimated_price_min
            incident.estimated_price_max = incident_seed.estimated_price_max
            incident.ai_summary_status = incident_seed.ai_summary_status
            incident.summary_provider_name = incident_seed.summary_provider_name
            incident.structured_summary = incident_seed.structured_summary
            incident.suggested_category = incident_seed.suggested_category
            incident.suggested_priority = incident_seed.suggested_priority
            incident.requires_more_information = incident_seed.requires_more_information
            incident.summary_processed_at = processed_at

            db.add(incident)
            logger.info("Updated demo incident: %s", incident_seed.demo_key)

    db.flush()


def seed_evidences(db: Session) -> None:
    processed_at = datetime.now(timezone.utc) - timedelta(minutes=10)

    for evidence_seed in DEMO_EVIDENCES:
        incident = get_incident_by_demo_key(db, evidence_seed.incident_demo_key)
        if incident is None:
            raise RuntimeError(f"Incident {evidence_seed.incident_demo_key} was not found.")

        uploaded_by = get_user_by_email(db, evidence_seed.uploaded_by_email)
        if uploaded_by is None:
            raise RuntimeError(f"Uploader {evidence_seed.uploaded_by_email} was not found.")

        evidence = get_evidence_by_incident_and_filename(
            db=db,
            incident_id=incident.id,
            stored_filename=evidence_seed.stored_filename,
        )

        if evidence is None:
            evidence = IncidentEvidence(
                incident_id=incident.id,
                uploaded_by_user_id=uploaded_by.id,
                evidence_type=evidence_seed.evidence_type,
                original_filename=evidence_seed.original_filename,
                stored_filename=evidence_seed.stored_filename,
                file_extension=evidence_seed.file_extension,
                mime_type=evidence_seed.mime_type,
                file_size_bytes=evidence_seed.file_size_bytes,
                description=evidence_seed.description,
                text_content_snapshot=evidence_seed.text_content_snapshot,
                storage_provider="local",
                storage_bucket=None,
                storage_object_key=None,
                public_url=None,
                absolute_file_path=None,
                audio_processing_status=evidence_seed.audio_processing_status,
                audio_provider_name=evidence_seed.audio_provider_name,
                transcript_text=evidence_seed.transcript_text,
                transcript_language_code=evidence_seed.transcript_language_code,
                transcript_confidence=evidence_seed.transcript_confidence,
                transcript_segments_json=None,
                audio_processed_at=processed_at
                if evidence_seed.audio_processing_status == PROCESSING_STATUS_SUCCEEDED
                else None,
                audio_error_message=None,
                image_processing_status=evidence_seed.image_processing_status,
                image_provider_name=evidence_seed.image_provider_name,
                image_labels_json=evidence_seed.image_labels_json,
                image_detections_json=evidence_seed.image_detections_json,
                image_summary=evidence_seed.image_summary,
                image_processed_at=processed_at
                if evidence_seed.image_processing_status == PROCESSING_STATUS_SUCCEEDED
                else None,
                image_error_message=None,
            )
            db.add(evidence)
            logger.info(
                "Created demo evidence: incident=%s file=%s",
                evidence_seed.incident_demo_key,
                evidence_seed.stored_filename,
            )
        else:
            evidence.uploaded_by_user_id = uploaded_by.id
            evidence.evidence_type = evidence_seed.evidence_type
            evidence.original_filename = evidence_seed.original_filename
            evidence.stored_filename = evidence_seed.stored_filename
            evidence.file_extension = evidence_seed.file_extension
            evidence.mime_type = evidence_seed.mime_type
            evidence.file_size_bytes = evidence_seed.file_size_bytes
            evidence.description = evidence_seed.description
            evidence.text_content_snapshot = evidence_seed.text_content_snapshot
            evidence.storage_provider = "local"
            evidence.storage_bucket = None
            evidence.storage_object_key = None
            evidence.public_url = None
            evidence.absolute_file_path = None
            evidence.audio_processing_status = evidence_seed.audio_processing_status
            evidence.audio_provider_name = evidence_seed.audio_provider_name
            evidence.transcript_text = evidence_seed.transcript_text
            evidence.transcript_language_code = evidence_seed.transcript_language_code
            evidence.transcript_confidence = evidence_seed.transcript_confidence
            evidence.transcript_segments_json = None
            evidence.audio_processed_at = (
                processed_at
                if evidence_seed.audio_processing_status == PROCESSING_STATUS_SUCCEEDED
                else None
            )
            evidence.audio_error_message = None
            evidence.image_processing_status = evidence_seed.image_processing_status
            evidence.image_provider_name = evidence_seed.image_provider_name
            evidence.image_labels_json = evidence_seed.image_labels_json
            evidence.image_detections_json = evidence_seed.image_detections_json
            evidence.image_summary = evidence_seed.image_summary
            evidence.image_processed_at = (
                processed_at
                if evidence_seed.image_processing_status == PROCESSING_STATUS_SUCCEEDED
                else None
            )
            evidence.image_error_message = None

            db.add(evidence)
            logger.info(
                "Updated demo evidence: incident=%s file=%s",
                evidence_seed.incident_demo_key,
                evidence_seed.stored_filename,
            )

    db.flush()


def get_incident_by_demo_key(db: Session, demo_key: str) -> Incident | None:
    query = select(Incident).where(Incident.title.startswith(f"[{demo_key}]"))
    return db.execute(query).scalar_one_or_none()


def get_evidence_by_incident_and_filename(
    db: Session,
    incident_id: Any,
    stored_filename: str,
) -> IncidentEvidence | None:
    query = select(IncidentEvidence).where(
        IncidentEvidence.incident_id == incident_id,
        IncidentEvidence.stored_filename == stored_filename,
    )
    return db.execute(query).scalar_one_or_none()

def seed_assignment_candidates(db: Session) -> None:
    now = datetime.now(timezone.utc)

    for candidate_seed in DEMO_ASSIGNMENT_CANDIDATES:
        incident = get_incident_by_demo_key(db, candidate_seed.incident_demo_key)
        if incident is None:
            raise RuntimeError(f"Incident {candidate_seed.incident_demo_key} was not found.")

        provider = get_provider_by_owner_email(db, candidate_seed.provider_owner_email)
        if provider is None:
            raise RuntimeError(
                f"Provider linked to {candidate_seed.provider_owner_email} was not found."
            )

        candidate = get_assignment_candidate_by_incident_and_provider(
            db=db,
            incident_id=incident.id,
            provider_id=provider.id,
        )

        if candidate is None:
            candidate = IncidentAssignmentCandidate(
                incident_id=incident.id,
                provider_id=provider.id,
                status=candidate_seed.status,
                recommendation_rank=candidate_seed.recommendation_rank,
                score=candidate_seed.score,
                distance_km=candidate_seed.distance_km,
                required_service_codes_json=candidate_seed.required_service_codes_json,
                matched_service_codes_json=candidate_seed.matched_service_codes_json,
                rationale_json=candidate_seed.rationale_json,
                provider_average_rating_snapshot=provider.average_rating,
                provider_available_capacity_snapshot=(
                    candidate_seed.provider_available_capacity_snapshot
                ),
                available_technicians_count_snapshot=(
                    candidate_seed.available_technicians_count_snapshot
                ),
                published_at=now - timedelta(minutes=30),
                responded_at=now - timedelta(minutes=20)
                if candidate_seed.status in (
                    ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
                    ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
                )
                else None,
                expires_at=None,
            )
            db.add(candidate)
            logger.info(
                "Created assignment candidate: incident=%s provider=%s",
                candidate_seed.incident_demo_key,
                provider.business_name,
            )
        else:
            candidate.status = candidate_seed.status
            candidate.recommendation_rank = candidate_seed.recommendation_rank
            candidate.score = candidate_seed.score
            candidate.distance_km = candidate_seed.distance_km
            candidate.required_service_codes_json = candidate_seed.required_service_codes_json
            candidate.matched_service_codes_json = candidate_seed.matched_service_codes_json
            candidate.rationale_json = candidate_seed.rationale_json
            candidate.provider_average_rating_snapshot = provider.average_rating
            candidate.provider_available_capacity_snapshot = (
                candidate_seed.provider_available_capacity_snapshot
            )
            candidate.available_technicians_count_snapshot = (
                candidate_seed.available_technicians_count_snapshot
            )
            candidate.responded_at = (
                now - timedelta(minutes=20)
                if candidate_seed.status in (
                    ASSIGNMENT_CANDIDATE_STATUS_ACCEPTED,
                    ASSIGNMENT_CANDIDATE_STATUS_REJECTED,
                )
                else None
            )
            db.add(candidate)
            logger.info(
                "Updated assignment candidate: incident=%s provider=%s",
                candidate_seed.incident_demo_key,
                provider.business_name,
            )

    db.flush()


def seed_operation_events(db: Session) -> None:
    for event_seed in DEMO_OPERATION_EVENTS:
        incident = get_incident_by_demo_key(db, event_seed.incident_demo_key)
        if incident is None:
            raise RuntimeError(f"Incident {event_seed.incident_demo_key} was not found.")

        provider = None
        if event_seed.provider_owner_email:
            provider = get_provider_by_owner_email(db, event_seed.provider_owner_email)
            if provider is None:
                raise RuntimeError(
                    f"Provider linked to {event_seed.provider_owner_email} was not found."
                )

        technician = None
        if provider is not None and event_seed.technician_phone:
            technician = get_technician_by_provider_and_phone(
                db=db,
                provider_id=provider.id,
                phone_number=event_seed.technician_phone,
            )

        actor_user = None
        if event_seed.actor_email:
            actor_user = get_user_by_email(db, event_seed.actor_email)

        existing_event = get_operation_event_by_unique_demo_data(
            db=db,
            incident_id=incident.id,
            event_type=event_seed.event_type,
            to_status=event_seed.to_status,
            note=event_seed.note,
        )

        if existing_event is None:
            existing_event = IncidentOperationEvent(
                incident_id=incident.id,
                provider_id=provider.id if provider else None,
                technician_id=technician.id if technician else None,
                actor_user_id=actor_user.id if actor_user else None,
                event_type=event_seed.event_type,
                from_status=event_seed.from_status,
                to_status=event_seed.to_status,
                note=event_seed.note,
                payload_json=event_seed.payload_json,
            )
            db.add(existing_event)
            logger.info(
                "Created operation event: incident=%s event=%s",
                event_seed.incident_demo_key,
                event_seed.event_type,
            )
        else:
            existing_event.provider_id = provider.id if provider else None
            existing_event.technician_id = technician.id if technician else None
            existing_event.actor_user_id = actor_user.id if actor_user else None
            existing_event.from_status = event_seed.from_status
            existing_event.to_status = event_seed.to_status
            existing_event.note = event_seed.note
            existing_event.payload_json = event_seed.payload_json
            db.add(existing_event)
            logger.info(
                "Updated operation event: incident=%s event=%s",
                event_seed.incident_demo_key,
                event_seed.event_type,
            )

    db.flush()


def seed_tracking_pings(db: Session) -> None:
    now = datetime.now(timezone.utc)

    for ping_seed in DEMO_TRACKING_PINGS:
        incident = get_incident_by_demo_key(db, ping_seed.incident_demo_key)
        if incident is None:
            raise RuntimeError(f"Incident {ping_seed.incident_demo_key} was not found.")

        provider = get_provider_by_owner_email(db, ping_seed.provider_owner_email)
        if provider is None:
            raise RuntimeError(
                f"Provider linked to {ping_seed.provider_owner_email} was not found."
            )

        technician = None
        if ping_seed.technician_phone:
            technician = get_technician_by_provider_and_phone(
                db=db,
                provider_id=provider.id,
                phone_number=ping_seed.technician_phone,
            )

        recorded_at = now - timedelta(minutes=ping_seed.minutes_ago)

        existing_ping = get_tracking_ping_by_unique_demo_data(
            db=db,
            incident_id=incident.id,
            provider_id=provider.id,
            technician_id=technician.id if technician else None,
            latitude=ping_seed.latitude,
            longitude=ping_seed.longitude,
        )

        if existing_ping is None:
            existing_ping = IncidentResponderLocationPing(
                incident_id=incident.id,
                provider_id=provider.id,
                technician_id=technician.id if technician else None,
                source_type=ping_seed.source_type,
                latitude=ping_seed.latitude,
                longitude=ping_seed.longitude,
                accuracy_meters=ping_seed.accuracy_meters,
                recorded_at=recorded_at,
            )
            db.add(existing_ping)
            logger.info(
                "Created tracking ping: incident=%s lat=%s lon=%s",
                ping_seed.incident_demo_key,
                ping_seed.latitude,
                ping_seed.longitude,
            )
        else:
            existing_ping.source_type = ping_seed.source_type
            existing_ping.accuracy_meters = ping_seed.accuracy_meters
            existing_ping.recorded_at = recorded_at
            db.add(existing_ping)
            logger.info(
                "Updated tracking ping: incident=%s lat=%s lon=%s",
                ping_seed.incident_demo_key,
                ping_seed.latitude,
                ping_seed.longitude,
            )

    db.flush()


def update_demo_incident_tracking_snapshots(db: Session) -> None:
    now = datetime.now(timezone.utc)

    accident = get_incident_by_demo_key(db, "INC_ACCIDENT_001")
    if accident is not None:
        provider = get_provider_by_owner_email(db, "taller.gruas@mechanic.local")
        technician = (
            get_technician_by_provider_and_phone(db, provider.id, "70100008")
            if provider is not None
            else None
        )

        accident.provider_id = provider.id if provider else accident.provider_id
        accident.assigned_technician_id = technician.id if technician else accident.assigned_technician_id
        accident.status = INCIDENT_STATUS_ASSIGNED
        accident.dispatch_mode = DISPATCH_MODE_TECHNICIAN
        accident.assigned_at = now - timedelta(minutes=25)
        accident.responder_last_latitude = -17.8152
        accident.responder_last_longitude = -63.1997
        accident.responder_last_source_type = TRACKING_SOURCE_TECHNICIAN
        accident.responder_last_recorded_at = now - timedelta(minutes=6)
        accident.route_provider_name = "demo_haversine"
        accident.route_distance_meters = 1200.0
        accident.route_duration_seconds = 420
        accident.route_eta_seconds = 420
        accident.route_polyline = None
        accident.route_last_calculated_at = now - timedelta(minutes=6)
        accident.route_error_message = None
        db.add(accident)

    overheating = get_incident_by_demo_key(db, "INC_OVERHEATING_001")
    if overheating is not None:
        provider = get_provider_by_owner_email(db, "taller.norte@mechanic.local")
        technician = (
            get_technician_by_provider_and_phone(db, provider.id, "70100003")
            if provider is not None
            else None
        )

        overheating.provider_id = provider.id if provider else overheating.provider_id
        overheating.assigned_technician_id = technician.id if technician else overheating.assigned_technician_id
        overheating.status = INCIDENT_STATUS_EN_ROUTE
        overheating.dispatch_mode = DISPATCH_MODE_TECHNICIAN
        overheating.assigned_at = now - timedelta(minutes=18)
        overheating.en_route_at = now - timedelta(minutes=15)
        overheating.responder_last_latitude = -17.7721
        overheating.responder_last_longitude = -63.1792
        overheating.responder_last_source_type = TRACKING_SOURCE_TECHNICIAN
        overheating.responder_last_recorded_at = now - timedelta(minutes=5)
        overheating.route_provider_name = "demo_haversine"
        overheating.route_distance_meters = 1850.0
        overheating.route_duration_seconds = 600
        overheating.route_eta_seconds = 600
        overheating.route_polyline = None
        overheating.route_last_calculated_at = now - timedelta(minutes=5)
        overheating.route_error_message = None
        db.add(overheating)

    db.flush()

def get_assignment_candidate_by_incident_and_provider(
    db: Session,
    incident_id: Any,
    provider_id: Any,
) -> IncidentAssignmentCandidate | None:
    query = select(IncidentAssignmentCandidate).where(
        IncidentAssignmentCandidate.incident_id == incident_id,
        IncidentAssignmentCandidate.provider_id == provider_id,
    )
    return db.execute(query).scalar_one_or_none()


def get_operation_event_by_unique_demo_data(
    db: Session,
    incident_id: Any,
    event_type: str,
    to_status: str | None,
    note: str | None,
) -> IncidentOperationEvent | None:
    query = select(IncidentOperationEvent).where(
        IncidentOperationEvent.incident_id == incident_id,
        IncidentOperationEvent.event_type == event_type,
        IncidentOperationEvent.to_status == to_status,
        IncidentOperationEvent.note == note,
    )
    return db.execute(query).scalar_one_or_none()


def get_tracking_ping_by_unique_demo_data(
    db: Session,
    incident_id: Any,
    provider_id: Any,
    technician_id: Any,
    latitude: float,
    longitude: float,
) -> IncidentResponderLocationPing | None:
    query = select(IncidentResponderLocationPing).where(
        IncidentResponderLocationPing.incident_id == incident_id,
        IncidentResponderLocationPing.provider_id == provider_id,
        IncidentResponderLocationPing.technician_id == technician_id,
        IncidentResponderLocationPing.latitude == latitude,
        IncidentResponderLocationPing.longitude == longitude,
    )
    return db.execute(query).scalar_one_or_none()


if __name__ == "__main__":
    run()