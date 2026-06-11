import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideEye, lucideMapPin } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";

import { ProviderIncident } from "../../models/incident.types";

@Component({
	selector: "app-incident-table",
	standalone: true,
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports, HlmTableImports],
	providers: [provideIcons({ lucideEye, lucideMapPin })],
	host: {
		style: "display: block",
	},
	templateUrl: "./incident-table.html",
	styleUrl: "./incident-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class IncidentTable {
	readonly incidents = input.required<ProviderIncident[]>();

	readonly viewIncident = output<ProviderIncident>();

	onViewIncident(incident: ProviderIncident): void {
		this.viewIncident.emit(incident);
	}
}
