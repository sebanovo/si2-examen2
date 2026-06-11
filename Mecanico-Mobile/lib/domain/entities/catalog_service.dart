class CatalogItem {
  final String id;
  final String code;
  final String category;
  final String title;
  final String description;
  final bool supportsMobileService;
  final bool supportsEmergencyService;
  final bool isActive;
  final int sortOrder;
  final DateTime createdAt;
  final DateTime updatedAt;

  CatalogItem({
    required this.id,
    required this.code,
    required this.category,
    required this.title,
    required this.description,
    required this.supportsMobileService,
    required this.supportsEmergencyService,
    required this.isActive,
    required this.sortOrder,
    required this.createdAt,
    required this.updatedAt,
  });
}

class ProviderService {
  final String id;
  final String providerId;
  final String serviceCatalogItemId;
  final String serviceCode;
  final String serviceCategory;
  final String catalogTitle;
  final String catalogDescription;
  final String? customTitle;
  final String? customDescription;
  final String effectiveTitle;
  final String effectiveDescription;
  final double priceEstimateMin;
  final double priceEstimateMax;
  final int estimatedDurationMinutes;
  final bool supportsMobileService;
  final bool supportsEmergencyService;
  final bool isMobileServiceEnabled;
  final bool isEmergencyServiceEnabled;
  final bool isActive;
  final DateTime createdAt;
  final DateTime updatedAt;

  ProviderService({
    required this.id,
    required this.providerId,
    required this.serviceCatalogItemId,
    required this.serviceCode,
    required this.serviceCategory,
    required this.catalogTitle,
    required this.catalogDescription,
    this.customTitle,
    this.customDescription,
    required this.effectiveTitle,
    required this.effectiveDescription,
    required this.priceEstimateMin,
    required this.priceEstimateMax,
    required this.estimatedDurationMinutes,
    required this.supportsMobileService,
    required this.supportsEmergencyService,
    required this.isMobileServiceEnabled,
    required this.isEmergencyServiceEnabled,
    required this.isActive,
    required this.createdAt,
    required this.updatedAt,
  });

  String get priceRange => '\$$priceEstimateMin - \$$priceEstimateMax';
  String get displayTitle => customTitle ?? catalogTitle;
  String get displayDescription => customDescription ?? catalogDescription;
}

class CatalogServiceEntry {
  final CatalogItem catalogItem;
  final ProviderService? providerService;
  final bool isConfigured;

  CatalogServiceEntry({
    required this.catalogItem,
    this.providerService,
    required this.isConfigured,
  });

  bool get isActive => providerService?.isActive ?? false;
  String get effectiveTitle =>
      providerService?.effectiveTitle ?? catalogItem.title;
}
