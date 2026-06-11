import { Routes } from "@angular/router";

export const MI_EMPRESA_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "profile",
		pathMatch: "full",
	},
	{
		path: "profile",
		loadComponent: () =>
			import("./pages/mi-empresa-profile-page/mi-empresa-profile-page").then(
				m => m.MiEmpresaProfilePage
			),
	},
];
