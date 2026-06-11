import '../entities/provider_operation.dart';

abstract class CancelServiceUseCase {
  Future<ProviderOperation> execute(String incidentId, {String? note});
}
