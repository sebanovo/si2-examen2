import { HttpClient, HttpParams } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	GetProvidersParams,
	OnboardProviderRequest,
	ProviderDto,
	ProvidersMetaDto,
	UpdateProviderOperationsRequest,
} from "../models/provider.types";

@Injectable({
	providedIn: "root",
})
export class ProvidersApi {
	private readonly http = inject(HttpClient);

	onboardProvider(payload: OnboardProviderRequest): Observable<ProviderDto> {
		return this.http
			.post<ApiResponse<ProviderDto>>("/api/providers/onboarding", payload)
			.pipe(map(response => response.data));
	}

	getProviders(
		params: GetProvidersParams
	): Observable<ApiResponse<ProviderDto[], ProvidersMetaDto>> {
		const httpParams = new HttpParams()
			.set("limit", params.limit)
			.set("offset", params.offset);

		return this.http.get<ApiResponse<ProviderDto[], ProvidersMetaDto>>(
			"/api/providers",
			{
				params: httpParams,
			}
		);
	}

	getProviderById(providerId: string): Observable<ProviderDto> {
		return this.http
			.get<ApiResponse<ProviderDto>>(`/api/providers/${providerId}`)
			.pipe(map(response => response.data));
	}

	updateProviderOperations(
		providerId: string,
		payload: UpdateProviderOperationsRequest
	): Observable<ProviderDto> {
		return this.http
			.patch<
				ApiResponse<ProviderDto>
			>(`/api/providers/${providerId}/operations`, payload)
			.pipe(map(response => response.data));
	}
}
