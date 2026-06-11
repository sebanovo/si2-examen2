import { inject } from "@angular/core";
import { CanActivateFn, Router, UrlTree } from "@angular/router";

import { SessionStore } from "../store/session.store";

/**
 * Allows access only to unauthenticated users.
 * Redirects logged users to the app.
 */
export const guestGuard: CanActivateFn = async (): Promise<
	boolean | UrlTree
> => {
	const sessionStore = inject(SessionStore);
	const router = inject(Router);

	if (!sessionStore.initialized()) {
		await sessionStore.bootstrap();
	}

	if (sessionStore.isAuthenticated()) {
		return router.createUrlTree(["/app"]);
	}

	return true;
};
