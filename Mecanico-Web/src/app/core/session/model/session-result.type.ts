import { AuthUser } from "../../../features/auth/models/auth.types";

export type SessionBootstrapResult =
	| {
			status: "authenticated";
			user: AuthUser;
			errorMessage: null;
	  }
	| {
			status: "unauthenticated";
			user: null;
			errorMessage: string | null;
	  };
