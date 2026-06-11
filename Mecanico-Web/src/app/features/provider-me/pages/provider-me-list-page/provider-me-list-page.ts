import { Component, inject, OnInit, signal } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideInbox,
	lucidePlus,
	lucideUsers,
} from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { ProviderMeCreateDialog } from "../../components/provider-me-create-dialog/provider-me-create-dialog";
import { ProviderMeEditDialog } from "../../components/provider-me-edit-dialog/provider-me-edit-dialog";
import { ProviderMeTable } from "../../components/provider-me-table/provider-me-table";
import {
	CreateProviderMeTechnicianFormValue,
	ProviderMeTechnician,
	UpdateProviderMeTechnicianFormValue,
} from "../../models/provider-me.types";
import { ProviderMeStore } from "../../store/provider-me.store";

@Component({
	selector: "app-provider-me-list-page",
	imports: [
		NgIcon,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		ProviderMeTable,
		ProviderMeCreateDialog,
		ProviderMeEditDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideInbox,
			lucidePlus,
			lucideUsers,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./provider-me-list-page.html",
	styleUrl: "./provider-me-list-page.css",
})
export class ProviderMeListPage implements OnInit {
	readonly store = inject(ProviderMeStore);

	readonly createDialogOpen = signal(false);
	readonly selectedTechnicianForEdit = signal<ProviderMeTechnician | null>(
		null
	);

	readonly editDialogOpen = signal(false);

	ngOnInit(): void {
		void this.store.loadMyTechnicians();
	}

	onRetry(): void {
		void this.store.loadMyTechnicians();
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
		formValue: CreateProviderMeTechnicianFormValue
	): Promise<void> {
		const technician = await this.store.createMyTechnician(formValue);

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

	onEditTechnician(technician: ProviderMeTechnician): void {
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
		formValue: UpdateProviderMeTechnicianFormValue
	): Promise<void> {
		const technician = this.selectedTechnicianForEdit();

		if (!technician) {
			return;
		}

		const updatedTechnician = await this.store.updateMyTechnician(
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
