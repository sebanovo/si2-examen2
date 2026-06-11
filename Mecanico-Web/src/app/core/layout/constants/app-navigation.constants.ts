import { AppNavigationItem } from "../models/navigation.type";

export const APP_NAVIGATION: AppNavigationItem[] = [
	{
		type: "section",
		label: "Administración",
	},
	{
		label: "Dashboard",
		route: "/app/dashboard",
		exact: true,
		icon: {
			type: "remix",
			name: "ri-dashboard-line",
		},
		allowedRoles: ["PLATFORM_ADMIN", "PROVIDER_ADMIN"],
	},

	{
		label: "Mi empresa",
		route: "/app/empresa/profile",
		exact: true,
		icon: {
			type: "remix",
			name: "ri-building2-line",
		},
		allowedRoles: ["PROVIDER_ADMIN"],
	},

	{
		label: "Mis Tecnicos",
		route: "/app/provider-me",
		exact: true,
		icon: {
			type: "remix",
			name: "ri-team-line",
		},
		allowedRoles: ["PROVIDER_ADMIN"],
	},

	{
		label: "Usuarios",
		route: "/app/users",
		icon: {
			type: "lucide",
			name: "users",
		},
		allowedRoles: ["PLATFORM_ADMIN"],
	},
	{
		label: "Proveedores",
		route: "/app/providers",
		icon: {
			type: "remix",
			name: "ri-building-line",
		},
		allowedRoles: ["PLATFORM_ADMIN"],
	},
	{
		label: "Suscripciones",
		route: "/app/subscriptions",
		icon: {
			type: "remix",
			name: "ri-vip-crown-line",
		},
		allowedRoles: ["PLATFORM_ADMIN"],
	},

	// {
	// 	type: "section",
	// 	label: "Catálogo",
	// },
	{
		label: "Catálogos",
		route: "/app/catalogs",
		icon: {
			type: "remix",
			name: "ri-price-tag-3-line",
		},
		allowedRoles: ["PLATFORM_ADMIN"],
	},
	{
		label: "Mis servicios",
		route: "/app/service-me",
		icon: {
			type: "remix",
			name: "ri-price-tag-3-line",
		},
		allowedRoles: ["PROVIDER_ADMIN"],
	},
	{
		label: "Vehículos",
		route: "/app/vehicles",
		icon: {
			type: "remix",
			name: "ri-file-list-3-line",
		},
		allowedRoles: ["CLIENT"],
	},

	{
		type: "section",
		label: "Operación",
	},
	{
		label: "Trabajo aceptado",
		route: "/app/incidents-me",
		icon: {
			type: "lucide",
			name: "briefcase",
		},
		allowedRoles: ["PROVIDER_ADMIN"],
	},
	{
		label: "Incidentes",
		route: "/app/incidents",
		icon: {
			type: "remix",
			name: "ri-dashboard-line",
		},
		allowedRoles: ["CLIENT", "PLATFORM_ADMIN"],
	},
	{
		label: "Candidatos",
		route: "/app/candidates",
		icon: {
			type: "lucide",
			name: "target",
		},
		allowedRoles: ["PROVIDER_ADMIN"],
	},
	{
		label: "Evidencias",
		route: "/app/evidences",
		icon: {
			type: "remix",
			name: "ri-file-list-3-line",
		},
		allowedRoles: ["PROVIDER_ADMIN", "PLATFORM_ADMIN"],
	},
	{
		label: "Trabajos",
		route: "/app/jobs",
		icon: {
			type: "remix",
			name: "ri-shield-keyhole-line",
		},
		allowedRoles: ["PROVIDER_ADMIN", "PLATFORM_ADMIN"],
	},
	{
		label: "Operaciones",
		route: "/app/operations",
		icon: {
			type: "remix",
			name: "ri-bar-chart-box-line",
		},
		allowedRoles: ["PROVIDER_ADMIN", "PLATFORM_ADMIN"],
	},
	{
		label: "Seguimiento",
		route: "/app/tracking",
		icon: {
			type: "remix",
			name: "ri-key-line",
		},
		allowedRoles: ["CLIENT", "PROVIDER_ADMIN", "PLATFORM_ADMIN"],
	},

	{
		type: "section",
		label: "Finanzas",
	},
	{
		label: "Cobros",
		route: "/app/payments",
		icon: {
			type: "remix",
			name: "ri-price-tag-3-line",
		},
		allowedRoles: ["PROVIDER_ADMIN", "PLATFORM_ADMIN"],
	},
];
