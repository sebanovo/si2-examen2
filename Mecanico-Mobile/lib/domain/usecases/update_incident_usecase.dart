import '../entities/incident.dart';

abstract class UpdateIncidentUseCase {
  Future<Incident> execute(String incidentId, UpdateIncidentParams params);
}

class UpdateIncidentParams {
  final String? title;
  final String? description;
  final String? reportedCategory;
  final String? priority;
  final double? incidentLatitude;
  final double? incidentLongitude;
  final String? addressReference;

  UpdateIncidentParams({
    this.title,
    this.description,
    this.reportedCategory,
    this.priority,
    this.incidentLatitude,
    this.incidentLongitude,
    this.addressReference,
  });

  Map<String, dynamic> toJson() => {
    if (title != null) 'title': title,
    if (description != null) 'description': description,
    if (reportedCategory != null) 'reported_category': reportedCategory,
    if (priority != null) 'priority': priority,
    if (incidentLatitude != null) 'incident_latitude': incidentLatitude,
    if (incidentLongitude != null) 'incident_longitude': incidentLongitude,
    if (addressReference != null) 'address_reference': addressReference,
  };
}
