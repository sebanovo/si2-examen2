import { Routes } from "@angular/router";

export const INCIDENT_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/incident-list-page/incident-list-page").then(
				m => m.IncidentListPage
			),
	},
];
