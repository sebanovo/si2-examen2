from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session

import app.bootstrap.model_registry  # noqa: F401

from app.common.constants import (
    AUDIT_EVENT_BILLING_FINALIZED,
    AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
    AUDIT_EVENT_COVERAGE_APPLIED,
    AUDIT_EVENT_INCIDENT_ACCEPTED,
    AUDIT_EVENT_INCIDENT_COMPLETED,
    AUDIT_EVENT_PAYMENT_MARKED_PAID,
    AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,
    AUDIT_OUTCOME_SUCCESS,
    AUDIT_SCOPE_DOMAIN,
    DEFAULT_CURRENCY_CODE,
    PAYMENT_METHOD_QR,
    PAYMENT_METHOD_TRANSFER,
    PAYMENT_STATUS_PAID,
    PAYMENT_STATUS_PENDING_PAYMENT,
    PLAN_BILLING_PERIOD_ANNUAL,
    PLAN_BILLING_PERIOD_MONTHLY,
    PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
    PLAN_COVERAGE_TYPE_FULL,
    PLAN_COVERAGE_TYPE_PERCENTAGE,
    PUSH_DELIVERY_STATUS_SUCCEEDED,
    PUSH_EVENT_INCIDENT_ACCEPTED,
    PUSH_EVENT_INCIDENT_COMPLETED,
    PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
    PUSH_EVENT_PROVIDER_EN_ROUTE,
    ROLE_CLIENT,
    ROLE_PROVIDER_ADMIN,
    SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
    SUBSCRIPTION_STATUS_ACTIVE,
)
from app.services.audit.models import AuditLog, MetricSnapshot
from app.services.auth.models import User
from app.services.billing.models import IncidentBilling
from app.services.catalog.models import ServiceCatalogItem
from app.services.incidents.models import Incident
from app.services.notifications.models import PushNotificationDelivery, UserDeviceToken
from app.services.providers.models import Provider
from app.services.subscriptions.models import (
    ClientPlanSubscription,
    IncidentSubscriptionApplication,
    ProviderSubscriptionPlan,
    ProviderSubscriptionPlanCoverage,
)

logger = logging.getLogger(__name__)

MONEY_QUANTIZER = Decimal("0.01")
DEFAULT_COMMISSION_RATE = Decimal("0.1000")


@dataclass(frozen=True)
class ProviderPlanSeed:
    provider_owner_email: str
    code: str
    name: str
    description: str
    billing_period: str
    price_amount: Decimal
    auto_renews: bool


@dataclass(frozen=True)
class PlanCoverageSeed:
    provider_owner_email: str
    plan_code: str
    service_code: str | None
    incident_category: str | None
    coverage_type: str
    coverage_value: Decimal
    max_coverage_amount: Decimal | None
    waiting_period_days: int
    max_applications_per_subscription: int | None


@dataclass(frozen=True)
class ClientSubscriptionSeed:
    client_email: str
    provider_owner_email: str
    plan_code: str
    months_duration: int
    external_reference: str
    note: str | None


@dataclass(frozen=True)
class IncidentBillingSeed:
    incident_demo_key: str
    provider_owner_email: str
    final_price_amount: Decimal
    payment_status: str
    payment_method: str | None
    payment_provider_name: str | None
    payment_reference: str | None
    checkout_reference: str | None
    pricing_note: str
    apply_subscription_external_reference: str | None
    coverage_service_code: str | None
    coverage_incident_category: str | None


@dataclass(frozen=True)
class DeviceTokenSeed:
    user_email: str
    device_token: str
    device_platform: str
    device_label: str
    app_role: str


@dataclass(frozen=True)
class NotificationDeliverySeed:
    incident_demo_key: str | None
    recipient_email: str
    device_token: str
    event_code: str
    title: str
    body: str
    data_json: dict[str, Any]


@dataclass(frozen=True)
class AuditLogSeed:
    request_id: str
    actor_email: str | None
    incident_demo_key: str | None
    provider_owner_email: str | None
    event_type: str
    entity_type: str | None
    entity_demo_key: str | None
    payload_json: dict[str, Any] | None


PROVIDER_PLAN_SEEDS: tuple[ProviderPlanSeed, ...] = (
    ProviderPlanSeed(
        provider_owner_email="taller.norte@mechanic.local",
        code="NORTE_AUXILIO_MENSUAL",
        name="Auxilio Norte Mensual",
        description=(
            "Plan mensual demo para cubrir auxilios urbanos de batería, llanta y "
            "sobrecalentamiento con atención móvil prioritaria."
        ),
        billing_period=PLAN_BILLING_PERIOD_MONTHLY,
        price_amount=Decimal("120.00"),
        auto_renews=True,
    ),
    ProviderPlanSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        code="GRUAS_PROTECCION_ANUAL",
        name="Protección Grúas Anual",
        description=(
            "Plan anual demo orientado a accidentes leves, remolque y apoyo inicial "
            "con grúa dentro de la ciudad."
        ),
        billing_period=PLAN_BILLING_PERIOD_ANNUAL,
        price_amount=Decimal("900.00"),
        auto_renews=True,
    ),
)


PLAN_COVERAGE_SEEDS: tuple[PlanCoverageSeed, ...] = (
    PlanCoverageSeed(
        provider_owner_email="taller.norte@mechanic.local",
        plan_code="NORTE_AUXILIO_MENSUAL",
        service_code="BATTERY_JUMPSTART",
        incident_category="BATTERY",
        coverage_type=PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
        coverage_value=Decimal("60.00"),
        max_coverage_amount=Decimal("60.00"),
        waiting_period_days=0,
        max_applications_per_subscription=4,
    ),
    PlanCoverageSeed(
        provider_owner_email="taller.norte@mechanic.local",
        plan_code="NORTE_AUXILIO_MENSUAL",
        service_code="TIRE_CHANGE",
        incident_category="TIRE",
        coverage_type=PLAN_COVERAGE_TYPE_PERCENTAGE,
        coverage_value=Decimal("50.00"),
        max_coverage_amount=Decimal("70.00"),
        waiting_period_days=0,
        max_applications_per_subscription=4,
    ),
    PlanCoverageSeed(
        provider_owner_email="taller.norte@mechanic.local",
        plan_code="NORTE_AUXILIO_MENSUAL",
        service_code="OVERHEATING_ASSISTANCE",
        incident_category="OVERHEATING",
        coverage_type=PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
        coverage_value=Decimal("80.00"),
        max_coverage_amount=Decimal("80.00"),
        waiting_period_days=0,
        max_applications_per_subscription=4,
    ),
    PlanCoverageSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        plan_code="GRUAS_PROTECCION_ANUAL",
        service_code="TOWING",
        incident_category="ACCIDENT",
        coverage_type=PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
        coverage_value=Decimal("180.00"),
        max_coverage_amount=Decimal("180.00"),
        waiting_period_days=0,
        max_applications_per_subscription=2,
    ),
    PlanCoverageSeed(
        provider_owner_email="taller.gruas@mechanic.local",
        plan_code="GRUAS_PROTECCION_ANUAL",
        service_code="ACCIDENT_SUPPORT",
        incident_category="ACCIDENT",
        coverage_type=PLAN_COVERAGE_TYPE_PERCENTAGE,
        coverage_value=Decimal("40.00"),
        max_coverage_amount=Decimal("220.00"),
        waiting_period_days=0,
        max_applications_per_subscription=2,
    ),
)


