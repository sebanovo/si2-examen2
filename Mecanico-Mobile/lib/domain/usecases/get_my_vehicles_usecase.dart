import '../entities/vehicle.dart';
import '../repositories/vehicle_repository.dart';

class GetMyVehiclesUseCase {
  final VehicleRepository repository;

  GetMyVehiclesUseCase(this.repository);

  Future<List<Vehicle>> call() {
    return repository.getMyVehicles();
  }
}
