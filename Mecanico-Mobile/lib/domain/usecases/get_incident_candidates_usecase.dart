import '../entities/admin_incident.dart';

abstract class GetIncidentCandidatesUseCase {
  Future<List<Candidate>> execute(String incidentId);
}
