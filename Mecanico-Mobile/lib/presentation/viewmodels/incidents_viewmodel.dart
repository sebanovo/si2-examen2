import 'package:flutter/material.dart';
import '../../domain/entities/incident.dart';
import '../../domain/usecases/get_my_incidents_usecase.dart';
import '../../domain/usecases/create_incident_usecase.dart';
import '../../domain/usecases/update_incident_usecase.dart';
import '../../domain/usecases/cancel_incident_usecase.dart';

class IncidentsViewModel extends ChangeNotifier {
  final GetMyIncidentsUseCase _getMyIncidentsUseCase;
  final CreateIncidentUseCase _createIncidentUseCase;
  final UpdateIncidentUseCase _updateIncidentUseCase;
  final CancelIncidentUseCase _cancelIncidentUseCase;

  List<Incident> _incidents = [];
  bool _isLoading = false;
  String? _errorMessage;

  IncidentsViewModel({
    required GetMyIncidentsUseCase getMyIncidentsUseCase,
    required CreateIncidentUseCase createIncidentUseCase,
    required UpdateIncidentUseCase updateIncidentUseCase,
    required CancelIncidentUseCase cancelIncidentUseCase,
  }) : _getMyIncidentsUseCase = getMyIncidentsUseCase,
       _createIncidentUseCase = createIncidentUseCase,
       _updateIncidentUseCase = updateIncidentUseCase,
       _cancelIncidentUseCase = cancelIncidentUseCase;

  List<Incident> get incidents => _incidents;
  List<Incident> get activeIncidents =>
      _incidents.where((i) => i.isActive).toList();
  List<Incident> get completedIncidents => _incidents
      .where((i) => i.status == 'COMPLETED' || i.status == 'CANCELLED')
      .toList();
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadIncidents() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _incidents = await _getMyIncidentsUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> createIncident(CreateIncidentParams params) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final newIncident = await _createIncidentUseCase.execute(params);
      _incidents.insert(0, newIncident);
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

  Future<bool> updateIncident(
    String incidentId,
    UpdateIncidentParams params,
  ) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final updatedIncident = await _updateIncidentUseCase.execute(
        incidentId,
        params,
      );
      final index = _incidents.indexWhere((i) => i.id == incidentId);
      if (index != -1) {
        _incidents[index] = updatedIncident;
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

  Future<bool> cancelIncident(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      await _cancelIncidentUseCase.execute(incidentId);
      await loadIncidents(); // Recargar para obtener el estado actualizado
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
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
