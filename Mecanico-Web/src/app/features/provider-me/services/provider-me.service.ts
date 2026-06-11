import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	CreateProviderMeTechnicianRequest,
	ProviderMeDto,
	ProviderMeTechnicianDto,
	ProviderMeTechniciansMetaDto,
	UpdateProviderMeProfileRequest,
	UpdateProviderMeTechnicianRequest,
} from "../models/provider-me.types";

@Injectable({
	providedIn: "root",
})
export class ProviderMeApi {
	private readonly http = inject(HttpClient);

	getMyProviderProfile(): Observable<ProviderMeDto> {
		return this.http
			.get<ApiResponse<ProviderMeDto>>("/api/providers/me/profile")
			.pipe(map(response => response.data));
	}

	updateMyProviderProfile(
		payload: UpdateProviderMeProfileRequest
	): Observable<ProviderMeDto> {
		return this.http
			.patch<ApiResponse<ProviderMeDto>>("/api/providers/me/profile", payload)
			.pipe(map(response => response.data));
	}

	getMyTechnicians(): Observable<
		ApiResponse<ProviderMeTechnicianDto[], ProviderMeTechniciansMetaDto>
	> {
		return this.http.get<
			ApiResponse<ProviderMeTechnicianDto[], ProviderMeTechniciansMetaDto>
		>("/api/providers/me/technicians");
	}

	createMyTechnician(
		payload: CreateProviderMeTechnicianRequest
	): Observable<ProviderMeTechnicianDto> {
		return this.http
			.post<
				ApiResponse<ProviderMeTechnicianDto>
			>("/api/providers/me/technicians", payload)
			.pipe(map(response => response.data));
	}

	updateMyTechnician(
		technicianId: string,
		payload: UpdateProviderMeTechnicianRequest
	): Observable<ProviderMeTechnicianDto> {
		return this.http
			.patch<
				ApiResponse<ProviderMeTechnicianDto>
			>(`/api/providers/me/technicians/${technicianId}`, payload)
			.pipe(map(response => response.data));
	}
}
