import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toCreateProviderMeTechnicianRequest,
	toProviderMe,
	toProviderMeTechnician,
	toProviderMeTechnicians,
	toUpdateProviderMeProfileRequest,
	toUpdateProviderMeTechnicianRequest,
} from "../adapters/provider-me.adapter";
import {
	CreateProviderMeTechnicianFormValue,
	ProviderMe,
	ProviderMeTechnician,
	ProviderMeTechniciansMetaDto,
	UpdateProviderMeProfileFormValue,
	UpdateProviderMeTechnicianFormValue,
} from "../models/provider-me.types";
import { ProviderMeApi } from "../services/provider-me.service";

@Injectable({
	providedIn: "root",
})
export class ProviderMeStore {
	private readonly providerMeApi = inject(ProviderMeApi);

	// MY PROVIDER PROFILE
	readonly myProvider = signal<ProviderMe | null>(null);
	readonly myProviderLoading = signal(false);
	readonly myProviderError = signal<AppHttpError | null>(null);
	readonly hasMyProviderError = computed(() => this.myProviderError() !== null);

	readonly updatingMyProvider = signal(false);
	readonly updatingMyProviderError = signal<AppHttpError | null>(null);
	readonly hasUpdatingMyProviderError = computed(
		() => this.updatingMyProviderError() !== null
	);

	// TECHNICIANS
	readonly technicians = signal<ProviderMeTechnician[]>([]);
	readonly techniciansMeta = signal<ProviderMeTechniciansMetaDto | null>(null);
	readonly techniciansLoading = signal(false);
	readonly techniciansHasLoaded = signal(false);
	readonly techniciansError = signal<AppHttpError | null>(null);
	readonly hasTechniciansError = computed(
		() => this.techniciansError() !== null
	);

	readonly techniciansCount = computed(
		() => this.techniciansMeta()?.count ?? this.technicians().length
	);

	readonly techniciansIsEmpty = computed(
		() =>
			this.techniciansHasLoaded() &&
			!this.techniciansLoading() &&
			this.technicians().length === 0
	);

	// CREATE TECHNICIAN
	readonly creatingTechnician = signal(false);
	readonly creatingTechnicianError = signal<AppHttpError | null>(null);
	readonly hasCreatingTechnicianError = computed(
		() => this.creatingTechnicianError() !== null
	);

	// UPDATE TECHNICIAN
	readonly updatingTechnician = signal(false);
	readonly updatingTechnicianError = signal<AppHttpError | null>(null);
	readonly hasUpdatingTechnicianError = computed(
		() => this.updatingTechnicianError() !== null
	);

	readonly selectedTechnician = signal<ProviderMeTechnician | null>(null);

	// LOAD MY PROVIDER
	async loadMyProviderProfile(): Promise<ProviderMe | null> {
		this.myProviderLoading.set(true);
		this.myProviderError.set(null);

		try {
			const providerDto = await firstValueFrom(
				this.providerMeApi.getMyProviderProfile()
			);

			const provider = toProviderMe(providerDto);

			this.myProvider.set(provider);

			return provider;
		} catch (error) {
			this.myProviderError.set(error as AppHttpError);
			this.myProvider.set(null);
			return null;
		} finally {
			this.myProviderLoading.set(false);
		}
	}

	// UPDATE MY PROVIDER
	async updateMyProviderProfile(
		formValue: UpdateProviderMeProfileFormValue
	): Promise<ProviderMe | null> {
		this.updatingMyProvider.set(true);
		this.updatingMyProviderError.set(null);

		try {
			const payload = toUpdateProviderMeProfileRequest(formValue);

			const providerDto = await firstValueFrom(
				this.providerMeApi.updateMyProviderProfile(payload)
			);

			const provider = toProviderMe(providerDto);

			this.myProvider.set(provider);

			return provider;
		} catch (error) {
			this.updatingMyProviderError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingMyProvider.set(false);
		}
	}

