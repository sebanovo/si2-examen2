import '../../domain/entities/incident.dart';
import '../../domain/entities/user.dart';
import '../../domain/entities/vehicle.dart';

class IncidentModel {
  final String id;
  final String clientUserId;
  final String? vehicleId;
  final String? providerId;
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
  final double? estimatedPriceMin;
  final double? estimatedPriceMax;
  final String? aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;
  final double? responderLastLatitude;
  final double? responderLastLongitude;
  final double? routeDistanceKm;
  final int? routeEtaMinutes;
  final DateTime? requestedAt;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final DateTime createdAt;
  final DateTime updatedAt;
  final Vehicle? vehicle;
  final User? clientUser;
  final ProviderInfoModel? provider;
  final TechnicianInfoModel? assignedTechnician;

  IncidentModel({
    required this.id,
    required this.clientUserId,
    this.vehicleId,
    this.providerId,
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
    this.estimatedPriceMin,
    this.estimatedPriceMax,
    this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
    this.responderLastLatitude,
    this.responderLastLongitude,
    this.routeDistanceKm,
    this.routeEtaMinutes,
    this.requestedAt,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    required this.createdAt,
    required this.updatedAt,
    this.vehicle,
    this.clientUser,
    this.provider,
    this.assignedTechnician,
  });

  factory IncidentModel.fromJson(Map<String, dynamic> json) {
    return IncidentModel(
      id: _toStringOrFallback(json['id'], ''),
      clientUserId: _toStringOrFallback(json['client_user_id'], ''),
      vehicleId: json['vehicle_id'] as String?,
      providerId: json['provider_id'] as String?,
      assignedTechnicianId: json['assigned_technician_id'] as String?,
      dispatchMode: json['dispatch_mode'] as String?,
      status: _toStringOrFallback(json['status'], 'PENDING'),
      priority: _toStringOrFallback(json['priority'], 'MEDIUM'),
      reportedCategory: _toStringOrFallback(json['reported_category'], 'OTHER'),
      title: _toStringOrFallback(json['title'], 'Sin título'),
      description: _toStringOrFallback(json['description'], 'Sin descripción'),
      clientContactPhoneSnapshot:
          json['client_contact_phone_snapshot'] as String?,
      incidentLatitude: (json['incident_latitude'] as num?)?.toDouble(),
      incidentLongitude: (json['incident_longitude'] as num?)?.toDouble(),
      addressReference: json['address_reference'] as String?,
      estimatedPriceMin: (json['estimated_price_min'] as num?)?.toDouble(),
      estimatedPriceMax: (json['estimated_price_max'] as num?)?.toDouble(),
      aiSummaryStatus: json['ai_summary_status'] as String?,
      structuredSummary: json['structured_summary'] as String?,
      suggestedCategory: json['suggested_category'] as String?,
      suggestedPriority: json['suggested_priority'] as String?,
      requiresMoreInformation:
          json['requires_more_information'] as bool? ?? false,
      responderLastLatitude: (json['responder_last_latitude'] as num?)
          ?.toDouble(),
      responderLastLongitude: (json['responder_last_longitude'] as num?)
          ?.toDouble(),
      routeDistanceKm: (json['route_distance_km'] as num?)?.toDouble(),
      routeEtaMinutes: json['route_eta_minutes'] as int?,
      requestedAt: json['requested_at'] != null
          ? DateTime.tryParse(json['requested_at'] as String)
          : null,
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
      createdAt: json['created_at'] != null
          ? DateTime.parse(json['created_at'] as String)
          : DateTime.now(),
      updatedAt: json['updated_at'] != null
          ? DateTime.parse(json['updated_at'] as String)
          : DateTime.now(),
      vehicle: json['vehicle'] != null ? _parseVehicle(json['vehicle']) : null,
      clientUser: json['client_user'] != null
          ? _parseUser(json['client_user'])
          : null,
      provider: json['provider'] != null
          ? ProviderInfoModel.fromJson(json['provider'])
          : null,
      assignedTechnician: json['assigned_technician'] != null
          ? TechnicianInfoModel.fromJson(json['assigned_technician'])
          : null,
    );
  }

