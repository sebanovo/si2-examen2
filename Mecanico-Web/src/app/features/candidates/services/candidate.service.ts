import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";

import {
	ApiResponse,
	AssignmentCandidateDto,
	CandidateActionResultDto,
	CandidatesMetaDto,
} from "../models/candidate.types";

@Injectable({
	providedIn: "root",
})
export class CandidatesApi {
	private readonly http = inject(HttpClient);

	getAvailableCandidates(): Observable<
		ApiResponse<AssignmentCandidateDto[], CandidatesMetaDto>
	> {
		return this.http.get<
			ApiResponse<AssignmentCandidateDto[], CandidatesMetaDto>
		>("/api/assignment/provider/me/available");
	}

	getAvailableCandidateById(
		candidateId: string
	): Observable<AssignmentCandidateDto> {
		return this.http
			.get<
				ApiResponse<AssignmentCandidateDto>
			>(`/api/assignment/provider/me/available/${candidateId}`)
			.pipe(map(response => response.data));
	}

	acceptCandidate(candidateId: string): Observable<CandidateActionResultDto> {
		return this.http
			.post<
				ApiResponse<CandidateActionResultDto>
			>(`/api/assignment/provider/me/available/${candidateId}/accept`, {})
			.pipe(map(response => response.data));
	}

	rejectCandidate(candidateId: string): Observable<CandidateActionResultDto> {
		return this.http
			.post<
				ApiResponse<CandidateActionResultDto>
			>(`/api/assignment/provider/me/available/${candidateId}/reject`, {})
			.pipe(map(response => response.data));
	}
}
