export type ServiceCatalogItemDto = {
	id: string;
	code: string;
	category: string;
	title: string;
	description: string | null;
	supports_mobile_service: boolean;
	supports_emergency_service: boolean;
	is_active: boolean;
	sort_order: number;
	created_at: string;
	updated_at: string;
};

export type ServiceCatalogItem = {
	id: string;
	code: string;
	category: string;
	title: string;
	description: string | null;
	supportsMobileService: boolean;
	supportsEmergencyService: boolean;
	isActive: boolean;
	sortOrder: number;
	createdAt: string;
	updatedAt: string;
};

export type ProviderServiceDto = {
	id: string;
	provider_id: string;
	service_catalog_item_id: string;
	service_code: string;
	service_category: string;
	catalog_title: string;
	catalog_description: string | null;
	custom_title: string | null;
	custom_description: string | null;
	effective_title: string;
	effective_description: string | null;
	price_estimate_min: number;
	price_estimate_max: number;
	estimated_duration_minutes: number;
	supports_mobile_service: boolean;
	supports_emergency_service: boolean;
	is_mobile_service_enabled: boolean;
	is_emergency_service_enabled: boolean;
	is_active: boolean;
	created_at: string;
	updated_at: string;
};

export type ProviderService = {
	id: string;
	providerId: string;
	serviceCatalogItemId: string;
	serviceCode: string;
	serviceCategory: string;
	catalogTitle: string;
	catalogDescription: string | null;
	customTitle: string | null;
	customDescription: string | null;
	effectiveTitle: string;
	effectiveDescription: string | null;
	priceEstimateMin: number;
	priceEstimateMax: number;
	estimatedDurationMinutes: number;
	supportsMobileService: boolean;
	supportsEmergencyService: boolean;
	isMobileServiceEnabled: boolean;
	isEmergencyServiceEnabled: boolean;
	isActive: boolean;
	createdAt: string;
	updatedAt: string;
};

export type ProviderServiceCatalogConfigurationDto = {
	catalog_item: ServiceCatalogItemDto;
	provider_service: ProviderServiceDto | null;
	is_configured: boolean;
};

export type ProviderServiceCatalogConfiguration = {
	catalogItem: ServiceCatalogItem;
	providerService: ProviderService | null;
	isConfigured: boolean;
};

export type ProviderServiceCatalogMetaDto = {
	count: number;
	include_inactive_catalog: boolean;
};

export type ProviderServicesMetaDto = {
	count: number;
};

export type CreateProviderServiceRequest = {
	service_catalog_item_id: string;
	custom_title: string | null;
	custom_description: string | null;
	price_estimate_min: number;
	price_estimate_max: number;
	estimated_duration_minutes: number;
	is_mobile_service_enabled: boolean;
	is_emergency_service_enabled: boolean;
	is_active: boolean;
};

export type CreateProviderServiceFormValue = {
	serviceCatalogItemId: string;
	customTitle: string | null;
	customDescription: string | null;
	priceEstimateMin: number;
	priceEstimateMax: number;
	estimatedDurationMinutes: number;
	isMobileServiceEnabled: boolean;
	isEmergencyServiceEnabled: boolean;
	isActive: boolean;
};

export type UpdateProviderServiceRequest = {
	custom_title: string | null;
	custom_description: string | null;
	price_estimate_min: number;
	price_estimate_max: number;
	estimated_duration_minutes: number;
	is_mobile_service_enabled: boolean;
	is_emergency_service_enabled: boolean;
	is_active: boolean;
};

export type UpdateProviderServiceFormValue = {
	customTitle: string | null;
	customDescription: string | null;
	priceEstimateMin: number;
	priceEstimateMax: number;
	estimatedDurationMinutes: number;
	isMobileServiceEnabled: boolean;
	isEmergencyServiceEnabled: boolean;
	isActive: boolean;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
