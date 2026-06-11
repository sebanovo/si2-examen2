export type TechnicianDto = {
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

export type Technician = {
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

export type CreateTechnicianRequest = {
	first_name: string;
	last_name: string;
	phone_number: string | null;
	specialty: string;
	is_available: boolean;
	current_latitude: number;
	current_longitude: number;
};

export type CreateTechnicianFormValue = {
	firstName: string;
	lastName: string;
	phoneNumber: string | null;
	specialty: string;
	isAvailable: boolean;
	currentLatitude: number;
	currentLongitude: number;
};

export type UpdateTechnicianRequest = {
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

export type UpdateTechnicianFormValue = {
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

export type TechniciansMetaDto = {
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
