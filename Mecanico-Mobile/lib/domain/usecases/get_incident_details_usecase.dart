import '../entities/admin_incident.dart';

abstract class GetIncidentDetailsUseCase {
  Future<AdminIncident> execute(String incidentId);
}