CLIENT_SUBSCRIPTION_SEEDS: tuple[ClientSubscriptionSeed, ...] = (
    ClientSubscriptionSeed(
        client_email="cliente.bateria@mechanic.local",
        provider_owner_email="taller.norte@mechanic.local",
        plan_code="NORTE_AUXILIO_MENSUAL",
        months_duration=1,
        external_reference="DEMO-SUB-BAT-NORTE-001",
        note="Suscripción demo activa para cliente con caso de batería.",
    ),
    ClientSubscriptionSeed(
        client_email="cliente.accidente@mechanic.local",
        provider_owner_email="taller.norte@mechanic.local",
        plan_code="NORTE_AUXILIO_MENSUAL",
        months_duration=1,
        external_reference="DEMO-SUB-CAL-NORTE-001",
        note="Suscripción demo activa para caso de sobrecalentamiento.",
    ),
    ClientSubscriptionSeed(
        client_email="cliente.accidente@mechanic.local",
        provider_owner_email="taller.gruas@mechanic.local",
        plan_code="GRUAS_PROTECCION_ANUAL",
        months_duration=12,
        external_reference="DEMO-SUB-ACC-GRUAS-001",
        note="Suscripción demo activa para cobertura de accidente y grúa.",
    ),
)


INCIDENT_BILLING_SEEDS: tuple[IncidentBillingSeed, ...] = (
    IncidentBillingSeed(
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        final_price_amount=Decimal("350.00"),
        payment_status=PAYMENT_STATUS_PAID,
        payment_method=PAYMENT_METHOD_QR,
        payment_provider_name="demo_qr",
        payment_reference="DEMO-QR-ACC-001",
        checkout_reference="CHK-DEMO-ACC-001",
        pricing_note="Servicio demo completado con traslado por grúa y apoyo inicial.",
        apply_subscription_external_reference="DEMO-SUB-ACC-GRUAS-001",
        coverage_service_code="TOWING",
        coverage_incident_category="ACCIDENT",
    ),
    IncidentBillingSeed(
        incident_demo_key="INC_OVERHEATING_001",
        provider_owner_email="taller.norte@mechanic.local",
        final_price_amount=Decimal("120.00"),
        payment_status=PAYMENT_STATUS_PENDING_PAYMENT,
        payment_method=PAYMENT_METHOD_QR,
        payment_provider_name="demo_qr",
        payment_reference=None,
        checkout_reference="CHK-DEMO-CAL-001",
        pricing_note="Servicio demo en curso: revisión de refrigerante y sistema de enfriamiento.",
        apply_subscription_external_reference="DEMO-SUB-CAL-NORTE-001",
        coverage_service_code="OVERHEATING_ASSISTANCE",
        coverage_incident_category="OVERHEATING",
    ),
    IncidentBillingSeed(
        incident_demo_key="INC_BATTERY_001",
        provider_owner_email="taller.norte@mechanic.local",
        final_price_amount=Decimal("80.00"),
        payment_status=PAYMENT_STATUS_PENDING_PAYMENT,
        payment_method=PAYMENT_METHOD_TRANSFER,
        payment_provider_name="demo_transfer",
        payment_reference=None,
        checkout_reference="CHK-DEMO-BAT-001",
        pricing_note="Cotización demo para auxilio de batería con cobertura parcial disponible.",
        apply_subscription_external_reference="DEMO-SUB-BAT-NORTE-001",
        coverage_service_code="BATTERY_JUMPSTART",
        coverage_incident_category="BATTERY",
    ),
)


DEVICE_TOKEN_SEEDS: tuple[DeviceTokenSeed, ...] = (
    DeviceTokenSeed(
        user_email="cliente.bateria@mechanic.local",
        device_token="demo-fcm-token-cliente-bateria",
        device_platform="ANDROID",
        device_label="Flutter demo cliente batería",
        app_role=ROLE_CLIENT,
    ),
    DeviceTokenSeed(
        user_email="cliente.accidente@mechanic.local",
        device_token="demo-fcm-token-cliente-accidente",
        device_platform="ANDROID",
        device_label="Flutter demo cliente accidente",
        app_role=ROLE_CLIENT,
    ),
    DeviceTokenSeed(
        user_email="taller.norte@mechanic.local",
        device_token="demo-fcm-token-taller-norte",
        device_platform="WEB",
        device_label="Angular demo Taller Norte",
        app_role=ROLE_PROVIDER_ADMIN,
    ),
    DeviceTokenSeed(
        user_email="taller.gruas@mechanic.local",
        device_token="demo-fcm-token-taller-gruas",
        device_platform="WEB",
        device_label="Angular demo Taller Grúas",
        app_role=ROLE_PROVIDER_ADMIN,
    ),
)


