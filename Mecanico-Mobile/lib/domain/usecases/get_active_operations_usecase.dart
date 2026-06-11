import '../entities/provider_operation.dart';

abstract class GetActiveOperationsUseCase {
  Future<List<ProviderOperation>> execute();
}
