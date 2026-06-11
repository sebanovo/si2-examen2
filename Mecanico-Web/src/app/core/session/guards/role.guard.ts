import { inject } from "@angular/core";
import { CanActivateFn, Router, UrlTree } from "@angular/router";

import { RoleCode } from "../../../features/auth/models/auth.dto";
import { SessionStore } from "../store/session.store";

/**
 * Allows access only when user has one allowed role.
 * Requires route data.roles.
 */
export const roleGuard: CanActivateFn = async (
	route
): Promise<boolean | UrlTree> => {
	const sessionStore = inject(SessionStore);
	const router = inject(Router);

	if (!sessionStore.initialized()) {
		await sessionStore.bootstrap();
	}

	if (!sessionStore.isAuthenticated()) {
		return router.createUrlTree(["/auth/login"]);
	}

	const allowedRoles = route.data["roles"] as RoleCode[] | undefined;

	if (!allowedRoles?.length) {
		return true;
	}

	const userRoles = sessionStore.roles();

	const hasAllowedRole = allowedRoles.some(role => userRoles.includes(role));

	if (hasAllowedRole) {
		return true;
	}

	return router.createUrlTree(["/app/forbidden"]);
};
