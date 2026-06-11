import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { toAuthUser } from "../../../features/auth/adapters/auth.adapter";
import { AuthUser } from "../../../features/auth/models/auth.types";
import { AuthService } from "../../../features/auth/services/auth.service";
import { SessionBootstrapResult } from "../model/session-result.type";
import { SessionState } from "../model/session-state.type";

@Injectable({
	providedIn: "root",
})
export class SessionStore {
	private readonly authService = inject(AuthService);

	private readonly initialState: SessionState = {
		status: "idle",
		initialized: false,
		user: null,
		errorMessage: null,
	};

	private readonly stateSignal = signal<SessionState>(this.initialState);

	readonly state = this.stateSignal.asReadonly();

	readonly status = computed(() => this.stateSignal().status);
	readonly initialized = computed(() => this.stateSignal().initialized);
	readonly user = computed(() => this.stateSignal().user);
	readonly errorMessage = computed(() => this.stateSignal().errorMessage);

	readonly isIdle = computed(() => this.status() === "idle");
	readonly isBootstrapping = computed(() => this.status() === "bootstrapping");
	readonly isAuthenticated = computed(() => this.status() === "authenticated");
	readonly isUnauthenticated = computed(
		() => this.status() === "unauthenticated"
	);
	readonly isReady = computed(() => this.initialized());

	readonly roles = computed(() => this.user()?.roleCodes ?? []);

	readonly isClient = computed(() => this.roles().includes("CLIENT"));
	readonly isProviderAdmin = computed(() =>
		this.roles().includes("PROVIDER_ADMIN")
	);
	readonly isPlatformAdmin = computed(() =>
		this.roles().includes("PLATFORM_ADMIN")
	);

	readonly userFullName = computed(() => {
		const user = this.user();
		return user ? user.fullName : null;
	});

	/**
	 * Bootstraps session using current token and /auth/me.
	 * Clears session when token is missing or invalid.
	 */
	async bootstrap(): Promise<void> {
		this.startBootstrap();

		try {
			const result = await this.resolveBootstrapResult();
			this.applyBootstrapResult(result);
		} catch {
			this.authService.logout();
			this.setUnauthenticated("Unexpected session bootstrap error.");
		}
	}

	/**
	 * Reloads the authenticated user from /auth/me.
	 * Keeps token handling inside AuthService.
	 */
	async loadUser(): Promise<void> {
		try {
			const userDto = await firstValueFrom(this.authService.getMe());
			this.setAuthenticated(toAuthUser(userDto));
		} catch {
			this.authService.logout();
			this.setUnauthenticated();
		}
	}

	setAuthenticated(user: AuthUser): void {
		this.patchState({
			status: "authenticated",
			initialized: true,
			user,
			errorMessage: null,
		});
	}

	setUnauthenticated(errorMessage: string | null = null): void {
		this.patchState({
			status: "unauthenticated",
			initialized: true,
			user: null,
			errorMessage,
		});
	}

	clearSession(): void {
		this.patchState({
			status: "unauthenticated",
			initialized: true,
			user: null,
			errorMessage: null,
		});
	}

	reset(): void {
		this.stateSignal.set(this.initialState);
	}

	private async resolveBootstrapResult(): Promise<SessionBootstrapResult> {
		if (!this.authService.hasToken()) {
			return {
				status: "unauthenticated",
				user: null,
				errorMessage: null,
			};
		}

		try {
			const userDto = await firstValueFrom(this.authService.getMe());

			return {
				status: "authenticated",
				user: toAuthUser(userDto),
				errorMessage: null,
			};
		} catch {
			this.authService.logout();

			return {
				status: "unauthenticated",
				user: null,
				errorMessage: "Invalid or expired session.",
			};
		}
	}

	private startBootstrap(): void {
		this.patchState({
			status: "bootstrapping",
			initialized: false,
			errorMessage: null,
		});
	}

	private applyBootstrapResult(result: SessionBootstrapResult): void {
		if (result.status === "authenticated") {
			this.setAuthenticated(result.user);
			return;
		}

		this.setUnauthenticated(result.errorMessage);
	}

	private patchState(patch: Partial<SessionState>): void {
		this.stateSignal.update(currentState => ({
			...currentState,
			...patch,
		}));
	}
}
