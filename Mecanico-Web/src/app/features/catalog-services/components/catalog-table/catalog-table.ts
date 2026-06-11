import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideEye, lucidePencil } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";

import { CatalogService } from "../../models/catalog-service.types";

@Component({
	selector: "app-catalog-table",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports, HlmTableImports],
	providers: [provideIcons({ lucideEye, lucidePencil })],
	host: {
		style: "display: block",
	},
	templateUrl: "./catalog-table.html",
	styleUrl: "./catalog-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CatalogTable {
	readonly catalogServices = input.required<CatalogService[]>();

	readonly viewCatalogService = output<CatalogService>();
	readonly editCatalogService = output<CatalogService>();

	onViewCatalogService(catalogService: CatalogService): void {
		this.viewCatalogService.emit(catalogService);
	}

	onEditCatalogService(catalogService: CatalogService): void {
		this.editCatalogService.emit(catalogService);
	}
}