NOTIFICATION_DELIVERY_SEEDS: tuple[NotificationDeliverySeed, ...] = (
    NotificationDeliverySeed(
        incident_demo_key="INC_BATTERY_001",
        recipient_email="taller.norte@mechanic.local",
        device_token="demo-fcm-token-taller-norte",
        event_code=PUSH_EVENT_NEW_ASSIGNMENT_AVAILABLE,
        title="Nueva solicitud de auxilio de batería",
        body="Cliente cercano reportó vehículo que no enciende. Revisa candidatos disponibles.",
        data_json={"screen": "available_incidents", "demo_key": "INC_BATTERY_001"},
    ),
    NotificationDeliverySeed(
        incident_demo_key="INC_ACCIDENT_001",
        recipient_email="cliente.accidente@mechanic.local",
        device_token="demo-fcm-token-cliente-accidente",
        event_code=PUSH_EVENT_INCIDENT_ACCEPTED,
        title="Tu solicitud fue aceptada",
        body="Taller Grúas Santa Cruz aceptó la atención de tu accidente leve.",
        data_json={"screen": "incident_detail", "demo_key": "INC_ACCIDENT_001"},
    ),
    NotificationDeliverySeed(
        incident_demo_key="INC_OVERHEATING_001",
        recipient_email="cliente.accidente@mechanic.local",
        device_token="demo-fcm-token-cliente-accidente",
        event_code=PUSH_EVENT_PROVIDER_EN_ROUTE,
        title="El técnico está en camino",
        body="Taller Rápido Norte se dirige a tu ubicación para revisar el sobrecalentamiento.",
        data_json={"screen": "tracking", "demo_key": "INC_OVERHEATING_001"},
    ),
    NotificationDeliverySeed(
        incident_demo_key="INC_ACCIDENT_001",
        recipient_email="cliente.accidente@mechanic.local",
        device_token="demo-fcm-token-cliente-accidente",
        event_code=PUSH_EVENT_INCIDENT_COMPLETED,
        title="Servicio completado",
        body="El servicio de grúa demo fue marcado como completado y pagado.",
        data_json={"screen": "billing", "demo_key": "INC_ACCIDENT_001"},
    ),
)


AUDIT_LOG_SEEDS: tuple[AuditLogSeed, ...] = (
    AuditLogSeed(
        request_id="demo-audit-subscription-plan-norte",
        actor_email="taller.norte@mechanic.local",
        incident_demo_key=None,
        provider_owner_email="taller.norte@mechanic.local",
        event_type=AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,
        entity_type="ProviderSubscriptionPlan",
        entity_demo_key="NORTE_AUXILIO_MENSUAL",
        payload_json={"demo": True, "plan_code": "NORTE_AUXILIO_MENSUAL"},
    ),
    AuditLogSeed(
        request_id="demo-audit-client-subscribed-acc-gruas",
        actor_email="cliente.accidente@mechanic.local",
        incident_demo_key=None,
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
        entity_type="ClientPlanSubscription",
        entity_demo_key="DEMO-SUB-ACC-GRUAS-001",
        payload_json={"demo": True, "external_reference": "DEMO-SUB-ACC-GRUAS-001"},
    ),
    AuditLogSeed(
        request_id="demo-audit-incident-accepted-accident",
        actor_email="taller.gruas@mechanic.local",
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_INCIDENT_ACCEPTED,
        entity_type="Incident",
        entity_demo_key="INC_ACCIDENT_001",
        payload_json={"demo": True, "status": "ASSIGNED"},
    ),
    AuditLogSeed(
        request_id="demo-audit-billing-finalized-accident",
        actor_email="taller.gruas@mechanic.local",
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_BILLING_FINALIZED,
        entity_type="IncidentBilling",
        entity_demo_key="INC_ACCIDENT_001",
        payload_json={"demo": True, "final_price_amount": 350.00, "currency": "BOB"},
    ),
    AuditLogSeed(
        request_id="demo-audit-coverage-applied-accident",
        actor_email="cliente.accidente@mechanic.local",
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_COVERAGE_APPLIED,
        entity_type="IncidentSubscriptionApplication",
        entity_demo_key="INC_ACCIDENT_001",
        payload_json={"demo": True, "coverage_applied_amount": 180.00},
    ),
    AuditLogSeed(
        request_id="demo-audit-payment-paid-accident",
        actor_email="cliente.accidente@mechanic.local",
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_PAYMENT_MARKED_PAID,
        entity_type="IncidentBilling",
        entity_demo_key="INC_ACCIDENT_001",
        payload_json={"demo": True, "payment_method": "QR", "payment_status": "PAID"},
    ),
    AuditLogSeed(
        request_id="demo-audit-incident-completed-accident",
        actor_email="taller.gruas@mechanic.local",
        incident_demo_key="INC_ACCIDENT_001",
        provider_owner_email="taller.gruas@mechanic.local",
        event_type=AUDIT_EVENT_INCIDENT_COMPLETED,
        entity_type="Incident",
        entity_demo_key="INC_ACCIDENT_001",
        payload_json={"demo": True, "status": "COMPLETED"},
    ),
)


def seed_step_05_billing_subscriptions_notifications_and_audit(db: Session) -> None:
    """
    Cierra el flujo demo con datos de negocio que el frontend puede consumir:

    - planes y coberturas de suscripción,
    - suscripciones activas de clientes,
    - facturación y pagos demo,
    - aplicación de coberturas,
    - tokens y entregas de notificación,
    - auditoría y métricas.

    Todo es idempotente: puede ejecutarse varias veces sin duplicar registros.
    """

    logger.info("Starting demo seed step 05: billing, subscriptions, notifications and audit.")

    seed_provider_subscription_plans(db)
    seed_provider_plan_coverages(db)
    seed_client_plan_subscriptions(db)
    seed_incident_billings_and_coverages(db)
    seed_demo_device_tokens(db)
    seed_demo_notification_deliveries(db)
    seed_demo_audit_logs(db)
    seed_demo_metric_snapshots(db)

    logger.info("Finished demo seed step 05.")


# ---------------------------
# Provider subscription plans
# ---------------------------


