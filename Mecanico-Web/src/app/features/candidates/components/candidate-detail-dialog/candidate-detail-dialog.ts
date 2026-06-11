import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideCheck,
	lucideMapPin,
	lucideRoute,
	lucideSparkles,
	lucideStar,
	lucideWrench,
	lucideX,
	lucideXCircle,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { KeyValuePipe } from "@angular/common";
import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { AssignmentCandidate } from "../../models/candidate.types";

@Component({
	selector: "app-candidate-detail-dialog",
	standalone: true,
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDialogImports,
		HlmSkeletonImports,
		KeyValuePipe,
	],
	providers: [
		provideIcons({
			lucideMapPin,
			lucideRoute,
			lucideSparkles,
			lucideStar,
			lucideWrench,
			lucideCheck,
			lucideX,
			lucideXCircle,
		}),
	],
	host: {
		style: "display: contents",
	},
	templateUrl: "./candidate-detail-dialog.html",
	styleUrl: "./candidate-detail-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CandidateDetailDialog {
	readonly open = input.required<boolean>();
	readonly candidate = input<AssignmentCandidate | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);
	readonly acting = input(false);

	readonly openChange = output<boolean>();
	readonly acceptCandidate = output<AssignmentCandidate>();
	readonly rejectCandidate = output<AssignmentCandidate>();

	canAct(candidate: AssignmentCandidate): boolean {
		return candidate.status === "AVAILABLE" && !this.acting();
	}

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}

	onAcceptCandidate(): void {
		const candidate = this.candidate();

		if (!candidate) {
			return;
		}

		this.acceptCandidate.emit(candidate);
	}

	onRejectCandidate(): void {
		const candidate = this.candidate();

		if (!candidate) {
			return;
		}

		this.rejectCandidate.emit(candidate);
	}
}
