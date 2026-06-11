import { Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideCalendar } from "@ng-icons/lucide";
import { HlmCardImports } from "@shared/ui/card";
import { User } from "../../models/user.types";

@Component({
	selector: "app-user-profile-activity-card",
	imports: [NgIcon, HlmCardImports],
	providers: [provideIcons({ lucideCalendar })],
	host: {
		style: "display: block",
	},
	templateUrl: "./user-profile-activity-card.html",
	styleUrl: "./user-profile-activity-card.css",
})
export class UserProfileActivityCard {
	readonly user = input.required<User | null>();
}
