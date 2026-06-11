import { Routes } from "@angular/router";

export const PROVIDERS_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/provider-list-page/provider-list-page").then(
				m => m.ProviderListPage
			),
	},

	//Usa la feature Technicians
	{
		path: ":id/technicians",
		loadComponent: () =>
			import("../technicians/pages/technician-list-page/technician-list-page").then(
				m => m.TechnicianListPage
			),
	},

	//Usa la feature provider-services
	{
		path: ":id/services",
		loadComponent: () =>
			import("../provider-services/pages/provider-service-list-page/provider-service-list-page").then(
				m => m.ProviderServiceListPage
			),
	},
];
