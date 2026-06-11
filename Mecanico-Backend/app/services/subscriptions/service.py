from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP

from app.common.constants import (
    DEFAULT_CURRENCY_CODE,
    INCIDENT_STATUS_CANCELLED,
    PLAN_BILLING_PERIOD_ANNUAL,
    PLAN_BILLING_PERIOD_MONTHLY,
    PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
    PLAN_COVERAGE_TYPE_FULL,
    PLAN_COVERAGE_TYPE_PERCENTAGE,
    SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
    SUBSCRIPTION_APPLICATION_STATUS_VOIDED,
    SUBSCRIPTION_STATUS_ACTIVE,
    SUBSCRIPTION_STATUS_CANCELLED,
    AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
    AUDIT_EVENT_COVERAGE_APPLIED,
    AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,

)
from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.subscriptions.models import (
    ClientPlanSubscription,
    IncidentSubscriptionApplication,
    ProviderSubscriptionPlan,
    ProviderSubscriptionPlanCoverage,
)
from app.services.subscriptions.repository import SubscriptionsRepository
from app.services.subscriptions.schemas import (
    ClientPlanSubscriptionResponse,
    ClientSubscribeToPlanRequest,
    IncidentCoveragePreviewResponse,
    IncidentSubscriptionApplicationResponse,
    ProviderPlanCoverageResponse,
    ProviderPlanCoverageUpsertRequest,
    ProviderPlanResponse,
    ProviderPlanUpsertRequest,
    SubscriptionProviderSummaryResponse,
    SubscriptionUserSummaryResponse,
)
from app.services.audit.dispatcher import AuditEventDispatcher

MONEY_QUANTIZER = Decimal("0.01")


