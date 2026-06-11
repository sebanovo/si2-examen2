import { AuthUser } from "../../../features/auth/models/auth.types";

export type SessionStatus =
	| "idle"
	| "bootstrapping"
	| "authenticated"
	| "unauthenticated";

export type SessionState = {
	status: SessionStatus;
	initialized: boolean;
	user: AuthUser | null;
	errorMessage: string | null;
};
