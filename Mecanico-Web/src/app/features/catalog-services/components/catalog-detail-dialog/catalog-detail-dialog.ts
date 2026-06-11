import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideCalendar,
	lucideCheckCircle,
	lucideHash,
	lucideSettings,
	lucideTag,
	lucideXCircle,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { CatalogService } from "../../models/catalog-service.types";

@Component({
	selector: "app-catalog-detail-dialog",
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDialogImports,
		HlmSkeletonImports,
	],
	providers: [
		provideIcons({
			lucideSettings,
			lucideHash,
			lucideTag,
			lucideCalendar,
			lucideCheckCircle,
			lucideXCircle,
		}),
	],
	host: {
		style: "display: contents",
	},
	templateUrl: "./catalog-detail-dialog.html",
	styleUrl: "./catalog-detail-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CatalogDetailDialog {
	readonly open = input.required<boolean>();
	readonly catalogService = input<CatalogService | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly editCatalogService = output<CatalogService>();

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}

	onEditCatalogService(): void {
		const currentService = this.catalogService();

		if (!currentService) {
			return;
		}

		this.editCatalogService.emit(currentService);
	}
}