def seed_provider_subscription_plans(db: Session) -> None:
    for seed in PROVIDER_PLAN_SEEDS:
        provider = require_provider_by_owner_email(db, seed.provider_owner_email)
        plan = get_provider_plan_by_code(db, provider.id, seed.code)

        if plan is None:
            plan = ProviderSubscriptionPlan(
                provider_id=provider.id,
                code=normalize_code(seed.code),
                name=seed.name.strip(),
                description=normalize_optional_text(seed.description),
                billing_period=seed.billing_period,
                price_amount=money(seed.price_amount),
                currency_code=DEFAULT_CURRENCY_CODE,
                is_active=True,
                auto_renews=seed.auto_renews,
            )
            db.add(plan)
            logger.info("Created demo provider subscription plan: %s", seed.code)
        else:
            plan.name = seed.name.strip()
            plan.description = normalize_optional_text(seed.description)
            plan.billing_period = seed.billing_period
            plan.price_amount = money(seed.price_amount)
            plan.currency_code = DEFAULT_CURRENCY_CODE
            plan.is_active = True
            plan.auto_renews = seed.auto_renews
            db.add(plan)
            logger.info("Updated demo provider subscription plan: %s", seed.code)

    db.flush()


def seed_provider_plan_coverages(db: Session) -> None:
    for seed in PLAN_COVERAGE_SEEDS:
        provider = require_provider_by_owner_email(db, seed.provider_owner_email)
        plan = require_provider_plan_by_code(db, provider.id, seed.plan_code)

        service_catalog_item = None
        if seed.service_code:
            service_catalog_item = require_service_catalog_item_by_code(db, seed.service_code)

        coverage = get_plan_coverage(
            db=db,
            plan_id=plan.id,
            service_catalog_item_id=service_catalog_item.id if service_catalog_item else None,
            incident_category=seed.incident_category,
            coverage_type=seed.coverage_type,
        )

        if coverage is None:
            coverage = ProviderSubscriptionPlanCoverage(
                plan_id=plan.id,
                service_catalog_item_id=service_catalog_item.id if service_catalog_item else None,
                incident_category=normalize_optional_code(seed.incident_category),
                coverage_type=seed.coverage_type,
                coverage_value=money(seed.coverage_value),
                max_coverage_amount=money(seed.max_coverage_amount) if seed.max_coverage_amount else None,
                waiting_period_days=seed.waiting_period_days,
                max_applications_per_subscription=seed.max_applications_per_subscription,
                is_active=True,
            )
            db.add(coverage)
            logger.info(
                "Created demo plan coverage: plan=%s service=%s category=%s",
                seed.plan_code,
                seed.service_code,
                seed.incident_category,
            )
        else:
            coverage.incident_category = normalize_optional_code(seed.incident_category)
            coverage.coverage_type = seed.coverage_type
            coverage.coverage_value = money(seed.coverage_value)
            coverage.max_coverage_amount = (
                money(seed.max_coverage_amount) if seed.max_coverage_amount else None
            )
            coverage.waiting_period_days = seed.waiting_period_days
            coverage.max_applications_per_subscription = seed.max_applications_per_subscription
            coverage.is_active = True
            db.add(coverage)
            logger.info(
                "Updated demo plan coverage: plan=%s service=%s category=%s",
                seed.plan_code,
                seed.service_code,
                seed.incident_category,
            )

    db.flush()


def seed_client_plan_subscriptions(db: Session) -> None:
    now = datetime.now(timezone.utc)

    for seed in CLIENT_SUBSCRIPTION_SEEDS:
        client = require_user_by_email(db, seed.client_email)
        provider = require_provider_by_owner_email(db, seed.provider_owner_email)
        plan = require_provider_plan_by_code(db, provider.id, seed.plan_code)

        subscription = get_client_subscription_by_external_reference(
            db,
            seed.external_reference,
        )

        if subscription is None:
            subscription = ClientPlanSubscription(
                client_user_id=client.id,
                provider_id=provider.id,
                plan_id=plan.id,
                status=SUBSCRIPTION_STATUS_ACTIVE,
                started_at=now - timedelta(days=2),
                expires_at=now + timedelta(days=30 * seed.months_duration),
                cancelled_at=None,
                external_reference=seed.external_reference,
                note=normalize_optional_text(seed.note),
            )
            db.add(subscription)
            logger.info(
                "Created demo client subscription: %s",
                seed.external_reference,
            )
        else:
            subscription.client_user_id = client.id
            subscription.provider_id = provider.id
            subscription.plan_id = plan.id
            subscription.status = SUBSCRIPTION_STATUS_ACTIVE
            subscription.started_at = now - timedelta(days=2)
            subscription.expires_at = now + timedelta(days=30 * seed.months_duration)
            subscription.cancelled_at = None
            subscription.note = normalize_optional_text(seed.note)
            db.add(subscription)
            logger.info(
                "Updated demo client subscription: %s",
                seed.external_reference,
            )

    db.flush()


# ---------------------------
# Billing and coverage
# ---------------------------


def seed_incident_billings_and_coverages(db: Session) -> None:
    for seed in INCIDENT_BILLING_SEEDS:
        incident = require_incident_by_demo_key(db, seed.incident_demo_key)
        provider = require_provider_by_owner_email(db, seed.provider_owner_email)

        final_price_amount = money(seed.final_price_amount)
        platform_commission_amount = calculate_commission(final_price_amount)
        provider_net_amount = final_price_amount - platform_commission_amount

        billing = get_incident_billing_by_incident_id(db, incident.id)

        if billing is None:
            billing = IncidentBilling(
                incident_id=incident.id,
                client_user_id=incident.client_user_id,
                provider_id=provider.id,
                currency_code=DEFAULT_CURRENCY_CODE,
                estimated_price_min=incident.estimated_price_min,
                estimated_price_max=incident.estimated_price_max,
                final_price_amount=final_price_amount,
                platform_commission_rate=DEFAULT_COMMISSION_RATE,
                platform_commission_amount=platform_commission_amount,
                provider_gross_amount=final_price_amount,
                provider_net_amount=provider_net_amount,
                payment_status=seed.payment_status,
                payment_method=seed.payment_method,
                payment_provider_name=seed.payment_provider_name,
                payment_reference=seed.payment_reference,
                checkout_reference=seed.checkout_reference,
                checkout_payload_json=build_checkout_payload(seed, final_price_amount),
                pricing_note=seed.pricing_note,
                pricing_finalized_at=datetime.now(timezone.utc),
                payment_completed_at=(
                    datetime.now(timezone.utc)
                    if seed.payment_status == PAYMENT_STATUS_PAID
                    else None
                ),
                cancelled_at=None,
            )
            db.add(billing)
            logger.info("Created demo incident billing: %s", seed.incident_demo_key)
        else:
            billing.client_user_id = incident.client_user_id
            billing.provider_id = provider.id
            billing.currency_code = DEFAULT_CURRENCY_CODE
            billing.estimated_price_min = incident.estimated_price_min
            billing.estimated_price_max = incident.estimated_price_max
            billing.final_price_amount = final_price_amount
            billing.platform_commission_rate = DEFAULT_COMMISSION_RATE
            billing.platform_commission_amount = platform_commission_amount
            billing.provider_gross_amount = final_price_amount
            billing.provider_net_amount = provider_net_amount
            billing.payment_status = seed.payment_status
            billing.payment_method = seed.payment_method
            billing.payment_provider_name = seed.payment_provider_name
            billing.payment_reference = seed.payment_reference
            billing.checkout_reference = seed.checkout_reference
            billing.checkout_payload_json = build_checkout_payload(seed, final_price_amount)
            billing.pricing_note = seed.pricing_note
            billing.pricing_finalized_at = billing.pricing_finalized_at or datetime.now(timezone.utc)
            billing.payment_completed_at = (
                billing.payment_completed_at or datetime.now(timezone.utc)
                if seed.payment_status == PAYMENT_STATUS_PAID
                else None
            )
            billing.cancelled_at = None
            db.add(billing)
            logger.info("Updated demo incident billing: %s", seed.incident_demo_key)

        db.flush()

        if seed.apply_subscription_external_reference:
            apply_demo_subscription_coverage(
                db=db,
                seed=seed,
                incident=incident,
                provider=provider,
                billing=billing,
                original_amount=final_price_amount,
            )

    db.flush()