class SubscriptionsService:
    def __init__(self, repository: SubscriptionsRepository) -> None:
        self.repository = repository

    # ---------------------------
    # Provider plans
    # ---------------------------

    def list_my_provider_plans(
        self,
        current_user: User,
        include_inactive: bool = False,
    ) -> list[ProviderPlanResponse]:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        plans = self.repository.list_provider_plans(str(provider.id), include_inactive=include_inactive)
        return [self._build_plan_response(item) for item in plans]

    def create_my_provider_plan(
        self,
        current_user: User,
        payload: ProviderPlanUpsertRequest,
    ) -> ProviderPlanResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        billing_period = payload.billing_period.strip().upper()
        if billing_period not in (PLAN_BILLING_PERIOD_MONTHLY, PLAN_BILLING_PERIOD_ANNUAL):
            raise ConflictException("Unsupported billing_period. Use MONTHLY or ANNUAL.")

        plan = ProviderSubscriptionPlan(
            provider_id=provider.id,
            code=payload.code.strip().upper(),
            name=payload.name.strip(),
            description=self._normalize_optional_text(payload.description),
            billing_period=billing_period,
            price_amount=self._to_money_decimal(payload.price_amount),
            currency_code=payload.currency_code.strip().upper() if payload.currency_code else DEFAULT_CURRENCY_CODE,
            is_active=payload.is_active,
            auto_renews=payload.auto_renews,
        )

        try:
            self.repository.save(plan)
            self.repository.commit()
            self.repository.refresh(plan)
        except Exception:
            self.repository.rollback()
            raise

        plan = self.repository.get_plan_by_id(str(plan.id))
        if plan is None:
            raise NotFoundException("Plan not found after creation.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=None,
        provider_id=str(provider.id),
        event_type=AUDIT_EVENT_SUBSCRIPTION_PLAN_CREATED,
        entity_type="SUBSCRIPTION_PLAN",
        entity_id=str(plan.id),
        payload_json={
            "code": plan.code,
            "billing_period": plan.billing_period,
            "price_amount": float(plan.price_amount),
            "currency_code": plan.currency_code,
            "is_active": plan.is_active,
        },
    )


        return self._build_plan_response(plan)

    def update_my_provider_plan(
        self,
        current_user: User,
        plan_id: str,
        payload: ProviderPlanUpsertRequest,
    ) -> ProviderPlanResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        try:
            plan = self.repository.get_plan_by_id_for_update(plan_id)
            if plan is None:
                raise NotFoundException("Provider subscription plan not found.")

            if str(plan.provider_id) != str(provider.id):
                raise ForbiddenException("This plan does not belong to your provider.")

            billing_period = payload.billing_period.strip().upper()
            if billing_period not in (PLAN_BILLING_PERIOD_MONTHLY, PLAN_BILLING_PERIOD_ANNUAL):
                raise ConflictException("Unsupported billing_period. Use MONTHLY or ANNUAL.")

            plan.code = payload.code.strip().upper()
            plan.name = payload.name.strip()
            plan.description = self._normalize_optional_text(payload.description)
            plan.billing_period = billing_period
            plan.price_amount = self._to_money_decimal(payload.price_amount)
            plan.currency_code = payload.currency_code.strip().upper() if payload.currency_code else DEFAULT_CURRENCY_CODE
            plan.is_active = payload.is_active
            plan.auto_renews = payload.auto_renews

            self.repository.save(plan)
            self.repository.commit()
        except Exception:
            self.repository.rollback()
            raise

        plan = self.repository.get_plan_by_id(plan_id)
        if plan is None:
            raise NotFoundException("Provider subscription plan not found after update.")

        return self._build_plan_response(plan)

    def upsert_my_provider_plan_coverage(
        self,
        current_user: User,
        plan_id: str,
        payload: ProviderPlanCoverageUpsertRequest,
    ) -> ProviderPlanCoverageResponse:
        provider = self.repository.get_provider_by_owner_user_id(str(current_user.id))
        if provider is None:
            raise NotFoundException("No provider profile is linked to this account.")

        coverage_type = payload.coverage_type.strip().upper()
        if coverage_type not in (
            PLAN_COVERAGE_TYPE_FIXED_AMOUNT,
            PLAN_COVERAGE_TYPE_PERCENTAGE,
            PLAN_COVERAGE_TYPE_FULL,
        ):
            raise ConflictException("Unsupported coverage_type.")

        if payload.service_catalog_item_id is None and payload.incident_category is None:
            raise ConflictException(
                "At least one matching rule is required: service_catalog_item_id or incident_category."
            )

        service_catalog_item = None
        if payload.service_catalog_item_id is not None:
            service_catalog_item = self.repository.get_service_catalog_item_by_id(payload.service_catalog_item_id)
            if service_catalog_item is None:
                raise NotFoundException("Service catalog item not found.")

        try:
            plan = self.repository.get_plan_by_id_for_update(plan_id)
            if plan is None:
                raise NotFoundException("Provider subscription plan not found.")

            if str(plan.provider_id) != str(provider.id):
                raise ForbiddenException("This plan does not belong to your provider.")

            if payload.coverage_id:
                coverage = self.repository.get_plan_coverage_by_id_for_update(payload.coverage_id)
                if coverage is None:
                    raise NotFoundException("Plan coverage not found.")
                if str(coverage.plan_id) != str(plan.id):
                    raise ForbiddenException("This coverage rule does not belong to the selected plan.")
            else:
                coverage = ProviderSubscriptionPlanCoverage(
                    plan_id=plan.id,
                    service_catalog_item_id=None,
                    incident_category=None,
                    coverage_type=coverage_type,
                    coverage_value=self._to_money_decimal(payload.coverage_value),
                    max_coverage_amount=None,
                    waiting_period_days=payload.waiting_period_days,
                    max_applications_per_subscription=payload.max_applications_per_subscription,
                    is_active=payload.is_active,
                )

            coverage.service_catalog_item_id = payload.service_catalog_item_id
            coverage.incident_category = (
                payload.incident_category.strip().upper() if payload.incident_category else None
            )
            coverage.coverage_type = coverage_type
            coverage.coverage_value = self._to_money_decimal(payload.coverage_value)
            coverage.max_coverage_amount = (
                self._to_money_decimal(payload.max_coverage_amount)
                if payload.max_coverage_amount is not None
                else None
            )
            coverage.waiting_period_days = payload.waiting_period_days
            coverage.max_applications_per_subscription = payload.max_applications_per_subscription
            coverage.is_active = payload.is_active

            self.repository.save(coverage)
            self.repository.commit()
            self.repository.refresh(coverage)
        except Exception:
            self.repository.rollback()
            raise

        coverage = self.repository.get_plan_coverage_by_id(str(coverage.id))
        if coverage is None:
            raise NotFoundException("Plan coverage not found after upsert.")

        return self._build_coverage_response(coverage)

    def list_provider_plans_for_client(self, provider_id: str) -> list[ProviderPlanResponse]:
        provider = self.repository.get_provider_by_id(provider_id)
        if provider is None:
            raise NotFoundException("Provider not found.")

        plans = self.repository.list_available_provider_plans_for_client(provider_id)
        return [self._build_plan_response(item) for item in plans]

    # ---------------------------
    # Client subscriptions
    # ---------------------------

    def subscribe_client_to_plan(
        self,
        current_user: User,
        plan_id: str,
        payload: ClientSubscribeToPlanRequest,
    ) -> ClientPlanSubscriptionResponse:
        plan = self.repository.get_plan_by_id(plan_id)
        if plan is None:
            raise NotFoundException("Provider subscription plan not found.")

        if not plan.is_active:
            raise ConflictException("This plan is not currently active.")

        existing_subscription = self.repository.get_active_subscription_for_client_and_plan(
            client_user_id=str(current_user.id),
            plan_id=plan_id,
        )
        if existing_subscription is not None and existing_subscription.expires_at > datetime.now(timezone.utc):
            raise ConflictException("The client already has an active subscription for this plan.")

        started_at = datetime.now(timezone.utc)
        expires_at = self._calculate_expiration(
            started_at=started_at,
            billing_period=plan.billing_period,
        )

        subscription = ClientPlanSubscription(
            client_user_id=current_user.id,
            provider_id=plan.provider_id,
            plan_id=plan.id,
            status=SUBSCRIPTION_STATUS_ACTIVE,
            started_at=started_at,
            expires_at=expires_at,
            cancelled_at=None,
            external_reference=self._normalize_optional_text(payload.external_reference),
            note=self._normalize_optional_text(payload.note),
        )

        try:
            self.repository.save(subscription)
            self.repository.commit()
            self.repository.refresh(subscription)
        except Exception:
            self.repository.rollback()
            raise

        subscriptions = self.repository.list_client_subscriptions(str(current_user.id))
        created = next((item for item in subscriptions if str(item.id) == str(subscription.id)), None)
        if created is None:
            raise NotFoundException("Subscription not found after creation.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=None,
        provider_id=str(plan.provider_id),
        event_type=AUDIT_EVENT_CLIENT_SUBSCRIBED_TO_PLAN,
        entity_type="CLIENT_PLAN_SUBSCRIPTION",
        entity_id=str(subscription.id),
        payload_json={
            "plan_id": str(plan.id),
            "started_at": subscription.started_at.isoformat(),
            "expires_at": subscription.expires_at.isoformat(),
            "status": subscription.status,
        },
    )


        return self._build_client_subscription_response(created)

    def list_my_client_subscriptions(self, current_user: User) -> list[ClientPlanSubscriptionResponse]:
        subscriptions = self.repository.list_client_subscriptions(str(current_user.id))

        now = datetime.now(timezone.utc)
        updated_any = False

        for item in subscriptions:
            if item.status == SUBSCRIPTION_STATUS_ACTIVE and item.expires_at <= now:
                item.status = "EXPIRED"
                self.repository.save(item)
                updated_any = True

        if updated_any:
            self.repository.commit()
            subscriptions = self.repository.list_client_subscriptions(str(current_user.id))

        return [self._build_client_subscription_response(item) for item in subscriptions]

    # ---------------------------
    # Coverage preview / apply
    # ---------------------------

    def preview_applicable_coverage_for_incident(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentCoveragePreviewResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        if incident.provider_id is None:
            raise ConflictException("This incident does not yet have an assigned provider.")

        if incident.status == INCIDENT_STATUS_CANCELLED:
            raise ConflictException("Cancelled incidents cannot use subscription coverage.")

        billing = self.repository.get_incident_billing_by_incident_id(incident_id)
        if billing is None:
            raise ConflictException("This incident does not yet have billing information.")

        amount_basis = self._resolve_billing_amount_basis(billing)
        used_category = self._resolve_incident_category(incident)

        active_subscriptions = self.repository.list_active_subscriptions_for_client_and_provider(
            client_user_id=str(current_user.id),
            provider_id=str(incident.provider_id),
        )

        best_option = self._find_best_coverage_option(
            incident=incident,
            billing=billing,
            active_subscriptions=active_subscriptions,
            amount_basis=amount_basis,
            used_category=used_category,
        )

        if best_option is None:
            return IncidentCoveragePreviewResponse(
                incident_id=incident_id,
                billing_amount_basis=float(amount_basis),
                matched_incident_category=used_category,
                has_applicable_coverage=False,
                rationale={
                    "reason": "No active subscription with applicable coverage was found for this incident."
                },
            )

        return IncidentCoveragePreviewResponse(
            incident_id=incident_id,
            billing_amount_basis=float(amount_basis),
            matched_incident_category=used_category,
            has_applicable_coverage=True,
            client_plan_subscription_id=str(best_option["subscription"].id),
            plan_id=str(best_option["plan"].id),
            plan_name=best_option["plan"].name,
            plan_coverage_id=str(best_option["coverage"].id),
            coverage_type=best_option["coverage"].coverage_type,
            coverage_value=float(best_option["coverage"].coverage_value),
            coverage_applied_amount=float(best_option["coverage_applied_amount"]),
            client_payable_amount=float(best_option["client_payable_amount"]),
            rationale=best_option["rationale"],
        )

    def apply_best_coverage_for_incident(
        self,
        current_user: User,
        incident_id: str,
    ) -> IncidentSubscriptionApplicationResponse:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        if str(incident.client_user_id) != str(current_user.id):
            raise ForbiddenException("This incident does not belong to the authenticated client.")

        if incident.provider_id is None:
            raise ConflictException("This incident does not yet have an assigned provider.")

        if incident.status == INCIDENT_STATUS_CANCELLED:
            raise ConflictException("Cancelled incidents cannot use subscription coverage.")

        try:
            billing = self.repository.get_incident_billing_by_incident_id_for_update(incident_id)
            if billing is None:
                raise ConflictException("This incident does not yet have billing information.")

            if billing.final_price_amount is None:
                raise ConflictException(
                    "Coverage can only be applied after the provider finalizes the service price."
                )

            active_subscriptions = self.repository.list_active_subscriptions_for_client_and_provider(
                client_user_id=str(current_user.id),
                provider_id=str(incident.provider_id),
            )

            used_category = self._resolve_incident_category(incident)

            best_option = self._find_best_coverage_option(
                incident=incident,
                billing=billing,
                active_subscriptions=active_subscriptions,
                amount_basis=billing.final_price_amount,
                used_category=used_category,
            )

            if best_option is None:
                raise ConflictException("No applicable subscription coverage was found for this incident.")

            previous_applications = self.repository.list_incident_applications_for_update(incident_id)
            for previous in previous_applications:
                previous.status = SUBSCRIPTION_APPLICATION_STATUS_VOIDED
                self.repository.save(previous)

            application = IncidentSubscriptionApplication(
                incident_id=incident.id,
                incident_billing_id=billing.id,
                client_plan_subscription_id=best_option["subscription"].id,
                plan_coverage_id=best_option["coverage"].id,
                matched_service_catalog_item_id=best_option["matched_service_catalog_item_id"],
                matched_incident_category=used_category,
                coverage_type=best_option["coverage"].coverage_type,
                coverage_value=best_option["coverage"].coverage_value,
                original_amount=billing.final_price_amount,
                coverage_applied_amount=best_option["coverage_applied_amount"],
                client_payable_amount=best_option["client_payable_amount"],
                status=SUBSCRIPTION_APPLICATION_STATUS_APPLIED,
                snapshot_json=best_option["rationale"],
            )

            billing.client_plan_subscription_id = best_option["subscription"].id
            billing.plan_coverage_id = best_option["coverage"].id
            billing.coverage_applied_amount = best_option["coverage_applied_amount"]
            billing.client_payable_amount = best_option["client_payable_amount"]

            self.repository.save(application)
            self.repository.save(billing)
            self.repository.commit()
            self.repository.refresh(application)
        except Exception:
            self.repository.rollback()
            raise

        applications = self.repository.list_incident_applications(incident_id)
        applied = next(
            (
                item
                for item in applications
                if str(item.id) == str(application.id)
            ),
            None,
        )
        if applied is None:
            raise NotFoundException("Incident subscription application not found after apply.")

        self._emit_audit_safely(
        actor_user_id=str(current_user.id),
        incident_id=incident_id,
        provider_id=str(incident.provider_id),
        event_type=AUDIT_EVENT_COVERAGE_APPLIED,
        entity_type="INCIDENT_SUBSCRIPTION_APPLICATION",
        entity_id=str(application.id),
        payload_json={
            "client_plan_subscription_id": str(application.client_plan_subscription_id),
            "plan_coverage_id": str(application.plan_coverage_id),
            "coverage_applied_amount": float(application.coverage_applied_amount),
            "client_payable_amount": float(application.client_payable_amount),
        },
    )


        return self._build_application_response(applied)

    def list_platform_incident_subscription_applications(
        self,
        incident_id: str,
    ) -> list[IncidentSubscriptionApplicationResponse]:
        incident = self.repository.get_incident_by_id(incident_id)
        if incident is None:
            raise NotFoundException("Incident not found.")

        items = self.repository.list_incident_applications(incident_id)
        return [self._build_application_response(item) for item in items]

    # ---------------------------
    # Internal helpers
    # ---------------------------

    def _find_best_coverage_option(
        self,
        *,
        incident,
        billing,
        active_subscriptions: list[ClientPlanSubscription],
        amount_basis: Decimal,
        used_category: str,
    ) -> dict | None:
        now = datetime.now(timezone.utc)
        best_option = None

        for subscription in active_subscriptions:
            if subscription.status != SUBSCRIPTION_STATUS_ACTIVE:
                continue
            if subscription.expires_at <= now:
                continue

            plan = subscription.plan
            if plan is None or not plan.is_active:
                continue

            for coverage in plan.coverages:
                if not coverage.is_active:
                    continue

                waiting_limit = subscription.started_at + timedelta(days=coverage.waiting_period_days)
                if waiting_limit > now:
                    continue

                current_usage_count = self.repository.count_applied_coverage_usages(
                    subscription_id=str(subscription.id),
                    coverage_id=str(coverage.id),
                )
                if (
                    coverage.max_applications_per_subscription is not None
                    and current_usage_count >= coverage.max_applications_per_subscription
                ):
                    continue

                matched_service_catalog_item_id = None

                if coverage.service_catalog_item is not None:
                    if coverage.service_catalog_item.category != used_category:
                        continue
                    matched_service_catalog_item_id = coverage.service_catalog_item.id
                elif coverage.incident_category is not None:
                    if coverage.incident_category != used_category:
                        continue

                coverage_applied_amount = self._calculate_coverage_amount(
                    amount_basis=amount_basis,
                    coverage=coverage,
                )
                if coverage_applied_amount <= Decimal("0.00"):
                    continue

                client_payable_amount = (amount_basis - coverage_applied_amount).quantize(
                    MONEY_QUANTIZER,
                    rounding=ROUND_HALF_UP,
                )

                candidate = {
                    "subscription": subscription,
                    "plan": plan,
                    "coverage": coverage,
                    "matched_service_catalog_item_id": matched_service_catalog_item_id,
                    "coverage_applied_amount": coverage_applied_amount,
                    "client_payable_amount": client_payable_amount,
                    "rationale": {
                        "used_category": used_category,
                        "matched_rule_scope": (
                            "SERVICE_CATEGORY"
                            if coverage.service_catalog_item_id is not None
                            else "INCIDENT_CATEGORY"
                            if coverage.incident_category is not None
                            else "GLOBAL"
                        ),
                        "waiting_period_days": coverage.waiting_period_days,
                        "current_usage_count": current_usage_count,
                        "max_applications_per_subscription": coverage.max_applications_per_subscription,
                        "amount_basis": float(amount_basis),
                    },
                }

                if best_option is None:
                    best_option = candidate
                    continue

                if candidate["coverage_applied_amount"] > best_option["coverage_applied_amount"]:
                    best_option = candidate

        return best_option

    def _calculate_coverage_amount(
        self,
        *,
        amount_basis: Decimal,
        coverage: ProviderSubscriptionPlanCoverage,
    ) -> Decimal:
        if coverage.coverage_type == PLAN_COVERAGE_TYPE_FULL:
            applied_amount = amount_basis
        elif coverage.coverage_type == PLAN_COVERAGE_TYPE_FIXED_AMOUNT:
            applied_amount = min(amount_basis, coverage.coverage_value)
        elif coverage.coverage_type == PLAN_COVERAGE_TYPE_PERCENTAGE:
            applied_amount = (
                amount_basis * coverage.coverage_value / Decimal("100")
            ).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)
        else:
            raise ConflictException("Unsupported coverage_type.")

        if coverage.max_coverage_amount is not None:
            applied_amount = min(applied_amount, coverage.max_coverage_amount)

        if applied_amount < Decimal("0.00"):
            applied_amount = Decimal("0.00")

        if applied_amount > amount_basis:
            applied_amount = amount_basis

        return applied_amount.quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _resolve_billing_amount_basis(self, billing) -> Decimal:
        if billing.final_price_amount is not None:
            return billing.final_price_amount

        if billing.estimated_price_max is not None:
            return billing.estimated_price_max

        if billing.estimated_price_min is not None:
            return billing.estimated_price_min

        raise ConflictException("This incident still does not have an estimated or final billing amount.")

    def _resolve_incident_category(self, incident) -> str:
        if incident.suggested_category:
            return incident.suggested_category.strip().upper()
        return incident.reported_category.strip().upper()

    def _calculate_expiration(self, *, started_at: datetime, billing_period: str) -> datetime:
        if billing_period == PLAN_BILLING_PERIOD_MONTHLY:
            return started_at + timedelta(days=30)

        if billing_period == PLAN_BILLING_PERIOD_ANNUAL:
            return started_at + timedelta(days=365)

        raise ConflictException("Unsupported billing period.")

    def _build_plan_response(self, plan: ProviderSubscriptionPlan) -> ProviderPlanResponse:
        provider_payload = None
        if plan.provider is not None:
            owner_payload = None
            if plan.provider.owner_user is not None:
                owner = plan.provider.owner_user
                owner_payload = SubscriptionUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = SubscriptionProviderSummaryResponse(
                id=str(plan.provider.id),
                provider_type=plan.provider.provider_type,
                business_name=plan.provider.business_name,
                owner_user=owner_payload,
            )

        return ProviderPlanResponse(
            id=str(plan.id),
            provider_id=str(plan.provider_id),
            code=plan.code,
            name=plan.name,
            description=plan.description,
            billing_period=plan.billing_period,
            price_amount=float(plan.price_amount),
            currency_code=plan.currency_code,
            is_active=plan.is_active,
            auto_renews=plan.auto_renews,
            created_at=plan.created_at,
            updated_at=plan.updated_at,
            provider=provider_payload,
            coverages=[self._build_coverage_response(item) for item in plan.coverages],
        )

    def _build_coverage_response(
        self,
        coverage: ProviderSubscriptionPlanCoverage,
    ) -> ProviderPlanCoverageResponse:
        service_item = coverage.service_catalog_item
        return ProviderPlanCoverageResponse(
            id=str(coverage.id),
            plan_id=str(coverage.plan_id),
            service_catalog_item_id=(
                str(coverage.service_catalog_item_id) if coverage.service_catalog_item_id else None
            ),
            service_catalog_item_code=service_item.code if service_item is not None else None,
            service_catalog_item_title=service_item.title if service_item is not None else None,
            incident_category=coverage.incident_category,
            coverage_type=coverage.coverage_type,
            coverage_value=float(coverage.coverage_value),
            max_coverage_amount=float(coverage.max_coverage_amount) if coverage.max_coverage_amount is not None else None,
            waiting_period_days=coverage.waiting_period_days,
            max_applications_per_subscription=coverage.max_applications_per_subscription,
            is_active=coverage.is_active,
            created_at=coverage.created_at,
            updated_at=coverage.updated_at,
        )

    def _build_client_subscription_response(
        self,
        subscription: ClientPlanSubscription,
    ) -> ClientPlanSubscriptionResponse:
        provider_payload = None
        if subscription.provider is not None:
            owner_payload = None
            if subscription.provider.owner_user is not None:
                owner = subscription.provider.owner_user
                owner_payload = SubscriptionUserSummaryResponse(
                    id=str(owner.id),
                    email=owner.email,
                    first_name=owner.first_name,
                    last_name=owner.last_name,
                    full_name=owner.full_name,
                    phone_number=owner.phone_number,
                )

            provider_payload = SubscriptionProviderSummaryResponse(
                id=str(subscription.provider.id),
                provider_type=subscription.provider.provider_type,
                business_name=subscription.provider.business_name,
                owner_user=owner_payload,
            )

        return ClientPlanSubscriptionResponse(
            id=str(subscription.id),
            client_user_id=str(subscription.client_user_id),
            provider_id=str(subscription.provider_id),
            plan_id=str(subscription.plan_id),
            status=subscription.status,
            started_at=subscription.started_at,
            expires_at=subscription.expires_at,
            cancelled_at=subscription.cancelled_at,
            external_reference=subscription.external_reference,
            note=subscription.note,
            created_at=subscription.created_at,
            updated_at=subscription.updated_at,
            provider=provider_payload,
            plan=self._build_plan_response(subscription.plan),
        )

    def _build_application_response(
        self,
        application: IncidentSubscriptionApplication,
    ) -> IncidentSubscriptionApplicationResponse:
        return IncidentSubscriptionApplicationResponse(
            id=str(application.id),
            incident_id=str(application.incident_id),
            incident_billing_id=(
                str(application.incident_billing_id) if application.incident_billing_id else None
            ),
            client_plan_subscription_id=str(application.client_plan_subscription_id),
            plan_coverage_id=str(application.plan_coverage_id),
            matched_service_catalog_item_id=(
                str(application.matched_service_catalog_item_id)
                if application.matched_service_catalog_item_id
                else None
            ),
            matched_incident_category=application.matched_incident_category,
            coverage_type=application.coverage_type,
            coverage_value=float(application.coverage_value),
            original_amount=float(application.original_amount),
            coverage_applied_amount=float(application.coverage_applied_amount),
            client_payable_amount=float(application.client_payable_amount),
            status=application.status,
            snapshot_json=application.snapshot_json,
            applied_at=application.applied_at,
            updated_at=application.updated_at,
        )

    def _to_money_decimal(self, value) -> Decimal:
        return Decimal(str(value)).quantize(MONEY_QUANTIZER, rounding=ROUND_HALF_UP)

    def _normalize_optional_text(self, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None


    def _emit_audit_safely(
        self,
        *,
        actor_user_id: str | None,
        incident_id: str | None,
        provider_id: str | None,
        event_type: str,
        entity_type: str | None,
        entity_id: str | None,
        payload_json: dict | None,
    ) -> None:
        try:
            AuditEventDispatcher().emit(
                actor_user_id=actor_user_id,
                incident_id=incident_id,
                provider_id=provider_id,
                request_id=None,
                event_scope="DOMAIN",
                event_type=event_type,
                entity_type=entity_type,
                entity_id=entity_id,
                outcome="SUCCESS",
                payload_json=payload_json,
            )
        except Exception:
            return
