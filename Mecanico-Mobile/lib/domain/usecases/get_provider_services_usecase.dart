import '../entities/catalog_service.dart';

abstract class GetProviderServicesUseCase {
  Future<List<ProviderService>> execute();
}