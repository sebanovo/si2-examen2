import { HttpErrorResponse } from "@angular/common/http";

import {
	AppFieldError,
	AppHttpError,
	AppHttpErrorCode,
} from "../models/app-http-error.model";

type BackendErrorResponse = {
	success: false;
	message: string;
	error?: {
		code?: string;
		field_errors?: BackendFieldError[];
	} | null;
	meta?: {
		request_id?: string;
	} | null;
};

type BackendFieldError = {
	field?: string | null;
	message: string;
};

function getErrorCode(status: number): AppHttpErrorCode {
	switch (status) {
		case 400:
			return "BAD_REQUEST";
		case 401:
			return "UNAUTHORIZED";
		case 403:
			return "FORBIDDEN";
		case 404:
			return "NOT_FOUND";
		case 409:
			return "CONFLICT";
		case 422:
			return "UNPROCESSABLE_ENTITY";
		default:
			return status >= 500 ? "SERVER" : "UNKNOWN";
	}
}

function isBackendErrorResponse(value: unknown): value is BackendErrorResponse {
	if (!value || typeof value !== "object") {
		return false;
	}

	const candidate = value as Record<string, unknown>;

	return (
		candidate["success"] === false && typeof candidate["message"] === "string"
	);
}

function toFieldErrors(payload: BackendErrorResponse | null): AppFieldError[] {
	const fieldErrors = payload?.error?.field_errors;

	if (!fieldErrors?.length) {
		return [];
	}

	return fieldErrors.map(item => ({
		field: item.field ?? "",
		message: item.message,
	}));
}

/**
 * Maps unknown HTTP failures to AppHttpError.
 * Preserves backend message, code and request id.
 */
export function toAppHttpError(error: unknown): AppHttpError {
	if (!(error instanceof HttpErrorResponse)) {
		return {
			code: "UNKNOWN",
			status: null,
			message: "Unexpected error",
			fieldErrors: [],
			timestamp: null,
			requestId: null,
		};
	}

	if (error.status === 0) {
		return {
			code: "NETWORK",
			status: 0,
			message: "Could not connect to the server",
			fieldErrors: [],
			timestamp: null,
			requestId: null,
		};
	}

	const payload = isBackendErrorResponse(error.error) ? error.error : null;

	return {
		code: getErrorCode(error.status),
		status: error.status || null,
		message: payload?.message ?? error.message ?? "Request failed",
		fieldErrors: toFieldErrors(payload),
		timestamp: null,
		requestId: payload?.meta?.request_id ?? null,
	};
}
