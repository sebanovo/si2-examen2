import { Component, inject, OnInit, signal } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideAlertCircle, lucideInbox, lucideSiren } from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { IncidentDetailDialog } from "../../components/incident-detail-dialog/incident-detail-dialog";
import { IncidentTable } from "../../components/incident-table/incident-table";
import { ProviderIncident } from "../../models/incident.types";
import { IncidentsStore } from "../../store/incident.store";

@Component({
	selector: "app-incident-list-page",
	standalone: true,
	imports: [
		NgIcon,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		IncidentTable,
		IncidentDetailDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideInbox,
			lucideSiren,
		}),
	],
	templateUrl: "./incident-list-page.html",
	styleUrl: "./incident-list-page.css",
})
export class IncidentListPage implements OnInit {
	readonly store = inject(IncidentsStore);

	readonly detailDialogOpen = signal(false);

	ngOnInit(): void {
		void this.store.loadMyProviderIncidents();
	}

	onRetry(): void {
		void this.store.loadMyProviderIncidents();
	}

	async onViewIncident(incident: ProviderIncident): Promise<void> {
		this.store.clearSelectedIncidentError();
		this.store.clearSelectedIncident();
		this.detailDialogOpen.set(true);

		const loadedIncident = await this.store.loadMyProviderIncidentById(
			incident.id
		);

		if (!loadedIncident) {
			toast("No se pudo cargar el incidente", {
				description:
					this.store.selectedIncidentError()?.message ||
					"Ocurrió un error inesperado.",
			});
		}
	}

	onDetailDialogOpenChange(isOpen: boolean): void {
		this.detailDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearSelectedIncidentError();
			this.store.clearSelectedIncident();
		}
	}
}
