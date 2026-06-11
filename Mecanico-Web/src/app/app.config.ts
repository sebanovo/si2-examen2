import {
	provideHttpClient,
	withFetch,
	withInterceptors,
} from "@angular/common/http";
import {
	ApplicationConfig,
	inject,
	provideAppInitializer,
	provideBrowserGlobalErrorListeners,
} from "@angular/core";
import { provideRouter } from "@angular/router";

import { routes } from "./app.routes";
import { authTokenInterceptor } from "./core/http/interceptors/auth-token.interceptor";
import { httpErrorInterceptor } from "./core/http/interceptors/http-error.interceptor";
import { SessionBootstrapService } from "./core/session/services/session-bootstrap.service";

export const appConfig: ApplicationConfig = {
	providers: [
		provideBrowserGlobalErrorListeners(), // catch global errors
		provideRouter(routes),

		provideHttpClient(
			withFetch(),
			withInterceptors([authTokenInterceptor, httpErrorInterceptor])
		),
		provideAppInitializer(() => {
			const sessionBootstrapService = inject(SessionBootstrapService);
			return sessionBootstrapService.runBootstrap();
		}),
	],
};
