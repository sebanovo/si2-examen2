import '../entities/catalog_service.dart';

abstract class GetCatalogServicesUseCase {
  Future<List<CatalogServiceEntry>> execute();
}
