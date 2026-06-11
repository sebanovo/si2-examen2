from app.common.exceptions import ConflictException, ForbiddenException, NotFoundException
from app.services.auth.models import User
from app.services.vehicles.models import Vehicle
from app.services.vehicles.repository import VehiclesRepository
from app.services.vehicles.schemas import CreateVehicleRequest, UpdateOwnVehicleRequest, VehicleResponse


class VehiclesService:
    def __init__(self, repository: VehiclesRepository) -> None:
        self.repository = repository

    def create_own_vehicle(self, current_user: User, payload: CreateVehicleRequest) -> VehicleResponse:
        normalized_plate_number = payload.plate_number.strip().upper()

        existing_vehicle = self.repository.get_vehicle_by_plate_number(normalized_plate_number)
        if existing_vehicle is not None:
            raise ConflictException("A vehicle with this plate number already exists.")

        new_vehicle = Vehicle(
            owner_user_id=current_user.id,
            plate_number=normalized_plate_number,
            vehicle_type=payload.vehicle_type,
            brand=payload.brand.strip(),
            model=payload.model.strip(),
            year=payload.year,
            color=payload.color.strip() if payload.color else None,
            notes=payload.notes.strip() if payload.notes else None,
            is_active=True,
        )

        created_vehicle = self.repository.create_vehicle(new_vehicle)
        return self._build_vehicle_response(created_vehicle)

    def list_own_vehicles(self, current_user: User) -> list[VehicleResponse]:
        vehicles = self.repository.list_vehicles_by_owner_user_id(str(current_user.id))
        return [self._build_vehicle_response(vehicle) for vehicle in vehicles]

    def get_own_vehicle(self, current_user: User, vehicle_id: str) -> VehicleResponse:
        vehicle = self.repository.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        return self._build_vehicle_response(vehicle)

    def update_own_vehicle(
        self,
        current_user: User,
        vehicle_id: str,
        payload: UpdateOwnVehicleRequest,
    ) -> VehicleResponse:
        vehicle = self.repository.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            raise NotFoundException("Vehicle not found.")

        if str(vehicle.owner_user_id) != str(current_user.id):
            raise ForbiddenException("This vehicle does not belong to the authenticated user.")

        if payload.vehicle_type is not None:
            vehicle.vehicle_type = payload.vehicle_type

        if payload.brand is not None:
            vehicle.brand = payload.brand.strip()

        if payload.model is not None:
            vehicle.model = payload.model.strip()

        if payload.year is not None:
            vehicle.year = payload.year

        if payload.color is not None:
            cleaned_value = payload.color.strip()
            vehicle.color = cleaned_value or None

        if payload.notes is not None:
            cleaned_value = payload.notes.strip()
            vehicle.notes = cleaned_value or None

        if payload.is_active is not None:
            vehicle.is_active = payload.is_active

        updated_vehicle = self.repository.save_vehicle(vehicle)
        return self._build_vehicle_response(updated_vehicle)

    def _build_vehicle_response(self, vehicle: Vehicle) -> VehicleResponse:
        return VehicleResponse(
            id=str(vehicle.id),
            owner_user_id=str(vehicle.owner_user_id),
            plate_number=vehicle.plate_number,
            vehicle_type=vehicle.vehicle_type,
            brand=vehicle.brand,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            notes=vehicle.notes,
            is_active=vehicle.is_active,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at,
        )