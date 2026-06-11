import '../entities/vehicle.dart';
import '../repositories/vehicle_repository.dart';

class CreateVehicleUseCase {
  final VehicleRepository repository;

  CreateVehicleUseCase(this.repository);

  Future<Vehicle> call(Map<String, dynamic> body) {
    return repository.createVehicle(body);
  }
}
