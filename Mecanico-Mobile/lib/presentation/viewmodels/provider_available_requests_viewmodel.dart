import 'package:flutter/material.dart';
import '../../domain/entities/provider_candidate.dart';
import '../../domain/usecases/get_available_candidates_usecase.dart';
import '../../domain/usecases/get_candidate_details_usecase.dart';
import '../../domain/usecases/accept_candidate_usecase.dart';
import '../../domain/usecases/reject_candidate_usecase.dart';

class ProviderAvailableRequestsViewModel extends ChangeNotifier {
  final GetAvailableCandidatesUseCase _getAvailableCandidatesUseCase;
  final GetCandidateDetailsUseCase _getCandidateDetailsUseCase;
  final RejectCandidateUseCase _rejectCandidateUseCase;

  List<ProviderCandidate> _candidates = [];
  ProviderCandidate? _selectedCandidate;
  bool _isLoading = false;
  String? _errorMessage;

  ProviderAvailableRequestsViewModel({
    required GetAvailableCandidatesUseCase getAvailableCandidatesUseCase,
    required GetCandidateDetailsUseCase getCandidateDetailsUseCase,
    required AcceptCandidateUseCase acceptCandidateUseCase,
    required RejectCandidateUseCase rejectCandidateUseCase,
  }) : _getAvailableCandidatesUseCase = getAvailableCandidatesUseCase,
       _getCandidateDetailsUseCase = getCandidateDetailsUseCase,
       _rejectCandidateUseCase = rejectCandidateUseCase;

  List<ProviderCandidate> get candidates => _candidates;
  ProviderCandidate? get selectedCandidate => _selectedCandidate;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  Future<void> loadAvailableCandidates() async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _candidates = await _getAvailableCandidatesUseCase.execute();
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<void> loadCandidateDetails(String candidateId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      _selectedCandidate = await _getCandidateDetailsUseCase.execute(
        candidateId,
      );
      notifyListeners();
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> acceptCandidate(String candidateId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      // Remover el candidato de la lista
      _candidates.removeWhere((c) => c.id == candidateId);
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
    } finally {
      _setLoading(false);
    }
  }

  Future<bool> rejectCandidate(String candidateId) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      await _rejectCandidateUseCase.execute(candidateId);
      // Remover el candidato de la lista
      _candidates.removeWhere((c) => c.id == candidateId);
      notifyListeners();
      return true;
    } catch (e) {
      _errorMessage = e.toString();
      notifyListeners();
      return false;
    } finally {
      _setLoading(false);
    }
  }

  void clearSelectedCandidate() {
    _selectedCandidate = null;
    notifyListeners();
  }

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }
}
