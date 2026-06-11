import { ChangeDetectionStrategy, Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideClock } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmTableImports } from "@shared/ui/table";

import { ProviderService } from "../../models/provider-service.types";

@Component({
	selector: "app-provider-service-table",
	imports: [NgIcon, HlmBadgeImports, HlmTableImports],
	providers: [provideIcons({ lucideClock })],
	host: {
		style: "display: block",
	},
	templateUrl: "./provider-service-table.html",
	styleUrl: "./provider-service-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProviderServiceTable {
	readonly providerServices = input.required<ProviderService[]>();
}
