import '../entities/provider_summary.dart';

abstract class GetProvidersUseCase {
  Future<List<ProviderSummary>> execute({int limit = 50, int offset = 0});
}

class GetProvidersParams {
  final int limit;
  final int offset;

  GetProvidersParams({this.limit = 50, this.offset = 0});
}
