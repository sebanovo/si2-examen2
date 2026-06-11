import {
	CreateProviderMeTechnicianFormValue,
	CreateProviderMeTechnicianRequest,
	ProviderMe,
	ProviderMeDto,
	ProviderMeOwnerUser,
	ProviderMeOwnerUserDto,
	ProviderMeTechnician,
	ProviderMeTechnicianDto,
	UpdateProviderMeProfileFormValue,
	UpdateProviderMeProfileRequest,
	UpdateProviderMeTechnicianFormValue,
	UpdateProviderMeTechnicianRequest,
} from "../models/provider-me.types";

export function toProviderMeOwnerUser(
	dto: ProviderMeOwnerUserDto
): ProviderMeOwnerUser {
	return {
		id: dto.id,
		email: dto.email,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
		isActive: dto.is_active,
	};
}

export function toProviderMe(dto: ProviderMeDto): ProviderMe {
	return {
		id: dto.id,
		ownerUserId: dto.owner_user_id,
		providerType: dto.provider_type,
		businessName: dto.business_name,
		legalName: dto.legal_name,
		description: dto.description,
		contactEmail: dto.contact_email,
		contactPhone: dto.contact_phone,
		city: dto.city,
		address: dto.address,
		baseLatitude: dto.base_latitude,
		baseLongitude: dto.base_longitude,
		isActive: dto.is_active,
		isAvailable: dto.is_available,
		maxConcurrentServices: dto.max_concurrent_services,
		currentActiveServices: dto.current_active_services,
		availableCapacity: dto.available_capacity,
		averageRating: dto.average_rating,
		ownerUser: toProviderMeOwnerUser(dto.owner_user),
		techniciansCount: dto.technicians_count,
		availableTechniciansCount: dto.available_technicians_count,
		configuredServicesCount: dto.configured_services_count,
		activeServicesCount: dto.active_services_count,
		activeServices: dto.active_services,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toProviderMeTechnician(
	dto: ProviderMeTechnicianDto
): ProviderMeTechnician {
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

export function toProviderMeTechnicians(
	dtos: ProviderMeTechnicianDto[]
): ProviderMeTechnician[] {
	return dtos.map(toProviderMeTechnician);
}

export function toUpdateProviderMeProfileRequest(
	formValue: UpdateProviderMeProfileFormValue
): UpdateProviderMeProfileRequest {
	return {
		business_name: formValue.businessName.trim(),
		legal_name: formValue.legalName.trim(),
		description: formValue.description?.trim() || null,
		contact_email: formValue.contactEmail.trim(),
		contact_phone: formValue.contactPhone?.trim() || null,
		city: formValue.city.trim(),
		address: formValue.address.trim(),
		base_latitude: formValue.baseLatitude,
		base_longitude: formValue.baseLongitude,
		is_available: formValue.isAvailable,
		max_concurrent_services: formValue.maxConcurrentServices,
	};
}

export function toCreateProviderMeTechnicianRequest(
	formValue: CreateProviderMeTechnicianFormValue
): CreateProviderMeTechnicianRequest {
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

export function toUpdateProviderMeTechnicianRequest(
	formValue: UpdateProviderMeTechnicianFormValue
): UpdateProviderMeTechnicianRequest {
	return {
		first_name: formValue.firstName.trim(),
		last_name: formValue.lastName.trim(),
		full_name: formValue.fullName.trim(),
		phone_number: formValue.phoneNumber?.trim() || null,
		specialty: formValue.specialty.trim(),
		is_active: formValue.isActive,
		is_available: formValue.isAvailable,
		current_latitude: formValue.currentLatitude,
		current_longitude: formValue.currentLongitude,
	};
}
