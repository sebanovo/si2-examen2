import { Component, input, output } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideBadgeCheck,
	lucideCheck,
	lucideMail,
	lucidePencil,
	lucideUser,
} from "@ng-icons/lucide";
import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-profile-hero",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports],
	providers: [
		provideIcons({
			lucideUser,
			lucideMail,
			lucidePencil,
			lucideCheck,
			lucideBadgeCheck,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./user-profile-hero.html",
	styleUrl: "./user-profile-hero.css",
})
export class UserProfileHero {
	readonly user = input.required<User | null>();
	readonly editMode = input(false);

	readonly editClick = output<void>();

	onEditClick(): void {
		this.editClick.emit();
	}
}
