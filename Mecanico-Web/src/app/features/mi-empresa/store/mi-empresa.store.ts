import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toMiEmpresa,
	toUpdateMiEmpresaRequest,
} from "../adapters/mi-empresa.adapter";
import {
	MiEmpresa,
	UpdateMiEmpresaFormValue,
} from "../models/mi-empresa.types";
import { MiEmpresaApi } from "../services/mi-empresa.service";

@Injectable({
	providedIn: "root",
})
export class MiEmpresaStore {
	private readonly miEmpresaApi = inject(MiEmpresaApi);

	readonly miEmpresa = signal<MiEmpresa | null>(null);
	readonly loading = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly updating = signal(false);
	readonly updateError = signal<AppHttpError | null>(null);
	readonly hasUpdateError = computed(() => this.updateError() !== null);

	async loadMiEmpresa(): Promise<MiEmpresa | null> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const dto = await firstValueFrom(this.miEmpresaApi.getMiEmpresaProfile());

			const empresa = toMiEmpresa(dto);

			this.miEmpresa.set(empresa);

			return empresa;
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.miEmpresa.set(null);
			return null;
		} finally {
			this.loading.set(false);
		}
	}

	async updateMiEmpresa(
		formValue: UpdateMiEmpresaFormValue
	): Promise<MiEmpresa | null> {
		this.updating.set(true);
		this.updateError.set(null);

		try {
			const payload = toUpdateMiEmpresaRequest(formValue);

			const dto = await firstValueFrom(
				this.miEmpresaApi.updateMiEmpresaProfile(payload)
			);

			const empresa = toMiEmpresa(dto);

			this.miEmpresa.set(empresa);

			return empresa;
		} catch (error) {
			this.updateError.set(error as AppHttpError);
			return null;
		} finally {
			this.updating.set(false);
		}
	}

	clearError(): void {
		this.error.set(null);
	}

	clearUpdateError(): void {
		this.updateError.set(null);
	}
}
