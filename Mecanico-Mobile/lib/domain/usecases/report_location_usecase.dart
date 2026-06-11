import '../entities/tracking.dart';

abstract class ReportLocationUseCase {
  Future<TrackingData> execute(String incidentId, ReportLocationParams params);
}

class ReportLocationParams {
  final double latitude;
  final double longitude;
  final double? accuracyMeters;
  final String technicianId;

  ReportLocationParams({
    required this.latitude,
    required this.longitude,
    this.accuracyMeters,
    required this.technicianId,
  });

  Map<String, dynamic> toJson() => {
    'latitude': latitude,
    'longitude': longitude,
    if (accuracyMeters != null) 'accuracy_meters': accuracyMeters,
    'technician_id': technicianId,
  };
}
