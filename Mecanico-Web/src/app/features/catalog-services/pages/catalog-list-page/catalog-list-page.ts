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

import { CatalogCreateDialog } from "../../components/catalog-create-dialog/catalog-create-dialog";
import { CatalogDetailDialog } from "../../components/catalog-detail-dialog/catalog-detail-dialog";
import { CatalogEditDialog } from "../../components/catalog-edit-dialog/catalog-edit-dialog";
import { CatalogTable } from "../../components/catalog-table/catalog-table";
import {
	CatalogService,
	CreateCatalogServiceFormValue,
	UpdateCatalogServiceFormValue,
} from "../../models/catalog-service.types";
import { CatalogServicesStore } from "../../store/catalog-service.store";

@Component({
	selector: "app-catalog-list-page",
	imports: [
		NgIcon,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		CatalogTable,
		CatalogCreateDialog,
		CatalogEditDialog,
		CatalogDetailDialog,
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
	templateUrl: "./catalog-list-page.html",
	styleUrl: "./catalog-list-page.css",
})
export class CatalogListPage implements OnInit {
	readonly store = inject(CatalogServicesStore);

	readonly createDialogOpen = signal(false);
	readonly editDialogOpen = signal(false);
	readonly detailDialogOpen = signal(false);

	readonly selectedCatalogServiceForEdit = signal<CatalogService | null>(null);

	ngOnInit(): void {
		void this.store.loadCatalogServices();
	}

	onRetry(): void {
		void this.store.loadCatalogServices();
	}

	onOpenCreateDialog(): void {
		this.store.clearCreatingCatalogServiceError();
		this.createDialogOpen.set(true);
	}

	onCreateDialogOpenChange(isOpen: boolean): void {
		this.createDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearCreatingCatalogServiceError();
		}
	}

	async onCreateCatalogService(
		formValue: CreateCatalogServiceFormValue
	): Promise<void> {
		const catalogService = await this.store.createCatalogService(formValue);

		if (!catalogService) {
			toast("No se pudo crear el servicio", {
				description:
					this.store.creatingCatalogServiceError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.createDialogOpen.set(false);
		toast.success("Servicio creado correctamente");
	}

	async onViewCatalogService(catalogService: CatalogService): Promise<void> {
		this.store.clearSelectedCatalogServiceError();
		this.store.clearSelectedCatalogService();
		this.detailDialogOpen.set(true);

		const loadedService = await this.store.loadCatalogServiceById(
			catalogService.id
		);

		if (!loadedService) {
			toast("No se pudo cargar el servicio", {
				description:
					this.store.selectedCatalogServiceError()?.message ||
					"Ocurrió un error inesperado.",
			});
		}
	}

	onDetailDialogOpenChange(isOpen: boolean): void {
		this.detailDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearSelectedCatalogServiceError();
			this.store.clearSelectedCatalogService();
		}
	}

	onOpenEditDialog(catalogService: CatalogService): void {
		this.store.clearUpdatingCatalogServiceError();
		this.selectedCatalogServiceForEdit.set(catalogService);
		this.editDialogOpen.set(true);
	}

	onEditDialogOpenChange(isOpen: boolean): void {
		this.editDialogOpen.set(isOpen);

		if (!isOpen) {
			this.selectedCatalogServiceForEdit.set(null);
			this.store.clearUpdatingCatalogServiceError();
		}
	}

	async onUpdateCatalogService(
		formValue: UpdateCatalogServiceFormValue
	): Promise<void> {
		const catalogService = this.selectedCatalogServiceForEdit();

		if (!catalogService) {
			return;
		}

		const updatedService = await this.store.updateCatalogService(
			catalogService.id,
			formValue
		);

		if (!updatedService) {
			toast("No se pudo actualizar el servicio", {
				description:
					this.store.updatingCatalogServiceError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.selectedCatalogServiceForEdit.set(updatedService);
		this.editDialogOpen.set(false);

		toast.success("Servicio actualizado correctamente");
	}

	onEditFromDetail(catalogService: CatalogService): void {
		this.detailDialogOpen.set(false);
		this.onOpenEditDialog(catalogService);
	}
}
