import { Component, inject, OnInit, signal } from "@angular/core";
import { FormBuilder, ReactiveFormsModule, Validators } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideX } from "@ng-icons/lucide";
import { HlmSkeletonImports } from "@shared/ui/skeleton";
import { toast } from "@spartan-ng/brain/sonner";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { UserProfileActivityCard } from "../../components/user-profile-activity-card/user-profile-activity-card";
import { UserProfileFormCard } from "../../components/user-profile-form-card/user-profile-form-card";
import { UserProfileHero } from "../../components/user-profile-hero/user-profile-hero";
import { UserProfileRolesCard } from "../../components/user-profile-roles-card/user-profile-roles-card";
import { UsersStore } from "../../store/user.store";

@Component({
	selector: "app-user-profile-page",
	imports: [
		ReactiveFormsModule,
		NgIcon,
		HlmSkeletonImports,
		TableError,
		UserProfileHero,
		UserProfileFormCard,
		UserProfileRolesCard,
		UserProfileActivityCard,
	],
	providers: [provideIcons({ lucideX })],
	templateUrl: "./user-profile-page.html",
	styleUrl: "./user-profile-page.css",
})
export class UserProfilePage implements OnInit {
	readonly store = inject(UsersStore);
	private readonly fb = inject(FormBuilder);

	readonly editMode = signal(false);

	readonly form = this.fb.nonNullable.group({
		firstName: ["", [Validators.required, Validators.maxLength(80)]],
		lastName: ["", [Validators.required, Validators.maxLength(80)]],
		phoneNumber: ["" as string | null, [Validators.maxLength(30)]],
	});

	async ngOnInit(): Promise<void> {
		await this.loadProfile();
	}

	async loadProfile(): Promise<void> {
		const user = await this.store.loadOwnProfile();

		if (user) {
			this.form.patchValue({
				firstName: user.firstName,
				lastName: user.lastName,
				phoneNumber: user.phoneNumber,
			});
		}

		this.form.disable();
	}

	onRetry(): void {
		void this.loadProfile();
	}

	onEnableEdit(): void {
		this.editMode.set(true);
		this.form.enable();
	}

	onCancelEdit(): void {
		const user = this.store.ownProfile();

		if (user) {
			this.form.patchValue({
				firstName: user.firstName,
				lastName: user.lastName,
				phoneNumber: user.phoneNumber,
			});
		}

		this.form.disable();
		this.editMode.set(false);
		this.store.clearUpdateOwnProfileError();
	}

	async onSubmit(): Promise<void> {
		if (this.form.invalid) {
			this.form.markAllAsTouched();
			return;
		}

		const updatedUser = await this.store.updateOwnProfile({
			firstName: this.form.controls.firstName.value,
			lastName: this.form.controls.lastName.value,
			phoneNumber: this.form.controls.phoneNumber.value || null,
		});

		if (!updatedUser) {
			toast("No se pudo actualizar el perfil", {
				description:
					this.store.updateOwnProfileError()?.message ||
					"Ocurrió un error inesperado.",
			});

			return;
		}

		this.form.patchValue({
			firstName: updatedUser.firstName,
			lastName: updatedUser.lastName,
			phoneNumber: updatedUser.phoneNumber,
		});

		this.form.disable();
		this.editMode.set(false);

		toast("Perfil actualizado correctamente");
	}
}

// export class UserProfilePage implements OnInit {
// 	readonly store = inject(UsersStore);
// 	private readonly fb = inject(FormBuilder);

// 	readonly editMode = signal(false);

// 	readonly form = this.fb.nonNullable.group({
// 		firstName: ["", [Validators.required, Validators.maxLength(80)]],
// 		lastName: ["", [Validators.required, Validators.maxLength(80)]],
// 		phoneNumber: ["" as string | null, [Validators.maxLength(30)]],
// 	});

// 	async ngOnInit(): Promise<void> {
// 		const user = await this.store.loadOwnProfile();

// 		if (user) {
// 			this.form.patchValue({
// 				firstName: user.firstName,
// 				lastName: user.lastName,
// 				phoneNumber: user.phoneNumber,
// 			});
// 		}

// 		this.form.disable();
// 	}

// 	onEnableEdit(): void {
// 		this.editMode.set(true);
// 		this.form.enable();
// 	}

// 	onCancelEdit(): void {
// 		const user = this.store.ownProfile();

// 		if (user) {
// 			this.form.patchValue({
// 				firstName: user.firstName,
// 				lastName: user.lastName,
// 				phoneNumber: user.phoneNumber,
// 			});
// 		}

// 		this.form.disable();
// 		this.editMode.set(false);
// 		this.store.clearUpdateOwnProfileError();
// 	}

// 	async onSubmit(): Promise<void> {
// 		if (this.form.invalid) {
// 			this.form.markAllAsTouched();
// 			return;
// 		}

// 		const updatedUser = await this.store.updateOwnProfile({
// 			firstName: this.form.controls.firstName.value,
// 			lastName: this.form.controls.lastName.value,
// 			phoneNumber: this.form.controls.phoneNumber.value || null,
// 		});

// 		if (!updatedUser) {
// 			toast("No se pudo actualizar el perfil", {
// 				description:
// 					this.store.updateOwnProfileError()?.message ||
// 					"Ocurrió un error inesperado.",
// 			});

// 			return;
// 		}

// 		this.form.patchValue({
// 			firstName: updatedUser.firstName,
// 			lastName: updatedUser.lastName,
// 			phoneNumber: updatedUser.phoneNumber,
// 		});

// 		this.form.disable();
// 		this.editMode.set(false);

// 		toast("Perfil actualizado correctamente");
// 	}
// }
