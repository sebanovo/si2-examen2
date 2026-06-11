import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	CreateTechnicianRequest,
	TechnicianDto,
	TechniciansMetaDto,
	UpdateTechnicianRequest,
} from "../models/technician.types";

@Injectable({
	providedIn: "root",
})
export class TechniciansApi {
	private readonly http = inject(HttpClient);

	getProviderTechnicians(
		providerId: string
	): Observable<ApiResponse<TechnicianDto[], TechniciansMetaDto>> {
		return this.http.get<ApiResponse<TechnicianDto[], TechniciansMetaDto>>(
			`/api/providers/${providerId}/technicians`
		);
	}

	createProviderTechnician(
		providerId: string,
		payload: CreateTechnicianRequest
	): Observable<TechnicianDto> {
		return this.http
			.post<
				ApiResponse<TechnicianDto>
			>(`/api/providers/${providerId}/technicians`, payload)
			.pipe(map(response => response.data));
	}

	updateProviderTechnician(
		providerId: string,
		technicianId: string,
		payload: UpdateTechnicianRequest
	): Observable<TechnicianDto> {
		return this.http
			.patch<
				ApiResponse<TechnicianDto>
			>(`/api/providers/${providerId}/technicians/${technicianId}`, payload)
			.pipe(map(response => response.data));
	}
}
