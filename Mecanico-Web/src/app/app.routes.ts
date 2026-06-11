import { Routes } from "@angular/router";
import { AdminAuthLayout } from "./core/layout/layouts/admin-auth-layout/admin-auth-layout";
import { AppLayout } from "./core/layout/layouts/app-layout/app-layout";
import { AuthLayout } from "./core/layout/layouts/auth-layout/auth-layout";
import { PublicLayout } from "./core/layout/layouts/public-layout/public-layout";
import { authGuard } from "./core/session/guards/auth.guard";

export const routes: Routes = [
	// Public
	{
		path: "",
		component: PublicLayout,
		children: [
			{
				path: "",
				loadChildren: () =>
					import("./features/public/public.routes").then(m => m.PUBLIC_ROUTES),
			},
		],
	},

	// Authentication
	{
		path: "auth",
		component: AuthLayout,
		children: [
			// public login
			{
				path: "",
				loadChildren: () =>
					import("./features/auth/auth.routes").then(m => m.AUTH_ROUTES),
			},
		],
	},

	{
		path: "",
		component: AdminAuthLayout,
		// canActivateChild: [adminGuestGuard],
		children: [
			// hidden login
			{
				path: "platform/auth",
				loadChildren: () =>
					import("./features/auth/auth.routes").then(m => m.ADMIN_ROUTES),
			},
		],
	},

	// Private
	{
		path: "app",
		canActivate: [authGuard],
		component: AppLayout,
		children: [
			{
				path: "", //default route
				redirectTo: "dashboard",
				pathMatch: "full",
			},

			{
				path: "dashboard",
				loadChildren: () =>
					import("./features/dashboard/dashboard.routes").then(
						m => m.DASHBOARD_ROUTES
					),
			},
			{
				path: "empresa",
				loadChildren: () =>
					import("./features/mi-empresa/mi-empresa.routes").then(
						m => m.MI_EMPRESA_ROUTES
					),
			},

			{
				path: "providers",
				loadChildren: () =>
					import("./features/providers/provider.routes").then(
						m => m.PROVIDERS_ROUTES
					),
			},

			{
				path: "provider-me",
				loadChildren: () =>
					import("./features/provider-me/provider-me.routes").then(
						m => m.PROVIDER_ME_ROUTES
					),
			},
			{
				path: "users",
				loadChildren: () =>
					import("./features/users/users.routes").then(m => m.USERS_ROUTES),
			},

			{
				path: "catalogs",
				loadChildren: () =>
					import("./features/catalog-services/catalog-service.routes").then(
						m => m.CATALOG_ROUTES
					),
			},
			{
				path: "service-me",
				loadChildren: () =>
					import("./features/services/service.routes").then(
						m => m.SERVICE_ROUTES
					),
			},

			{
				path: "incidents-me",
				loadChildren: () =>
					import("./features/provider-incidents/incident.routes").then(
						m => m.INCIDENT_ROUTES
					),
			},

			{
				path: "candidates",
				loadChildren: () =>
					import("./features/candidates/candidate.routes").then(
						m => m.CANDIDATE_ROUTES
					),
			},

			{
				path: "**",
				loadComponent: () =>
					import("./features/not-found/pages/private-not-found-page/private-not-found-page").then(
						m => m.PrivateNotFoundPage
					),
			},
		],
	},

	//unknown routes
	{
		path: "**",
		loadComponent: () =>
			import("./features/not-found/pages/public-not-found-page/public-not-found-page").then(
				m => m.PublicNotFoundPage
			),
	},
];

// EXAMPLE
// {
// 	path: "tenants",
// 	canActivate: [roleGuard],
// 	data: {
// 		roles: ["PROVIDER_ADMIN", "CLIENT", "PLATFORM_ADMIN"],
// 	},
// 	loadChildren: () =>
// 		import("./features/tanants/tenants.routes").then(
// 			m => m.TENANTS_ROUTES),
// },