def apply_demo_subscription_coverage(
    *,
    db: Session,
    seed: IncidentBillingSeed,
    incident: Incident,
    provider: Provider,
    billing: IncidentBilling,
    original_amount: Decimal,
) -> None:
    subscription = require_client_subscription_by_external_reference(
        db,
        seed.apply_subscription_external_reference or "",
    )

    service_catalog_item = None
    if seed.coverage_service_code:
        service_catalog_item = require_service_catalog_item_by_code(
            db,
            seed.coverage_service_code,
        )

    coverage = get_best_matching_coverage(
        db=db,
        plan_id=subscription.plan_id,
        service_catalog_item_id=service_catalog_item.id if service_catalog_item else None,
        incident_category=seed.coverage_incident_category,
    )

    if coverage is None:
        raise RuntimeError(
            "Coverage was not found for demo incident "
            f"{seed.incident_demo_key} using subscription "
            f"{seed.apply_subscription_external_reference}."
        )

    coverage_applied_amount = calculate_coverage_amount(
        original_amount=original_amount,
        coverage=coverage,
    )
    client_payable_amount = max(
        Decimal("0.00"),
        original_amount - coverage_applied_amount,
    ).quantize(MONEY_QUANTIZER)

    application = get_incident_subscription_application(
        db=db,
        incident_id=incident.id,
        client_plan_subscription_id=subscription.id,
        plan_coverage_id=coverage.id,
    )

    snapshot = {
        "demo": True,
        "incident_demo_key": seed.incident_demo_key,
        "provider_id": str(provider.id),
        "subscription_external_reference": subscription.external_reference,
        "coverage_type": coverage.coverage_type,
        "coverage_value": float(coverage.coverage_value),
        "max_coverage_amount": float(coverage.max_coverage_amount)
        if coverage.max_coverage_amount is not None
        else None,
        "original_amount": float(original_amount),
        "coverage_applied_amount": float(coverage_applied_amount),
        "client_payable_amount": float(client_payable_amount),
    }

    if application is None:
        application = IncidentSubscriptionApplication(
            incident_id=incident.id,
            incident_billing_id=billing.id,
            client_plan_subscription_id=subscription.id,
            plan_coverage_id=coverage.id,
            matched_service_catalog_item_id=(
                service_catalog_item.id if service_catalog_item else None
            ),
            matched_incident_category=normalize_optional_code(seed.coverage_incident_category),
            coverage_type=coverage.coverage_type,
            coverage_value=coverage.coverage_value,
            original_amount=original_amount,
            coverage_applied_amount=coverage_applied_amount,
            client_payable_amount=client_payable_amount,
            status=SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
            snapshot_json=snapshot,
        )
        db.add(application)
        logger.info("Created demo coverage application: %s", seed.incident_demo_key)
    else:
        application.incident_billing_id = billing.id
        application.matched_service_catalog_item_id = (
            service_catalog_item.id if service_catalog_item else None
        )
        application.matched_incident_category = normalize_optional_code(seed.coverage_incident_category)
        application.coverage_type = coverage.coverage_type
        application.coverage_value = coverage.coverage_value
        application.original_amount = original_amount
        application.coverage_applied_amount = coverage_applied_amount
        application.client_payable_amount = client_payable_amount
        application.status = SUBSCRIPTION_APPLICATION_STATUS_APPLIED
        application.snapshot_json = snapshot
        db.add(application)
        logger.info("Updated demo coverage application: %s", seed.incident_demo_key)

    billing.client_plan_subscription_id = subscription.id
    billing.plan_coverage_id = coverage.id
    billing.coverage_applied_amount = coverage_applied_amount
    billing.client_payable_amount = client_payable_amount
    db.add(billing)


# ---------------------------
# Notifications
# ---------------------------


def seed_demo_device_tokens(db: Session) -> None:
    for seed in DEVICE_TOKEN_SEEDS:
        user = require_user_by_email(db, seed.user_email)
        device_token = get_device_token_by_token(db, seed.device_token)

        if device_token is None:
            device_token = UserDeviceToken(
                user_id=user.id,
                device_token=seed.device_token,
                device_platform=seed.device_platform,
                device_label=seed.device_label,
                app_role=seed.app_role,
                push_provider_name="demo_fcm",
                is_active=True,
                last_seen_at=datetime.now(timezone.utc),
            )
            db.add(device_token)
            logger.info("Created demo device token for user: %s", seed.user_email)
        else:
            device_token.user_id = user.id
            device_token.device_platform = seed.device_platform
            device_token.device_label = seed.device_label
            device_token.app_role = seed.app_role
            device_token.push_provider_name = "demo_fcm"
            device_token.is_active = True
            device_token.last_seen_at = datetime.now(timezone.utc)
            db.add(device_token)
            logger.info("Updated demo device token for user: %s", seed.user_email)

    db.flush()


