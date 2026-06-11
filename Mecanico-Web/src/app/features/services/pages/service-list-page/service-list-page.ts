import { Component, inject, OnInit, signal } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideInbox,
	lucidePlus,
	lucideSettings,
} from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { ServiceCreateDialog } from "../../components/service-create-dialog/service-create-dialog";
import { ServiceEditDialog } from "../../components/service-edit-dialog/service-edit-dialog";
import { ServiceTable } from "../../components/service-table/service-table";
import {
	CreateProviderServiceFormValue,
	ProviderService,
	UpdateProviderServiceFormValue,
} from "../../models/service.types";
import { ServicesStore } from "../../store/service.store";

@Component({
	selector: "app-service-list-page",
	imports: [
		NgIcon,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		ServiceTable,
		ServiceCreateDialog,
		ServiceEditDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideInbox,
			lucidePlus,
			lucideSettings,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./service-list-page.html",
	styleUrl: "./service-list-page.css",
})
export class ServiceListPage implements OnInit {
	readonly store = inject(ServicesStore);

	readonly createDialogOpen = signal(false);
	readonly editDialogOpen = signal(false);
	readonly selectedServiceForEdit = signal<ProviderService | null>(null);

	ngOnInit(): void {
		void this.store.loadServicesPageData();
	}

	onRetry(): void {
		void this.store.loadServicesPageData();
	}

	onOpenCreateDialog(): void {
		this.store.clearCreatingProviderServiceError();

		if (!this.store.catalogHasLoaded()) {
			void this.store.loadCatalogConfigurations();
		}

		this.createDialogOpen.set(true);
	}

	onCreateDialogOpenChange(isOpen: boolean): void {
		this.createDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearCreatingProviderServiceError();
		}
	}

	async onCreateService(
		formValue: CreateProviderServiceFormValue
	): Promise<void> {
		const service = await this.store.createMyProviderService(formValue);

		if (!service) {
			toast("No se pudo configurar el servicio", {
				description:
					this.store.creatingProviderServiceError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.createDialogOpen.set(false);
		toast.success("Servicio configurado correctamente");
	}

	onOpenEditDialog(service: ProviderService): void {
		this.store.clearUpdatingProviderServiceError();
		this.store.setSelectedProviderService(service);
		this.selectedServiceForEdit.set(service);
		this.editDialogOpen.set(true);
	}

	onEditDialogOpenChange(isOpen: boolean): void {
		this.editDialogOpen.set(isOpen);

		if (!isOpen) {
			this.selectedServiceForEdit.set(null);
			this.store.setSelectedProviderService(null);
			this.store.clearUpdatingProviderServiceError();
		}
	}

	async onUpdateService(
		formValue: UpdateProviderServiceFormValue
	): Promise<void> {
		const service = this.selectedServiceForEdit();

		if (!service) {
			return;
		}

		const updatedService = await this.store.updateMyProviderService(
			service.id,
			formValue
		);

		if (!updatedService) {
			toast("No se pudo actualizar el servicio", {
				description:
					this.store.updatingProviderServiceError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.selectedServiceForEdit.set(updatedService);
		this.editDialogOpen.set(false);

		toast.success("Servicio actualizado correctamente");
	}
}
