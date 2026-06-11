export type ProviderMeType = "WORKSHOP" | "INDEPENDENT_MECHANIC";

export type ProviderMeOwnerUserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	is_active: boolean;
};

export type ProviderMeDto = {
	id: string;
	owner_user_id: string;
	provider_type: ProviderMeType;
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
	owner_user: ProviderMeOwnerUserDto;
	technicians_count: number;
	available_technicians_count: number;
	configured_services_count: number;
	active_services_count: number;
	active_services: unknown[];
	created_at: string;
	updated_at: string;
};

export type ProviderMeOwnerUser = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	isActive: boolean;
};

export type ProviderMe = {
	id: string;
	ownerUserId: string;
	providerType: ProviderMeType;
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
	ownerUser: ProviderMeOwnerUser;
	techniciansCount: number;
	availableTechniciansCount: number;
	configuredServicesCount: number;
	activeServicesCount: number;
	activeServices: unknown[];
	createdAt: string;
	updatedAt: string;
};

export type UpdateProviderMeProfileRequest = {
	business_name: string;
	legal_name: string;
	description: string | null;
	contact_email: string;
	contact_phone: string | null;
	city: string;
	address: string;
	base_latitude: number;
	base_longitude: number;
	is_available: boolean;
	max_concurrent_services: number;
};

export type UpdateProviderMeProfileFormValue = {
	businessName: string;
	legalName: string;
	description: string | null;
	contactEmail: string;
	contactPhone: string | null;
	city: string;
	address: string;
	baseLatitude: number;
	baseLongitude: number;
	isAvailable: boolean;
	maxConcurrentServices: number;
};

export type ProviderMeTechnicianDto = {
	id: string;
	provider_id: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	specialty: string;
	is_active: boolean;
	is_available: boolean;
	current_latitude: number;
	current_longitude: number;
	created_at: string;
	updated_at: string;
};

export type ProviderMeTechnician = {
	id: string;
	providerId: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	specialty: string;
	isActive: boolean;
	isAvailable: boolean;
	currentLatitude: number;
	currentLongitude: number;
	createdAt: string;
	updatedAt: string;
};

export type CreateProviderMeTechnicianRequest = {
	first_name: string;
	last_name: string;
	phone_number: string | null;
	specialty: string;
	is_available: boolean;
	current_latitude: number;
	current_longitude: number;
};

export type CreateProviderMeTechnicianFormValue = {
	firstName: string;
	lastName: string;
	phoneNumber: string | null;
	specialty: string;
	isAvailable: boolean;
	currentLatitude: number;
	currentLongitude: number;
};

export type UpdateProviderMeTechnicianRequest = {
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	specialty: string;
	is_active: boolean;
	is_available: boolean;
	current_latitude: number;
	current_longitude: number;
};

export type UpdateProviderMeTechnicianFormValue = {
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	specialty: string;
	isActive: boolean;
	isAvailable: boolean;
	currentLatitude: number;
	currentLongitude: number;
};

export type ProviderMeTechniciansMetaDto = {
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
