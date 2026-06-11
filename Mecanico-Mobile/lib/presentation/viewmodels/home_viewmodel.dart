import 'package:flutter/material.dart';
import 'package:mechanic_mobile/domain/usecases/get_all_incidents_usecase.dart';
import '../../domain/usecases/get_service_requests_usecase.dart';

class HomeViewModel extends ChangeNotifier {
  final GetServiceRequestsUseCase getServiceRequestsUseCase;
  final GetAllIncidentsUseCase getAllIncidentsUseCase;

  List<dynamic> _requests = []; // ✅ Cambiar a dynamic para aceptar ambos tipos
  bool _isLoading = false;
  String? _errorMessage;

  HomeViewModel({
    required this.getServiceRequestsUseCase,
    required this.getAllIncidentsUseCase,
  });

  List<dynamic> get requests => _requests;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadRequests() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _requests = await getServiceRequestsUseCase.call();
      notifyListeners();
    } catch (e) {
      _errorMessage = 'Error al cargar las solicitudes: ${e.toString()}';
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  // ✅ Método para admin - carga todos los incidentes
  Future<void> loadAllIncidents() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _requests = await getAllIncidentsUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = 'Error al cargar incidentes: ${e.toString()}';
      notifyListeners();
    } finally {
      _setLoading(false);
    }
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
