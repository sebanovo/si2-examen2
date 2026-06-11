import '../entities/incident.dart';

abstract class CreateIncidentUseCase {
  Future<Incident> execute(CreateIncidentParams params);
}

class CreateIncidentParams {
  final String vehicleId;
  final String title;
  final String description;
  final String reportedCategory;
  final String priority;
  final double incidentLatitude;
  final double incidentLongitude;
  final String addressReference;

  CreateIncidentParams({
    required this.vehicleId,
    required this.title,
    required this.description,
    required this.reportedCategory,
    required this.priority,
    required this.incidentLatitude,
    required this.incidentLongitude,
    required this.addressReference,
  });

  Map<String, dynamic> toJson() => {
    'vehicle_id': vehicleId,
    'title': title,
    'description': description,
    'reported_category': reportedCategory,
    'priority': priority,
    'incident_latitude': incidentLatitude,
    'incident_longitude': incidentLongitude,
    'address_reference': addressReference,
  };
}
