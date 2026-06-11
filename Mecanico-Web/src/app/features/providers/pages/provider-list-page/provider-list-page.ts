import { Component, inject, OnInit, signal } from "@angular/core";
import { Router } from "@angular/router";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideChevronLeft,
	lucideChevronRight,
	lucideInbox,
	lucidePlus,
	lucideStore,
} from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { ProviderDetailDialog } from "../../components/provider-detail-dialog/provider-detail-dialog";
import { ProviderOnboardingDialog } from "../../components/provider-onboarding-dialog/provider-onboarding-dialog";
import { ProviderOperationsDialog } from "../../components/provider-operations-dialog/provider-operations-dialog";
import { ProviderTable } from "../../components/provider-table/provider-table";
import {
	OnboardProviderFormValue,
	Provider,
	UpdateProviderOperationsFormValue,
} from "../../models/provider.types";
import { ProvidersStore } from "../../store/provider.store";

@Component({
	selector: "app-provider-list-page",
	imports: [
		NgIcon,
		ProviderTable,
		ProviderDetailDialog,
		HlmButtonImports,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		ProviderOperationsDialog,
		ProviderOnboardingDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideChevronLeft,
			lucideChevronRight,
			lucideInbox,
			lucidePlus,
			lucideStore,
		}),
	],
	templateUrl: "./provider-list-page.html",
	styleUrl: "./provider-list-page.css",
})
export class ProviderListPage implements OnInit {
	readonly store = inject(ProvidersStore);
	private readonly router = inject(Router);

	readonly viewDialogOpen = signal(false);

	readonly operationsDialogOpen = signal(false);
	readonly selectedProviderForOperations = signal<Provider | null>(null);

	readonly onboardingDialogOpen = signal(false);

	ngOnInit(): void {
		void this.store.loadProviders();
	}

	onRetry(): void {
		void this.store.reloadProviders();
	}

	onCreateProvider(): void {
		this.store.clearOnboardingProviderError();
		this.onboardingDialogOpen.set(true);
	}

	async onViewProvider(provider: Provider): Promise<void> {
		this.store.clearSelectedProviderError();
		this.store.clearSelectedProvider();
		this.viewDialogOpen.set(true);

		const loadedProvider = await this.store.loadProviderById(provider.id);

		if (!loadedProvider) {
			toast("No se pudo cargar el proveedor", {
				description:
					this.store.selectedProviderError()?.message ||
					"Ocurrió un error inesperado.",
			});
		}
	}

	onViewDialogOpenChange(isOpen: boolean): void {
		this.viewDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearSelectedProviderError();
			this.store.clearSelectedProvider();
		}
	}

	async onPreviousPage(): Promise<void> {
		await this.store.previousPage();
	}

	async onNextPage(): Promise<void> {
		const previousOffset = this.store.offset();

		await this.store.nextPage();

		if (
			this.store.offset() === previousOffset &&
			this.store.lastPageReached()
		) {
			toast("No hay más proveedores para mostrar");
		}
	}

	onEditOperations(provider: Provider): void {
		this.store.clearUpdatingProviderOperationsError();
		this.selectedProviderForOperations.set(provider);
		this.operationsDialogOpen.set(true);
	}

	onOperationsDialogOpenChange(isOpen: boolean): void {
		this.operationsDialogOpen.set(isOpen);

		if (!isOpen) {
			this.selectedProviderForOperations.set(null);
			this.store.clearUpdatingProviderOperationsError();
		}
	}

	async onSaveOperations(
		formValue: UpdateProviderOperationsFormValue
	): Promise<void> {
		const provider = this.selectedProviderForOperations();

		if (!provider) {
			return;
		}

		const updatedProvider = await this.store.updateProviderOperations(
			provider.id,
			formValue
		);

		if (!updatedProvider) {
			toast("No se pudieron actualizar las operaciones", {
				description:
					this.store.updatingProviderOperationsError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.selectedProviderForOperations.set(updatedProvider);
		this.operationsDialogOpen.set(false);

		toast.success("Operaciones actualizadas correctamente");
	}

	onOnboardingDialogOpenChange(isOpen: boolean): void {
		this.onboardingDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearOnboardingProviderError();
		}
	}

	async onOnboardProvider(formValue: OnboardProviderFormValue): Promise<void> {
		const provider = await this.store.onboardProvider(formValue);

		if (!provider) {
			toast("No se pudo registrar el proveedor", {
				description:
					this.store.onboardingProviderError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.onboardingDialogOpen.set(false);

		toast("Proveedor registrado correctamente");
	}
}
