import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	CreateProviderServiceRequest,
	ProviderServiceCatalogConfigurationDto,
	ProviderServiceCatalogMetaDto,
	ProviderServiceDto,
	ProviderServicesMetaDto,
	UpdateProviderServiceRequest,
} from "../models/service.types";

@Injectable({
	providedIn: "root",
})
export class ServicesApi {
	private readonly http = inject(HttpClient);

	getMyCatalogWithConfiguration(): Observable<
		ApiResponse<
			ProviderServiceCatalogConfigurationDto[],
			ProviderServiceCatalogMetaDto
		>
	> {
		return this.http.get<
			ApiResponse<
				ProviderServiceCatalogConfigurationDto[],
				ProviderServiceCatalogMetaDto
			>
		>("/api/catalog/me/services/catalog");
	}

	getMyProviderServices(): Observable<
		ApiResponse<ProviderServiceDto[], ProviderServicesMetaDto>
	> {
		return this.http.get<
			ApiResponse<ProviderServiceDto[], ProviderServicesMetaDto>
		>("/api/catalog/me/services");
	}

	createMyProviderService(
		payload: CreateProviderServiceRequest
	): Observable<ProviderServiceDto> {
		return this.http
			.post<
				ApiResponse<ProviderServiceDto>
			>("/api/catalog/me/services", payload)
			.pipe(map(response => response.data));
	}

	updateMyProviderService(
		providerServiceId: string,
		payload: UpdateProviderServiceRequest
	): Observable<ProviderServiceDto> {
		return this.http
			.patch<
				ApiResponse<ProviderServiceDto>
			>(`/api/catalog/me/services/${providerServiceId}`, payload)
			.pipe(map(response => response.data));
	}
}
