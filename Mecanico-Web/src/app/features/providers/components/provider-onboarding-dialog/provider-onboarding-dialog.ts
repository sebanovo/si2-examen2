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
import {
	lucideSave,
	lucideStore,
	lucideUserPlus,
	lucideX,
} from "@ng-icons/lucide";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmDialogImports } from "@shared/ui/dialog";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmRadioGroupImports } from "@shared/ui/radio-group";

import { AppHttpError } from "../../../../core/http/models/app-http-error.model";
import {
	OnboardProviderFormValue,
	ProviderType,
} from "../../models/provider.types";

@Component({
	selector: "app-provider-onboarding-dialog",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmButtonImports,
		HlmDialogImports,
		HlmFieldImports,
		HlmInputImports,
		HlmRadioGroupImports,
	],
	providers: [
		provideIcons({ lucideStore, lucideUserPlus, lucideSave, lucideX }),
	],
	templateUrl: "./provider-onboarding-dialog.html",
	styleUrl: "./provider-onboarding-dialog.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ProviderOnboardingDialog {
	private readonly fb = inject(FormBuilder);

	readonly open = input.required<boolean>();
	readonly loading = input(false);
	readonly error = input<AppHttpError | null>(null);

	readonly openChange = output<boolean>();
	readonly onboardProvider = output<OnboardProviderFormValue>();

	readonly form = this.fb.nonNullable.group({
		adminUser: this.fb.nonNullable.group({
			email: ["", [Validators.required, Validators.email]],
			password: ["", [Validators.required, Validators.minLength(8)]],
			firstName: ["", [Validators.required, Validators.maxLength(80)]],
			lastName: ["", [Validators.required, Validators.maxLength(80)]],
			phoneNumber: ["" as string | null, [Validators.maxLength(30)]],
		}),
		provider: this.fb.nonNullable.group({
			providerType: ["WORKSHOP" as ProviderType, [Validators.required]],
			businessName: ["", [Validators.required, Validators.maxLength(160)]],
			legalName: ["", [Validators.required, Validators.maxLength(160)]],
			description: ["" as string | null, [Validators.maxLength(500)]],
			contactEmail: ["", [Validators.required, Validators.email]],
			contactPhone: ["" as string | null, [Validators.maxLength(30)]],
			city: ["", [Validators.required, Validators.maxLength(80)]],
			address: ["", [Validators.required, Validators.maxLength(200)]],
			baseLatitude: [0, [Validators.required]],
			baseLongitude: [0, [Validators.required]],
			maxConcurrentServices: [1, [Validators.required, Validators.min(1)]],
		}),
	});

	constructor() {
		effect(() => {
			if (!this.open()) {
				this.form.reset({
					adminUser: {
						email: "",
						password: "",
						firstName: "",
						lastName: "",
						phoneNumber: "",
					},
					provider: {
						providerType: "WORKSHOP",
						businessName: "",
						legalName: "",
						description: "",
						contactEmail: "",
						contactPhone: "",
						city: "",
						address: "",
						baseLatitude: 0,
						baseLongitude: 0,
						maxConcurrentServices: 1,
					},
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

		this.onboardProvider.emit(this.form.getRawValue());
	}
}
