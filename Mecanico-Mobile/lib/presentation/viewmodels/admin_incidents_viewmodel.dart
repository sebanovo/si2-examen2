import 'package:flutter/material.dart';
import '../../domain/entities/admin_incident.dart';
import '../../domain/usecases/get_all_incidents_usecase.dart';
import '../../domain/usecases/get_incident_details_usecase.dart';
import '../../domain/usecases/get_incident_candidates_usecase.dart';
import '../../domain/usecases/publish_incident_usecase.dart';

class AdminIncidentsViewModel extends ChangeNotifier {
  final GetAllIncidentsUseCase _getAllIncidentsUseCase;
  final GetIncidentDetailsUseCase _getIncidentDetailsUseCase;
  final GetIncidentCandidatesUseCase _getIncidentCandidatesUseCase;
  final PublishIncidentUseCase _publishIncidentUseCase;

  List<AdminIncident> _incidents = [];
  List<Candidate> _candidates = [];
  AdminIncident? _selectedIncident;
  bool _isLoading = false;
  String? _errorMessage;
  String _selectedTab = 'all';

  AdminIncidentsViewModel({
    required GetAllIncidentsUseCase getAllIncidentsUseCase,
    required GetIncidentDetailsUseCase getIncidentDetailsUseCase,
    required GetIncidentCandidatesUseCase getIncidentCandidatesUseCase,
    required PublishIncidentUseCase publishIncidentUseCase,
  }) : _getAllIncidentsUseCase = getAllIncidentsUseCase,
       _getIncidentDetailsUseCase = getIncidentDetailsUseCase,
       _getIncidentCandidatesUseCase = getIncidentCandidatesUseCase,
       _publishIncidentUseCase = publishIncidentUseCase;

  List<AdminIncident> get incidents => _incidents;
  List<Candidate> get candidates => _candidates;
  AdminIncident? get selectedIncident => _selectedIncident;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  String get selectedTab => _selectedTab;

  List<AdminIncident> get filteredIncidents {
    if (_selectedTab == 'all') return _incidents;
    if (_selectedTab == 'pending') {
      return _incidents.where((i) => i.status == 'PENDING').toList();
    }
    if (_selectedTab == 'published') {
      return _incidents.where((i) => i.status == 'PUBLISHED').toList();
    }
    if (_selectedTab == 'active') {
      return _incidents
          .where(
            (i) =>
                i.isActive && i.status != 'PENDING' && i.status != 'PUBLISHED',
          )
          .toList();
    }
    if (_selectedTab == 'completed') {
      return _incidents
          .where((i) => i.status == 'COMPLETED' || i.status == 'CANCELLED')
          .toList();
    }
    return _incidents;
  }

  Future<void> loadIncidents() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _incidents = await _getAllIncidentsUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadIncidentDetails(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _selectedIncident = await _getIncidentDetailsUseCase.execute(incidentId);
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadCandidates(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _candidates = await _getIncidentCandidatesUseCase.execute(incidentId);
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> publishIncident(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final updatedIncident = await _publishIncidentUseCase.execute(incidentId);

      // Actualizar en la lista
      final index = _incidents.indexWhere((i) => i.id == incidentId);
      if (index != -1) {
        _incidents[index] = updatedIncident;
      }
      if (_selectedIncident?.id == incidentId) {
        _selectedIncident = updatedIncident;
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

  void setSelectedTab(String tab) {
    _selectedTab = tab;
    notifyListeners();
  }

  void clearSelectedIncident() {
    _selectedIncident = null;
    _candidates = [];
    notifyListeners();
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
