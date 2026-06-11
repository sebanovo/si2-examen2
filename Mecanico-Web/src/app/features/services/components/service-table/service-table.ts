import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucidePencil } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";

import { ProviderService } from "../../models/service.types";

@Component({
	selector: "app-service-table",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports, HlmTableImports],
	providers: [provideIcons({ lucidePencil })],
	host: {
		style: "display: block",
	},
	templateUrl: "./service-table.html",
	styleUrl: "./service-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ServiceTable {
	readonly services = input.required<ProviderService[]>();

	readonly editService = output<ProviderService>();

	onEditService(service: ProviderService): void {
		this.editService.emit(service);
	}
}
