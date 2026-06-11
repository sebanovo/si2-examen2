import { RoleDto, UserDto } from "../models/auth.dto";
import { AuthUser, UserRole } from "../models/auth.types";

export function toUserRole(dto: RoleDto): UserRole {
	return {
		id: dto.id,
		code: dto.code,
		name: dto.name,
		description: dto.description,
	};
}

export function toAuthUser(dto: UserDto): AuthUser {
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
		roles: dto.roles.map(toUserRole),
		createdAt: dto.created_at,
		updatedAt: dto.updated_at,
	};
}
