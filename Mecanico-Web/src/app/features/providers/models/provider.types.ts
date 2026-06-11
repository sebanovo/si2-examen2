export type ProviderType = "WORKSHOP" | "INDEPENDENT_MECHANIC";

export type ProviderOwnerUserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	is_active: boolean;
};

export type ProviderDto = {
	id: string;
	owner_user_id: string;
	provider_type: ProviderType;
	business_name: string;
	legal_name: string;
	description: string | null;
	contact_email: string;
	contact_phone: string | null;
	city: string;
	address: string;
	base_latitude: number;
	base_longitude: number;
	is_active: boolean;
	is_available: boolean;
	max_concurrent_services: number;
	current_active_services: number;
	available_capacity: number;
	average_rating: number;
	owner_user: ProviderOwnerUserDto;
	technicians_count: number;
	available_technicians_count: number;
	configured_services_count: number;
	active_services_count: number;
	active_services: unknown[];
	created_at: string;
	updated_at: string;
};

export type ProviderOwnerUser = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	isActive: boolean;
};

export type Provider = {
	id: string;
	ownerUserId: string;
	providerType: ProviderType;
	businessName: string;
	legalName: string;
	description: string | null;
	contactEmail: string;
	contactPhone: string | null;
	city: string;
	address: string;
	baseLatitude: number;
	baseLongitude: number;
	isActive: boolean;
	isAvailable: boolean;
	maxConcurrentServices: number;
	currentActiveServices: number;
	availableCapacity: number;
	averageRating: number;
	ownerUser: ProviderOwnerUser;
	techniciansCount: number;
	availableTechniciansCount: number;
	configuredServicesCount: number;
	activeServicesCount: number;
	activeServices: unknown[];
	createdAt: string;
	updatedAt: string;
};

export type OnboardProviderRequest = {
	admin_user: {
		email: string;
		password: string;
		first_name: string;
		last_name: string;
		phone_number: string | null;
	};
	provider: {
		provider_type: ProviderType;
		business_name: string;
		legal_name: string;
		description: string | null;
		contact_email: string;
		contact_phone: string | null;
		city: string;
		address: string;
		base_latitude: number;
		base_longitude: number;
		max_concurrent_services: number;
	};
};

export type OnboardProviderFormValue = {
	adminUser: {
		email: string;
		password: string;
		firstName: string;
		lastName: string;
		phoneNumber: string | null;
	};
	provider: {
		providerType: ProviderType;
		businessName: string;
		legalName: string;
		description: string | null;
		contactEmail: string;
		contactPhone: string | null;
		city: string;
		address: string;
		baseLatitude: number;
		baseLongitude: number;
		maxConcurrentServices: number;
	};
};

export type GetProvidersParams = {
	limit: number;
	offset: number;
};

export type ProvidersMetaDto = {
	limit: number;
	offset: number;
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};

export type UpdateProviderOperationsRequest = {
	is_active: boolean;
	is_available: boolean;
	max_concurrent_services: number;
	current_active_services: number;
};

export type UpdateProviderOperationsFormValue = {
	isActive: boolean;
	isAvailable: boolean;
	maxConcurrentServices: number;
	currentActiveServices: number;
};
