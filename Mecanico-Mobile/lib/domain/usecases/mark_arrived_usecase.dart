import '../entities/provider_operation.dart';

abstract class MarkArrivedUseCase {
  Future<ProviderOperation> execute(String incidentId, {String? note});
}
