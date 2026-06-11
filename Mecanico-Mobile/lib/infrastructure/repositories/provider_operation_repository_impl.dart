import '../../domain/entities/provider_operation.dart';
import '../../domain/usecases/get_active_operations_usecase.dart';
import '../../domain/usecases/get_operation_state_usecase.dart';
import '../../domain/usecases/dispatch_incident_usecase.dart';
import '../../domain/usecases/mark_arrived_usecase.dart';
import '../../domain/usecases/start_service_usecase.dart';
import '../../domain/usecases/complete_service_usecase.dart';
import '../../domain/usecases/cancel_service_usecase.dart';
import '../datasources/provider_operation_remote_data_source.dart';

class ProviderOperationRepository {
  final ProviderOperationRemoteDataSource _dataSource;

  ProviderOperationRepository(this._dataSource);

  Future<List<ProviderOperation>> getActiveOperations() async {
    final models = await _dataSource.getActiveOperations();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<ProviderOperation> getOperationState(String incidentId) async {
    final model = await _dataSource.getOperationState(incidentId);
    return model.toEntity();
  }

  Future<ProviderOperation> dispatchIncident(
    String incidentId,
    DispatchParams params,
  ) async {
    final model = await _dataSource.dispatchIncident(
      incidentId,
      params.toJson(),
    );
    return model.toEntity();
  }

  Future<ProviderOperation> markArrived(
    String incidentId, {
    String? note,
  }) async {
    final model = await _dataSource.markArrived(incidentId, note: note);
    return model.toEntity();
  }

  Future<ProviderOperation> startService(
    String incidentId, {
    String? note,
  }) async {
    final model = await _dataSource.startService(incidentId, note: note);
    return model.toEntity();
  }

  Future<ProviderOperation> completeService(
    String incidentId,
    CompleteParams params,
  ) async {
    final model = await _dataSource.completeService(
      incidentId,
      params.toJson(),
    );
    return model.toEntity();
  }

  Future<ProviderOperation> cancelService(
    String incidentId, {
    String? note,
  }) async {
    final model = await _dataSource.cancelService(incidentId, note: note);
    return model.toEntity();
  }
}

// Implementación de UseCases
class GetActiveOperationsUseCaseImpl implements GetActiveOperationsUseCase {
  final ProviderOperationRepository _repository;

  GetActiveOperationsUseCaseImpl(this._repository);

  @override
  Future<List<ProviderOperation>> execute() async {
    return await _repository.getActiveOperations();
  }
}

class GetOperationStateUseCaseImpl implements GetOperationStateUseCase {
  final ProviderOperationRepository _repository;

  GetOperationStateUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(String incidentId) async {
    return await _repository.getOperationState(incidentId);
  }
}

class DispatchIncidentUseCaseImpl implements DispatchIncidentUseCase {
  final ProviderOperationRepository _repository;

  DispatchIncidentUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(
    String incidentId,
    DispatchParams params,
  ) async {
    return await _repository.dispatchIncident(incidentId, params);
  }
}

class MarkArrivedUseCaseImpl implements MarkArrivedUseCase {
  final ProviderOperationRepository _repository;

  MarkArrivedUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(String incidentId, {String? note}) async {
    return await _repository.markArrived(incidentId, note: note);
  }
}

class StartServiceUseCaseImpl implements StartServiceUseCase {
  final ProviderOperationRepository _repository;

  StartServiceUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(String incidentId, {String? note}) async {
    return await _repository.startService(incidentId, note: note);
  }
}

class CompleteServiceUseCaseImpl implements CompleteServiceUseCase {
  final ProviderOperationRepository _repository;

  CompleteServiceUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(
    String incidentId,
    CompleteParams params,
  ) async {
    return await _repository.completeService(incidentId, params);
  }
}

class CancelServiceUseCaseImpl implements CancelServiceUseCase {
  final ProviderOperationRepository _repository;

  CancelServiceUseCaseImpl(this._repository);

  @override
  Future<ProviderOperation> execute(String incidentId, {String? note}) async {
    return await _repository.cancelService(incidentId, note: note);
  }
}
