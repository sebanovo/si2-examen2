import { Injectable } from "@angular/core";

export type TokenData = {
	access_token: string;
	token_type: string;
	expires_in_minutes: number;
};

@Injectable({
	providedIn: "root",
})
export class AccessTokenService {
	private readonly sessionKey = "session";

	getTokens(): TokenData | null {
		const raw = localStorage.getItem(this.sessionKey);

		if (!raw) {
			return null;
		}

		try {
			const parsed = JSON.parse(raw) as unknown;

			if (!this.isTokenData(parsed)) {
				this.clearTokens();
				return null;
			}

			return parsed;
		} catch {
			this.clearTokens();
			return null;
		}
	}

	setTokens(session: TokenData): void {
		localStorage.setItem(this.sessionKey, JSON.stringify(session));
	}

	getAccessToken(): string | null {
		const token = this.getTokens()?.access_token.trim();
		return token ? token : null;
	}

	getTokenType(): string {
		return this.getTokens()?.token_type.trim() || "bearer";
	}

	clearTokens(): void {
		localStorage.removeItem(this.sessionKey);
	}

	private isTokenData(value: unknown): value is TokenData {
		if (!value || typeof value !== "object") {
			return false;
		}

		const candidate = value as Record<string, unknown>;

		return (
			typeof candidate["access_token"] === "string" &&
			typeof candidate["token_type"] === "string" &&
			typeof candidate["expires_in_minutes"] === "number"
		);
	}
}
