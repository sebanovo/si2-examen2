import 'package:flutter/material.dart';
import '../../domain/entities/provider_operation.dart';
import '../../domain/usecases/get_active_operations_usecase.dart';
import '../../domain/usecases/get_operation_state_usecase.dart';
import '../../domain/usecases/dispatch_incident_usecase.dart';
import '../../domain/usecases/mark_arrived_usecase.dart';
import '../../domain/usecases/start_service_usecase.dart';
import '../../domain/usecases/complete_service_usecase.dart';
import '../../domain/usecases/cancel_service_usecase.dart';

class ProviderOperationViewModel extends ChangeNotifier {
  final GetActiveOperationsUseCase _getActiveOperationsUseCase;
  final GetOperationStateUseCase _getOperationStateUseCase;
  final DispatchIncidentUseCase _dispatchIncidentUseCase;
  final MarkArrivedUseCase _markArrivedUseCase;
  final StartServiceUseCase _startServiceUseCase;
  final CompleteServiceUseCase _completeServiceUseCase;
  final CancelServiceUseCase _cancelServiceUseCase;

  List<ProviderOperation> _operations = [];
  ProviderOperation? _selectedOperation;
  bool _isLoading = false;
  String? _errorMessage;

  ProviderOperationViewModel({
    required GetActiveOperationsUseCase getActiveOperationsUseCase,
    required GetOperationStateUseCase getOperationStateUseCase,
    required DispatchIncidentUseCase dispatchIncidentUseCase,
    required MarkArrivedUseCase markArrivedUseCase,
    required StartServiceUseCase startServiceUseCase,
    required CompleteServiceUseCase completeServiceUseCase,
    required CancelServiceUseCase cancelServiceUseCase,
  }) : _getActiveOperationsUseCase = getActiveOperationsUseCase,
       _getOperationStateUseCase = getOperationStateUseCase,
       _dispatchIncidentUseCase = dispatchIncidentUseCase,
       _markArrivedUseCase = markArrivedUseCase,
       _startServiceUseCase = startServiceUseCase,
       _completeServiceUseCase = completeServiceUseCase,
       _cancelServiceUseCase = cancelServiceUseCase;

  List<ProviderOperation> get operations => _operations;
  ProviderOperation? get selectedOperation => _selectedOperation;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadActiveOperations() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _operations = await _getActiveOperationsUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadOperationState(String incidentId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _selectedOperation = await _getOperationStateUseCase.execute(incidentId);
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<ProviderOperation?> dispatchIncident(
    String incidentId,
    String technicianId, {
    String? note,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = DispatchParams(technicianId: technicianId, note: note);
      final result = await _dispatchIncidentUseCase.execute(incidentId, params);

      // Actualizar en la lista
      final index = _operations.indexWhere((op) => op.incidentId == incidentId);
      if (index != -1) {
        _operations[index] = result;
      }
      if (_selectedOperation?.incidentId == incidentId) {
        _selectedOperation = result;
      }

      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  Future<ProviderOperation?> markArrived(
    String incidentId, {
    String? note,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final result = await _markArrivedUseCase.execute(incidentId, note: note);

      final index = _operations.indexWhere((op) => op.incidentId == incidentId);
      if (index != -1) {
        _operations[index] = result;
      }
      if (_selectedOperation?.incidentId == incidentId) {
        _selectedOperation = result;
      }

      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  Future<ProviderOperation?> startService(
    String incidentId, {
    String? note,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final result = await _startServiceUseCase.execute(incidentId, note: note);

      final index = _operations.indexWhere((op) => op.incidentId == incidentId);
      if (index != -1) {
        _operations[index] = result;
      }
      if (_selectedOperation?.incidentId == incidentId) {
        _selectedOperation = result;
      }

      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  Future<ProviderOperation?> completeService(
    String incidentId,
    String completionSummary, {
    String? note,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = CompleteParams(
        note: note,
        completionSummary: completionSummary,
      );
      final result = await _completeServiceUseCase.execute(incidentId, params);

      final index = _operations.indexWhere((op) => op.incidentId == incidentId);
      if (index != -1) {
        _operations[index] = result;
      }
      if (_selectedOperation?.incidentId == incidentId) {
        _selectedOperation = result;
      }

      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  Future<ProviderOperation?> cancelService(
    String incidentId, {
    String? note,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final result = await _cancelServiceUseCase.execute(
        incidentId,
        note: note,
      );

      final index = _operations.indexWhere((op) => op.incidentId == incidentId);
      if (index != -1) {
        _operations.removeAt(index);
      }
      if (_selectedOperation?.incidentId == incidentId) {
        _selectedOperation = result;
      }

      notifyListeners();
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return null;
    } finally {
      _setLoading(false);
    }
  }

  void clearSelectedOperation() {
    _selectedOperation = null;
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
