import { Routes } from "@angular/router";

export const SERVICE_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/service-list-page/service-list-page").then(
				m => m.ServiceListPage
			),
	},
];
