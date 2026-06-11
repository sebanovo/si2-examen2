export type MiEmpresaType = "WORKSHOP" | "INDEPENDENT_MECHANIC";

export type MiEmpresaOwnerUserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	is_active: boolean;
};

export type MiEmpresaDto = {
	id: string;
	owner_user_id: string;
	provider_type: MiEmpresaType;
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
	owner_user: MiEmpresaOwnerUserDto;
	technicians_count: number;
	available_technicians_count: number;
	configured_services_count: number;
	active_services_count: number;
	active_services: unknown[];
	created_at: string;
	updated_at: string;
};

export type MiEmpresaOwnerUser = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	isActive: boolean;
};

export type MiEmpresa = {
	id: string;
	ownerUserId: string;
	providerType: MiEmpresaType;
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
	ownerUser: MiEmpresaOwnerUser;
	techniciansCount: number;
	availableTechniciansCount: number;
	configuredServicesCount: number;
	activeServicesCount: number;
	activeServices: unknown[];
	createdAt: string;
	updatedAt: string;
};

export type UpdateMiEmpresaRequest = {
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

export type UpdateMiEmpresaFormValue = {
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

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
