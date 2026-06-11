import { Component, inject, input, output } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideArchive,
	lucideEllipsis,
	lucideEye,
	lucideMailCheck,
	lucideMoreVertical,
	lucidePaperclip,
	lucidePencil,
	lucideShieldAlert,
	lucideUserPlus,
	lucideWrench,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";

import { Router } from "@angular/router";
import { HlmDropdownMenuImports } from "@shared/ui/dropdown-menu";
import { Provider } from "../../models/provider.types";
@Component({
	selector: "app-provider-table",
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmTableImports,
		HlmDropdownMenuImports,
	],
	providers: [
		provideIcons({
			lucideEye,
			lucidePencil,
			lucideUserPlus,
			lucideEllipsis,
			lucideArchive,
			lucideMailCheck,
			lucideMoreVertical,
			lucideWrench,
			lucideShieldAlert,
			lucidePaperclip,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./provider-table.html",
	styleUrl: "./provider-table.css",
})
export class ProviderTable {
	readonly providers = input.required<Provider[]>();
	readonly router = inject(Router);

	readonly viewProvider = output<Provider>();

	readonly editOperations = output<Provider>();

	onViewProvider(provider: Provider): void {
		this.viewProvider.emit(provider);
	}

	onEditOperations(provider: Provider): void {
		this.editOperations.emit(provider);
	}

	onAddTechnicias(provider: Provider): void {
		console.log("go to technicians click");
		this.router.navigate(["/app/providers", provider.id, "technicians"]);
	}

	onListarServicios(provider: Provider): void {
		console.log("go to technicians click");
		this.router.navigate(["/app/providers", provider.id, "services"]);
	}
}
