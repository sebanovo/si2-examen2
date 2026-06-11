import '../entities/provider_operation.dart';

abstract class CompleteServiceUseCase {
  Future<ProviderOperation> execute(String incidentId, CompleteParams params);
}

class CompleteParams {
  final String? note;
  final String completionSummary;

  CompleteParams({this.note, required this.completionSummary});

  Map<String, dynamic> toJson() => {
    if (note != null) 'note': note,
    'completion_summary': completionSummary,
  };
}
