import {
	GetProvidersParams,
	OnboardProviderFormValue,
	OnboardProviderRequest,
	Provider,
	ProviderDto,
	ProviderOwnerUser,
	ProviderOwnerUserDto,
	UpdateProviderOperationsFormValue,
	UpdateProviderOperationsRequest,
} from "../models/provider.types";

export function toProviderOwnerUser(
	dto: ProviderOwnerUserDto
): ProviderOwnerUser {
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

export function toProvider(dto: ProviderDto): Provider {
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
		ownerUser: toProviderOwnerUser(dto.owner_user),
		techniciansCount: dto.technicians_count,
		availableTechniciansCount: dto.available_technicians_count,
		configuredServicesCount: dto.configured_services_count,
		activeServicesCount: dto.active_services_count,
		activeServices: dto.active_services,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toProviders(dtos: ProviderDto[]): Provider[] {
	return dtos.map(toProvider);
}

export function toOnboardProviderRequest(
	formValue: OnboardProviderFormValue
): OnboardProviderRequest {
	return {
		admin_user: {
			email: formValue.adminUser.email.trim(),
			password: formValue.adminUser.password,
			first_name: formValue.adminUser.firstName.trim(),
			last_name: formValue.adminUser.lastName.trim(),
			phone_number: formValue.adminUser.phoneNumber?.trim() || null,
		},
		provider: {
			provider_type: formValue.provider.providerType,
			business_name: formValue.provider.businessName.trim(),
			legal_name: formValue.provider.legalName.trim(),
			description: formValue.provider.description?.trim() || null,
			contact_email: formValue.provider.contactEmail.trim(),
			contact_phone: formValue.provider.contactPhone?.trim() || null,
			city: formValue.provider.city.trim(),
			address: formValue.provider.address.trim(),
			base_latitude: formValue.provider.baseLatitude,
			base_longitude: formValue.provider.baseLongitude,
			max_concurrent_services: formValue.provider.maxConcurrentServices,
		},
	};
}

export function toGetProvidersParams(
	limit: number,
	offset: number
): GetProvidersParams {
	return {
		limit,
		offset,
	};
}

export function toUpdateProviderOperationsRequest(
	formValue: UpdateProviderOperationsFormValue
): UpdateProviderOperationsRequest {
	return {
		is_active: formValue.isActive,
		is_available: formValue.isAvailable,
		max_concurrent_services: formValue.maxConcurrentServices,
		current_active_services: formValue.currentActiveServices,
	};
}
