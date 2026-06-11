import '../entities/provider_candidate.dart';

abstract class GetAvailableCandidatesUseCase {
  Future<List<ProviderCandidate>> execute();
}