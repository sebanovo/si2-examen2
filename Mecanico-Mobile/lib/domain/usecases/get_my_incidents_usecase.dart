import '../entities/incident.dart';

abstract class GetMyIncidentsUseCase {
  Future<List<Incident>> execute();
}
