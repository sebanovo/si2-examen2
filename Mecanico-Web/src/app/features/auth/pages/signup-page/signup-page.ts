import { ChangeDetectionStrategy, Component, inject } from "@angular/core";
import { Router } from "@angular/router";
import { RegisterForm } from "../../components/register-form/register-form";
import { RegisterRequest } from "../../models/auth.dto";
import { AuthStore } from "../../store/auth.store";

@Component({
	selector: "app-signup-page",
	standalone: true,
	imports: [RegisterForm],
	changeDetection: ChangeDetectionStrategy.OnPush,
	templateUrl: "./signup-page.html",
	styleUrl: "./signup-page.css",
})
export class SignupPage {
	private readonly authStore = inject(AuthStore);
	private readonly router = inject(Router);

	readonly isSubmitting = this.authStore.loading;
	readonly errorMessage = this.authStore.errorMessage;

	async onSubmit(payload: RegisterRequest): Promise<void> {
		const success = await this.authStore.register(payload);

		if (!success) {
			return;
		}

		await this.router.navigateByUrl("/app");
	}

	onFormEdited(): void {
		this.authStore.clearError();
	}
}
