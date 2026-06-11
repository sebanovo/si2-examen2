import '../entities/vehicle.dart';

abstract class VehicleRepository {
  Future<Vehicle> createVehicle(Map<String, dynamic> body);
  Future<List<Vehicle>> getMyVehicles();
  Future<Vehicle> getVehicleById(String vehicleId);
  Future<Vehicle> updateVehicle(String vehicleId, Map<String, dynamic> body);
}
