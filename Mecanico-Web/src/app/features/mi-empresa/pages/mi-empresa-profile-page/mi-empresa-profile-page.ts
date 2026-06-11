import { Component, inject, OnInit, signal } from "@angular/core";
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideX } from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmSkeletonImports } from "@shared/ui/skeleton";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";

import { MiEmpresaActivityCard } from "../../components/mi-empresa-activity-card/mi-empresa-activity-card";
import { MiEmpresaFormCard } from "../../components/mi-empresa-form-card/mi-empresa-form-card";
import { MiEmpresaHero } from "../../components/mi-empresa-hero/mi-empresa-hero";
import { MiEmpresaMetricsCard } from "../../components/mi-empresa-metrics-card/mi-empresa-metrics-card";
import { MiEmpresaOwnerCard } from "../../components/mi-empresa-owner-card/mi-empresa-owner-card";
import { MiEmpresaStore } from "../../store/mi-empresa.store";

@Component({
	selector: "app-mi-empresa-profile-page",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmSkeletonImports,
		TableError,
		MiEmpresaHero,
		MiEmpresaFormCard,
		MiEmpresaOwnerCard,
		MiEmpresaMetricsCard,
		MiEmpresaActivityCard,
	],
	providers: [provideIcons({ lucideX })],
	host: {
		style: "display: block",
	},
	templateUrl: "./mi-empresa-profile-page.html",
	styleUrl: "./mi-empresa-profile-page.css",
})
export class MiEmpresaProfilePage implements OnInit {
	readonly store = inject(MiEmpresaStore);
	private readonly fb = inject(FormBuilder);

	readonly editMode = signal(false);

	readonly form = this.fb.nonNullable.group({
		businessName: ["", [Validators.required, Validators.maxLength(160)]],
		legalName: ["", [Validators.required, Validators.maxLength(160)]],
		description: ["" as string | null, [Validators.maxLength(500)]],
		contactEmail: ["", [Validators.required, Validators.email]],
		contactPhone: ["" as string | null, [Validators.maxLength(30)]],
		city: ["", [Validators.required, Validators.maxLength(80)]],
		address: ["", [Validators.required, Validators.maxLength(200)]],
		baseLatitude: [0, [Validators.required]],
		baseLongitude: [0, [Validators.required]],
		isAvailable: [true],
		maxConcurrentServices: [1, [Validators.required, Validators.min(1)]],
	});

	async ngOnInit(): Promise<void> {
		await this.loadEmpresa();
	}

	async loadEmpresa(): Promise<void> {
		const empresa = await this.store.loadMiEmpresa();

		if (empresa) {
			this.patchForm(empresa);
		}

		this.form.disable();
	}

	onRetry(): void {
		void this.loadEmpresa();
	}

	onEnableEdit(): void {
		this.editMode.set(true);
		this.form.enable();
	}

	onCancelEdit(): void {
		const empresa = this.store.miEmpresa();

		if (empresa) {
			this.patchForm(empresa);
		}

		this.form.disable();
		this.editMode.set(false);
		this.store.clearUpdateError();
	}

	async onSubmit(): Promise<void> {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		const updatedEmpresa = await this.store.updateMiEmpresa({
			businessName: this.form.controls.businessName.value,
			legalName: this.form.controls.legalName.value,
			description: this.form.controls.description.value || null,
			contactEmail: this.form.controls.contactEmail.value,
			contactPhone: this.form.controls.contactPhone.value || null,
			city: this.form.controls.city.value,
			address: this.form.controls.address.value,
			baseLatitude: this.form.controls.baseLatitude.value,
			baseLongitude: this.form.controls.baseLongitude.value,
			isAvailable: this.form.controls.isAvailable.value,
			maxConcurrentServices: this.form.controls.maxConcurrentServices.value,
		});

		if (!updatedEmpresa) {
			toast("No se pudo actualizar la empresa", {
				description:
					this.store.updateError()?.message || "Ocurrió un error inesperado.",
			});

			return;
		}

		this.patchForm(updatedEmpresa);
		this.form.disable();
		this.editMode.set(false);

		toast.success("Empresa actualizada correctamente");
	}

	private patchForm(
		empresa: NonNullable<ReturnType<MiEmpresaStore["miEmpresa"]>>
	): void {
		this.form.patchValue({
			businessName: empresa.businessName,
			legalName: empresa.legalName,
			description: empresa.description,
			contactEmail: empresa.contactEmail,
			contactPhone: empresa.contactPhone,
			city: empresa.city,
			address: empresa.address,
			baseLatitude: empresa.baseLatitude,
			baseLongitude: empresa.baseLongitude,
			isAvailable: empresa.isAvailable,
			maxConcurrentServices: empresa.maxConcurrentServices,
		});
	}
}
