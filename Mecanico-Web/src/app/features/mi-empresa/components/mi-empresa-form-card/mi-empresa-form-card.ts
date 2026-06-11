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
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { MiEmpresa } from "../../models/mi-empresa.types";

@Component({
	selector: "app-mi-empresa-form-card",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmBadgeImports,
		HlmButtonImports,
		HlmCardImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSwitchImports,
	],
	host: {
		style: "display: block",
	},
	providers: [provideIcons({ lucideLock, lucideRotateCcw, lucideSave })],
	templateUrl: "./mi-empresa-form-card.html",
	styleUrl: "./mi-empresa-form-card.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MiEmpresaFormCard {
	readonly empresa = input.required<MiEmpresa | null>();
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
