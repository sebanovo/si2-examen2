export type RoleDto = {
	id: string;
	code: string;
	name: string;
	description: string | null;
};

export type UserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	is_active: boolean;
	is_superuser: boolean;
	role_codes: string[];
	roles: RoleDto[];
	created_at: string;
	updated_at: string;
};

export type Role = {
	id: string;
	code: string;
	name: string;
	description: string | null;
};

export type User = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	isActive: boolean;
	isSuperuser: boolean;
	roleCodes: string[];
	roles: Role[];
	createdAt: string;
	updatedAt: string;
};

export type UpdateOwnProfileRequest = {
	first_name: string;
	last_name: string;
	phone_number: string | null;
};

export type UpdateOwnProfileFormValue = {
	firstName: string;
	lastName: string;
	phoneNumber: string | null;
};

export type GetUsersParams = {
	limit: number;
	offset: number;
};

export type UsersMetaDto = {
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