def seed_demo_notification_deliveries(db: Session) -> None:
    for seed in NOTIFICATION_DELIVERY_SEEDS:
        recipient = require_user_by_email(db, seed.recipient_email)
        device_token = require_device_token_by_token(db, seed.device_token)
        incident = (
            require_incident_by_demo_key(db, seed.incident_demo_key)
            if seed.incident_demo_key
            else None
        )

        delivery = get_notification_delivery(
            db=db,
            event_code=seed.event_code,
            incident_id=incident.id if incident else None,
            recipient_user_id=recipient.id,
            user_device_token_id=device_token.id,
        )

        data_json = {
            **seed.data_json,
            "incident_id": str(incident.id) if incident else None,
            "recipient_user_id": str(recipient.id),
            "source": "demo_seed",
        }

        if delivery is None:
            delivery = PushNotificationDelivery(
                background_job_id=None,
                incident_id=incident.id if incident else None,
                recipient_user_id=recipient.id,
                user_device_token_id=device_token.id,
                provider_name="demo_fcm",
                event_code=seed.event_code,
                title=seed.title,
                body=seed.body,
                data_json=data_json,
                status=PUSH_DELIVERY_STATUS_SUCCEEDED,
                provider_message_id=f"demo-message-{seed.event_code.lower()}",
                error_message=None,
                sent_at=datetime.now(timezone.utc),
            )
            db.add(delivery)
            logger.info("Created demo notification delivery: %s", seed.event_code)
        else:
            delivery.title = seed.title
            delivery.body = seed.body
            delivery.data_json = data_json
            delivery.status = PUSH_DELIVERY_STATUS_SUCCEEDED
            delivery.provider_name = "demo_fcm"
            delivery.provider_message_id = (
                delivery.provider_message_id
                or f"demo-message-{seed.event_code.lower()}"
            )
            delivery.error_message = None
            delivery.sent_at = delivery.sent_at or datetime.now(timezone.utc)
            db.add(delivery)
            logger.info("Updated demo notification delivery: %s", seed.event_code)

    db.flush()


# ---------------------------
# Audit and metrics
# ---------------------------


def seed_demo_audit_logs(db: Session) -> None:
    for seed in AUDIT_LOG_SEEDS:
        actor = require_user_by_email(db, seed.actor_email) if seed.actor_email else None
        incident = (
            require_incident_by_demo_key(db, seed.incident_demo_key)
            if seed.incident_demo_key
            else None
        )
        provider = (
            require_provider_by_owner_email(db, seed.provider_owner_email)
            if seed.provider_owner_email
            else None
        )

        entity_id = resolve_audit_entity_id(
            db=db,
            entity_type=seed.entity_type,
            entity_demo_key=seed.entity_demo_key,
            incident=incident,
            provider=provider,
        )

        audit_log = get_audit_log_by_request_id(db, seed.request_id)

        if audit_log is None:
            audit_log = AuditLog(
                actor_user_id=actor.id if actor else None,
                incident_id=incident.id if incident else None,
                provider_id=provider.id if provider else None,
                request_id=seed.request_id,
                event_scope=AUDIT_SCOPE_DOMAIN,
                event_type=seed.event_type,
                entity_type=seed.entity_type,
                entity_id=entity_id,
                http_method=None,
                route_path=None,
                ip_address="127.0.0.1",
                user_agent="demo-seed",
                status_code=None,
                outcome=AUDIT_OUTCOME_SUCCESS,
                payload_json=seed.payload_json,
            )
            db.add(audit_log)
            logger.info("Created demo audit log: %s", seed.request_id)
        else:
            audit_log.actor_user_id = actor.id if actor else None
            audit_log.incident_id = incident.id if incident else None
            audit_log.provider_id = provider.id if provider else None
            audit_log.event_scope = AUDIT_SCOPE_DOMAIN
            audit_log.event_type = seed.event_type
            audit_log.entity_type = seed.entity_type
            audit_log.entity_id = entity_id
            audit_log.ip_address = "127.0.0.1"
            audit_log.user_agent = "demo-seed"
            audit_log.outcome = AUDIT_OUTCOME_SUCCESS
            audit_log.payload_json = seed.payload_json
            db.add(audit_log)
            logger.info("Updated demo audit log: %s", seed.request_id)

    db.flush()


def seed_demo_metric_snapshots(db: Session) -> None:
    admin = require_user_by_email(db, "admin@mechanic.local")

    payload = {
        "demo": True,
        "snapshot_key": "DEMO_DASHBOARD_OVERVIEW",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "users_count": count_rows(db, User),
            "providers_count": count_rows(db, Provider),
            "incidents_count": count_rows(db, Incident),
            "active_subscriptions_count": count_rows(
                db,
                ClientPlanSubscription,
                ClientPlanSubscription.status == SUBSCRIPTION_STATUS_ACTIVE,
            ),
            "paid_billings_count": count_rows(
                db,
                IncidentBilling,
                IncidentBilling.payment_status == PAYMENT_STATUS_PAID,
            ),
            "pending_payment_billings_count": count_rows(
                db,
                IncidentBilling,
                IncidentBilling.payment_status == PAYMENT_STATUS_PENDING_PAYMENT,
            ),
            "notifications_sent_count": count_rows(
                db,
                PushNotificationDelivery,
                PushNotificationDelivery.status == PUSH_DELIVERY_STATUS_SUCCEEDED,
            ),
            "audit_logs_count": count_rows(db, AuditLog),
        },
        "business_metrics": {
            "total_final_prices_bob": float(sum_decimal_column(db, IncidentBilling.final_price_amount)),
            "total_platform_commission_bob": float(
                sum_decimal_column(db, IncidentBilling.platform_commission_amount)
            ),
            "total_coverage_applied_bob": float(
                sum_decimal_column(db, IncidentBilling.coverage_applied_amount)
            ),
        },
    }

    snapshot = get_metric_snapshot_by_type(db, "DEMO_DASHBOARD_OVERVIEW")

    if snapshot is None:
        snapshot = MetricSnapshot(
            captured_by_user_id=admin.id,
            snapshot_type="DEMO_DASHBOARD_OVERVIEW",
            payload_json=payload,
        )
        db.add(snapshot)
        logger.info("Created demo metric snapshot.")
    else:
        snapshot.captured_by_user_id = admin.id
        snapshot.payload_json = payload
        db.add(snapshot)
        logger.info("Updated demo metric snapshot.")

    db.flush()


