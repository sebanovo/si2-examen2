import '../../domain/entities/admin_incident.dart';
import '../../domain/usecases/get_all_incidents_usecase.dart';
import '../../domain/usecases/get_incident_details_usecase.dart';
import '../../domain/usecases/get_incident_candidates_usecase.dart';
import '../../domain/usecases/publish_incident_usecase.dart';
import '../datasources/admin_incident_remote_data_source.dart';

// Repositorio base
class AdminIncidentRepository {
  final AdminIncidentRemoteDataSource _dataSource;

  AdminIncidentRepository(this._dataSource);

  Future<List<AdminIncident>> getAllIncidents() async {
    final models = await _dataSource.getAllIncidents();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<AdminIncident> getIncidentDetails(String incidentId) async {
    final model = await _dataSource.getIncidentDetails(incidentId);
    return model.toEntity();
  }

  Future<List<Candidate>> getIncidentCandidates(String incidentId) async {
    final models = await _dataSource.getIncidentCandidates(incidentId);
    return models.map((model) => model.toEntity()).toList();
  }

  Future<AdminIncident> publishIncident(String incidentId) async {
    final model = await _dataSource.publishIncident(incidentId);
    return model.toEntity();
  }
}

// Implementación de UseCases
class GetAllIncidentsUseCaseImpl implements GetAllIncidentsUseCase {
  final AdminIncidentRepository _repository;

  GetAllIncidentsUseCaseImpl(this._repository);

  @override
  Future<List<AdminIncident>> execute() async {
    return await _repository.getAllIncidents();
  }
}

class GetIncidentDetailsUseCaseImpl implements GetIncidentDetailsUseCase {
  final AdminIncidentRepository _repository;

  GetIncidentDetailsUseCaseImpl(this._repository);

  @override
  Future<AdminIncident> execute(String incidentId) async {
    return await _repository.getIncidentDetails(incidentId);
  }
}

class GetIncidentCandidatesUseCaseImpl implements GetIncidentCandidatesUseCase {
  final AdminIncidentRepository _repository;

  GetIncidentCandidatesUseCaseImpl(this._repository);

  @override
  Future<List<Candidate>> execute(String incidentId) async {
    return await _repository.getIncidentCandidates(incidentId);
  }
}

class PublishIncidentUseCaseImpl implements PublishIncidentUseCase {
  final AdminIncidentRepository _repository;

  PublishIncidentUseCaseImpl(this._repository);

  @override
  Future<AdminIncident> execute(String incidentId) async {
    return await _repository.publishIncident(incidentId);
  }
}
