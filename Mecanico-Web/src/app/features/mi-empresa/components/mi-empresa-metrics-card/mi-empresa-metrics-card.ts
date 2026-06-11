import { ChangeDetectionStrategy, Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideActivity,
	lucideStar,
	lucideUsers,
	lucideWrench,
} from "@ng-icons/lucide";

import { HlmCardImports } from "@shared/ui/card";
import { MiEmpresa } from "../../models/mi-empresa.types";

@Component({
	selector: "app-mi-empresa-metrics-card",
	imports: [NgIcon, HlmCardImports],
	providers: [
		provideIcons({
			lucideUsers,
			lucideWrench,
			lucideActivity,
			lucideStar,
		}),
	],
	host: {
		style: "display: block",
	},
	changeDetection: ChangeDetectionStrategy.OnPush,
	templateUrl: "./mi-empresa-metrics-card.html",
	styleUrl: "./mi-empresa-metrics-card.css",
})
export class MiEmpresaMetricsCard {
	readonly empresa = input.required<MiEmpresa | null>();
}
