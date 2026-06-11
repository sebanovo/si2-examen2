import '../entities/provider_operation.dart';

abstract class GetOperationStateUseCase {
  Future<ProviderOperation> execute(String incidentId);
}
