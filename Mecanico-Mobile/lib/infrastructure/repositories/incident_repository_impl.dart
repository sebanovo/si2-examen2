import '../../domain/entities/incident.dart';
import '../../domain/usecases/get_my_incidents_usecase.dart';
import '../../domain/usecases/create_incident_usecase.dart';
import '../../domain/usecases/update_incident_usecase.dart';
import '../../domain/usecases/cancel_incident_usecase.dart';
import '../datasources/incident_remote_data_source.dart';

// Repositorio base
class IncidentRepository {
  final IncidentRemoteDataSource _dataSource;

  IncidentRepository(this._dataSource);

  Future<List<Incident>> getMyIncidents() async {
    final models = await _dataSource.getMyIncidents();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<Incident> createIncident(CreateIncidentParams params) async {
    final model = await _dataSource.createIncident(params.toJson());
    return model.toEntity();
  }

  Future<Incident> updateIncident(
    String incidentId,
    UpdateIncidentParams params,
  ) async {
    final model = await _dataSource.updateIncident(incidentId, params.toJson());
    return model.toEntity();
  }

  Future<void> cancelIncident(String incidentId) async {
    await _dataSource.cancelIncident(incidentId);
  }
}

// Implementación de UseCases
class GetMyIncidentsUseCaseImpl implements GetMyIncidentsUseCase {
  final IncidentRepository _repository;

  GetMyIncidentsUseCaseImpl(this._repository);

  @override
  Future<List<Incident>> execute() async {
    return await _repository.getMyIncidents();
  }
}

class CreateIncidentUseCaseImpl implements CreateIncidentUseCase {
  final IncidentRepository _repository;

  CreateIncidentUseCaseImpl(this._repository);

  @override
  Future<Incident> execute(CreateIncidentParams params) async {
    return await _repository.createIncident(params);
  }
}

class UpdateIncidentUseCaseImpl implements UpdateIncidentUseCase {
  final IncidentRepository _repository;

  UpdateIncidentUseCaseImpl(this._repository);

  @override
  Future<Incident> execute(
    String incidentId,
    UpdateIncidentParams params,
  ) async {
    return await _repository.updateIncident(incidentId, params);
  }
}

class CancelIncidentUseCaseImpl implements CancelIncidentUseCase {
  final IncidentRepository _repository;

  CancelIncidentUseCaseImpl(this._repository);

  @override
  Future<void> execute(String incidentId) async {
    await _repository.cancelIncident(incidentId);
  }
}
