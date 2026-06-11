import {
	MiEmpresa,
	MiEmpresaDto,
	MiEmpresaOwnerUser,
	MiEmpresaOwnerUserDto,
	UpdateMiEmpresaFormValue,
	UpdateMiEmpresaRequest,
} from "../models/mi-empresa.types";

export function toMiEmpresaOwnerUser(
	dto: MiEmpresaOwnerUserDto
): MiEmpresaOwnerUser {
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

export function toMiEmpresa(dto: MiEmpresaDto): MiEmpresa {
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
		ownerUser: toMiEmpresaOwnerUser(dto.owner_user),
		techniciansCount: dto.technicians_count,
		availableTechniciansCount: dto.available_technicians_count,
		configuredServicesCount: dto.configured_services_count,
		activeServicesCount: dto.active_services_count,
		activeServices: dto.active_services,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toUpdateMiEmpresaRequest(
	formValue: UpdateMiEmpresaFormValue
): UpdateMiEmpresaRequest {
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
