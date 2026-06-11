import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toProviderIncident,
	toProviderIncidents,
} from "../adapters/incident.adapter";
import {
	ProviderIncident,
	ProviderIncidentsMetaDto,
} from "../models/incident.types";
import { IncidentsApi } from "../services/incident.service";

@Injectable({
	providedIn: "root",
})
export class IncidentsStore {
	private readonly incidentsApi = inject(IncidentsApi);

	readonly incidents = signal<ProviderIncident[]>([]);
	readonly meta = signal<ProviderIncidentsMetaDto | null>(null);

	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly count = computed(
		() => this.meta()?.count ?? this.incidents().length
	);

	readonly isEmpty = computed(
		() => this.hasLoaded() && !this.loading() && this.incidents().length === 0
	);

	readonly selectedIncident = signal<ProviderIncident | null>(null);
	readonly selectedIncidentLoading = signal(false);
	readonly selectedIncidentError = signal<AppHttpError | null>(null);
	readonly hasSelectedIncidentError = computed(
		() => this.selectedIncidentError() !== null
	);

	async loadMyProviderIncidents(): Promise<void> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.incidentsApi.getMyProviderIncidents()
			);

			this.incidents.set(toProviderIncidents(response.data));
			this.meta.set(response.meta);
			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.incidents.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	async loadMyProviderIncidentById(
		incidentId: string
	): Promise<ProviderIncident | null> {
		this.selectedIncidentLoading.set(true);
		this.selectedIncidentError.set(null);
		this.selectedIncident.set(null);

		try {
			const dto = await firstValueFrom(
				this.incidentsApi.getMyProviderIncidentById(incidentId)
			);

			const incident = toProviderIncident(dto);

			this.selectedIncident.set(incident);

			return incident;
		} catch (error) {
			this.selectedIncidentError.set(error as AppHttpError);
			this.selectedIncident.set(null);
			return null;
		} finally {
			this.selectedIncidentLoading.set(false);
		}
	}

	clearError(): void {
		this.error.set(null);
	}

	clearSelectedIncident(): void {
		this.selectedIncident.set(null);
	}

	clearSelectedIncidentError(): void {
		this.selectedIncidentError.set(null);
	}
}
