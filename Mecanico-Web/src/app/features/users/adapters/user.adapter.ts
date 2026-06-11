import {
	GetUsersParams,
	Role,
	RoleDto,
	UpdateOwnProfileFormValue,
	UpdateOwnProfileRequest,
	User,
	UserDto,
} from "../models/user.types";

export function toRole(dto: RoleDto): Role {
	return {
		id: dto.id,
		code: dto.code,
		name: dto.name,
		description: dto.description,
	};
}

export function toRoles(dtos: RoleDto[]): Role[] {
	return dtos.map(toRole);
}

export function toUser(dto: UserDto): User {
	return {
		id: dto.id,
		email: dto.email,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
		isActive: dto.is_active,
		isSuperuser: dto.is_superuser,
		roleCodes: dto.role_codes,
		roles: toRoles(dto.roles),
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toUsers(dtos: UserDto[]): User[] {
	return dtos.map(toUser);
}

export function toUpdateOwnProfileRequest(
	formValue: UpdateOwnProfileFormValue
): UpdateOwnProfileRequest {
	return {
		first_name: formValue.firstName.trim(),
		last_name: formValue.lastName.trim(),
		phone_number: formValue.phoneNumber?.trim() || null,
	};
}

export function toGetUsersParams(
	limit: number,
	offset: number
): GetUsersParams {
	return {
		limit,
		offset,
	};
}
