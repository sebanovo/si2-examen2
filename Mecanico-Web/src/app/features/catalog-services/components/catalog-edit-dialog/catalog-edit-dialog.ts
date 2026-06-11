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
import { lucideSave, lucideSettings2, lucideX } from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import {
	CatalogService,
	UpdateCatalogServiceFormValue,
} from "../../models/catalog-service.types";

@Component({
	selector: "app-catalog-edit-dialog",
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
	providers: [provideIcons({ lucideSettings2, lucideSave, lucideX })],
	templateUrl: "./catalog-edit-dialog.html",
	styleUrl: "./catalog-edit-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CatalogEditDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly catalogService = input<CatalogService | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly updateCatalogService = output<UpdateCatalogServiceFormValue>();

	readonly form = this.fb.nonNullable.group({
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
			const currentService = this.catalogService();

			if (!currentService) {
				return;
			}

			this.form.patchValue({
				category: currentService.category,
				title: currentService.title,
				description: currentService.description,
				supportsMobileService: currentService.supportsMobileService,
				supportsEmergencyService: currentService.supportsEmergencyService,
				isActive: currentService.isActive,
				sortOrder: currentService.sortOrder,
			});
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

		this.updateCatalogService.emit(this.form.getRawValue());
	}
}
