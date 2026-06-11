import '../../domain/entities/provider_candidate.dart';

class ProviderCandidateModel {
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

  ProviderCandidateModel({
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

  factory ProviderCandidateModel.fromJson(Map<String, dynamic> json) {
    return ProviderCandidateModel(
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

  ProviderCandidate toEntity() {
    return ProviderCandidate(
      id: id,
      incidentId: incidentId,
      providerId: providerId,
      status: status,
      recommendationRank: recommendationRank,
      score: score,
      distanceKm: distanceKm,
      requiredServiceCodes: requiredServiceCodes,
      matchedServiceCodes: matchedServiceCodes,
      rationale: rationale,
      providerAverageRatingSnapshot: providerAverageRatingSnapshot,
      providerAvailableCapacitySnapshot: providerAvailableCapacitySnapshot,
      availableTechniciansCountSnapshot: availableTechniciansCountSnapshot,
      publishedAt: publishedAt,
      respondedAt: respondedAt,
      expiresAt: expiresAt,
      provider: provider.toEntity(),
      incident: incident.toEntity(),
    );
  }
}

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

  CandidateProvider toEntity() {
    return CandidateProvider(
      id: id,
      providerType: providerType,
      businessName: businessName,
      city: city,
      contactPhone: contactPhone,
      averageRating: averageRating,
      availableCapacity: availableCapacity,
      availableTechniciansCount: availableTechniciansCount,
      baseLatitude: baseLatitude,
      baseLongitude: baseLongitude,
      ownerUser: ownerUser.toEntity(),
      matchedServices: matchedServices.map((s) => s.toEntity()).toList(),
    );
  }
}

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

  CandidateProviderOwnerUser toEntity() {
    return CandidateProviderOwnerUser(
      id: id,
      email: email,
      firstName: firstName,
      lastName: lastName,
      fullName: fullName,
      phoneNumber: phoneNumber,
    );
  }
}

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

  CandidateMatchedService toEntity() {
    return CandidateMatchedService(
      code: code,
      category: category,
      title: title,
    );
  }
}

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

  CandidateIncident toEntity() {
    return CandidateIncident(
      id: id,
      status: status,
      priority: priority,
      reportedCategory: reportedCategory,
      title: title,
      description: description,
      incidentLatitude: incidentLatitude,
      incidentLongitude: incidentLongitude,
      addressReference: addressReference,
      aiSummaryStatus: aiSummaryStatus,
      structuredSummary: structuredSummary,
      suggestedCategory: suggestedCategory,
      suggestedPriority: suggestedPriority,
      requiresMoreInformation: requiresMoreInformation,
    );
  }
}
