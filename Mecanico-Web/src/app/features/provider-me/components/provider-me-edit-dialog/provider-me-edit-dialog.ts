import { Component, effect, inject, input, output } from "@angular/core";
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideSave, lucideUserCog, lucideX } from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import {
	ProviderMeTechnician,
	UpdateProviderMeTechnicianFormValue,
} from "../../models/provider-me.types";

@Component({
	selector: "app-provider-me-edit-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSwitchImports,
	],
	providers: [provideIcons({ lucideUserCog, lucideSave, lucideX })],
	templateUrl: "./provider-me-edit-dialog.html",
	styleUrl: "./provider-me-edit-dialog.css",
})
export class ProviderMeEditDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly technician = input<ProviderMeTechnician | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly updateTechnician = output<UpdateProviderMeTechnicianFormValue>();

	readonly form = this.fb.nonNullable.group({
		firstName: ["", [Validators.required, Validators.maxLength(80)]],
		lastName: ["", [Validators.required, Validators.maxLength(80)]],
		phoneNumber: ["" as string | null, [Validators.maxLength(30)]],
		specialty: ["", [Validators.required, Validators.maxLength(120)]],
		isActive: [true],
		isAvailable: [true],
		currentLatitude: [0, [Validators.required]],
		currentLongitude: [0, [Validators.required]],
	});

	constructor() {
		effect(() => {
			const currentTechnician = this.technician();

			if (!currentTechnician) {
				return;
			}

			this.form.patchValue({
				firstName: currentTechnician.firstName,
				lastName: currentTechnician.lastName,
				phoneNumber: currentTechnician.phoneNumber,
				specialty: currentTechnician.specialty,
				isActive: currentTechnician.isActive,
				isAvailable: currentTechnician.isAvailable,
				currentLatitude: currentTechnician.currentLatitude,
				currentLongitude: currentTechnician.currentLongitude,
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

		const formValue = this.form.getRawValue();

		this.updateTechnician.emit({
			...formValue,
			fullName:
				`${formValue.firstName.trim()} ${formValue.lastName.trim()}`.trim(),
		});
	}
}
