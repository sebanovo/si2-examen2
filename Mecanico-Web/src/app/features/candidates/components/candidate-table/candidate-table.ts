import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideCheck,
	lucideEye,
	lucideMoreVertical,
	lucideX,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDropdownMenuImports } from "@shared/ui/dropdown-menu";
import { HlmTableImports } from "@shared/ui/table";

import { AssignmentCandidate } from "../../models/candidate.types";

@Component({
	selector: "app-candidate-table",
	standalone: true,
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDropdownMenuImports,
		HlmTableImports,
	],
	providers: [
		provideIcons({
			lucideEye,
			lucideCheck,
			lucideX,
			lucideMoreVertical,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./candidate-table.html",
	styleUrl: "./candidate-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CandidateTable {
	readonly candidates = input.required<AssignmentCandidate[]>();
	readonly actingCandidateIds = input<string[]>([]);

	readonly viewCandidate = output<AssignmentCandidate>();
	readonly acceptCandidate = output<AssignmentCandidate>();
	readonly rejectCandidate = output<AssignmentCandidate>();

	isCandidateActing(candidateId: string): boolean {
		return this.actingCandidateIds().includes(candidateId);
	}

	canAct(candidate: AssignmentCandidate): boolean {
		return (
			candidate.status === "AVAILABLE" && !this.isCandidateActing(candidate.id)
		);
	}

	onViewCandidate(candidate: AssignmentCandidate): void {
		this.viewCandidate.emit(candidate);
	}

	onAcceptCandidate(candidate: AssignmentCandidate): void {
		this.acceptCandidate.emit(candidate);
	}

	onRejectCandidate(candidate: AssignmentCandidate): void {
		this.rejectCandidate.emit(candidate);
	}
}