# ---------------------------
# Query helpers
# ---------------------------


def require_user_by_email(db: Session, email: str) -> User:
    user = get_user_by_email(db, email)
    if user is None:
        raise RuntimeError(f"Demo user was not found: {email}")
    return user


def get_user_by_email(db: Session, email: str) -> User | None:
    query: Select[tuple[User]] = select(User).where(User.email == normalize_email(email))
    return db.execute(query).scalar_one_or_none()


def require_provider_by_owner_email(db: Session, owner_email: str) -> Provider:
    owner = require_user_by_email(db, owner_email)
    query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner.id)
    provider = db.execute(query).scalar_one_or_none()

    if provider is None:
        raise RuntimeError(f"Demo provider was not found for owner: {owner_email}")

    return provider


def require_incident_by_demo_key(db: Session, demo_key: str) -> Incident:
    query: Select[tuple[Incident]] = select(Incident).where(
        Incident.title.startswith(f"[{demo_key}]")
    )
    incident = db.execute(query).scalar_one_or_none()

    if incident is None:
        raise RuntimeError(f"Demo incident was not found: {demo_key}")

    return incident


def require_service_catalog_item_by_code(db: Session, service_code: str) -> ServiceCatalogItem:
    query: Select[tuple[ServiceCatalogItem]] = select(ServiceCatalogItem).where(
        ServiceCatalogItem.code == normalize_code(service_code)
    )
    service_item = db.execute(query).scalar_one_or_none()

    if service_item is None:
        raise RuntimeError(f"Service catalog item was not found: {service_code}")

    return service_item


def get_provider_plan_by_code(
    db: Session,
    provider_id: Any,
    plan_code: str,
) -> ProviderSubscriptionPlan | None:
    query: Select[tuple[ProviderSubscriptionPlan]] = select(ProviderSubscriptionPlan).where(
        ProviderSubscriptionPlan.provider_id == provider_id,
        ProviderSubscriptionPlan.code == normalize_code(plan_code),
    )
    return db.execute(query).scalar_one_or_none()


def require_provider_plan_by_code(
    db: Session,
    provider_id: Any,
    plan_code: str,
) -> ProviderSubscriptionPlan:
    plan = get_provider_plan_by_code(db, provider_id, plan_code)

    if plan is None:
        raise RuntimeError(f"Provider subscription plan was not found: {plan_code}")

    return plan


def get_plan_coverage(
    *,
    db: Session,
    plan_id: Any,
    service_catalog_item_id: Any | None,
    incident_category: str | None,
    coverage_type: str,
) -> ProviderSubscriptionPlanCoverage | None:
    query: Select[tuple[ProviderSubscriptionPlanCoverage]] = select(
        ProviderSubscriptionPlanCoverage
    ).where(
        ProviderSubscriptionPlanCoverage.plan_id == plan_id,
        ProviderSubscriptionPlanCoverage.coverage_type == coverage_type,
    )

    if service_catalog_item_id is None:
        query = query.where(ProviderSubscriptionPlanCoverage.service_catalog_item_id.is_(None))
    else:
        query = query.where(
            ProviderSubscriptionPlanCoverage.service_catalog_item_id == service_catalog_item_id
        )

    normalized_category = normalize_optional_code(incident_category)
    if normalized_category is None:
        query = query.where(ProviderSubscriptionPlanCoverage.incident_category.is_(None))
    else:
        query = query.where(
            ProviderSubscriptionPlanCoverage.incident_category == normalized_category
        )

    return db.execute(query).scalar_one_or_none()


def get_best_matching_coverage(
    *,
    db: Session,
    plan_id: Any,
    service_catalog_item_id: Any | None,
    incident_category: str | None,
) -> ProviderSubscriptionPlanCoverage | None:
    normalized_category = normalize_optional_code(incident_category)

    if service_catalog_item_id is not None:
        query = (
            select(ProviderSubscriptionPlanCoverage)
            .where(
                ProviderSubscriptionPlanCoverage.plan_id == plan_id,
                ProviderSubscriptionPlanCoverage.service_catalog_item_id == service_catalog_item_id,
                ProviderSubscriptionPlanCoverage.is_active.is_(True),
            )
            .order_by(ProviderSubscriptionPlanCoverage.created_at.asc())
        )
        coverage = db.execute(query).scalars().first()
        if coverage is not None:
            return coverage

    if normalized_category is not None:
        query = (
            select(ProviderSubscriptionPlanCoverage)
            .where(
                ProviderSubscriptionPlanCoverage.plan_id == plan_id,
                ProviderSubscriptionPlanCoverage.incident_category == normalized_category,
                ProviderSubscriptionPlanCoverage.is_active.is_(True),
            )
            .order_by(ProviderSubscriptionPlanCoverage.created_at.asc())
        )
        return db.execute(query).scalars().first()

    return None


def get_client_subscription_by_external_reference(
    db: Session,
    external_reference: str,
) -> ClientPlanSubscription | None:
    query: Select[tuple[ClientPlanSubscription]] = select(ClientPlanSubscription).where(
        ClientPlanSubscription.external_reference == external_reference
    )
    return db.execute(query).scalar_one_or_none()


def require_client_subscription_by_external_reference(
    db: Session,
    external_reference: str,
) -> ClientPlanSubscription:
    subscription = get_client_subscription_by_external_reference(db, external_reference)

    if subscription is None:
        raise RuntimeError(f"Client subscription was not found: {external_reference}")

    return subscription


def get_incident_billing_by_incident_id(
    db: Session,
    incident_id: Any,
) -> IncidentBilling | None:
    query: Select[tuple[IncidentBilling]] = select(IncidentBilling).where(
        IncidentBilling.incident_id == incident_id
    )
    return db.execute(query).scalar_one_or_none()


def get_incident_subscription_application(
    *,
    db: Session,
    incident_id: Any,
    client_plan_subscription_id: Any,
    plan_coverage_id: Any,
) -> IncidentSubscriptionApplication | None:
    query: Select[tuple[IncidentSubscriptionApplication]] = select(
        IncidentSubscriptionApplication
    ).where(
        IncidentSubscriptionApplication.incident_id == incident_id,
        IncidentSubscriptionApplication.client_plan_subscription_id == client_plan_subscription_id,
        IncidentSubscriptionApplication.plan_coverage_id == plan_coverage_id,
    )
    return db.execute(query).scalar_one_or_none()


