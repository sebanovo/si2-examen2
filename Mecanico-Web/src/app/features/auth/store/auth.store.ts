import { computed, inject, Injectable, signal } from "@angular/core";
import { Router } from "@angular/router";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import { SessionStore } from "../../../core/session/store/session.store";

import { toAuthUser } from "../adapters/auth.adapter";

import { LoginRequest, RegisterRequest } from "../models/auth.dto";
import { AuthUser } from "../models/auth.types";
import { AuthService } from "../services/auth.service";

@Injectable({
	providedIn: "root",
})
export class AuthStore {
	private readonly authService = inject(AuthService);
	private readonly sessionStore = inject(SessionStore);
	private readonly router = inject(Router);

	private readonly loadingSignal = signal(false);
	private readonly errorSignal = signal<AppHttpError | null>(null);
	private readonly userSignal = signal<AuthUser | null>(null);

	readonly loading = this.loadingSignal.asReadonly();
	readonly error = this.errorSignal.asReadonly();
	readonly user = this.userSignal.asReadonly();

	readonly isAuthenticated = computed(() => this.userSignal() !== null);
	readonly errorMessage = computed(() => this.errorSignal()?.message ?? null);

	/**
	 * Executes login and stores only the authenticated user.
	 */
	async login(payload: LoginRequest): Promise<boolean> {
		this.startRequest();

		try {
			const session = await firstValueFrom(this.authService.login(payload));

			const user = toAuthUser(session.user);

			this.userSignal.set(user);
			this.sessionStore.setAuthenticated(user);

			return true;
		} catch (error: unknown) {
			this.setRequestError(error);
			return false;
		} finally {
			this.loadingSignal.set(false);
		}
	}

	/**
	 * Executes register and stores only the authenticated user.
	 */
	async register(payload: RegisterRequest): Promise<boolean> {
		this.startRequest();

		try {
			const session = await firstValueFrom(this.authService.register(payload));

			const user = toAuthUser(session.user);

			this.userSignal.set(user);
			this.sessionStore.setAuthenticated(user);

			return true;
		} catch (error: unknown) {
			this.setRequestError(error);
			return false;
		} finally {
			this.loadingSignal.set(false);
		}
	}

	/**
	 * Loads current user from backend.
	 */
	async loadMe(): Promise<boolean> {
		this.startRequest();

		try {
			const userDto = await firstValueFrom(this.authService.getMe());
			const user = toAuthUser(userDto);

			this.userSignal.set(user);
			this.sessionStore.setAuthenticated(user);

			return true;
		} catch (error: unknown) {
			this.setRequestError(error);
			return false;
		} finally {
			this.loadingSignal.set(false);
		}
	}

	/**
	 * Clears session locally.
	 */
	async logout(): Promise<void> {
		this.authService.logout(); // solo limpia tokens
		this.reset();
		this.sessionStore.clearSession();

		await this.router.navigate(["/auth/login"]);
	}

	clearError(): void {
		this.errorSignal.set(null);
	}

	reset(): void {
		this.loadingSignal.set(false);
		this.errorSignal.set(null);
		this.userSignal.set(null);
	}

	private startRequest(): void {
		this.loadingSignal.set(true);
		this.errorSignal.set(null);
	}

	private setRequestError(error: unknown): void {
		this.errorSignal.set(error as AppHttpError);
	}
}
