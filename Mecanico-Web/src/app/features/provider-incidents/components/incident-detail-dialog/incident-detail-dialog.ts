import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideCalendar,
	lucideCar,
	lucideClock,
	lucideMapPin,
	lucidePhone,
	lucideRoute,
	lucideSparkles,
	lucideUser,
	lucideWrench,
	lucideXCircle,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { ProviderIncident } from "../../models/incident.types";

@Component({
	selector: "app-incident-detail-dialog",
	standalone: true,
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDialogImports,
		HlmSkeletonImports,
	],
	providers: [
		provideIcons({
			lucideUser,
			lucideCar,
			lucideMapPin,
			lucidePhone,
			lucideWrench,
			lucideClock,
			lucideRoute,
			lucideSparkles,
			lucideCalendar,
			lucideXCircle,
		}),
	],
	host: {
		style: "display: contents",
	},
	templateUrl: "./incident-detail-dialog.html",
	styleUrl: "./incident-detail-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class IncidentDetailDialog {
	readonly open = input.required<boolean>();
	readonly incident = input<ProviderIncident | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}
}
