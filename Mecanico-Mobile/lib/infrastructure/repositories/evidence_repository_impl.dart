import '../../domain/entities/evidence.dart';
import '../../domain/usecases/add_text_evidence_usecase.dart';
import '../../domain/usecases/add_file_evidence_usecase.dart';
import '../datasources/evidence_remote_data_source.dart';

class EvidenceRepository {
  final EvidenceRemoteDataSource _dataSource;

  EvidenceRepository(this._dataSource);

  Future<Evidence> addTextEvidence(
    String incidentId,
    AddTextEvidenceParams params,
  ) async {
    final model = await _dataSource.addTextEvidence(
      incidentId,
      params.toJson(),
    );
    return model.toEntity();
  }

  Future<Evidence> addFileEvidence(
    String incidentId,
    AddFileEvidenceParams params,
  ) async {
    // ✅ Pasar el XFile directamente
    final model = await _dataSource.addFileEvidence(
      incidentId,
      params.evidenceType,
      params.description,
      params.file, // Esto es XFile
    );
    return model.toEntity();
  }
}

class AddTextEvidenceUseCaseImpl implements AddTextEvidenceUseCase {
  final EvidenceRepository _repository;

  AddTextEvidenceUseCaseImpl(this._repository);

  @override
  Future<Evidence> execute(AddTextEvidenceParams params) async {
    return await _repository.addTextEvidence(params.incidentId, params);
  }
}

class AddFileEvidenceUseCaseImpl implements AddFileEvidenceUseCase {
  final EvidenceRepository _repository;

  AddFileEvidenceUseCaseImpl(this._repository);

  @override
  Future<Evidence> execute(AddFileEvidenceParams params) async {
    return await _repository.addFileEvidence(params.incidentId, params);
  }
}
