import {
	ChangeDetectionStrategy,
	Component,
	DestroyRef,
	inject,
	input,
	output,
} from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms";
import { RouterLink } from "@angular/router";

import { HlmButtonImports } from "@shared/ui/button";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";
import { HlmSelectImports } from "@shared/ui/select";

import { EmailInput } from "../../../../shared/custom-components/email-input/email-input";
import { NumberInput } from "../../../../shared/custom-components/number-input/number-input";
import { PasswordInput } from "../../../../shared/custom-components/password-input/password-input";
import { TextInput } from "../../../../shared/custom-components/text-input/text-input";

import { AccountType, RegisterRequest } from "../../models/auth.dto";

@Component({
	selector: "app-register-form",
	imports: [
		ReactiveFormsModule,
		RouterLink,
		HlmFieldImports,
		HlmInputImports,
		HlmButtonImports,
		HlmSelectImports,
		EmailInput,
		PasswordInput,
		TextInput,
		NumberInput,
	],
	changeDetection: ChangeDetectionStrategy.OnPush,
	templateUrl: "./register-form.html",
})
export class RegisterForm {
	private readonly fb = inject(FormBuilder);
	private readonly destroyRef = inject(DestroyRef);

	readonly isSubmitting = input(false);
	readonly errorMessage = input<string | null>(null);

	readonly submitRegister = output<RegisterRequest>();
	readonly formEdited = output<void>();

	readonly form = this.fb.nonNullable.group({
		accountType: ["Standard", [Validators.required]],
		email: ["", [Validators.required, Validators.email]],
		password: ["", [Validators.required, Validators.minLength(8)]],
		firstName: ["", [Validators.required, Validators.minLength(2)]],
		lastName: ["", [Validators.required, Validators.minLength(2)]],
		phoneNumber: [
			"",
			[
				Validators.required,
				Validators.minLength(8),
				Validators.pattern(/^[0-9]+$/),
			],
		],
	});

	constructor() {
		this.form.valueChanges
			.pipe(takeUntilDestroyed(this.destroyRef))
			.subscribe(() => {
				if (this.errorMessage()) {
					this.formEdited.emit();
				}
			});
	}

	/**
	 * Builds RegisterRequest from form values.
	 * Provider profile is always sent as null for now.
	 */
	submit(): void {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		const value = this.form.getRawValue();

		console.log("seleccionado", value.accountType);

		this.submitRegister.emit({
			email: value.email.trim(),
			password: value.password,
			first_name: value.firstName.trim(),
			last_name: value.lastName.trim(),
			account_type: this.resolveAccountType(value.accountType),
			phone_number: value.phoneNumber.trim() || null,
			provider_profile: this.buildProviderProfile(value.accountType),
		});
	}

	private resolveAccountType(name: string): AccountType {
		switch (name) {
			case "Standard":
				return "CLIENT";

			case "Independiente":
				return "INDEPENDENT_MECHANIC";

			case "Empresa":
				return "WORKSHOP";

			default:
				throw new Error(`Tipo de cuenta no válido: ${name}`);
		}
	}

	private buildProviderProfile(accountType: string) {
		if (accountType === "Cliente") {
			return null;
		}

		return {
			business_name: "Sin definir",
			legal_name: "Sin definir",
			description: "Sin definir",
			contact_email: "Sin definir",
			contact_phone: "Sin definir",
			city: "Sin definir",
			address: "Sin definir",
			base_latitude: 0,
			base_longitude: 0,
			max_concurrent_services: 1,
		};
	}
}
