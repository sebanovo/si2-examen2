import '../entities/provider_operation.dart';

abstract class DispatchIncidentUseCase {
  Future<ProviderOperation> execute(String incidentId, DispatchParams params);
}

class DispatchParams {
  final String technicianId;
  final String? note;

  DispatchParams({required this.technicianId, this.note});

  Map<String, dynamic> toJson() => {
    'technician_id': technicianId,
    if (note != null) 'note': note,
  };
}
