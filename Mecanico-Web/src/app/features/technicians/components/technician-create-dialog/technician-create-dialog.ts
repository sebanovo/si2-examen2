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
import { lucideSave, lucideUserPlus, lucideX } from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmSwitchImports } from "@shared/ui/switch";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import { CreateTechnicianFormValue } from "../../models/technician.types";

@Component({
	selector: "app-technician-create-dialog",
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
	providers: [provideIcons({ lucideUserPlus, lucideSave, lucideX })],
	templateUrl: "./technician-create-dialog.html",
	styleUrl: "./technician-create-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TechnicianCreateDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly createTechnician = output<CreateTechnicianFormValue>();

	readonly form = this.fb.nonNullable.group({
		firstName: ["", [Validators.required, Validators.maxLength(80)]],
		lastName: ["", [Validators.required, Validators.maxLength(80)]],
		phoneNumber: ["" as string | null, [Validators.maxLength(30)]],
		specialty: ["", [Validators.required, Validators.maxLength(120)]],
		isAvailable: [true],
		currentLatitude: [0, [Validators.required]],
		currentLongitude: [0, [Validators.required]],
	});

	constructor() {
		effect(() => {
			if (!this.open()) {
				this.form.reset({
					firstName: "",
					lastName: "",
					phoneNumber: "",
					specialty: "",
					isAvailable: true,
					currentLatitude: 0,
					currentLongitude: 0,
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

		this.createTechnician.emit(this.form.getRawValue());
	}
}
