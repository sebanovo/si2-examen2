import '../../domain/entities/provider_profile.dart';
import '../../domain/usecases/get_provider_profile_usecase.dart';
import '../../domain/usecases/update_provider_profile_usecase.dart';
import '../datasources/provider_remote_data_source.dart';

class ProviderRepository {
  final ProviderRemoteDataSource _dataSource;

  ProviderRepository(this._dataSource);

  Future<ProviderProfile> getProviderProfile() async {
    final model = await _dataSource.getProviderProfile();
    return model.toEntity();
  }

  Future<ProviderProfile> updateProviderProfile(
    UpdateProviderProfileParams params,
  ) async {
    final model = await _dataSource.updateProviderProfile(params.toJson());
    return model.toEntity();
  }
}

// Implementación del UseCase para obtener perfil
class GetProviderProfileUseCaseImpl implements GetProviderProfileUseCase {
  final ProviderRepository _repository;

  GetProviderProfileUseCaseImpl(this._repository);

  @override
  Future<ProviderProfile> execute() async {
    return await _repository.getProviderProfile();
  }
}

// Implementación del UseCase para actualizar perfil
class UpdateProviderProfileUseCaseImpl implements UpdateProviderProfileUseCase {
  final ProviderRepository _repository;

  UpdateProviderProfileUseCaseImpl(this._repository);

  @override
  Future<ProviderProfile> execute(UpdateProviderProfileParams params) async {
    return await _repository.updateProviderProfile(params);
  }
}
