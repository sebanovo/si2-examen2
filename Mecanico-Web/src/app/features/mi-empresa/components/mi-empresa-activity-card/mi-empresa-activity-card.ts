import { ChangeDetectionStrategy, Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideCalendar } from "@ng-icons/lucide";

import { HlmCardImports } from "@shared/ui/card";
import { MiEmpresa } from "../../models/mi-empresa.types";

@Component({
	selector: "app-mi-empresa-activity-card",
	imports: [NgIcon, HlmCardImports],
	providers: [provideIcons({ lucideCalendar })],
	host: {
		style: "display: block",
	},
	templateUrl: "./mi-empresa-activity-card.html",
	styleUrl: "./mi-empresa-activity-card.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MiEmpresaActivityCard {
	readonly empresa = input.required<MiEmpresa | null>();
}
