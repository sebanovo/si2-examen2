import '../../domain/entities/catalog_service.dart';
import '../../domain/usecases/get_catalog_services_usecase.dart';
import '../../domain/usecases/get_provider_services_usecase.dart';
import '../../domain/usecases/create_provider_service_usecase.dart';
import '../datasources/catalog_remote_data_source.dart';

class CatalogRepository {
  final CatalogRemoteDataSource _dataSource;

  CatalogRepository(this._dataSource);

  Future<List<CatalogServiceEntry>> getCatalogServices() async {
    final models = await _dataSource.getCatalogServices();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<List<ProviderService>> getProviderServices() async {
    final models = await _dataSource.getProviderServices();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<ProviderService> createProviderService(CreateProviderServiceParams params) async {
    final model = await _dataSource.createProviderService(params.toJson());
    return model.toEntity();
  }
}

// Implementación de UseCases
class GetCatalogServicesUseCaseImpl implements GetCatalogServicesUseCase {
  final CatalogRepository _repository;

  GetCatalogServicesUseCaseImpl(this._repository);

  @override
  Future<List<CatalogServiceEntry>> execute() async {
    return await _repository.getCatalogServices();
  }
}

class GetProviderServicesUseCaseImpl implements GetProviderServicesUseCase {
  final CatalogRepository _repository;

  GetProviderServicesUseCaseImpl(this._repository);

  @override
  Future<List<ProviderService>> execute() async {
    return await _repository.getProviderServices();
  }
}

class CreateProviderServiceUseCaseImpl implements CreateProviderServiceUseCase {
  final CatalogRepository _repository;

  CreateProviderServiceUseCaseImpl(this._repository);

  @override
  Future<ProviderService> execute(CreateProviderServiceParams params) async {
    return await _repository.createProviderService(params);
  }
}