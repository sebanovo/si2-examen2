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
import { HlmSelectImports } from "@shared/ui/select";
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import {
	CreateProviderServiceFormValue,
	ProviderServiceCatalogConfiguration,
} from "../../models/service.types";

@Component({
	selector: "app-service-create-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSelectImports,
		HlmSwitchImports,
	],
	providers: [provideIcons({ lucideSettings, lucideSave, lucideX })],
	host: {
		style: "display: contents",
	},
	templateUrl: "./service-create-dialog.html",
	styleUrl: "./service-create-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ServiceCreateDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly catalogOptions =
		input.required<ProviderServiceCatalogConfiguration[]>();
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly createService = output<CreateProviderServiceFormValue>();

	readonly form = this.fb.nonNullable.group({
		serviceCatalogItemId: ["", [Validators.required]],
		customTitle: ["" as string | null, [Validators.maxLength(160)]],
		customDescription: ["" as string | null, [Validators.maxLength(500)]],
		priceEstimateMin: [0, [Validators.required, Validators.min(0)]],
		priceEstimateMax: [0, [Validators.required, Validators.min(0)]],
		estimatedDurationMinutes: [30, [Validators.required, Validators.min(1)]],
		isMobileServiceEnabled: [true],
		isEmergencyServiceEnabled: [true],
		isActive: [true],
	});

	constructor() {
		effect(() => {
			if (!this.open()) {
				this.form.reset({
					serviceCatalogItemId: "",
					customTitle: "",
					customDescription: "",
					priceEstimateMin: 0,
					priceEstimateMax: 0,
					estimatedDurationMinutes: 30,
					isMobileServiceEnabled: true,
					isEmergencyServiceEnabled: true,
					isActive: true,
				});
			}
		});
	}

	onOpenChange(value: boolean): void {
		this.openChange.emit(value);
	}

	onCatalogChange(catalogItemId: string): void {
		const selected = this.catalogOptions().find(
			item => item.catalogItem.id === catalogItemId
		);

		this.form.controls.serviceCatalogItemId.setValue(catalogItemId);

		if (!selected) {
			return;
		}

		this.form.patchValue({
			customTitle: selected.catalogItem.title,
			customDescription: selected.catalogItem.description,
			isMobileServiceEnabled: selected.catalogItem.supportsMobileService,
			isEmergencyServiceEnabled: selected.catalogItem.supportsEmergencyService,
		});
	}

	onSubmit(): void {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		const value = this.form.getRawValue();

		if (value.priceEstimateMax < value.priceEstimateMin) {
			this.form.controls.priceEstimateMax.setErrors({ minPrice: true });
			return;
		}

		this.createService.emit(value);
	}
}
