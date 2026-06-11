import '../../domain/entities/vehicle.dart';
import '../../domain/repositories/vehicle_repository.dart';
import '../datasources/vehicle_remote_data_source.dart';

class VehicleRepositoryImpl implements VehicleRepository {
  final VehicleRemoteDataSource remote;

  VehicleRepositoryImpl(this.remote);

  @override
  Future<Vehicle> createVehicle(Map<String, dynamic> body) {
    return remote.createVehicle(body);
  }

  @override
  Future<List<Vehicle>> getMyVehicles() {
    return remote.getMyVehicles();
  }

  @override
  Future<Vehicle> getVehicleById(String vehicleId) {
    return remote.getVehicleById(vehicleId);
  }

  @override
  Future<Vehicle> updateVehicle(String vehicleId, Map<String, dynamic> body) {
    return remote.updateVehicle(vehicleId, body);
  }
}
