import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	MiEmpresaDto,
	UpdateMiEmpresaRequest,
} from "../models/mi-empresa.types";

@Injectable({
	providedIn: "root",
})
export class MiEmpresaApi {
	private readonly http = inject(HttpClient);

	getMiEmpresaProfile(): Observable<MiEmpresaDto> {
		return this.http
			.get<ApiResponse<MiEmpresaDto>>("/api/providers/me/profile")
			.pipe(map(response => response.data));
	}

	updateMiEmpresaProfile(
		payload: UpdateMiEmpresaRequest
	): Observable<MiEmpresaDto> {
		return this.http
			.patch<ApiResponse<MiEmpresaDto>>("/api/providers/me/profile", payload)
			.pipe(map(response => response.data));
	}
}
