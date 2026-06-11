import {
	ChangeDetectionStrategy,
	Component,
	effect,
	inject,
	input,
	output,
} from "@angular/core";
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideSave, lucideSettings, lucideX } from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { CreateCatalogServiceFormValue } from "../../models/catalog-service.types";

@Component({
	selector: "app-catalog-create-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSwitchImports,
	],
	host: {
		style: "display: contents",
	},
	providers: [provideIcons({ lucideSettings, lucideSave, lucideX })],
	templateUrl: "./catalog-create-dialog.html",
	styleUrl: "./catalog-create-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CatalogCreateDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly createCatalogService = output<CreateCatalogServiceFormValue>();

	readonly form = this.fb.nonNullable.group({
		code: ["", [Validators.required, Validators.maxLength(50)]],
		category: ["", [Validators.required, Validators.maxLength(80)]],
		title: ["", [Validators.required, Validators.maxLength(160)]],
		description: ["" as string | null, [Validators.maxLength(500)]],
		supportsMobileService: [true],
		supportsEmergencyService: [true],
		isActive: [true],
		sortOrder: [0, [Validators.required, Validators.min(0)]],
	});

	constructor() {
		effect(() => {
			if (!this.open()) {
				this.form.reset({
					code: "",
					category: "",
					title: "",
					description: "",
					supportsMobileService: true,
					supportsEmergencyService: true,
					isActive: true,
					sortOrder: 0,
				});
			}
		});
	}

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}

	onSubmit(): void {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		this.createCatalogService.emit(this.form.getRawValue());
	}
}
