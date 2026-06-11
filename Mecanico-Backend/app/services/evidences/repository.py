from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.evidences.models import IncidentEvidence
from app.services.incidents.models import Incident
from app.services.providers.models import Provider


class EvidencesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_incident_by_id(self, incident_id: str) -> Incident | None:
        query: Select[tuple[Incident]] = select(Incident).where(Incident.id == incident_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_provider_by_owner_user_id(self, owner_user_id: str) -> Provider | None:
        query: Select[tuple[Provider]] = select(Provider).where(Provider.owner_user_id == owner_user_id)
        return self.db.execute(query).scalar_one_or_none()

    def create_evidence(self, evidence: IncidentEvidence) -> IncidentEvidence:
        self.db.add(evidence)
        self.db.commit()
        self.db.refresh(evidence)
        return evidence

    def get_evidence_by_id(self, evidence_id: str) -> IncidentEvidence | None:
        query: Select[tuple[IncidentEvidence]] = select(IncidentEvidence).where(IncidentEvidence.id == evidence_id)
        return self.db.execute(query).scalar_one_or_none()

    def list_evidences_by_incident_id(self, incident_id: str) -> list[IncidentEvidence]:
        query: Select[tuple[IncidentEvidence]] = (
            select(IncidentEvidence)
            .where(IncidentEvidence.incident_id == incident_id)
            .order_by(IncidentEvidence.created_at.asc())
        )
        return list(self.db.execute(query).scalars().all())