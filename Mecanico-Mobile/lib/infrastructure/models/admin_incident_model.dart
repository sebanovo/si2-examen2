import '../../domain/entities/admin_incident.dart';
import '../../domain/entities/user.dart';
import '../../domain/entities/vehicle.dart';

class AdminIncidentModel {
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

  AdminIncidentModel({
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

  factory AdminIncidentModel.fromJson(Map<String, dynamic> json) {
    return AdminIncidentModel(
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
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
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
    );
  }

  AdminIncident toEntity() {
    return AdminIncident(
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

class CandidateModel {
  final String id;
  final String incidentId;
  final String providerId;
  final String status;
  final int recommendationRank;
  final double score;
  final double distanceKm;
  final List<String> requiredServiceCodes;
  final List<String> matchedServiceCodes;
  final Map<String, dynamic> rationale;
  final double providerAverageRatingSnapshot;
  final int providerAvailableCapacitySnapshot;
  final int availableTechniciansCountSnapshot;
  final DateTime publishedAt;
  final DateTime? respondedAt;
  final DateTime? expiresAt;
  final CandidateProviderModel provider;
  final CandidateIncidentModel incident;

  CandidateModel({
    required this.id,
    required this.incidentId,
    required this.providerId,
    required this.status,
    required this.recommendationRank,
    required this.score,
    required this.distanceKm,
    required this.requiredServiceCodes,
    required this.matchedServiceCodes,
    required this.rationale,
    required this.providerAverageRatingSnapshot,
    required this.providerAvailableCapacitySnapshot,
    required this.availableTechniciansCountSnapshot,
    required this.publishedAt,
    this.respondedAt,
    this.expiresAt,
    required this.provider,
    required this.incident,
  });

  factory CandidateModel.fromJson(Map<String, dynamic> json) {
    return CandidateModel(
      id: _toStringOrFallback(json['id'], ''),
      incidentId: _toStringOrFallback(json['incident_id'], ''),
      providerId: _toStringOrFallback(json['provider_id'], ''),
      status: _toStringOrFallback(json['status'], 'AVAILABLE'),
      recommendationRank: json['recommendation_rank'] as int? ?? 0,
      score: (json['score'] as num?)?.toDouble() ?? 0.0,
      distanceKm: (json['distance_km'] as num?)?.toDouble() ?? 0.0,
      requiredServiceCodes: json['required_service_codes'] != null
          ? List<String>.from(json['required_service_codes'] as List)
          : [],
      matchedServiceCodes: json['matched_service_codes'] != null
          ? List<String>.from(json['matched_service_codes'] as List)
          : [],
      rationale: json['rationale'] as Map<String, dynamic>? ?? {},
      providerAverageRatingSnapshot:
          (json['provider_average_rating_snapshot'] as num?)?.toDouble() ?? 0.0,
      providerAvailableCapacitySnapshot:
          json['provider_available_capacity_snapshot'] as int? ?? 0,
      availableTechniciansCountSnapshot:
          json['available_technicians_count_snapshot'] as int? ?? 0,
      publishedAt: DateTime.parse(json['published_at'] as String),
      respondedAt: json['responded_at'] != null
          ? DateTime.tryParse(json['responded_at'] as String)
          : null,
      expiresAt: json['expires_at'] != null
          ? DateTime.tryParse(json['expires_at'] as String)
          : null,
      provider: CandidateProviderModel.fromJson(json['provider']),
      incident: CandidateIncidentModel.fromJson(json['incident']),
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  Candidate toEntity() {
    return Candidate(
      id: id,
      providerId: providerId,
      providerName: provider.businessName,
      providerType: provider.providerType,
      averageRating: providerAverageRatingSnapshot,
      availableCapacity: providerAvailableCapacitySnapshot,
      availableTechniciansCount: availableTechniciansCountSnapshot,
      distanceKm: distanceKm,
      matchedServices: matchedServiceCodes,
      score: score,
      rationale: _formatRationale(rationale),
      createdAt: publishedAt,
    );
  }

  String _formatRationale(Map<String, dynamic> rationale) {
    final parts = <String>[];
    if (rationale['distance_score'] != null) {
      parts.add('Distancia: ${rationale['distance_score']} puntos');
    }
    if (rationale['service_score'] != null) {
      parts.add('Servicios: ${rationale['service_score']} puntos');
    }
    if (rationale['capacity_score'] != null) {
      parts.add('Capacidad: ${rationale['capacity_score']} puntos');
    }
    if (rationale['technician_score'] != null) {
      parts.add('Técnicos: ${rationale['technician_score']} puntos');
    }
    if (rationale['rating_score'] != null) {
      parts.add('Calificación: ${rationale['rating_score']} puntos');
    }
    return parts.join(' · ');
  }
}

// ✅ MODELO DE PROVEEDOR DENTRO DEL CANDIDATO
class CandidateProviderModel {
  final String id;
  final String providerType;
  final String businessName;
  final String city;
  final String? contactPhone;
  final double averageRating;
  final int availableCapacity;
  final int availableTechniciansCount;
  final double baseLatitude;
  final double baseLongitude;
  final CandidateProviderOwnerUserModel ownerUser;
  final List<CandidateMatchedServiceModel> matchedServices;

  CandidateProviderModel({
    required this.id,
    required this.providerType,
    required this.businessName,
    required this.city,
    this.contactPhone,
    required this.averageRating,
    required this.availableCapacity,
    required this.availableTechniciansCount,
    required this.baseLatitude,
    required this.baseLongitude,
    required this.ownerUser,
    required this.matchedServices,
  });

  factory CandidateProviderModel.fromJson(Map<String, dynamic> json) {
    return CandidateProviderModel(
      id: _toStringOrFallback(json['id'], ''),
      providerType: _toStringOrFallback(json['provider_type'], 'WORKSHOP'),
      businessName: _toStringOrFallback(json['business_name'], ''),
      city: _toStringOrFallback(json['city'], ''),
      contactPhone: json['contact_phone'] as String?,
      averageRating: (json['average_rating'] as num?)?.toDouble() ?? 0.0,
      availableCapacity: json['available_capacity'] as int? ?? 0,
      availableTechniciansCount:
          json['available_technicians_count'] as int? ?? 0,
      baseLatitude: (json['base_latitude'] as num?)?.toDouble() ?? 0.0,
      baseLongitude: (json['base_longitude'] as num?)?.toDouble() ?? 0.0,
      ownerUser: CandidateProviderOwnerUserModel.fromJson(json['owner_user']),
      matchedServices:
          (json['matched_services'] as List<dynamic>?)
              ?.map((e) => CandidateMatchedServiceModel.fromJson(e))
              .toList() ??
          [],
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }
}

// ✅ MODELO DEL USUARIO DUEÑO DEL PROVEEDOR
class CandidateProviderOwnerUserModel {
  final String id;
  final String email;
  final String firstName;
  final String lastName;
  final String fullName;
  final String phoneNumber;

  CandidateProviderOwnerUserModel({
    required this.id,
    required this.email,
    required this.firstName,
    required this.lastName,
    required this.fullName,
    required this.phoneNumber,
  });

  factory CandidateProviderOwnerUserModel.fromJson(Map<String, dynamic> json) {
    return CandidateProviderOwnerUserModel(
      id: _toStringOrFallback(json['id'], ''),
      email: _toStringOrFallback(json['email'], ''),
      firstName: _toStringOrFallback(json['first_name'], ''),
      lastName: _toStringOrFallback(json['last_name'], ''),
      fullName: _toStringOrFallback(json['full_name'], ''),
      phoneNumber: _toStringOrFallback(json['phone_number'], ''),
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }
}

// ✅ MODELO DE SERVICIO COINCIDENTE
class CandidateMatchedServiceModel {
  final String code;
  final String category;
  final String title;

  CandidateMatchedServiceModel({
    required this.code,
    required this.category,
    required this.title,
  });

  factory CandidateMatchedServiceModel.fromJson(Map<String, dynamic> json) {
    return CandidateMatchedServiceModel(
      code: _toStringOrFallback(json['code'], ''),
      category: _toStringOrFallback(json['category'], ''),
      title: _toStringOrFallback(json['title'], ''),
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }
}

// ✅ MODELO DEL INCIDENTE DENTRO DEL CANDIDATO
class CandidateIncidentModel {
  final String id;
  final String status;
  final String priority;
  final String reportedCategory;
  final String title;
  final String description;
  final double incidentLatitude;
  final double incidentLongitude;
  final String addressReference;
  final String aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;

  CandidateIncidentModel({
    required this.id,
    required this.status,
    required this.priority,
    required this.reportedCategory,
    required this.title,
    required this.description,
    required this.incidentLatitude,
    required this.incidentLongitude,
    required this.addressReference,
    required this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
  });

  factory CandidateIncidentModel.fromJson(Map<String, dynamic> json) {
    return CandidateIncidentModel(
      id: _toStringOrFallback(json['id'], ''),
      status: _toStringOrFallback(json['status'], 'PENDING'),
      priority: _toStringOrFallback(json['priority'], 'MEDIUM'),
      reportedCategory: _toStringOrFallback(json['reported_category'], 'OTHER'),
      title: _toStringOrFallback(json['title'], ''),
      description: _toStringOrFallback(json['description'], ''),
      incidentLatitude: (json['incident_latitude'] as num?)?.toDouble() ?? 0.0,
      incidentLongitude:
          (json['incident_longitude'] as num?)?.toDouble() ?? 0.0,
      addressReference: _toStringOrFallback(json['address_reference'], ''),
      aiSummaryStatus: _toStringOrFallback(
        json['ai_summary_status'],
        'NOT_REQUESTED',
      ),
      structuredSummary: json['structured_summary'] as String?,
      suggestedCategory: json['suggested_category'] as String?,
      suggestedPriority: json['suggested_priority'] as String?,
      requiresMoreInformation:
          json['requires_more_information'] as bool? ?? false,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }
}
