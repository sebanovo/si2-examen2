import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../../domain/entities/evidence.dart';
import '../../domain/usecases/add_text_evidence_usecase.dart';
import '../../domain/usecases/add_file_evidence_usecase.dart';

class EvidenceViewModel extends ChangeNotifier {
  final AddTextEvidenceUseCase _addTextEvidenceUseCase;
  final AddFileEvidenceUseCase _addFileEvidenceUseCase;

  bool _isLoading = false;
  String? _errorMessage;
  Evidence? _lastAddedEvidence;

  EvidenceViewModel({
    required AddTextEvidenceUseCase addTextEvidenceUseCase,
    required AddFileEvidenceUseCase addFileEvidenceUseCase,
  }) : _addTextEvidenceUseCase = addTextEvidenceUseCase,
       _addFileEvidenceUseCase = addFileEvidenceUseCase;

  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  Evidence? get lastAddedEvidence => _lastAddedEvidence;

  Future<bool> addTextEvidence({
    required String incidentId,
    required String description,
    required String textContent,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = AddTextEvidenceParams(
        incidentId: incidentId,
        description: description,
        textContent: textContent,
      );
      _lastAddedEvidence = await _addTextEvidenceUseCase.execute(params);
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

  // ✅ Recibir XFile directamente
  Future<bool> addImageEvidence({
    required String incidentId,
    required String description,
    required XFile imageFile,
  }) async {
    _setLoading(true);
    _errorMessage = null;

    try {
      final params = AddFileEvidenceParams(
        incidentId: incidentId,
        evidenceType: 'IMAGE',
        description: description,
        file: imageFile,
      );
      _lastAddedEvidence = await _addFileEvidenceUseCase.execute(params);
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

  void _setLoading(bool loading) {
    _isLoading = loading;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }

  void clearLastEvidence() {
    _lastAddedEvidence = null;
    notifyListeners();
  }
}
