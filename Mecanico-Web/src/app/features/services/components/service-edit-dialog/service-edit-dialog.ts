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
	ProviderService,
	UpdateProviderServiceFormValue,
} from "../../models/service.types";

@Component({
	selector: "app-service-edit-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSwitchImports,
	],
	providers: [provideIcons({ lucideSettings2, lucideSave, lucideX })],
	host: {
		style: "display: contents",
	},
	templateUrl: "./service-edit-dialog.html",
	styleUrl: "./service-edit-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ServiceEditDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly providerService = input<ProviderService | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly updateService = output<UpdateProviderServiceFormValue>();

	readonly form = this.fb.nonNullable.group({
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
			const currentService = this.providerService();

			if (!currentService) {
				return;
			}

			this.form.patchValue({
				customTitle: currentService.customTitle,
				customDescription: currentService.customDescription,
				priceEstimateMin: currentService.priceEstimateMin,
				priceEstimateMax: currentService.priceEstimateMax,
				estimatedDurationMinutes: currentService.estimatedDurationMinutes,
				isMobileServiceEnabled: currentService.isMobileServiceEnabled,
				isEmergencyServiceEnabled: currentService.isEmergencyServiceEnabled,
				isActive: currentService.isActive,
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

		const value = this.form.getRawValue();

		if (value.priceEstimateMax < value.priceEstimateMin) {
			this.form.controls.priceEstimateMax.setErrors({ minPrice: true });
			return;
		}

		this.updateService.emit(value);
	}
}
