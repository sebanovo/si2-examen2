import 'package:mechanic_mobile/domain/usecases/get_technicians_usecase.dart';
import 'package:mechanic_mobile/infrastructure/datasources/technician_datasource.dart';
import '../../domain/entities/technician.dart';
import '../../domain/usecases/create_technician_usecase.dart';
import '../../domain/usecases/update_technician_usecase.dart';

class TechnicianRepository {
  final TechnicianRemoteDataSource _dataSource;

  TechnicianRepository(this._dataSource);

  Future<Technician> createTechnician(CreateTechnicianParams params) async {
    final model = await _dataSource.createTechnician(params.toJson());
    return model.toEntity();
  }

  Future<List<Technician>> getTechnicians() async {
    final models = await _dataSource.getTechnicians();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<Technician> updateTechnician(
    String technicianId,
    UpdateTechnicianParams params,
  ) async {
    final model = await _dataSource.updateTechnician(
      technicianId,
      params.toJson(),
    );
    return model.toEntity();
  }
}

// Implementación del UseCase para crear
class CreateTechnicianUseCaseImpl implements CreateTechnicianUseCase {
  final TechnicianRepository _repository;

  CreateTechnicianUseCaseImpl(this._repository);

  @override
  Future<Technician> execute(CreateTechnicianParams params) async {
    return await _repository.createTechnician(params);
  }
}

// Implementación del UseCase para listar
class GetTechniciansUseCaseImpl implements GetTechniciansUseCase {
  final TechnicianRepository _repository;

  GetTechniciansUseCaseImpl(this._repository);

  @override
  Future<List<Technician>> execute() async {
    return await _repository.getTechnicians();
  }
}

// ✅ Nueva implementación del UseCase para actualizar
class UpdateTechnicianUseCaseImpl implements UpdateTechnicianUseCase {
  final TechnicianRepository _repository;

  UpdateTechnicianUseCaseImpl(this._repository);

  @override
  Future<Technician> execute(
    String technicianId,
    UpdateTechnicianParams params,
  ) async {
    return await _repository.updateTechnician(technicianId, params);
  }
}
