import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideBuilding2,
	lucideCalendar,
	lucideCheckCircle,
	lucideMail,
	lucideMapPin,
	lucidePhone,
	lucideShield,
	lucideStar,
	lucideUser,
	lucideUsers,
	lucideWrench,
	lucideXCircle,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmSkeletonImports } from "@shared/ui/skeleton";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { Provider } from "../../models/provider.types";

@Component({
	selector: "app-provider-detail-dialog",
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDialogImports,
		HlmSkeletonImports,
	],
	providers: [
		provideIcons({
			lucideBuilding2,
			lucideMail,
			lucidePhone,
			lucideMapPin,
			lucideUser,
			lucideShield,
			lucideUsers,
			lucideWrench,
			lucideStar,
			lucideCalendar,
			lucideCheckCircle,
			lucideXCircle,
		}),
	],
	templateUrl: "./provider-detail-dialog.html",
	styleUrl: "./provider-detail-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProviderDetailDialog {
	readonly open = input.required<boolean>();
	readonly provider = input<Provider | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}
}