	// LOAD TECHNICIANS
	async loadMyTechnicians(): Promise<void> {
		this.techniciansLoading.set(true);
		this.techniciansError.set(null);

		try {
			const response = await firstValueFrom(
				this.providerMeApi.getMyTechnicians()
			);

			this.technicians.set(toProviderMeTechnicians(response.data));
			this.techniciansMeta.set(response.meta);
			this.techniciansHasLoaded.set(true);
		} catch (error) {
			this.techniciansError.set(error as AppHttpError);
			this.technicians.set([]);
			this.techniciansMeta.set(null);
			this.techniciansHasLoaded.set(true);
		} finally {
			this.techniciansLoading.set(false);
		}
	}

	// CREATE TECHNICIAN
	async createMyTechnician(
		formValue: CreateProviderMeTechnicianFormValue
	): Promise<ProviderMeTechnician | null> {
		this.creatingTechnician.set(true);
		this.creatingTechnicianError.set(null);

		try {
			const payload = toCreateProviderMeTechnicianRequest(formValue);

			const technicianDto = await firstValueFrom(
				this.providerMeApi.createMyTechnician(payload)
			);

			const technician = toProviderMeTechnician(technicianDto);

			this.technicians.update(current => [technician, ...current]);
			this.techniciansMeta.update(current => ({
				count: (current?.count ?? this.technicians().length - 1) + 1,
			}));

			this.syncMyProviderTechniciansCount(1, technician.isAvailable);

			return technician;
		} catch (error) {
			this.creatingTechnicianError.set(error as AppHttpError);
			return null;
		} finally {
			this.creatingTechnician.set(false);
		}
	}

	// UPDATE TECHNICIAN
	async updateMyTechnician(
		technicianId: string,
		formValue: UpdateProviderMeTechnicianFormValue
	): Promise<ProviderMeTechnician | null> {
		this.updatingTechnician.set(true);
		this.updatingTechnicianError.set(null);

		try {
			const payload = toUpdateProviderMeTechnicianRequest(formValue);

			const technicianDto = await firstValueFrom(
				this.providerMeApi.updateMyTechnician(technicianId, payload)
			);

			const technician = toProviderMeTechnician(technicianDto);

			const previousTechnician = this.technicians().find(
				item => item.id === technician.id
			);

			this.technicians.update(current =>
				current.map(item => (item.id === technician.id ? technician : item))
			);

			if (this.selectedTechnician()?.id === technician.id) {
				this.selectedTechnician.set(technician);
			}

			this.syncMyProviderTechnicianAvailability(
				previousTechnician?.isAvailable ?? technician.isAvailable,
				technician.isAvailable
			);

			return technician;
		} catch (error) {
			this.updatingTechnicianError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingTechnician.set(false);
		}
	}

	// INTERNAL SYNC
	private syncMyProviderTechniciansCount(
		incrementBy: number,
		isAvailable: boolean
	): void {
		this.myProvider.update(current => {
			if (!current) {
				return current;
			}

			return {
				...current,
				techniciansCount: current.techniciansCount + incrementBy,
				availableTechniciansCount: isAvailable
					? current.availableTechniciansCount + incrementBy
					: current.availableTechniciansCount,
			};
		});
	}

	private syncMyProviderTechnicianAvailability(
		previousIsAvailable: boolean,
		nextIsAvailable: boolean
	): void {
		if (previousIsAvailable === nextIsAvailable) {
			return;
		}

		this.myProvider.update(current => {
			if (!current) {
				return current;
			}

			const delta = nextIsAvailable ? 1 : -1;

			return {
				...current,
				availableTechniciansCount: Math.max(
					current.availableTechniciansCount + delta,
					0
				),
			};
		});
	}

	// CLEANERS

	clearMyProviderError(): void {
		this.myProviderError.set(null);
	}

	clearUpdatingMyProviderError(): void {
		this.updatingMyProviderError.set(null);
	}

	clearTechniciansError(): void {
		this.techniciansError.set(null);
	}

	clearCreatingTechnicianError(): void {
		this.creatingTechnicianError.set(null);
	}

	clearUpdatingTechnicianError(): void {
		this.updatingTechnicianError.set(null);
	}

	setSelectedTechnician(technician: ProviderMeTechnician | null): void {
		this.selectedTechnician.set(technician);
	}
}
