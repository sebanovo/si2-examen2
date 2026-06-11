import '../entities/provider_candidate.dart';

abstract class GetCandidateDetailsUseCase {
  Future<ProviderCandidate> execute(String candidateId);
}