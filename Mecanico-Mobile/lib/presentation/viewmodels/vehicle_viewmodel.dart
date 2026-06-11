import 'package:flutter/material.dart';

import '../../domain/entities/vehicle.dart';
import '../../domain/usecases/create_vehicle_usecase.dart';
import '../../domain/usecases/get_my_vehicles_usecase.dart';
import '../../domain/usecases/get_vehicle_by_id_usecase.dart';
import '../../domain/usecases/update_vehicle_usecase.dart';

class VehicleViewModel extends ChangeNotifier {
  final CreateVehicleUseCase createVehicleUseCase;
  final GetMyVehiclesUseCase getMyVehiclesUseCase;
  final GetVehicleByIdUseCase getVehicleByIdUseCase;
  final UpdateVehicleUseCase updateVehicleUseCase;

  VehicleViewModel({
    required this.createVehicleUseCase,
    required this.getMyVehiclesUseCase,
    required this.getVehicleByIdUseCase,
    required this.updateVehicleUseCase,
  });

  List<Vehicle> vehicles = [];
  bool isLoading = false;
  String? errorMessage;

  Future<void> loadVehicles() async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();
    try {
      vehicles = await getMyVehiclesUseCase();
    } catch (e) {
      errorMessage = e.toString();
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> createVehicle(Map<String, dynamic> body) async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();
    try {
      await createVehicleUseCase(body);
      await loadVehicles();
      return true;
    } catch (e) {
      errorMessage = e.toString();
      isLoading = false;
      notifyListeners();
      return false;
    }
  }

  Future<Vehicle?> getVehicleById(String vehicleId) async {
    try {
      return await getVehicleByIdUseCase(vehicleId);
    } catch (e) {
      errorMessage = e.toString();
      notifyListeners();
      return null;
    }
  }

  Future<bool> updateVehicle(
    String vehicleId,
    Map<String, dynamic> body,
  ) async {
    isLoading = true;
    errorMessage = null;
    notifyListeners();
    try {
      await updateVehicleUseCase(vehicleId, body);
      await loadVehicles();
      return true;
    } catch (e) {
      errorMessage = e.toString();
      isLoading = false;
      notifyListeners();
      return false;
    }
  }
}
