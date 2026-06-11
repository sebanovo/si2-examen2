import '../entities/vehicle.dart';
import '../repositories/vehicle_repository.dart';

class GetVehicleByIdUseCase {
  final VehicleRepository repository;

  GetVehicleByIdUseCase(this.repository);

  Future<Vehicle> call(String vehicleId) {
    return repository.getVehicleById(vehicleId);
  }
}
