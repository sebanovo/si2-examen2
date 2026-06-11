import { Component } from "@angular/core";
import { HlmCalendarImports } from "@shared/ui/calendar";

@Component({
	selector: "app-dashboard-page",
	imports: [HlmCalendarImports],
	templateUrl: "./dashboard-page.html",
	styleUrl: "./dashboard-page.css",
})
export class DashboardPage {
	readonly selectedDate = new Date();

	readonly minDate = new Date(2023, 0, 1);

	readonly maxDate = new Date(2030, 11, 31);
}
