import '../../domain/entities/catalog_service.dart';

class CatalogItemModel {
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

  CatalogItemModel({
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

  factory CatalogItemModel.fromJson(Map<String, dynamic> json) {
    return CatalogItemModel(
      id: json['id'] as String,
      code: json['code'] as String,
      category: json['category'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      supportsMobileService: json['supports_mobile_service'] as bool? ?? false,
      supportsEmergencyService: json['supports_emergency_service'] as bool? ?? false,
      isActive: json['is_active'] as bool? ?? true,
      sortOrder: json['sort_order'] as int? ?? 0,
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
    );
  }

  CatalogItem toEntity() => CatalogItem(
    id: id,
    code: code,
    category: category,
    title: title,
    description: description,
    supportsMobileService: supportsMobileService,
    supportsEmergencyService: supportsEmergencyService,
    isActive: isActive,
    sortOrder: sortOrder,
    createdAt: createdAt,
    updatedAt: updatedAt,
  );
}

class ProviderServiceModel {
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

  ProviderServiceModel({
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

  factory ProviderServiceModel.fromJson(Map<String, dynamic> json) {
    return ProviderServiceModel(
      id: json['id'] as String,
      providerId: json['provider_id'] as String,
      serviceCatalogItemId: json['service_catalog_item_id'] as String,
      serviceCode: json['service_code'] as String,
      serviceCategory: json['service_category'] as String,
      catalogTitle: json['catalog_title'] as String,
      catalogDescription: json['catalog_description'] as String,
      customTitle: json['custom_title'] as String?,
      customDescription: json['custom_description'] as String?,
      effectiveTitle: json['effective_title'] as String,
      effectiveDescription: json['effective_description'] as String,
      priceEstimateMin: (json['price_estimate_min'] as num?)?.toDouble() ?? 0.0,
      priceEstimateMax: (json['price_estimate_max'] as num?)?.toDouble() ?? 0.0,
      estimatedDurationMinutes: json['estimated_duration_minutes'] as int? ?? 0,
      supportsMobileService: json['supports_mobile_service'] as bool? ?? false,
      supportsEmergencyService: json['supports_emergency_service'] as bool? ?? false,
      isMobileServiceEnabled: json['is_mobile_service_enabled'] as bool? ?? false,
      isEmergencyServiceEnabled: json['is_emergency_service_enabled'] as bool? ?? false,
      isActive: json['is_active'] as bool? ?? true,
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
    );
  }

  ProviderService toEntity() => ProviderService(
    id: id,
    providerId: providerId,
    serviceCatalogItemId: serviceCatalogItemId,
    serviceCode: serviceCode,
    serviceCategory: serviceCategory,
    catalogTitle: catalogTitle,
    catalogDescription: catalogDescription,
    customTitle: customTitle,
    customDescription: customDescription,
    effectiveTitle: effectiveTitle,
    effectiveDescription: effectiveDescription,
    priceEstimateMin: priceEstimateMin,
    priceEstimateMax: priceEstimateMax,
    estimatedDurationMinutes: estimatedDurationMinutes,
    supportsMobileService: supportsMobileService,
    supportsEmergencyService: supportsEmergencyService,
    isMobileServiceEnabled: isMobileServiceEnabled,
    isEmergencyServiceEnabled: isEmergencyServiceEnabled,
    isActive: isActive,
    createdAt: createdAt,
    updatedAt: updatedAt,
  );
}

class CatalogServiceEntryModel {
  final CatalogItemModel catalogItem;
  final ProviderServiceModel? providerService;
  final bool isConfigured;

  CatalogServiceEntryModel({
    required this.catalogItem,
    this.providerService,
    required this.isConfigured,
  });

  factory CatalogServiceEntryModel.fromJson(Map<String, dynamic> json) {
    return CatalogServiceEntryModel(
      catalogItem: CatalogItemModel.fromJson(json['catalog_item']),
      providerService: json['provider_service'] != null 
          ? ProviderServiceModel.fromJson(json['provider_service'])
          : null,
      isConfigured: json['is_configured'] as bool? ?? false,
    );
  }

  CatalogServiceEntry toEntity() => CatalogServiceEntry(
    catalogItem: catalogItem.toEntity(),
    providerService: providerService?.toEntity(),
    isConfigured: isConfigured,
  );
}