import 'package:mechanic_mobile/domain/entities/admin_incident.dart';

import '../../domain/entities/tracking.dart';
import '../../domain/entities/user.dart';
import '../../domain/entities/technician.dart';

class TrackingDataModel {
  final String incidentId;
  final String status;
  final String priority;
  final String title;
  final String description;
  final String? addressReference;
  final double? incidentLatitude;
  final double? incidentLongitude;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final ProviderInfoModel? provider;
  final Technician? assignedTechnician;
  final User? clientUser;
  final ResponderPositionModel? responderPosition;
  final RouteInfoModel? route;

  TrackingDataModel({
    required this.incidentId,
    required this.status,
    required this.priority,
    required this.title,
    required this.description,
    this.addressReference,
    this.incidentLatitude,
    this.incidentLongitude,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    this.provider,
    this.assignedTechnician,
    this.clientUser,
    this.responderPosition,
    this.route,
  });

  factory TrackingDataModel.fromJson(Map<String, dynamic> json) {
    return TrackingDataModel(
      incidentId: _toStringOrFallback(json['incident_id'], ''),
      status: _toStringOrFallback(json['status'], ''),
      priority: _toStringOrFallback(json['priority'], 'MEDIUM'),
      title: _toStringOrFallback(json['title'], ''),
      description: _toStringOrFallback(json['description'], ''),
      addressReference: json['address_reference'] as String?,
      incidentLatitude: (json['incident_latitude'] as num?)?.toDouble(),
      incidentLongitude: (json['incident_longitude'] as num?)?.toDouble(),
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
      provider: json['provider'] != null
          ? ProviderInfoModel.fromJson(json['provider'])
          : null,
      assignedTechnician: json['assigned_technician'] != null
          ? _parseTechnician(json['assigned_technician'])
          : null,
      clientUser: json['client_user'] != null
          ? _parseUser(json['client_user'])
          : null,
      responderPosition: json['responder_position'] != null
          ? ResponderPositionModel.fromJson(json['responder_position'])
          : null,
      route: json['route'] != null
          ? RouteInfoModel.fromJson(json['route'])
          : null,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
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

  TrackingData toEntity() {
    return TrackingData(
      incidentId: incidentId,
      status: status,
      priority: priority,
      title: title,
      description: description,
      addressReference: addressReference,
      incidentLatitude: incidentLatitude,
      incidentLongitude: incidentLongitude,
      assignedAt: assignedAt,
      enRouteAt: enRouteAt,
      arrivedAt: arrivedAt,
      startedAt: startedAt,
      completedAt: completedAt,
      cancelledAt: cancelledAt,
      provider: provider?.toEntity(),
      assignedTechnician: assignedTechnician,
      clientUser: clientUser,
      responderPosition: responderPosition?.toEntity(),
      route: route?.toEntity(),
    );
  }
}

class ProviderInfoModel {
  final String id;
  final String providerType;
  final String businessName;
  final String? contactPhone;
  final String? city;
  final double averageRating;

  ProviderInfoModel({
    required this.id,
    required this.providerType,
    required this.businessName,
    this.contactPhone,
    this.city,
    required this.averageRating,
  });

  factory ProviderInfoModel.fromJson(Map<String, dynamic> json) {
    return ProviderInfoModel(
      id: _toStringOrFallback(json['id'], ''),
      providerType: _toStringOrFallback(json['provider_type'], 'WORKSHOP'),
      businessName: _toStringOrFallback(json['business_name'], ''),
      contactPhone: json['contact_phone'] as String?,
      city: json['city'] as String?,
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
    isAvailable: true,
    averageRating: averageRating,
  );
}

class ResponderPositionModel {
  final double latitude;
  final double longitude;
  final String sourceType;
  final DateTime recordedAt;

  ResponderPositionModel({
    required this.latitude,
    required this.longitude,
    required this.sourceType,
    required this.recordedAt,
  });

  factory ResponderPositionModel.fromJson(Map<String, dynamic> json) {
    return ResponderPositionModel(
      latitude: (json['latitude'] as num?)?.toDouble() ?? 0.0,
      longitude: (json['longitude'] as num?)?.toDouble() ?? 0.0,
      sourceType: _toStringOrFallback(json['source_type'], 'UNKNOWN'),
      recordedAt: json['recorded_at'] != null
          ? DateTime.parse(json['recorded_at'] as String)
          : DateTime.now(),
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  ResponderPosition toEntity() => ResponderPosition(
    latitude: latitude,
    longitude: longitude,
    sourceType: sourceType,
    recordedAt: recordedAt,
  );
}

class RouteInfoModel {
  final String providerName;
  final double distanceMeters;
  final double distanceKm;
  final int durationSeconds;
  final int etaSeconds;
  final int etaMinutes;
  final String? polyline;
  final DateTime? lastCalculatedAt;
  final String? errorMessage;

  RouteInfoModel({
    required this.providerName,
    required this.distanceMeters,
    required this.distanceKm,
    required this.durationSeconds,
    required this.etaSeconds,
    required this.etaMinutes,
    this.polyline,
    this.lastCalculatedAt,
    this.errorMessage,
  });

  factory RouteInfoModel.fromJson(Map<String, dynamic> json) {
    return RouteInfoModel(
      providerName: _toStringOrFallback(json['provider_name'], 'unknown'),
      distanceMeters: (json['distance_meters'] as num?)?.toDouble() ?? 0.0,
      distanceKm: (json['distance_km'] as num?)?.toDouble() ?? 0.0,
      durationSeconds: json['duration_seconds'] as int? ?? 0,
      etaSeconds: json['eta_seconds'] as int? ?? 0,
      etaMinutes: json['eta_minutes'] as int? ?? 0,
      polyline: json['polyline'] as String?,
      lastCalculatedAt: json['last_calculated_at'] != null
          ? DateTime.tryParse(json['last_calculated_at'] as String)
          : null,
      errorMessage: json['error_message'] as String?,
    );
  }
  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  RouteInfo toEntity() => RouteInfo(
    providerName: providerName,
    distanceMeters: distanceMeters,
    distanceKm: distanceKm,
    durationSeconds: durationSeconds,
    etaSeconds: etaSeconds,
    etaMinutes: etaMinutes,
    polyline: polyline,
    lastCalculatedAt: lastCalculatedAt,
    errorMessage: errorMessage,
  );
}

class TrackingHistoryItemModel {
  final String id;
  final String incidentId;
  final String providerId;
  final String? technicianId;
  final String sourceType;
  final double latitude;
  final double longitude;
  final double? accuracyMeters;
  final DateTime recordedAt;
  final String? providerBusinessName;
  final String? technicianFullName;

  TrackingHistoryItemModel({
    required this.id,
    required this.incidentId,
    required this.providerId,
    this.technicianId,
    required this.sourceType,
    required this.latitude,
    required this.longitude,
    this.accuracyMeters,
    required this.recordedAt,
    this.providerBusinessName,
    this.technicianFullName,
  });

  factory TrackingHistoryItemModel.fromJson(Map<String, dynamic> json) {
    return TrackingHistoryItemModel(
      id: _toStringOrFallback(json['id'], ''),
      incidentId: _toStringOrFallback(json['incident_id'], ''),
      providerId: _toStringOrFallback(json['provider_id'], ''),
      technicianId: json['technician_id'] as String?,
      sourceType: _toStringOrFallback(json['source_type'], 'UNKNOWN'),
      latitude: (json['latitude'] as num?)?.toDouble() ?? 0.0,
      longitude: (json['longitude'] as num?)?.toDouble() ?? 0.0,
      accuracyMeters: (json['accuracy_meters'] as num?)?.toDouble(),
      recordedAt: json['recorded_at'] != null
          ? DateTime.parse(json['recorded_at'] as String)
          : DateTime.now(),
      providerBusinessName: json['provider_business_name'] as String?,
      technicianFullName: json['technician_full_name'] as String?,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  TrackingHistoryItem toEntity() => TrackingHistoryItem(
    id: id,
    incidentId: incidentId,
    providerId: providerId,
    technicianId: technicianId,
    sourceType: sourceType,
    latitude: latitude,
    longitude: longitude,
    accuracyMeters: accuracyMeters,
    recordedAt: recordedAt,
    providerBusinessName: providerBusinessName,
    technicianFullName: technicianFullName,
  );
}
