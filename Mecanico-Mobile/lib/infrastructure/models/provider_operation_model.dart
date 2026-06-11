import '../../domain/entities/provider_operation.dart';
import '../../domain/entities/user.dart';
import '../../domain/entities/technician.dart';

class ProviderOperationModel {
  final String incidentId;
  final String providerId;
  final String? assignedTechnicianId;
  final String? dispatchMode;
  final String status;
  final String priority;
  final String reportedCategory;
  final String title;
  final String description;
  final String? clientContactPhoneSnapshot;
  final double? incidentLatitude;
  final double? incidentLongitude;
  final String? addressReference;
  final String? aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final User? clientUser;
  final Technician? assignedTechnician;

  ProviderOperationModel({
    required this.incidentId,
    required this.providerId,
    this.assignedTechnicianId,
    this.dispatchMode,
    required this.status,
    required this.priority,
    required this.reportedCategory,
    required this.title,
    required this.description,
    this.clientContactPhoneSnapshot,
    this.incidentLatitude,
    this.incidentLongitude,
    this.addressReference,
    this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    this.clientUser,
    this.assignedTechnician,
  });

  factory ProviderOperationModel.fromJson(Map<String, dynamic> json) {
    return ProviderOperationModel(
      incidentId: _toStringOrFallback(json['incident_id'], ''),
      providerId: _toStringOrFallback(json['provider_id'], ''),
      assignedTechnicianId: json['assigned_technician_id'] as String?,
      dispatchMode: json['dispatch_mode'] as String?,
      status: _toStringOrFallback(json['status'], 'ASSIGNED'),
      priority: _toStringOrFallback(json['priority'], 'MEDIUM'),
      reportedCategory: _toStringOrFallback(json['reported_category'], 'OTHER'),
      title: _toStringOrFallback(json['title'], ''),
      description: _toStringOrFallback(json['description'], ''),
      clientContactPhoneSnapshot:
          json['client_contact_phone_snapshot'] as String?,
      incidentLatitude: (json['incident_latitude'] as num?)?.toDouble(),
      incidentLongitude: (json['incident_longitude'] as num?)?.toDouble(),
      addressReference: json['address_reference'] as String?,
      aiSummaryStatus: json['ai_summary_status'] as String?,
      structuredSummary: json['structured_summary'] as String?,
      suggestedCategory: json['suggested_category'] as String?,
      suggestedPriority: json['suggested_priority'] as String?,
      requiresMoreInformation:
          json['requires_more_information'] as bool? ?? false,
      assignedAt: json['assigned_at'] != null
          ? DateTime.tryParse(json['assigned_at'] as String)
          : null,
      enRouteAt: json['en_route_at'] != null
          ? DateTime.tryParse(json['en_route_at'] as String)
          : null,
      arrivedAt: json['arrived_at'] != null
          ? DateTime.tryParse(json['arrived_at'] as String)
          : null,
      startedAt: json['started_at'] != null
          ? DateTime.tryParse(json['started_at'] as String)
          : null,
      completedAt: json['completed_at'] != null
          ? DateTime.tryParse(json['completed_at'] as String)
          : null,
      cancelledAt: json['cancelled_at'] != null
          ? DateTime.tryParse(json['cancelled_at'] as String)
          : null,
      clientUser: json['client_user'] != null
          ? _parseUser(json['client_user'])
          : null,
      assignedTechnician: json['assigned_technician'] != null
          ? _parseTechnician(json['assigned_technician'])
          : null,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  static User _parseUser(Map<String, dynamic> json) {
    return User(
      id: _toStringOrFallback(json['id'], ''),
      email: _toStringOrFallback(json['email'], ''),
      fullName: _toStringOrFallback(json['full_name'], ''),
      firstName: json['first_name'] as String?,
      lastName: json['last_name'] as String?,
      phoneNumber: json['phone_number'] as String?,
      isActive: json['is_active'] as bool? ?? true,
      isSuperuser: json['is_superuser'] as bool? ?? false,
      roleCodes: [],
    );
  }

  static Technician _parseTechnician(Map<String, dynamic> json) {
    return Technician(
      id: _toStringOrFallback(json['id'], ''),
      firstName: _toStringOrFallback(json['first_name'], ''),
      lastName: _toStringOrFallback(json['last_name'], ''),
      phoneNumber: _toStringOrFallback(json['phone_number'], ''),
      specialty: json['specialty'] as String? ?? '',
      isAvailable: json['is_available'] as bool? ?? false,
      currentLatitude: (json['current_latitude'] as num?)?.toDouble(),
      currentLongitude: (json['current_longitude'] as num?)?.toDouble(),
    );
  }

  ProviderOperation toEntity() {
    return ProviderOperation(
      incidentId: incidentId,
      providerId: providerId,
      assignedTechnicianId: assignedTechnicianId,
      dispatchMode: dispatchMode,
      status: status,
      priority: priority,
      reportedCategory: reportedCategory,
      title: title,
      description: description,
      clientContactPhoneSnapshot: clientContactPhoneSnapshot,
      incidentLatitude: incidentLatitude,
      incidentLongitude: incidentLongitude,
      addressReference: addressReference,
      aiSummaryStatus: aiSummaryStatus,
      structuredSummary: structuredSummary,
      suggestedCategory: suggestedCategory,
      suggestedPriority: suggestedPriority,
      requiresMoreInformation: requiresMoreInformation,
      assignedAt: assignedAt,
      enRouteAt: enRouteAt,
      arrivedAt: arrivedAt,
      startedAt: startedAt,
      completedAt: completedAt,
      cancelledAt: cancelledAt,
      clientUser: clientUser,
      assignedTechnician: assignedTechnician,
    );
  }
}
