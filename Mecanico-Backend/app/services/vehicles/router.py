from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.constants import ROLE_CLIENT
from app.common.responses import success_response
from app.core.dependencies import get_db_session
from app.core.security import require_roles
from app.services.auth.models import User
from app.services.vehicles.repository import VehiclesRepository
from app.services.vehicles.schemas import CreateVehicleRequest, UpdateOwnVehicleRequest
from app.services.vehicles.service import VehiclesService

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("")
def create_own_vehicle(
    payload: CreateVehicleRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.create_own_vehicle(current_user, payload)

    return success_response(
        message="Vehicle created successfully.",
        data=result.model_dump(mode="json"),
    )


@router.get("")
def list_own_vehicles(
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.list_own_vehicles(current_user)

    return success_response(
        message="Vehicles loaded successfully.",
        data=[item.model_dump(mode="json") for item in result],
        meta={
            "count": len(result),
        },
    )


@router.get("/{vehicle_id}")
def get_own_vehicle(
    vehicle_id: str,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.get_own_vehicle(current_user, vehicle_id)

    return success_response(
        message="Vehicle loaded successfully.",
        data=result.model_dump(mode="json"),
    )


@router.patch("/{vehicle_id}")
def update_own_vehicle(
    vehicle_id: str,
    payload: UpdateOwnVehicleRequest,
    current_user: User = Depends(require_roles(ROLE_CLIENT)),
    db: Session = Depends(get_db_session),
) -> dict:
    service = VehiclesService(VehiclesRepository(db))
    result = service.update_own_vehicle(current_user, vehicle_id, payload)

    return success_response(
        message="Vehicle updated successfully.",
        data=result.model_dump(mode="json"),
    )