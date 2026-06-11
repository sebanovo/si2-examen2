import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import { toProviderServices } from "../adapters/provider-service.adapter";
import {
	ProviderService,
	ProviderServicesMetaDto,
} from "../models/provider-service.types";
import { ProviderServicesApi } from "../services/provider-service.service";

@Injectable({
	providedIn: "root",
})
export class ProviderServicesStore {
	private readonly providerServicesApi = inject(ProviderServicesApi);

	readonly providerId = signal<string | null>(null);

	// =============================
	// LISTADO
	// =============================

	readonly providerServices = signal<ProviderService[]>([]);
	readonly meta = signal<ProviderServicesMetaDto | null>(null);

	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly providerServicesCount = computed(
		() => this.meta()?.count ?? this.providerServices().length
	);

	readonly isEmpty = computed(
		() =>
			this.hasLoaded() &&
			!this.loading() &&
			this.providerServices().length === 0
	);

	// =============================
	// LOAD
	// =============================

	async loadProviderServices(providerId: string): Promise<void> {
		this.providerId.set(providerId);
		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.providerServicesApi.getProviderServices(providerId)
			);

			this.providerServices.set(toProviderServices(response.data));
			this.meta.set(response.meta);
			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.providerServices.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	// =============================
	// CLEANERS / HELPERS
	// =============================

	clearError(): void {
		this.error.set(null);
	}

	clearState(): void {
		this.providerId.set(null);
		this.providerServices.set([]);
		this.meta.set(null);
		this.loading.set(false);
		this.hasLoaded.set(false);
		this.error.set(null);
	}
}
