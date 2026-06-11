from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.jobs.models import BackgroundJob


class JobsRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def save_job(self, job: BackgroundJob) -> BackgroundJob:
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def get_job_by_id(self, job_id: str) -> BackgroundJob | None:
        query: Select[tuple[BackgroundJob]] = select(BackgroundJob).where(BackgroundJob.id == job_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_job_by_celery_task_id(self, celery_task_id: str) -> BackgroundJob | None:
        query: Select[tuple[BackgroundJob]] = (
            select(BackgroundJob).where(BackgroundJob.celery_task_id == celery_task_id)
        )
        return self.db.execute(query).scalar_one_or_none()

    def list_jobs(self, limit: int = 50, offset: int = 0) -> list[BackgroundJob]:
        query: Select[tuple[BackgroundJob]] = (
            select(BackgroundJob)
            .order_by(BackgroundJob.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.execute(query).scalars().all())

    def incident_exists(self, incident_id: str) -> bool:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none() is not None

    def evidence_exists(self, evidence_id: str) -> bool:
        query: Select[tuple[IncidentEvidence]] = select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        return self.db.execute(query).scalar_one_or_none() is not None