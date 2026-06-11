from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.services.vehicles.models import Vehicle


class VehiclesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_vehicle_by_id(self, vehicle_id: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.id == vehicle_id)
        return self.db.execute(query).scalar_one_or_none()

    def get_vehicle_by_plate_number(self, plate_number: str) -> Vehicle | None:
        query: Select[tuple[Vehicle]] = select(Vehicle).where(Vehicle.plate_number == plate_number)
        return self.db.execute(query).scalar_one_or_none()

    def list_vehicles_by_owner_user_id(self, owner_user_id: str) -> list[Vehicle]:
        query: Select[tuple[Vehicle]] = (
            select(Vehicle)
            .where(Vehicle.owner_user_id == owner_user_id)
            .order_by(Vehicle.created_at.desc())
        )
        return list(self.db.execute(query).scalars().all())

    def create_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle

    def save_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle