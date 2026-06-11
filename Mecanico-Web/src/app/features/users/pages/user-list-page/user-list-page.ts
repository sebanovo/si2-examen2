import { Component, inject, OnInit, signal } from "@angular/core";
import { Router } from "@angular/router";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideAlertCircle,
	lucideChevronLeft,
	lucideChevronRight,
	lucideInbox,
	lucidePlus,
	lucideUsers,
} from "@ng-icons/lucide";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmCardImports } from "@shared/ui/card";
import { HlmSkeletonImports } from "@shared/ui/skeleton";
import { toast } from "@spartan-ng/brain/sonner";
import { CardHeader } from "../../../../shared/custom-components/card-header/card-header";
import { EmptyState } from "../../../../shared/custom-components/empty-state/empty-state";
import { TableError } from "../../../../shared/custom-components/table-error/table-error";
import { UserDetailDialog } from "../../components/user-detail-dialog/user-detail-dialog";
import { UserTable } from "../../components/user-table/user-table";
import { User } from "../../models/user.types";
import { UsersStore } from "../../store/user.store";

@Component({
	selector: "app-user-list-page",
	imports: [
		NgIcon,
		UserTable,
		HlmButtonImports,
		HlmCardImports,
		HlmSkeletonImports,
		UserDetailDialog,
		CardHeader,
		TableError,
		EmptyState,
	],
	providers: [
		provideIcons({
			lucideAlertCircle,
			lucideChevronLeft,
			lucideChevronRight,
			lucideInbox,
			lucidePlus,
			lucideUsers,
		}),
	],
	templateUrl: "./user-list-page.html",
	styleUrl: "./user-list-page.css",
})
export class UserListPage implements OnInit {
	readonly store = inject(UsersStore);
	private readonly router = inject(Router);

	readonly viewDialogOpen = signal(false);

	ngOnInit(): void {
		void this.store.loadUsers();
	}

	onRetry(): void {
		void this.store.reloadUsers();
	}

	onCreateUser(): void {
		void this.router.navigate(["/app", "users", "create"]);
	}

	onEditUser(userId: string): void {
		void this.router.navigate(["/app", "users", userId, "edit"]);
	}

	async onViewUser(user: User): Promise<void> {
		this.store.clearSelectedUserError();
		this.store.clearSelectedUser();
		this.viewDialogOpen.set(true);

		const loadedUser = await this.store.loadUserById(user.id);

		if (!loadedUser) {
			toast("No se pudo cargar el usuario", {
				description:
					this.store.selectedUserError()?.message ||
					"Ocurrió un error inesperado.",
			});
		}
	}

	onViewDialogOpenChange(isOpen: boolean): void {
		this.viewDialogOpen.set(isOpen);

		if (!isOpen) {
			this.store.clearSelectedUserError();
			this.store.clearSelectedUser();
		}
	}

	onManageRoles(user: User): void {
		console.log("manage roles", user);
	}

	async onPreviousPage(): Promise<void> {
		await this.store.previousPage();
	}

	async onNextPage(): Promise<void> {
		const previousOffset = this.store.offset();

		await this.store.nextPage();

		if (
			this.store.offset() === previousOffset &&
			this.store.lastPageReached()
		) {
			toast("No hay más usuarios para mostrar");
		}
	}
}
