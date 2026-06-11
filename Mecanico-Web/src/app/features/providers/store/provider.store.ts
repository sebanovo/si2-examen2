import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toGetProvidersParams,
	toOnboardProviderRequest,
	toProvider,
	toProviders,
	toUpdateProviderOperationsRequest,
} from "../adapters/provider.adapter";
import {
	OnboardProviderFormValue,
	Provider,
	ProvidersMetaDto,
	UpdateProviderOperationsFormValue,
} from "../models/provider.types";
import { ProvidersApi } from "../services/provider.service";

@Injectable({
	providedIn: "root",
})
export class ProvidersStore {
	private readonly providersApi = inject(ProvidersApi);

	// LISTADO
	readonly providers = signal<Provider[]>([]);
	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly isEmpty = computed(
		() => this.hasLoaded() && !this.loading() && this.providers().length === 0
	);

	// OPERATIONS
	readonly updatingProviderOperations = signal(false);
	readonly updatingProviderOperationsError = signal<AppHttpError | null>(null);
	readonly hasUpdatingProviderOperationsError = computed(
		() => this.updatingProviderOperationsError() !== null
	);

	// PAGINACIÓN

	readonly limit = signal(10);
	readonly offset = signal(0);
	readonly meta = signal<ProvidersMetaDto | null>(null);
	readonly lastPageReached = signal(false);

	readonly canGoPrevious = computed(() => this.offset() > 0 && !this.loading());

	readonly canGoNext = computed(
		() =>
			!this.loading() &&
			!this.lastPageReached() &&
			this.providers().length === this.limit()
	);

	readonly currentPageLabel = computed(() => {
		const start = this.offset() + 1;
		const end = this.offset() + this.providers().length;

		return this.providers().length === 0
			? "Sin resultados"
			: `Mostrando ${start} - ${end}`;
	});

	// DETALLE

	readonly selectedProvider = signal<Provider | null>(null);
	readonly selectedProviderLoading = signal(false);
	readonly selectedProviderError = signal<AppHttpError | null>(null);
	readonly hasSelectedProviderError = computed(
		() => this.selectedProviderError() !== null
	);

	// ONBOARDING
	readonly onboardingProvider = signal(false);
	readonly onboardingProviderError = signal<AppHttpError | null>(null);
	readonly hasOnboardingProviderError = computed(
		() => this.onboardingProviderError() !== null
	);

	// LOAD PROVIDERS
	async loadProviders(
		limit = this.limit(),
		offset = this.offset()
	): Promise<void> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const params = toGetProvidersParams(limit, offset);

			const response = await firstValueFrom(
				this.providersApi.getProviders(params)
			);

			const mappedProviders = toProviders(response.data);

			this.providers.set(mappedProviders);
			this.meta.set(response.meta);
			this.limit.set(response.meta.limit);
			this.offset.set(response.meta.offset);

			this.lastPageReached.set(mappedProviders.length < response.meta.limit);

			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.providers.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	// NEXT PAGE
	async nextPage(): Promise<void> {
		if (!this.canGoNext()) {
			return;
		}

		const currentProviders = this.providers();
		const currentOffset = this.offset();
		const nextOffset = currentOffset + this.limit();

		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.providersApi.getProviders({
					limit: this.limit(),
					offset: nextOffset,
				})
			);

			const mappedProviders = toProviders(response.data);

			if (mappedProviders.length === 0) {
				this.providers.set(currentProviders);
				this.offset.set(currentOffset);
				this.lastPageReached.set(true);
				return;
			}

			this.providers.set(mappedProviders);
			this.meta.set(response.meta);
			this.offset.set(response.meta.offset);
			this.limit.set(response.meta.limit);

			this.lastPageReached.set(mappedProviders.length < response.meta.limit);
		} catch (error) {
			this.error.set(error as AppHttpError);
		} finally {
			this.loading.set(false);
		}
	}

	// PREVIOUS PAGE
	async previousPage(): Promise<void> {
		if (!this.canGoPrevious()) {
			return;
		}

		const previousOffset = Math.max(this.offset() - this.limit(), 0);

		await this.loadProviders(this.limit(), previousOffset);
	}

	// DETALLE
	async loadProviderById(providerId: string): Promise<Provider | null> {
		this.selectedProviderLoading.set(true);
		this.selectedProviderError.set(null);
		this.selectedProvider.set(null);

		try {
			const providerDto = await firstValueFrom(
				this.providersApi.getProviderById(providerId)
			);

			const provider = toProvider(providerDto);

			this.selectedProvider.set(provider);

			return provider;
		} catch (error) {
			this.selectedProviderError.set(error as AppHttpError);
			this.selectedProvider.set(null);
			return null;
		} finally {
			this.selectedProviderLoading.set(false);
		}
	}

	// ONBOARDING
	async onboardProvider(
		formValue: OnboardProviderFormValue
	): Promise<Provider | null> {
		this.onboardingProvider.set(true);
		this.onboardingProviderError.set(null);

		try {
			const payload = toOnboardProviderRequest(formValue);

			const providerDto = await firstValueFrom(
				this.providersApi.onboardProvider(payload)
			);

			const provider = toProvider(providerDto);

			this.providers.update(current => {
				if (this.offset() !== 0) {
					return current;
				}

				return [provider, ...current].slice(0, this.limit());
			});

			this.selectedProvider.set(provider);

			return provider;
		} catch (error) {
			this.onboardingProviderError.set(error as AppHttpError);
			return null;
		} finally {
			this.onboardingProvider.set(false);
		}
	}

	async updateProviderOperations(
		providerId: string,
		formValue: UpdateProviderOperationsFormValue
	): Promise<Provider | null> {
		this.updatingProviderOperations.set(true);
		this.updatingProviderOperationsError.set(null);

		try {
			const payload = toUpdateProviderOperationsRequest(formValue);

			const providerDto = await firstValueFrom(
				this.providersApi.updateProviderOperations(providerId, payload)
			);

			const provider = toProvider(providerDto);

			this.selectedProvider.set(provider);

			this.providers.update(current =>
				current.map(item => (item.id === provider.id ? provider : item))
			);

			return provider;
		} catch (error) {
			this.updatingProviderOperationsError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingProviderOperations.set(false);
		}
	}

	// HELPERS PAGINACIÓN

	async reloadProviders(): Promise<void> {
		this.lastPageReached.set(false);
		await this.loadProviders(this.limit(), this.offset());
	}

	async resetPagination(): Promise<void> {
		this.offset.set(0);
		this.lastPageReached.set(false);
		await this.loadProviders(this.limit(), 0);
	}

	// CLEANERS

	clearError(): void {
		this.error.set(null);
	}

	clearSelectedProvider(): void {
		this.selectedProvider.set(null);
	}

	clearSelectedProviderError(): void {
		this.selectedProviderError.set(null);
	}

	clearOnboardingProviderError(): void {
		this.onboardingProviderError.set(null);
	}

	clearUpdatingProviderOperationsError(): void {
		this.updatingProviderOperationsError.set(null);
	}
}
