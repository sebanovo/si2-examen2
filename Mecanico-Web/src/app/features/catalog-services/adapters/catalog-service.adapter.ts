import {
	CatalogService,
	CatalogServiceDto,
	CreateCatalogServiceFormValue,
	CreateCatalogServiceRequest,
	UpdateCatalogServiceFormValue,
	UpdateCatalogServiceRequest,
} from "../models/catalog-service.types";

export function toCatalogService(dto: CatalogServiceDto): CatalogService {
	return {
		id: dto.id,
		code: dto.code,
		category: dto.category,
		title: dto.title,
		description: dto.description,
		supportsMobileService: dto.supports_mobile_service,
		supportsEmergencyService: dto.supports_emergency_service,
		isActive: dto.is_active,
		sortOrder: dto.sort_order,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
	};
}

export function toCatalogServices(dtos: CatalogServiceDto[]): CatalogService[] {
	return dtos.map(toCatalogService);
}

export function toCreateCatalogServiceRequest(
	formValue: CreateCatalogServiceFormValue
): CreateCatalogServiceRequest {
	return {
		code: formValue.code.trim().toUpperCase(),
		category: formValue.category.trim().toUpperCase(),
		title: formValue.title.trim(),
		description: formValue.description?.trim() || null,
		supports_mobile_service: formValue.supportsMobileService,
		supports_emergency_service: formValue.supportsEmergencyService,
		is_active: formValue.isActive,
		sort_order: formValue.sortOrder,
	};
}

export function toUpdateCatalogServiceRequest(
	formValue: UpdateCatalogServiceFormValue
): UpdateCatalogServiceRequest {
	return {
		category: formValue.category.trim().toUpperCase(),
		title: formValue.title.trim(),
		description: formValue.description?.trim() || null,
		supports_mobile_service: formValue.supportsMobileService,
		supports_emergency_service: formValue.supportsEmergencyService,
		is_active: formValue.isActive,
		sort_order: formValue.sortOrder,
	};
}
