import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { FormGroup, ReactiveFormsModule } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideLock, lucideRotateCcw, lucideSave } from "@ng-icons/lucide";
import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmCardImports } from "@shared/ui/card";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-profile-form-card",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmCardImports,
		HlmFieldImports,
		HlmInputImports,
	],
	host: {
		style: "display: block",
	},
	providers: [provideIcons({ lucideLock, lucideRotateCcw, lucideSave })],
	templateUrl: "./user-profile-form-card.html",
	styleUrl: "./user-profile-form-card.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UserProfileFormCard {
	readonly user = input.required<User | null>();
	readonly form = input.required<FormGroup>();
	readonly editMode = input(false);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly cancelClick = output<void>();
	readonly saveClick = output<void>();

	onCancelClick(): void {
		this.cancelClick.emit();
	}

	onSubmit(): void {
		this.saveClick.emit();
	}
}
