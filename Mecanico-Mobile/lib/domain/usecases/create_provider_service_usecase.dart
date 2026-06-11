import '../entities/catalog_service.dart';

abstract class CreateProviderServiceUseCase {
  Future<ProviderService> execute(CreateProviderServiceParams params);
}

class CreateProviderServiceParams {
  final String serviceCatalogItemId;
  final String? customTitle;
  final String? customDescription;
  final double priceEstimateMin;
  final double priceEstimateMax;
  final int estimatedDurationMinutes;
  final bool isMobileServiceEnabled;
  final bool isEmergencyServiceEnabled;
  final bool isActive;

  CreateProviderServiceParams({
    required this.serviceCatalogItemId,
    this.customTitle,
    this.customDescription,
    required this.priceEstimateMin,
    required this.priceEstimateMax,
    required this.estimatedDurationMinutes,
    required this.isMobileServiceEnabled,
    required this.isEmergencyServiceEnabled,
    required this.isActive,
  });

  Map<String, dynamic> toJson() => {
    'service_catalog_item_id': serviceCatalogItemId,
    if (customTitle != null) 'custom_title': customTitle,
    if (customDescription != null) 'custom_description': customDescription,
    'price_estimate_min': priceEstimateMin,
    'price_estimate_max': priceEstimateMax,
    'estimated_duration_minutes': estimatedDurationMinutes,
    'is_mobile_service_enabled': isMobileServiceEnabled,
    'is_emergency_service_enabled': isEmergencyServiceEnabled,
    'is_active': isActive,
  };
}