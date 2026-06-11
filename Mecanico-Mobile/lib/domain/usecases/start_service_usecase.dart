import '../entities/provider_operation.dart';

abstract class StartServiceUseCase {
  Future<ProviderOperation> execute(String incidentId, {String? note});
}
