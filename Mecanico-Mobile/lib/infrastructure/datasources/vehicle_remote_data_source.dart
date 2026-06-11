import '../../core/network/api_client.dart';
import '../models/vehicle_model.dart';

class VehicleRemoteDataSource {
  final ApiClient api;

  VehicleRemoteDataSource(this.api);

  Future<VehicleModel> createVehicle(Map<String, dynamic> body) async {
    final response = await api.post('/api/vehicles', body);
    final Map<String, dynamic> jsonResponse = response.data;
    if (jsonResponse['success'] == true) {
      return VehicleModel.fromJson(jsonResponse['data']);
    } else {
      throw Exception(jsonResponse['message'] ?? 'Error al crear vehículo');
    }
  }

  Future<List<VehicleModel>> getMyVehicles() async {
    final response = await api.get('/api/vehicles');
    final Map<String, dynamic> jsonResponse = response.data;
    if (jsonResponse['success'] == true) {
      final List<dynamic> list = jsonResponse['data'] as List<dynamic>;
      return list
          .map((item) => VehicleModel.fromJson(item as Map<String, dynamic>))
          .toList();
    } else {
      throw Exception(jsonResponse['message'] ?? 'Error al cargar vehículos');
    }
  }

  Future<VehicleModel> getVehicleById(String vehicleId) async {
    final response = await api.get('/api/vehicles/$vehicleId');
    final Map<String, dynamic> jsonResponse = response.data;
    if (jsonResponse['success'] == true) {
      return VehicleModel.fromJson(jsonResponse['data']);
    } else {
      throw Exception(jsonResponse['message'] ?? 'Error al cargar vehículo');
    }
  }

  Future<VehicleModel> updateVehicle(
    String vehicleId,
    Map<String, dynamic> body,
  ) async {
    final response = await api.patch('/api/vehicles/$vehicleId', body);
    final Map<String, dynamic> jsonResponse = response.data;
    if (jsonResponse['success'] == true) {
      return VehicleModel.fromJson(jsonResponse['data']);
    } else {
      throw Exception(
        jsonResponse['message'] ?? 'Error al actualizar vehículo',
      );
    }
  }
}
