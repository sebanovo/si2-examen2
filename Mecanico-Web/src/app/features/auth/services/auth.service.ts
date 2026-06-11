import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable, tap } from "rxjs";
import { AccessTokenService } from "../../../core/http/services/access-token.service";
import {
	AuthResponse,
	AuthSessionDto,
	LoginRequest,
	RegisterRequest,
	UserDto,
} from "../models/auth.dto";

@Injectable({
	providedIn: "root",
})
export class AuthService {
	private readonly http = inject(HttpClient);
	private readonly tokenService = inject(AccessTokenService);

	private readonly basePath = "/api/auth";

	/**
	 * Handles authentication endpoints and manages session tokens.
	 * Wraps register, login and user retrieval.
	 * Persists access token on successful authentication.
	 */
	register(payload: RegisterRequest): Observable<AuthSessionDto> {
		return this.http
			.post<AuthResponse<AuthSessionDto>>(`${this.basePath}/register`, payload)
			.pipe(
				map(res => res.data),
				tap(session => {
					this.tokenService.setTokens(session);
				})
			);
	}

	login(payload: LoginRequest): Observable<AuthSessionDto> {
		console.log("login request", payload);
		return this.http
			.post<AuthResponse<AuthSessionDto>>(`${this.basePath}/login`, payload)
			.pipe(
				map(res => res.data),
				tap(session => {
					console.log("respuesta", session);
					this.tokenService.setTokens(session);
				})
			);
	}

	getMe(): Observable<UserDto> {
		return this.http
			.get<AuthResponse<UserDto>>(`${this.basePath}/me`)
			.pipe(map(res => res.data));
	}

	logout(): void {
		this.tokenService.clearTokens();
	}

	hasToken(): boolean {
		const tokens = this.tokenService.getTokens();
		return !!tokens?.access_token;
	}
}
