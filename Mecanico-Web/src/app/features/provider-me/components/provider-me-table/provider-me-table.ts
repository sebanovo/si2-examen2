import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideMapPin, lucidePencil } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";

import { ProviderMeTechnician } from "../../models/provider-me.types";

@Component({
	selector: "app-provider-me-table",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports, HlmTableImports],
	providers: [provideIcons({ lucidePencil, lucideMapPin })],
	host: {
		style: "display: block",
	},
	templateUrl: "./provider-me-table.html",
	styleUrl: "./provider-me-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProviderMeTable {
	readonly technicians = input.required<ProviderMeTechnician[]>();

	readonly editTechnician = output<ProviderMeTechnician>();

	onEditTechnician(technician: ProviderMeTechnician): void {
		console.log("click en editar");
		this.editTechnician.emit(technician);
	}
}
