import { Component, inject, OnDestroy, OnInit, signal } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideArrowLeft,
	lucideInbox,
	lucidePlus,
	lucideUsers,
} from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { TechnicianCreateDialog } from "../../components/technician-create-dialog/technician-create-dialog";
import { TechnicianEditDialog } from "../../components/technician-edit-dialog/technician-edit-dialog";
import { TechnicianTable } from "../../components/technician-table/technician-table";
import {
	CreateTechnicianFormValue,
	Technician,
	UpdateTechnicianFormValue,
} from "../../models/technician.types";
import { TechniciansStore } from "../../store/technician.store";

@Component({
	selector: "app-technician-list-page",
	imports: [
		NgIcon,
		HlmButtonImports,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		TechnicianTable,
		TechnicianCreateDialog,
		TechnicianEditDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideArrowLeft,
			lucideInbox,
			lucidePlus,
			lucideUsers,
		}),
	],

	templateUrl: "./technician-list-page.html",
	styleUrl: "./technician-list-page.css",
})
export class TechnicianListPage implements OnInit, OnDestroy {
	readonly store = inject(TechniciansStore);
	private readonly route = inject(ActivatedRoute);
	private readonly router = inject(Router);

	readonly createDialogOpen = signal(false);
	readonly editDialogOpen = signal(false);
	readonly selectedTechnicianForEdit = signal<Technician | null>(null);

	readonly providerId = signal<string | null>(null);

	ngOnInit(): void {
		const providerId = this.route.snapshot.paramMap.get("id");

		if (!providerId) {
			void this.router.navigate(["/app", "providers"]);
			return;
		}

		this.providerId.set(providerId);
		void this.store.loadProviderTechnicians(providerId);
	}

	ngOnDestroy(): void {
		this.store.clearState();
	}

	onBack(): void {
		void this.router.navigate(["/app", "providers"]);
	}

	onRetry(): void {
		const providerId = this.providerId();

		if (!providerId) {
			return;
		}

		void this.store.loadProviderTechnicians(providerId);
	}

	onOpenCreateDialog(): void {
		this.store.clearCreatingTechnicianError();
		this.createDialogOpen.set(true);
	}

	onCreateDialogOpenChange(isOpen: boolean): void {
		this.createDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearCreatingTechnicianError();
		}
	}

	async onCreateTechnician(
		formValue: CreateTechnicianFormValue
	): Promise<void> {
		const technician = await this.store.createProviderTechnician(formValue);

		if (!technician) {
			toast("No se pudo registrar el técnico", {
				description:
					this.store.creatingTechnicianError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.createDialogOpen.set(false);
		toast("Técnico registrado correctamente");
	}

	onEditTechnician(technician: Technician): void {
		this.store.clearUpdatingTechnicianError();
		this.store.setSelectedTechnician(technician);
		this.selectedTechnicianForEdit.set(technician);
		this.editDialogOpen.set(true);
	}

	onEditDialogOpenChange(isOpen: boolean): void {
		this.editDialogOpen.set(isOpen);

		if (!isOpen) {
			this.selectedTechnicianForEdit.set(null);
			this.store.setSelectedTechnician(null);
			this.store.clearUpdatingTechnicianError();
		}
	}

	async onUpdateTechnician(
		formValue: UpdateTechnicianFormValue
	): Promise<void> {
		const technician = this.selectedTechnicianForEdit();

		if (!technician) {
			return;
		}

		const updatedTechnician = await this.store.updateProviderTechnician(
			technician.id,
			formValue
		);

		if (!updatedTechnician) {
			toast("No se pudo actualizar el técnico", {
				description:
					this.store.updatingTechnicianError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.selectedTechnicianForEdit.set(updatedTechnician);
		this.editDialogOpen.set(false);

		toast.success("Técnico actualizado correctamente");
	}
}
