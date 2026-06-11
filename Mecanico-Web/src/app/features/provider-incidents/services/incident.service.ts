import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	ProviderIncidentDto,
	ProviderIncidentsMetaDto,
} from "../models/incident.types";

@Injectable({
	providedIn: "root",
})
export class IncidentsApi {
	private readonly http = inject(HttpClient);

	getMyProviderIncidents(): Observable<
		ApiResponse<ProviderIncidentDto[], ProviderIncidentsMetaDto>
	> {
		return this.http.get<
			ApiResponse<ProviderIncidentDto[], ProviderIncidentsMetaDto>
		>("/api/incidents/provider/me");
	}

	getMyProviderIncidentById(
		incidentId: string
	): Observable<ProviderIncidentDto> {
		return this.http
			.get<
				ApiResponse<ProviderIncidentDto>
			>(`/api/incidents/provider/me/${incidentId}`)
			.pipe(map(response => response.data));
	}
}
