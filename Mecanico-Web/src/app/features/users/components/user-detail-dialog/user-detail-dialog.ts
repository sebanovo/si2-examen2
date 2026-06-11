import { Component, input, output } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideCalendar,
	lucideCheckCircle,
	lucideMail,
	lucidePencil,
	lucidePhone,
	lucideShield,
	lucideUser,
	lucideXCircle,
} from "@ng-icons/lucide";
import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmSkeletonImports } from "@shared/ui/skeleton";
import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-detail-dialog",
	imports: [
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmDialogImports,
		HlmSkeletonImports,
	],
	providers: [
		provideIcons({
			lucideUser,
			lucideMail,
			lucidePhone,
			lucideShield,
			lucideCalendar,
			lucidePencil,
			lucideCheckCircle,
			lucideXCircle,
		}),
	],
	templateUrl: "./user-detail-dialog.html",
	styleUrl: "./user-detail-dialog.css",
})
export class UserDetailDialog {
	readonly open = input.required<boolean>();
	readonly user = input<User | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly editUser = output<string>();

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}

	onEditUser(): void {
		const currentUser = this.user();

		if (!currentUser) {
			return;
		}

		this.editUser.emit(currentUser.id);
	}
}
