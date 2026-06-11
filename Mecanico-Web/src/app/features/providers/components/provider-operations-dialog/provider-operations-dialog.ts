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
import {
	Provider,
	UpdateProviderOperationsFormValue,
} from "../../models/provider.types";

@Component({
	selector: "app-provider-operations-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmSwitchImports,
	],
	providers: [provideIcons({ lucideSave, lucideSettings, lucideX })],
	templateUrl: "./provider-operations-dialog.html",
	styleUrl: "./provider-operations-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProviderOperationsDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly provider = input<Provider | null>(null);
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly saveOperations = output<UpdateProviderOperationsFormValue>();

	readonly form = this.fb.nonNullable.group({
		isActive: [true],
		isAvailable: [true],
		maxConcurrentServices: [1, [Validators.required, Validators.min(1)]],
		currentActiveServices: [0, [Validators.required, Validators.min(0)]],
	});

	constructor() {
		effect(() => {
			const currentProvider = this.provider();

			if (!currentProvider) {
				return;
			}

			this.form.patchValue({
				isActive: currentProvider.isActive,
				isAvailable: currentProvider.isAvailable,
				maxConcurrentServices: currentProvider.maxConcurrentServices,
				currentActiveServices: currentProvider.currentActiveServices,
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

		this.saveOperations.emit(this.form.getRawValue());
	}
}
