import '../entities/technician.dart';

abstract class GetTechniciansUseCase {
  Future<List<Technician>> execute();
}
