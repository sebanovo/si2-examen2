import 'package:mechanic_mobile/domain/entities/user.dart';

class ProviderProfile {
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
  final List<ProviderService> activeServices;
  final DateTime createdAt;
  final DateTime updatedAt;

  ProviderProfile({
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

  String get fullAddress => [address, city].where((e) => e != null).join(', ');

  String get location {
    if (baseLatitude != null && baseLongitude != null) {
      return '${baseLatitude!.toStringAsFixed(4)}, ${baseLongitude!.toStringAsFixed(4)}';
    }
    return 'Sin ubicación';
  }

  bool get hasCapacity => currentActiveServices < maxConcurrentServices;
  int get remainingCapacity => maxConcurrentServices - currentActiveServices;
}

class ProviderService {
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

  ProviderService({
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

  String get priceRange => '\$$priceEstimateMin - \$$priceEstimateMax';
}
