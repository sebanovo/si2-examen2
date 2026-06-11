import { Routes } from "@angular/router";

export const PROVIDER_ME_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/provider-me-list-page/provider-me-list-page").then(
				m => m.ProviderMeListPage
			),
	},
];
