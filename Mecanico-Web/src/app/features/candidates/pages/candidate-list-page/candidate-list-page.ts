import { Component, inject, OnInit, signal } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideInbox,
	lucideListChecks,
} from "@ng-icons/lucide";
import { toast } from "@spartan-ng/brain/sonner";

import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { CandidateDetailDialog } from "../../components/candidate-detail-dialog/candidate-detail-dialog";
import { CandidateTable } from "../../components/candidate-table/candidate-table";
import { AssignmentCandidate } from "../../models/candidate.types";
import { CandidatesStore } from "../../store/candidate.store";

@Component({
	selector: "app-candidate-list-page",
	standalone: true,
	imports: [
		NgIcon,
		HlmCardImports,
		HlmSkeletonImports,
		CardHeader,
		TableError,
		EmptyState,
		CandidateTable,
		CandidateDetailDialog,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideInbox,
			lucideListChecks,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./candidate-list-page.html",
	styleUrl: "./candidate-list-page.css",
})
export class CandidateListPage implements OnInit {
	readonly store = inject(CandidatesStore);

	readonly detailDialogOpen = signal(false);

	ngOnInit(): void {
		void this.store.loadAvailableCandidates();
	}

	onRetry(): void {
		void this.store.loadAvailableCandidates();
	}

	async onViewCandidate(candidate: AssignmentCandidate): Promise<void> {
		this.store.clearSelectedCandidateError();
		this.store.clearSelectedCandidate();
		this.detailDialogOpen.set(true);

		const loadedCandidate = await this.store.loadAvailableCandidateById(
			candidate.id
		);

		if (!loadedCandidate) {
			toast("No se pudo cargar el candidato", {
				description:
					this.store.selectedCandidateError()?.message ||
					"Ocurrió un error inesperado.",
			});
		}
	}

	onDetailDialogOpenChange(isOpen: boolean): void {
		this.detailDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearSelectedCandidateError();
			this.store.clearSelectedCandidate();
		}
	}

	async onAcceptCandidate(candidate: AssignmentCandidate): Promise<void> {
		const result = await this.store.acceptCandidate(candidate.id);

		if (!result) {
			toast("No se pudo aceptar el candidato", {
				description:
					this.store.acceptingCandidateError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		toast("Candidato aceptado correctamente");
	}

	async onRejectCandidate(candidate: AssignmentCandidate): Promise<void> {
		const result = await this.store.rejectCandidate(candidate.id);

		if (!result) {
			toast("No se pudo rechazar el candidato", {
				description:
					this.store.rejectingCandidateError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		toast("Candidato rechazado correctamente");
	}
}
