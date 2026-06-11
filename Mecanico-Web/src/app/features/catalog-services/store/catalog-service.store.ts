import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toCatalogService,
	toCatalogServices,
	toCreateCatalogServiceRequest,
	toUpdateCatalogServiceRequest,
} from "../adapters/catalog-service.adapter";
import {
	CatalogService,
	CatalogServicesMetaDto,
	CreateCatalogServiceFormValue,
	UpdateCatalogServiceFormValue,
} from "../models/catalog-service.types";
import { CatalogServicesApi } from "../services/catalog-service.service";

@Injectable({
	providedIn: "root",
})
export class CatalogServicesStore {
	private readonly catalogServicesApi = inject(CatalogServicesApi);

	readonly catalogServices = signal<CatalogService[]>([]);
	readonly meta = signal<CatalogServicesMetaDto | null>(null);

	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly count = computed(
		() => this.meta()?.count ?? this.catalogServices().length
	);

	readonly includeInactive = computed(
		() => this.meta()?.include_inactive ?? false
	);

	readonly isEmpty = computed(
		() =>
			this.hasLoaded() && !this.loading() && this.catalogServices().length === 0
	);

	readonly selectedCatalogService = signal<CatalogService | null>(null);
	readonly selectedCatalogServiceLoading = signal(false);
	readonly selectedCatalogServiceError = signal<AppHttpError | null>(null);

	readonly creatingCatalogService = signal(false);
	readonly creatingCatalogServiceError = signal<AppHttpError | null>(null);
	readonly hasCreatingCatalogServiceError = computed(
		() => this.creatingCatalogServiceError() !== null
	);

	readonly updatingCatalogService = signal(false);
	readonly updatingCatalogServiceError = signal<AppHttpError | null>(null);
	readonly hasUpdatingCatalogServiceError = computed(
		() => this.updatingCatalogServiceError() !== null
	);

	async loadCatalogServices(): Promise<void> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.catalogServicesApi.getCatalogServices()
			);

			this.catalogServices.set(toCatalogServices(response.data));
			this.meta.set(response.meta);
			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.catalogServices.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	async loadCatalogServiceById(
		serviceCatalogItemId: string
	): Promise<CatalogService | null> {
		this.selectedCatalogServiceLoading.set(true);
		this.selectedCatalogServiceError.set(null);
		this.selectedCatalogService.set(null);

		try {
			const dto = await firstValueFrom(
				this.catalogServicesApi.getCatalogServiceById(serviceCatalogItemId)
			);

			const catalogService = toCatalogService(dto);

			this.selectedCatalogService.set(catalogService);

			return catalogService;
		} catch (error) {
			this.selectedCatalogServiceError.set(error as AppHttpError);
			this.selectedCatalogService.set(null);
			return null;
		} finally {
			this.selectedCatalogServiceLoading.set(false);
		}
	}

	async createCatalogService(
		formValue: CreateCatalogServiceFormValue
	): Promise<CatalogService | null> {
		this.creatingCatalogService.set(true);
		this.creatingCatalogServiceError.set(null);

		try {
			const payload = toCreateCatalogServiceRequest(formValue);

			const dto = await firstValueFrom(
				this.catalogServicesApi.createCatalogService(payload)
			);

			const catalogService = toCatalogService(dto);

			this.catalogServices.update(current => [catalogService, ...current]);
			this.meta.update(current => ({
				count: (current?.count ?? this.catalogServices().length - 1) + 1,
				include_inactive: current?.include_inactive ?? false,
			}));

			return catalogService;
		} catch (error) {
			this.creatingCatalogServiceError.set(error as AppHttpError);
			return null;
		} finally {
			this.creatingCatalogService.set(false);
		}
	}

	async updateCatalogService(
		serviceCatalogItemId: string,
		formValue: UpdateCatalogServiceFormValue
	): Promise<CatalogService | null> {
		this.updatingCatalogService.set(true);
		this.updatingCatalogServiceError.set(null);

		try {
			const payload = toUpdateCatalogServiceRequest(formValue);

			const dto = await firstValueFrom(
				this.catalogServicesApi.updateCatalogService(
					serviceCatalogItemId,
					payload
				)
			);

			const catalogService = toCatalogService(dto);

			this.catalogServices.update(current =>
				current.map(item =>
					item.id === catalogService.id ? catalogService : item
				)
			);

			if (this.selectedCatalogService()?.id === catalogService.id) {
				this.selectedCatalogService.set(catalogService);
			}

			return catalogService;
		} catch (error) {
			this.updatingCatalogServiceError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingCatalogService.set(false);
		}
	}

	clearError(): void {
		this.error.set(null);
	}

	clearSelectedCatalogService(): void {
		this.selectedCatalogService.set(null);
	}

	clearSelectedCatalogServiceError(): void {
		this.selectedCatalogServiceError.set(null);
	}

	clearCreatingCatalogServiceError(): void {
		this.creatingCatalogServiceError.set(null);
	}

	clearUpdatingCatalogServiceError(): void {
		this.updatingCatalogServiceError.set(null);
	}

	setSelectedCatalogService(catalogService: CatalogService | null): void {
		this.selectedCatalogService.set(catalogService);
	}
}
