import '../entities/vehicle.dart';
import '../repositories/vehicle_repository.dart';

class UpdateVehicleUseCase {
  final VehicleRepository repository;

  UpdateVehicleUseCase(this.repository);

  Future<Vehicle> call(String vehicleId, Map<String, dynamic> body) {
    return repository.updateVehicle(vehicleId, body);
  }
}
