import '../../domain/entities/provider_summary.dart';
import '../../domain/entities/user.dart';

class ProviderSummaryModel {
  final String id;
  final String ownerUserId;
  final String providerType;
  final String businessName;
  final String? legalName;
  final String? description;
  final String? contactEmail;
  final String? contactPhone;
  final String? city;
  final String? address;
  final double? baseLatitude;
  final double? baseLongitude;
  final bool isActive;
  final bool isAvailable;
  final int maxConcurrentServices;
  final int currentActiveServices;
  final int availableCapacity;
  final double averageRating;
  final User? ownerUser;
  final int techniciansCount;
  final int availableTechniciansCount;
  final int configuredServicesCount;
  final int activeServicesCount;
  final List<ProviderServiceSummaryModel> activeServices;
  final DateTime createdAt;
  final DateTime updatedAt;

  ProviderSummaryModel({
    required this.id,
    required this.ownerUserId,
    required this.providerType,
    required this.businessName,
    this.legalName,
    this.description,
    this.contactEmail,
    this.contactPhone,
    this.city,
    this.address,
    this.baseLatitude,
    this.baseLongitude,
    required this.isActive,
    required this.isAvailable,
    required this.maxConcurrentServices,
    required this.currentActiveServices,
    required this.availableCapacity,
    required this.averageRating,
    this.ownerUser,
    required this.techniciansCount,
    required this.availableTechniciansCount,
    required this.configuredServicesCount,
    required this.activeServicesCount,
    required this.activeServices,
    required this.createdAt,
    required this.updatedAt,
  });

  factory ProviderSummaryModel.fromJson(Map<String, dynamic> json) {
    return ProviderSummaryModel(
      id: _toStringOrFallback(json['id'], ''),
      ownerUserId: _toStringOrFallback(json['owner_user_id'], ''),
      providerType: _toStringOrFallback(json['provider_type'], 'WORKSHOP'),
      businessName: _toStringOrFallback(json['business_name'], ''),
      legalName: json['legal_name'] as String?,
      description: json['description'] as String?,
      contactEmail: json['contact_email'] as String?,
      contactPhone: json['contact_phone'] as String?,
      city: json['city'] as String?,
      address: json['address'] as String?,
      baseLatitude: (json['base_latitude'] as num?)?.toDouble(),
      baseLongitude: (json['base_longitude'] as num?)?.toDouble(),
      isActive: json['is_active'] as bool? ?? true,
      isAvailable: json['is_available'] as bool? ?? true,
      maxConcurrentServices: json['max_concurrent_services'] as int? ?? 1,
      currentActiveServices: json['current_active_services'] as int? ?? 0,
      availableCapacity: json['available_capacity'] as int? ?? 0,
      averageRating: (json['average_rating'] as num?)?.toDouble() ?? 0.0,
      ownerUser: json['owner_user'] != null
          ? _parseUser(json['owner_user'])
          : null,
      techniciansCount: json['technicians_count'] as int? ?? 0,
      availableTechniciansCount:
          json['available_technicians_count'] as int? ?? 0,
      configuredServicesCount: json['configured_services_count'] as int? ?? 0,
      activeServicesCount: json['active_services_count'] as int? ?? 0,
      activeServices:
          (json['active_services'] as List<dynamic>?)
              ?.map((e) => ProviderServiceSummaryModel.fromJson(e))
              .toList() ??
          [],
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
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

  ProviderSummary toEntity() {
    return ProviderSummary(
      id: id,
      ownerUserId: ownerUserId,
      providerType: providerType,
      businessName: businessName,
      legalName: legalName,
      description: description,
      contactEmail: contactEmail,
      contactPhone: contactPhone,
      city: city,
      address: address,
      baseLatitude: baseLatitude,
      baseLongitude: baseLongitude,
      isActive: isActive,
      isAvailable: isAvailable,
      maxConcurrentServices: maxConcurrentServices,
      currentActiveServices: currentActiveServices,
      availableCapacity: availableCapacity,
      averageRating: averageRating,
      ownerUser: ownerUser,
      techniciansCount: techniciansCount,
      availableTechniciansCount: availableTechniciansCount,
      configuredServicesCount: configuredServicesCount,
      activeServicesCount: activeServicesCount,
      activeServices: activeServices.map((s) => s.toEntity()).toList(),
      createdAt: createdAt,
      updatedAt: updatedAt,
    );
  }
}

class ProviderServiceSummaryModel {
  final String id;
  final String serviceCatalogItemId;
  final String code;
  final String category;
  final String title;
  final double priceEstimateMin;
  final double priceEstimateMax;
  final int estimatedDurationMinutes;
  final bool isMobileServiceEnabled;
  final bool isEmergencyServiceEnabled;
  final bool isActive;

  ProviderServiceSummaryModel({
    required this.id,
    required this.serviceCatalogItemId,
    required this.code,
    required this.category,
    required this.title,
    required this.priceEstimateMin,
    required this.priceEstimateMax,
    required this.estimatedDurationMinutes,
    required this.isMobileServiceEnabled,
    required this.isEmergencyServiceEnabled,
    required this.isActive,
  });

  factory ProviderServiceSummaryModel.fromJson(Map<String, dynamic> json) {
    return ProviderServiceSummaryModel(
      id: _toStringOrFallback(json['id'], ''),
      serviceCatalogItemId: _toStringOrFallback(
        json['service_catalog_item_id'],
        '',
      ),
      code: _toStringOrFallback(json['code'], ''),
      category: _toStringOrFallback(json['category'], ''),
      title: _toStringOrFallback(json['title'], ''),
      priceEstimateMin: (json['price_estimate_min'] as num?)?.toDouble() ?? 0.0,
      priceEstimateMax: (json['price_estimate_max'] as num?)?.toDouble() ?? 0.0,
      estimatedDurationMinutes: json['estimated_duration_minutes'] as int? ?? 0,
      isMobileServiceEnabled:
          json['is_mobile_service_enabled'] as bool? ?? false,
      isEmergencyServiceEnabled:
          json['is_emergency_service_enabled'] as bool? ?? false,
      isActive: json['is_active'] as bool? ?? true,
    );
  }

  static String _toStringOrFallback(dynamic value, String fallback) {
    if (value == null) return fallback;
    return value.toString();
  }

  ProviderServiceSummary toEntity() {
    return ProviderServiceSummary(
      id: id,
      serviceCatalogItemId: serviceCatalogItemId,
      code: code,
      category: category,
      title: title,
      priceEstimateMin: priceEstimateMin,
      priceEstimateMax: priceEstimateMax,
      estimatedDurationMinutes: estimatedDurationMinutes,
      isMobileServiceEnabled: isMobileServiceEnabled,
      isEmergencyServiceEnabled: isEmergencyServiceEnabled,
      isActive: isActive,
    );
  }
}
