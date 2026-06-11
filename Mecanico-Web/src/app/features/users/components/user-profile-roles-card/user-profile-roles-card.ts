import { Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideShield } from "@ng-icons/lucide";
import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmCardImports } from "@shared/ui/card";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-profile-roles-card",
	imports: [NgIcon, HlmBadgeImports, HlmCardImports],
	providers: [provideIcons({ lucideShield })],
	host: {
		style: "display: block",
	},
	templateUrl: "./user-profile-roles-card.html",
	styleUrl: "./user-profile-roles-card.css",
})
export class UserProfileRolesCard {
	readonly user = input.required<User | null>();
}
