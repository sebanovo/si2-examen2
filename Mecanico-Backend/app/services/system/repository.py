from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.services.audit.models import AuditLog
from app.services.billing.models import IncidentBilling
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob
from app.services.notifications.models import PushNotificationDelivery
from app.services.providers.models import Provider, Technician
from app.services.subscriptions.models import ClientPlanSubscription


class SystemRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incidents_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(Incident.status, func.count(Incident.id))
            .group_by(Incident.status)
            .order_by(Incident.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_background_jobs_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(BackgroundJob.status, func.count(BackgroundJob.id))
            .group_by(BackgroundJob.status)
            .order_by(BackgroundJob.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_push_deliveries_by_status(self) -> dict[str, int]:
        rows = self.db.execute(
            select(PushNotificationDelivery.status, func.count(PushNotificationDelivery.id))
            .group_by(PushNotificationDelivery.status)
            .order_by(PushNotificationDelivery.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_provider_summary(self) -> dict:
        total = int(self.db.execute(select(func.count(Provider.id))).scalar_one() or 0)
        active = int(
            self.db.execute(
                select(func.count(Provider.id)).where(Provider.is_active.is_(True))
            ).scalar_one()
            or 0
        )
        available = int(
            self.db.execute(
                select(func.count(Provider.id)).where(
                    Provider.is_active.is_(True),
                    Provider.is_available.is_(True),
                )
            ).scalar_one()
            or 0
        )

        total_capacity = int(
            self.db.execute(select(func.coalesce(func.sum(Provider.max_concurrent_services), 0))).scalar_one() or 0
        )
        active_services = int(
            self.db.execute(select(func.coalesce(func.sum(Provider.current_active_services), 0))).scalar_one() or 0
        )

        return {
            "total": total,
            "active": active,
            "available": available,
            "total_capacity": total_capacity,
            "current_active_services": active_services,
        }

    def get_technician_summary(self) -> dict:
        total = int(self.db.execute(select(func.count(Technician.id))).scalar_one() or 0)
        active = int(
            self.db.execute(
                select(func.count(Technician.id)).where(Technician.is_active.is_(True))
            ).scalar_one()
            or 0
        )
        available = int(
            self.db.execute(
                select(func.count(Technician.id)).where(
                    Technician.is_active.is_(True),
                    Technician.is_available.is_(True),
                )
            ).scalar_one()
            or 0
        )

        return {
            "total": total,
            "active": active,
            "available": available,
        }

    def get_financial_summary(self) -> dict:
        row = self.db.execute(
            select(
                func.coalesce(func.sum(IncidentBilling.final_price_amount), 0),
                func.coalesce(
                    func.sum(
                        func.case(
                            (IncidentBilling.payment_status == "PAID", func.coalesce(IncidentBilling.client_payable_amount, IncidentBilling.final_price_amount)),
                            else_=0,
                        )
                    ),
                    0,
                ),
                func.coalesce(func.sum(IncidentBilling.platform_commission_amount), 0),
                func.coalesce(func.sum(IncidentBilling.provider_net_amount), 0),
                func.coalesce(func.sum(IncidentBilling.client_payable_amount), 0),
            )
        ).one()

        return {
            "total_service_value": float(row[0] or 0),
            "total_paid_value": float(row[1] or 0),
            "total_platform_commission": float(row[2] or 0),
            "total_provider_net_amount": float(row[3] or 0),
            "total_client_payable_amount": float(row[4] or 0),
        }

    def get_subscription_summary(self) -> dict[str, int]:
        rows = self.db.execute(
            select(ClientPlanSubscription.status, func.count(ClientPlanSubscription.id))
            .group_by(ClientPlanSubscription.status)
            .order_by(ClientPlanSubscription.status.asc())
        ).all()
        return {str(status): int(count) for status, count in rows}

    def get_audit_events_last_24h_count(self) -> int:
        value = self.db.execute(
            select(func.count(AuditLog.id)).where(
                AuditLog.created_at >= func.now() - func.cast("24 hours", type_=func.interval())
            )
        ).scalar_one()
        return int(value or 0)

    def get_average_assignment_seconds(self) -> float | None:
        value = self.db.execute(
            select(
                func.avg(
                    func.extract("epoch", Incident.assigned_at) - func.extract("epoch", Incident.requested_at)
                )
            ).where(
                Incident.assigned_at.is_not(None),
                Incident.requested_at.is_not(None),
            )
        ).scalar_one()
        return float(value) if value is not None else None

    def get_average_completion_seconds(self) -> float | None:
        value = self.db.execute(
            select(
                func.avg(
                    func.extract("epoch", Incident.completed_at) - func.extract("epoch", Incident.requested_at)
                )
            ).where(
                Incident.completed_at.is_not(None),
                Incident.requested_at.is_not(None),
            )
        ).scalar_one()
        return float(value) if value is not None else None
