import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideEye, lucidePencil, lucideShield } from "@ng-icons/lucide";
import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { HlmTableImports } from "@shared/ui/table";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-table",
	imports: [HlmTableImports, HlmBadgeImports, HlmButtonImports, NgIcon],
	providers: [provideIcons({ lucidePencil, lucideEye, lucideShield })],
	templateUrl: "./user-table.html",
	styleUrl: "./user-table.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UserTable {
	readonly users = input.required<User[]>();

	readonly viewUser = output<User>();
	readonly editUser = output<string>();
	readonly manageRoles = output<User>();

	onViewUser(user: User): void {
		this.viewUser.emit(user);
	}

	onEditUser(userId: string): void {
		this.editUser.emit(userId);
	}

	onManageRoles(user: User): void {
		this.manageRoles.emit(user);
	}
}
