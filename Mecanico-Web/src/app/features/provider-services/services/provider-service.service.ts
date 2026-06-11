import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { Observable } from "rxjs";

import {
	ApiResponse,
	ProviderServiceDto,
	ProviderServicesMetaDto,
} from "../models/provider-service.types";

@Injectable({
	providedIn: "root",
})
export class ProviderServicesApi {
	private readonly http = inject(HttpClient);

	getProviderServices(
		providerId: string
	): Observable<ApiResponse<ProviderServiceDto[], ProviderServicesMetaDto>> {
		return this.http.get<
			ApiResponse<ProviderServiceDto[], ProviderServicesMetaDto>
		>(`/api/catalog/providers/${providerId}/services`);
	}
}