  // Función auxiliar para manejar nulls
  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  static Vehicle _parseVehicle(Map<String, dynamic> json) {
    return Vehicle(
      id: _toStringOrFallback(json['id'], ''),
      ownerUserId: _toStringOrFallback(json['owner_user_id'], ''),
      plateNumber: _toStringOrFallback(json['plate_number'], ''),
      vehicleType: _toStringOrFallback(json['vehicle_type'], 'CAR'),
      brand: _toStringOrFallback(json['brand'], ''),
      model: _toStringOrFallback(json['model'], ''),
      year: json['year'] as int? ?? 0,
      color: _toStringOrFallback(json['color'], ''),
      notes: json['notes'] ?? '',
      isActive: json['is_active'] as bool? ?? true,
    );
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
      roleCodes: json['role_codes'] != null
          ? List<String>.from(json['role_codes'] as List)
          : [],
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'] as String)
          : null,
      updatedAt: json['updated_at'] != null
          ? DateTime.tryParse(json['updated_at'] as String)
          : null,
    );
  }

  Incident toEntity() {
    return Incident(
      id: id,
      clientUserId: clientUserId,
      vehicleId: vehicleId,
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
      estimatedPriceMin: estimatedPriceMin,
      estimatedPriceMax: estimatedPriceMax,
      aiSummaryStatus: aiSummaryStatus,
      structuredSummary: structuredSummary,
      suggestedCategory: suggestedCategory,
      suggestedPriority: suggestedPriority,
      requiresMoreInformation: requiresMoreInformation,
      responderLastLatitude: responderLastLatitude,
      responderLastLongitude: responderLastLongitude,
      routeDistanceKm: routeDistanceKm,
      routeEtaMinutes: routeEtaMinutes,
      requestedAt: requestedAt,
      assignedAt: assignedAt,
      enRouteAt: enRouteAt,
      arrivedAt: arrivedAt,
      startedAt: startedAt,
      completedAt: completedAt,
      cancelledAt: cancelledAt,
      createdAt: createdAt,
      updatedAt: updatedAt,
      vehicle: vehicle,
      clientUser: clientUser,
      provider: provider?.toEntity(),
      assignedTechnician: assignedTechnician?.toEntity(),
    );
  }
}

// ProviderInfoModel y TechnicianInfoModel (sin cambios significativos)
class ProviderInfoModel {
  final String id;
  final String providerType;
  final String businessName;
  final String? contactPhone;
  final String? city;
  final bool isAvailable;
  final double averageRating;

  ProviderInfoModel({
    required this.id,
    required this.providerType,
    required this.businessName,
    this.contactPhone,
    this.city,
    required this.isAvailable,
    required this.averageRating,
  });

  factory ProviderInfoModel.fromJson(Map<String, dynamic> json) {
    return ProviderInfoModel(
      id: _toStringOrFallback(json['id'], ''),
      providerType: _toStringOrFallback(json['provider_type'], 'WORKSHOP'),
      businessName: _toStringOrFallback(json['business_name'], ''),
      contactPhone: json['contact_phone'] as String?,
      city: json['city'] as String?,
      isAvailable: json['is_available'] as bool? ?? false,
      averageRating: (json['average_rating'] as num?)?.toDouble() ?? 0.0,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  ProviderInfo toEntity() => ProviderInfo(
    id: id,
    providerType: providerType,
    businessName: businessName,
    contactPhone: contactPhone,
    city: city,
    isAvailable: isAvailable,
    averageRating: averageRating,
  );
}

class TechnicianInfoModel {
  final String id;
  final String providerId;
  final String firstName;
  final String lastName;
  final String? phoneNumber;
  final String? specialty;
  final bool isActive;
  final bool isAvailable;

  TechnicianInfoModel({
    required this.id,
    required this.providerId,
    required this.firstName,
    required this.lastName,
    this.phoneNumber,
    this.specialty,
    required this.isActive,
    required this.isAvailable,
  });

  factory TechnicianInfoModel.fromJson(Map<String, dynamic> json) {
    return TechnicianInfoModel(
      id: _toStringOrFallback(json['id'], ''),
      providerId: _toStringOrFallback(json['provider_id'], ''),
      firstName: _toStringOrFallback(json['first_name'], ''),
      lastName: _toStringOrFallback(json['last_name'], ''),
      phoneNumber: json['phone_number'] as String?,
      specialty: json['specialty'] as String?,
      isActive: json['is_active'] as bool? ?? true,
      isAvailable: json['is_available'] as bool? ?? false,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  TechnicianInfo toEntity() => TechnicianInfo(
    id: id,
    providerId: providerId,
    firstName: firstName,
    lastName: lastName,
    phoneNumber: phoneNumber,
    specialty: specialty,
    isActive: isActive,
    isAvailable: isAvailable,
  );
}
