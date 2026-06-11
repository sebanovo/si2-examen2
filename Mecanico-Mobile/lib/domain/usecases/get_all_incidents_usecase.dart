import '../entities/admin_incident.dart';

abstract class GetAllIncidentsUseCase {
  Future<List<AdminIncident>> execute();
}