import 'package:flutter/material.dart';
import '../../domain/entities/technician.dart';
import '../../domain/usecases/create_technician_usecase.dart';
import '../../domain/usecases/get_technicians_usecase.dart';
import '../../domain/usecases/update_technician_usecase.dart';

class TechniciansViewModel extends ChangeNotifier {
  final CreateTechnicianUseCase _createTechnicianUseCase;
  final GetTechniciansUseCase _getTechniciansUseCase;
  final UpdateTechnicianUseCase _updateTechnicianUseCase;

  List<Technician> _technicians = [];
  bool _isLoading = false;
  String? _errorMessage;

  TechniciansViewModel({
    required CreateTechnicianUseCase createTechnicianUseCase,
    required GetTechniciansUseCase getTechniciansUseCase,
    required UpdateTechnicianUseCase updateTechnicianUseCase,
  }) : _createTechnicianUseCase = createTechnicianUseCase,
       _getTechniciansUseCase = getTechniciansUseCase,
       _updateTechnicianUseCase = updateTechnicianUseCase;

  List<Technician> get technicians => _technicians;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadTechnicians() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _technicians = await _getTechniciansUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> createTechnician({
    required String firstName,
    required String lastName,
    required String phoneNumber,
    required String specialty,
    required bool isAvailable,
    double? latitude,
    double? longitude,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = CreateTechnicianParams(
        firstName: firstName,
        lastName: lastName,
        phoneNumber: phoneNumber,
        specialty: specialty,
        isAvailable: isAvailable,
        currentLatitude: latitude,
        currentLongitude: longitude,
      );

      final newTechnician = await _createTechnicianUseCase.execute(params);
      _technicians.add(newTechnician);
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> updateTechnician({
    required String technicianId,
    String? firstName,
    String? lastName,
    String? phoneNumber,
    String? specialty,
    bool? isAvailable,
    double? latitude,
    double? longitude,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = UpdateTechnicianParams(
        firstName: firstName,
        lastName: lastName,
        phoneNumber: phoneNumber,
        specialty: specialty,
        isAvailable: isAvailable,
        currentLatitude: latitude,
        currentLongitude: longitude,
      );

      final updatedTechnician = await _updateTechnicianUseCase.execute(
        technicianId,
        params,
      );

      // Actualizar en la lista
      final index = _technicians.indexWhere((t) => t.id == technicianId);
      if (index != -1) {
        _technicians[index] = updatedTechnician;
      }

      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> toggleAvailability(String technicianId, bool isAvailable) async {
    return await updateTechnician(
      technicianId: technicianId,
      isAvailable: isAvailable,
    );
  }

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }
}
