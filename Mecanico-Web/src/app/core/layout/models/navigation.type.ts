import { RoleCode } from "../../../features/auth/models/auth.dto";

export type AppNavigationIcon = {
	type: "lucide" | "remix";
	name: string;
};

export type AppNavigationSectionItem = {
	type: "section";
	label: string;
};

export type AppNavigationLinkItem = {
	type?: "link";
	label: string;
	route: string;
	exact?: boolean;
	icon: AppNavigationIcon;
	allowedRoles?: RoleCode[];
	requiredPermissions?: string[];
};

export type AppNavigationItem =
	| AppNavigationSectionItem
	| AppNavigationLinkItem;
