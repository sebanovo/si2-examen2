import { inject } from "@angular/core";
import { CanActivateFn, Router, UrlTree } from "@angular/router";

import { SessionStore } from "../store/session.store";

/**
 * Allows access only to authenticated users.
 * Bootstraps session before checking access.
 */
export const authGuard: CanActivateFn = async (
	_route,
	state
): Promise<boolean | UrlTree> => {
	const sessionStore = inject(SessionStore);
	const router = inject(Router);

	if (!sessionStore.initialized()) {
		await sessionStore.bootstrap();
	}

	if (sessionStore.isAuthenticated()) {
		return true;
	}

	return router.createUrlTree(["/auth/login"], {
		queryParams: {
			returnUrl: state.url,
		},
	});
};
