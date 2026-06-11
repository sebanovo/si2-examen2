import {
	ProviderService,
	ProviderServiceDto,
} from "../models/provider-service.types";

export function toProviderService(dto: ProviderServiceDto): ProviderService {
	return {
		id: dto.id,
		providerId: dto.provider_id,
		serviceCatalogItemId: dto.service_catalog_item_id,
		serviceCode: dto.service_code,
		serviceCategory: dto.service_category,
		catalogTitle: dto.catalog_title,
		catalogDescription: dto.catalog_description,
		customTitle: dto.custom_title,
		customDescription: dto.custom_description,
		effectiveTitle: dto.effective_title,
		effectiveDescription: dto.effective_description,
		priceEstimateMin: dto.price_estimate_min,
		priceEstimateMax: dto.price_estimate_max,
		estimatedDurationMinutes: dto.estimated_duration_minutes,
		supportsMobileService: dto.supports_mobile_service,
		supportsEmergencyService: dto.supports_emergency_service,
		isMobileServiceEnabled: dto.is_mobile_service_enabled,
		isEmergencyServiceEnabled: dto.is_emergency_service_enabled,
		isActive: dto.is_active,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toProviderServices(
	dtos: ProviderServiceDto[]
): ProviderService[] {
	return dtos.map(toProviderService);
}
