import '../entities/evidence.dart';

abstract class AddFileEvidenceUseCase {
  Future<Evidence> execute(AddFileEvidenceParams params);
}

class AddFileEvidenceParams {
  final String incidentId;
  final String evidenceType;
  final String description;
  final dynamic file;
  final String? fileName; // ✅ Agregar para web

  AddFileEvidenceParams({
    required this.incidentId,
    required this.evidenceType,
    required this.description,
    required this.file,
    this.fileName,
  });
}
