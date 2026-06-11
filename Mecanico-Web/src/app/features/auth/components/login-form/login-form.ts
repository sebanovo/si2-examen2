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

import { EmailInput } from "../../../../shared/custom-components/email-input/email-input";
import { PasswordInput } from "../../../../shared/custom-components/password-input/password-input";

import { LoginRequest } from "../../models/auth.dto";

@Component({
	selector: "app-login-form",
	imports: [
		ReactiveFormsModule,
		RouterLink,
		HlmFieldImports,
		HlmButtonImports,
		EmailInput,
		PasswordInput,
	],
	changeDetection: ChangeDetectionStrategy.OnPush,
	templateUrl: "./login-form.html",
})
export class LoginForm {
	private readonly fb = inject(FormBuilder);
	private readonly destroyRef = inject(DestroyRef);

	readonly isSubmitting = input(false);
	readonly errorMessage = input<string | null>(null);

	readonly submitLogin = output<LoginRequest>();
	readonly formEdited = output<void>();

	readonly form = this.fb.nonNullable.group({
		email: ["", [Validators.required, Validators.email]],
		password: ["", [Validators.required, Validators.minLength(8)]],
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
	 * Validates the form and emits normalized login credentials.
	 * Keeps token handling outside the component.
	 */
	submit(): void {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		const { email, password } = this.form.getRawValue();

		this.submitLogin.emit({
			email: email.trim(),
			password,
		});
	}
}
