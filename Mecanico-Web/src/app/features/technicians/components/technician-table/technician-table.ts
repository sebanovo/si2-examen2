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

import { Technician } from "../../models/technician.types";

@Component({
	selector: "app-technician-table",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports, HlmTableImports],
	providers: [provideIcons({ lucidePencil, lucideMapPin })],
	host: {
		style: "display: block",
	},
	templateUrl: "./technician-table.html",
	styleUrl: "./technician-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TechnicianTable {
	readonly technicians = input.required<Technician[]>();

	readonly editTechnician = output<Technician>();

	onEditTechnician(technician: Technician): void {
		this.editTechnician.emit(technician);
	}
}
