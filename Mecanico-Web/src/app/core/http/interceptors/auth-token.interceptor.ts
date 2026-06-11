import { HttpInterceptorFn } from "@angular/common/http";
import { inject } from "@angular/core";

import { AccessTokenService } from "../services/access-token.service";

/**
 * Adds Authorization header when a token exists.
 * Leaves public requests untouched.
 */
export const authTokenInterceptor: HttpInterceptorFn = (req, next) => {
	const tokenService = inject(AccessTokenService);

	const accessToken = tokenService.getAccessToken();

	if (!accessToken) {
		return next(req);
	}

	return next(
		req.clone({
			setHeaders: {
				Authorization: `${tokenService.getTokenType()} ${accessToken}`,
			},
		})
	);
};
