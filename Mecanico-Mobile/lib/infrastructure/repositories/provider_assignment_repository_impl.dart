import '../../domain/entities/provider_candidate.dart';
import '../../domain/usecases/get_available_candidates_usecase.dart';
import '../../domain/usecases/get_candidate_details_usecase.dart';
import '../../domain/usecases/accept_candidate_usecase.dart';
import '../../domain/usecases/reject_candidate_usecase.dart';
import '../datasources/provider_assignment_remote_data_source.dart';

class ProviderAssignmentRepository {
  final ProviderAssignmentRemoteDataSource _dataSource;

  ProviderAssignmentRepository(this._dataSource);

  Future<List<ProviderCandidate>> getAvailableCandidates() async {
    final models = await _dataSource.getAvailableCandidates();
    return models.map((model) => model.toEntity()).toList();
  }

  Future<ProviderCandidate> getCandidateDetails(String candidateId) async {
    final model = await _dataSource.getCandidateDetails(candidateId);
    return model.toEntity();
  }

  Future<Map<String, dynamic>> acceptCandidate(String candidateId) async {
    return await _dataSource.acceptCandidate(candidateId);
  }

  Future<void> rejectCandidate(String candidateId) async {
    await _dataSource.rejectCandidate(candidateId);
  }
}

// Implementación de UseCases
class GetAvailableCandidatesUseCaseImpl
    implements GetAvailableCandidatesUseCase {
  final ProviderAssignmentRepository _repository;

  GetAvailableCandidatesUseCaseImpl(this._repository);

  @override
  Future<List<ProviderCandidate>> execute() async {
    return await _repository.getAvailableCandidates();
  }
}

class GetCandidateDetailsUseCaseImpl implements GetCandidateDetailsUseCase {
  final ProviderAssignmentRepository _repository;

  GetCandidateDetailsUseCaseImpl(this._repository);

  @override
  Future<ProviderCandidate> execute(String candidateId) async {
    return await _repository.getCandidateDetails(candidateId);
  }
}

class AcceptCandidateUseCaseImpl implements AcceptCandidateUseCase {
  final ProviderAssignmentRepository _repository;

  AcceptCandidateUseCaseImpl(this._repository);

  @override
  Future<Map<String, dynamic>> execute(String candidateId) async {
    return await _repository.acceptCandidate(candidateId);
  }
}

class RejectCandidateUseCaseImpl implements RejectCandidateUseCase {
  final ProviderAssignmentRepository _repository;

  RejectCandidateUseCaseImpl(this._repository);

  @override
  Future<void> execute(String candidateId) async {
    await _repository.rejectCandidate(candidateId);
  }
}
