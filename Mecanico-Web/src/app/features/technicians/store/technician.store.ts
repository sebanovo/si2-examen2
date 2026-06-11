import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toCreateTechnicianRequest,
	toTechnician,
	toTechnicians,
	toUpdateTechnicianRequest,
} from "../adapters/technician.adapter";
import {
	CreateTechnicianFormValue,
	Technician,
	TechniciansMetaDto,
	UpdateTechnicianFormValue,
} from "../models/technician.types";
import { TechniciansApi } from "../services/technician.service";

@Injectable({
	providedIn: "root",
})
export class TechniciansStore {
	private readonly techniciansApi = inject(TechniciansApi);

	readonly providerId = signal<string | null>(null);

	// =============================
	// LISTADO
	// =============================

	readonly technicians = signal<Technician[]>([]);
	readonly meta = signal<TechniciansMetaDto | null>(null);

	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly techniciansCount = computed(
		() => this.meta()?.count ?? this.technicians().length
	);

	readonly isEmpty = computed(
		() => this.hasLoaded() && !this.loading() && this.technicians().length === 0
	);

	// =============================
	// CREATE
	// =============================

	readonly creatingTechnician = signal(false);
	readonly creatingTechnicianError = signal<AppHttpError | null>(null);
	readonly hasCreatingTechnicianError = computed(
		() => this.creatingTechnicianError() !== null
	);

	// =============================
	// UPDATE
	// =============================

	readonly selectedTechnician = signal<Technician | null>(null);

	readonly updatingTechnician = signal(false);
	readonly updatingTechnicianError = signal<AppHttpError | null>(null);
	readonly hasUpdatingTechnicianError = computed(
		() => this.updatingTechnicianError() !== null
	);

	// =============================
	// LOAD
	// =============================

	async loadProviderTechnicians(providerId: string): Promise<void> {
		this.providerId.set(providerId);
		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.techniciansApi.getProviderTechnicians(providerId)
			);

			this.technicians.set(toTechnicians(response.data));
			this.meta.set(response.meta);
			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.technicians.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	// =============================
	// CREATE
	// =============================

	async createProviderTechnician(
		formValue: CreateTechnicianFormValue
	): Promise<Technician | null> {
		const currentProviderId = this.providerId();

		if (!currentProviderId) {
			return null;
		}

		this.creatingTechnician.set(true);
		this.creatingTechnicianError.set(null);

		try {
			const payload = toCreateTechnicianRequest(formValue);

			const dto = await firstValueFrom(
				this.techniciansApi.createProviderTechnician(currentProviderId, payload)
			);

			const technician = toTechnician(dto);

			this.technicians.update(current => [technician, ...current]);
			this.meta.update(current => ({
				count: (current?.count ?? this.technicians().length - 1) + 1,
			}));

			return technician;
		} catch (error) {
			this.creatingTechnicianError.set(error as AppHttpError);
			return null;
		} finally {
			this.creatingTechnician.set(false);
		}
	}

	// =============================
	// UPDATE
	// =============================

	async updateProviderTechnician(
		technicianId: string,
		formValue: UpdateTechnicianFormValue
	): Promise<Technician | null> {
		const currentProviderId = this.providerId();

		if (!currentProviderId) {
			return null;
		}

		this.updatingTechnician.set(true);
		this.updatingTechnicianError.set(null);

		try {
			const payload = toUpdateTechnicianRequest(formValue);

			const dto = await firstValueFrom(
				this.techniciansApi.updateProviderTechnician(
					currentProviderId,
					technicianId,
					payload
				)
			);

			const technician = toTechnician(dto);

			this.technicians.update(current =>
				current.map(item => (item.id === technician.id ? technician : item))
			);

			if (this.selectedTechnician()?.id === technician.id) {
				this.selectedTechnician.set(technician);
			}

			return technician;
		} catch (error) {
			this.updatingTechnicianError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingTechnician.set(false);
		}
	}

	// =============================
	// CLEANERS / HELPERS
	// =============================

	clearError(): void {
		this.error.set(null);
	}

	clearCreatingTechnicianError(): void {
		this.creatingTechnicianError.set(null);
	}

	clearUpdatingTechnicianError(): void {
		this.updatingTechnicianError.set(null);
	}

	setSelectedTechnician(technician: Technician | null): void {
		this.selectedTechnician.set(technician);
	}

	clearState(): void {
		this.providerId.set(null);
		this.technicians.set([]);
		this.meta.set(null);
		this.loading.set(false);
		this.hasLoaded.set(false);
		this.error.set(null);
		this.creatingTechnician.set(false);
		this.creatingTechnicianError.set(null);
		this.selectedTechnician.set(null);
		this.updatingTechnician.set(false);
		this.updatingTechnicianError.set(null);
	}
}
