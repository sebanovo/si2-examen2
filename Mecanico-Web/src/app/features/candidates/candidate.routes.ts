import { Routes } from "@angular/router";

export const CANDIDATE_ROUTES: Routes = [
	{
		path: "", //default route
		redirectTo: "list",
		pathMatch: "full",
	},
	{
		path: "list",
		loadComponent: () =>
			import("./pages/candidate-list-page/candidate-list-page").then(
				m => m.CandidateListPage
			),
	},
];
