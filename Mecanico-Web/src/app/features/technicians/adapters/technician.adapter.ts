import {
	CreateTechnicianFormValue,
	CreateTechnicianRequest,
	Technician,
	TechnicianDto,
	UpdateTechnicianFormValue,
	UpdateTechnicianRequest,
} from "../models/technician.types";

export function toTechnician(dto: TechnicianDto): Technician {
	return {
		id: dto.id,
		providerId: dto.provider_id,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
		specialty: dto.specialty,
		isActive: dto.is_active,
		isAvailable: dto.is_available,
		currentLatitude: dto.current_latitude,
		currentLongitude: dto.current_longitude,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toTechnicians(dtos: TechnicianDto[]): Technician[] {
	return dtos.map(toTechnician);
}

export function toCreateTechnicianRequest(
	formValue: CreateTechnicianFormValue
): CreateTechnicianRequest {
	return {
		first_name: formValue.firstName.trim(),
		last_name: formValue.lastName.trim(),
		phone_number: formValue.phoneNumber?.trim() || null,
		specialty: formValue.specialty.trim(),
		is_available: formValue.isAvailable,
		current_latitude: formValue.currentLatitude,
		current_longitude: formValue.currentLongitude,
	};
}

export function toUpdateTechnicianRequest(
	formValue: UpdateTechnicianFormValue
): UpdateTechnicianRequest {
	return {
		first_name: formValue.firstName.trim(),
		last_name: formValue.lastName.trim(),
		full_name:
			`${formValue.firstName.trim()} ${formValue.lastName.trim()}`.trim(),
		phone_number: formValue.phoneNumber?.trim() || null,
		specialty: formValue.specialty.trim(),
		is_active: formValue.isActive,
		is_available: formValue.isAvailable,
		current_latitude: formValue.currentLatitude,
		current_longitude: formValue.currentLongitude,
	};
}
