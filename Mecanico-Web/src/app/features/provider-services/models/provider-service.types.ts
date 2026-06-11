export type ProviderServiceDto = {
	id: string;
	provider_id: string;
	service_catalog_item_id: string;
	service_code: string;
	service_category: string;
	catalog_title: string;
	catalog_description: string;
	custom_title: string | null;
	custom_description: string | null;
	effective_title: string;
	effective_description: string;
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
	catalogDescription: string;
	customTitle: string | null;
	customDescription: string | null;
	effectiveTitle: string;
	effectiveDescription: string;
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

export type ProviderServicesMetaDto = {
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
