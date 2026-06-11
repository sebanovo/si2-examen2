import '../entities/admin_incident.dart';

abstract class PublishIncidentUseCase {
  Future<AdminIncident> execute(String incidentId);
}
