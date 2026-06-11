import '../entities/evidence.dart';

abstract class AddTextEvidenceUseCase {
  Future<Evidence> execute(AddTextEvidenceParams params);
}

class AddTextEvidenceParams {
  final String incidentId;
  final String description;
  final String textContent;

  AddTextEvidenceParams({
    required this.incidentId,
    required this.description,
    required this.textContent,
  });

  Map<String, dynamic> toJson() => {
    'description': description,
    'text_content': textContent,
    'evidence_type': 'TEXT',
  };
}
