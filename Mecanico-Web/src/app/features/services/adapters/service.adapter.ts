import {
	CreateProviderServiceFormValue,
	CreateProviderServiceRequest,
	ProviderService,
	ProviderServiceCatalogConfiguration,
	ProviderServiceCatalogConfigurationDto,
	ProviderServiceDto,
	ServiceCatalogItem,
	ServiceCatalogItemDto,
	UpdateProviderServiceFormValue,
	UpdateProviderServiceRequest,
} from "../models/service.types";

export function toServiceCatalogItem(
	dto: ServiceCatalogItemDto
): ServiceCatalogItem {
	return {
		id: dto.id,
		code: dto.code,
		category: dto.category,
		title: dto.title,
		description: dto.description,
		supportsMobileService: dto.supports_mobile_service,
		supportsEmergencyService: dto.supports_emergency_service,
		isActive: dto.is_active,
		sortOrder: dto.sort_order,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

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

export function toProviderServiceCatalogConfiguration(
	dto: ProviderServiceCatalogConfigurationDto
): ProviderServiceCatalogConfiguration {
	return {
		catalogItem: toServiceCatalogItem(dto.catalog_item),
		providerService: dto.provider_service
			? toProviderService(dto.provider_service)
			: null,
		isConfigured: dto.is_configured,
	};
}

export function toProviderServiceCatalogConfigurations(
	dtos: ProviderServiceCatalogConfigurationDto[]
): ProviderServiceCatalogConfiguration[] {
	return dtos.map(toProviderServiceCatalogConfiguration);
}

export function toCreateProviderServiceRequest(
	formValue: CreateProviderServiceFormValue
): CreateProviderServiceRequest {
	return {
		service_catalog_item_id: formValue.serviceCatalogItemId,
		custom_title: formValue.customTitle?.trim() || null,
		custom_description: formValue.customDescription?.trim() || null,
		price_estimate_min: formValue.priceEstimateMin,
		price_estimate_max: formValue.priceEstimateMax,
		estimated_duration_minutes: formValue.estimatedDurationMinutes,
		is_mobile_service_enabled: formValue.isMobileServiceEnabled,
		is_emergency_service_enabled: formValue.isEmergencyServiceEnabled,
		is_active: formValue.isActive,
	};
}

export function toUpdateProviderServiceRequest(
	formValue: UpdateProviderServiceFormValue
): UpdateProviderServiceRequest {
	return {
		custom_title: formValue.customTitle?.trim() || null,
		custom_description: formValue.customDescription?.trim() || null,
		price_estimate_min: formValue.priceEstimateMin,
		price_estimate_max: formValue.priceEstimateMax,
		estimated_duration_minutes: formValue.estimatedDurationMinutes,
		is_mobile_service_enabled: formValue.isMobileServiceEnabled,
		is_emergency_service_enabled: formValue.isEmergencyServiceEnabled,
		is_active: formValue.isActive,
	};
}
