import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toCreateProviderServiceRequest,
	toProviderService,
	toProviderServiceCatalogConfigurations,
	toProviderServices,
	toUpdateProviderServiceRequest,
} from "../adapters/service.adapter";
import {
	CreateProviderServiceFormValue,
	ProviderService,
	ProviderServiceCatalogConfiguration,
	ProviderServiceCatalogMetaDto,
	ProviderServicesMetaDto,
	UpdateProviderServiceFormValue,
} from "../models/service.types";
import { ServicesApi } from "../services/service.service";

@Injectable({
	providedIn: "root",
})
export class ServicesStore {
	private readonly servicesApi = inject(ServicesApi);

	readonly catalogConfigurations = signal<
		ProviderServiceCatalogConfiguration[]
	>([]);
	readonly catalogMeta = signal<ProviderServiceCatalogMetaDto | null>(null);
	readonly catalogLoading = signal(false);
	readonly catalogHasLoaded = signal(false);
	readonly catalogError = signal<AppHttpError | null>(null);
	readonly hasCatalogError = computed(() => this.catalogError() !== null);

	readonly providerServices = signal<ProviderService[]>([]);
	readonly providerServicesMeta = signal<ProviderServicesMetaDto | null>(null);
	readonly providerServicesLoading = signal(false);
	readonly providerServicesHasLoaded = signal(false);
	readonly providerServicesError = signal<AppHttpError | null>(null);
	readonly hasProviderServicesError = computed(
		() => this.providerServicesError() !== null
	);

	readonly providerServicesCount = computed(
		() => this.providerServicesMeta()?.count ?? this.providerServices().length
	);

	readonly providerServicesIsEmpty = computed(
		() =>
			this.providerServicesHasLoaded() &&
			!this.providerServicesLoading() &&
			this.providerServices().length === 0
	);

	readonly availableCatalogOptions = computed(() =>
		this.catalogConfigurations().filter(item => !item.isConfigured)
	);

	readonly configuredCatalogOptions = computed(() =>
		this.catalogConfigurations().filter(item => item.isConfigured)
	);

	readonly creatingProviderService = signal(false);
	readonly creatingProviderServiceError = signal<AppHttpError | null>(null);
	readonly hasCreatingProviderServiceError = computed(
		() => this.creatingProviderServiceError() !== null
	);

	readonly selectedProviderService = signal<ProviderService | null>(null);

	readonly updatingProviderService = signal(false);
	readonly updatingProviderServiceError = signal<AppHttpError | null>(null);
	readonly hasUpdatingProviderServiceError = computed(
		() => this.updatingProviderServiceError() !== null
	);

	async loadCatalogConfigurations(): Promise<void> {
		this.catalogLoading.set(true);
		this.catalogError.set(null);

		try {
			const response = await firstValueFrom(
				this.servicesApi.getMyCatalogWithConfiguration()
			);

			this.catalogConfigurations.set(
				toProviderServiceCatalogConfigurations(response.data)
			);
			this.catalogMeta.set(response.meta);
			this.catalogHasLoaded.set(true);
		} catch (error) {
			this.catalogError.set(error as AppHttpError);
			this.catalogConfigurations.set([]);
			this.catalogMeta.set(null);
			this.catalogHasLoaded.set(true);
		} finally {
			this.catalogLoading.set(false);
		}
	}

	async loadMyProviderServices(): Promise<void> {
		this.providerServicesLoading.set(true);
		this.providerServicesError.set(null);

		try {
			const response = await firstValueFrom(
				this.servicesApi.getMyProviderServices()
			);

			this.providerServices.set(toProviderServices(response.data));
			this.providerServicesMeta.set(response.meta);
			this.providerServicesHasLoaded.set(true);
		} catch (error) {
			this.providerServicesError.set(error as AppHttpError);
			this.providerServices.set([]);
			this.providerServicesMeta.set(null);
			this.providerServicesHasLoaded.set(true);
		} finally {
			this.providerServicesLoading.set(false);
		}
	}

	async loadServicesPageData(): Promise<void> {
		await Promise.all([
			this.loadCatalogConfigurations(),
			this.loadMyProviderServices(),
		]);
	}

	async createMyProviderService(
		formValue: CreateProviderServiceFormValue
	): Promise<ProviderService | null> {
		this.creatingProviderService.set(true);
		this.creatingProviderServiceError.set(null);

		try {
			const payload = toCreateProviderServiceRequest(formValue);

			const dto = await firstValueFrom(
				this.servicesApi.createMyProviderService(payload)
			);

			const providerService = toProviderService(dto);

			this.providerServices.update(current => [providerService, ...current]);
			this.providerServicesMeta.update(current => ({
				count: (current?.count ?? this.providerServices().length - 1) + 1,
			}));

			this.markCatalogItemAsConfigured(providerService);

			return providerService;
		} catch (error) {
			this.creatingProviderServiceError.set(error as AppHttpError);
			return null;
		} finally {
			this.creatingProviderService.set(false);
		}
	}

	async updateMyProviderService(
		providerServiceId: string,
		formValue: UpdateProviderServiceFormValue
	): Promise<ProviderService | null> {
		this.updatingProviderService.set(true);
		this.updatingProviderServiceError.set(null);

		try {
			const payload = toUpdateProviderServiceRequest(formValue);

			const dto = await firstValueFrom(
				this.servicesApi.updateMyProviderService(providerServiceId, payload)
			);

			const providerService = toProviderService(dto);

			this.providerServices.update(current =>
				current.map(item =>
					item.id === providerService.id ? providerService : item
				)
			);

			if (this.selectedProviderService()?.id === providerService.id) {
				this.selectedProviderService.set(providerService);
			}

			this.markCatalogItemAsConfigured(providerService);

			return providerService;
		} catch (error) {
			this.updatingProviderServiceError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingProviderService.set(false);
		}
	}

	private markCatalogItemAsConfigured(providerService: ProviderService): void {
		this.catalogConfigurations.update(current =>
			current.map(item =>
				item.catalogItem.id === providerService.serviceCatalogItemId
					? {
							...item,
							isConfigured: true,
							providerService,
						}
					: item
			)
		);
	}

	clearCatalogError(): void {
		this.catalogError.set(null);
	}

	clearProviderServicesError(): void {
		this.providerServicesError.set(null);
	}

	clearCreatingProviderServiceError(): void {
		this.creatingProviderServiceError.set(null);
	}

	clearUpdatingProviderServiceError(): void {
		this.updatingProviderServiceError.set(null);
	}

	setSelectedProviderService(providerService: ProviderService | null): void {
		this.selectedProviderService.set(providerService);
	}
}