def get_device_token_by_token(
    db: Session,
    device_token: str,
) -> UserDeviceToken | None:
    query: Select[tuple[UserDeviceToken]] = select(UserDeviceToken).where(
        UserDeviceToken.device_token == device_token
    )
    return db.execute(query).scalar_one_or_none()


def require_device_token_by_token(db: Session, device_token: str) -> UserDeviceToken:
    token = get_device_token_by_token(db, device_token)

    if token is None:
        raise RuntimeError(f"Demo device token was not found: {device_token}")

    return token


def get_notification_delivery(
    *,
    db: Session,
    event_code: str,
    incident_id: Any | None,
    recipient_user_id: Any,
    user_device_token_id: Any,
) -> PushNotificationDelivery | None:
    query: Select[tuple[PushNotificationDelivery]] = select(PushNotificationDelivery).where(
        PushNotificationDelivery.event_code == event_code,
        PushNotificationDelivery.recipient_user_id == recipient_user_id,
        PushNotificationDelivery.user_device_token_id == user_device_token_id,
    )

    if incident_id is None:
        query = query.where(PushNotificationDelivery.incident_id.is_(None))
    else:
        query = query.where(PushNotificationDelivery.incident_id == incident_id)

    return db.execute(query).scalar_one_or_none()


def get_audit_log_by_request_id(db: Session, request_id: str) -> AuditLog | None:
    query: Select[tuple[AuditLog]] = select(AuditLog).where(AuditLog.request_id == request_id)
    return db.execute(query).scalar_one_or_none()


def get_metric_snapshot_by_type(
    db: Session,
    snapshot_type: str,
) -> MetricSnapshot | None:
    query: Select[tuple[MetricSnapshot]] = select(MetricSnapshot).where(
        MetricSnapshot.snapshot_type == snapshot_type
    )
    return db.execute(query).scalar_one_or_none()


# ---------------------------
# Calculation helpers
# ---------------------------


def calculate_commission(final_price_amount: Decimal) -> Decimal:
    return money(final_price_amount * DEFAULT_COMMISSION_RATE)


def calculate_coverage_amount(
    *,
    original_amount: Decimal,
    coverage: ProviderSubscriptionPlanCoverage,
) -> Decimal:
    coverage_value = Decimal(str(coverage.coverage_value))

    if coverage.coverage_type == PLAN_COVERAGE_TYPE_FULL:
        calculated_amount = original_amount
    elif coverage.coverage_type == PLAN_COVERAGE_TYPE_FIXED_AMOUNT:
        calculated_amount = min(original_amount, coverage_value)
    elif coverage.coverage_type == PLAN_COVERAGE_TYPE_PERCENTAGE:
        calculated_amount = original_amount * (coverage_value / Decimal("100"))
    else:
        calculated_amount = Decimal("0.00")

    if coverage.max_coverage_amount is not None:
        calculated_amount = min(calculated_amount, Decimal(str(coverage.max_coverage_amount)))

    return money(min(original_amount, calculated_amount))


def build_checkout_payload(
    seed: IncidentBillingSeed,
    amount: Decimal,
) -> dict[str, Any]:
    return {
        "demo": True,
        "checkout_reference": seed.checkout_reference,
        "payment_method": seed.payment_method,
        "payment_provider_name": seed.payment_provider_name,
        "amount": float(amount),
        "currency_code": DEFAULT_CURRENCY_CODE,
        "qr_payload": f"DEMO|{seed.checkout_reference}|{DEFAULT_CURRENCY_CODE}|{amount}"
        if seed.payment_method == PAYMENT_METHOD_QR
        else None,
        "instructions": (
            "Pago demo para defensa. No procesa dinero real; solo permite mostrar "
            "el flujo de checkout, confirmación y estado de pago."
        ),
    }


def count_rows(db: Session, model: Any, *conditions: Any) -> int:
    query = select(func.count(model.id))
    for condition in conditions:
        query = query.where(condition)
    return int(db.execute(query).scalar_one() or 0)


def sum_decimal_column(db: Session, column: Any) -> Decimal:
    value = db.execute(select(func.coalesce(func.sum(column), 0))).scalar_one()
    return money(Decimal(str(value)))


# ---------------------------
# Audit helpers
# ---------------------------


def resolve_audit_entity_id(
    *,
    db: Session,
    entity_type: str | None,
    entity_demo_key: str | None,
    incident: Incident | None,
    provider: Provider | None,
) -> str | None:
    if entity_type is None or entity_demo_key is None:
        return None

    if entity_type == "Incident" and incident is not None:
        return str(incident.id)

    if entity_type == "IncidentBilling" and incident is not None:
        billing = get_incident_billing_by_incident_id(db, incident.id)
        return str(billing.id) if billing else None

    if entity_type == "IncidentSubscriptionApplication" and incident is not None:
        query = (
            select(IncidentSubscriptionApplication)
            .where(IncidentSubscriptionApplication.incident_id == incident.id)
            .order_by(IncidentSubscriptionApplication.applied_at.desc())
        )
        application = db.execute(query).scalars().first()
        return str(application.id) if application else None

    if entity_type == "ProviderSubscriptionPlan" and provider is not None:
        plan = get_provider_plan_by_code(db, provider.id, entity_demo_key)
        return str(plan.id) if plan else None

    if entity_type == "ClientPlanSubscription":
        subscription = get_client_subscription_by_external_reference(db, entity_demo_key)
        return str(subscription.id) if subscription else None

    return entity_demo_key


# ---------------------------
# Normalization helpers
# ---------------------------


def money(value: Decimal | int | float | str) -> Decimal:
    return Decimal(str(value)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)


def normalize_email(email: str) -> str:
    return email.strip().lower()


def normalize_code(value: str) -> str:
    return value.strip().upper()


def normalize_optional_code(value: str | None) -> str | None:
    if value is None:
        return None

    normalized = value.strip().upper()
    return normalized or None


def normalize_optional_text(value: str | None) -> str | None:
    if value is None:
        return None

    normalized = value.strip()
    return normalized or None