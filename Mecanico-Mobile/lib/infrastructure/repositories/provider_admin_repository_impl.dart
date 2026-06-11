import '../../domain/entities/provider_summary.dart';
import '../../domain/usecases/get_providers_usecase.dart';
import '../datasources/provider_admin_remote_data_source.dart';

class ProviderAdminRepository {
  final ProviderAdminRemoteDataSource _dataSource;

  ProviderAdminRepository(this._dataSource);

  Future<List<ProviderSummary>> getProviders({
    int limit = 50,
    int offset = 0,
  }) async {
    final models = await _dataSource.getProviders(limit: limit, offset: offset);
    return models.map((model) => model.toEntity()).toList();
  }
}

// Implementación de UseCase
class GetProvidersUseCaseImpl implements GetProvidersUseCase {
  final ProviderAdminRepository _repository;

  GetProvidersUseCaseImpl(this._repository);

  @override
  Future<List<ProviderSummary>> execute({
    int limit = 50,
    int offset = 0,
  }) async {
    return await _repository.getProviders(limit: limit, offset: offset);
  }
}
