import { Routes } from "@angular/router";

export const CATALOG_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/catalog-list-page/catalog-list-page").then(
				m => m.CatalogListPage
			),
	},
];
