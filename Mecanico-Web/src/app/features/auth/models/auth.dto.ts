// ===== ENUMS =====
export type RoleCode = "CLIENT" | "PROVIDER_ADMIN" | "PLATFORM_ADMIN";
export type AccountType = "CLIENT" | "INDEPENDENT_MECHANIC" | "WORKSHOP";

// ===== REQUESTS =====
export type RegisterRequest = {
	email: string;
	password: string;
	first_name: string;
	last_name: string;
	account_type: AccountType;
	phone_number?: string | null;
	provider_profile?: ProviderProfileRequest | null;
};

export type ProviderProfileRequest = {
	business_name: string;
	legal_name?: string | null;
	description?: string | null;
	contact_email: string;
	contact_phone: string;
	city: string;
	address?: string | null;
	base_latitude?: number | null;
	base_longitude?: number | null;
	max_concurrent_services: number;
};

export type LoginRequest = {
	email: string;
	password: string;
};

// ===== RESPONSE WRAPPER (AUTH) =====
export type AuthResponse<T> = {
	success: boolean;
	message: string;
	data: T;
	meta: unknown;
};

// ===== SESSION =====
export type AuthSessionDto = {
	access_token: string;
	token_type: string;
	expires_in_minutes: number;
	user: UserDto;
};

// ===== USER =====
export type UserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	is_active: boolean;
	is_superuser: boolean;
	role_codes: RoleCode[];
	roles: RoleDto[];
	created_at: string;
	updated_at: string;
};

export type RoleDto = {
	id: string;
	code: RoleCode;
	name: string;
	description: string;
};
