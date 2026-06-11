import { HttpClient, HttpParams } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { map, Observable } from "rxjs";
import {
	ApiResponse,
	GetUsersParams,
	UpdateOwnProfileRequest,
	UserDto,
	UsersMetaDto,
} from "../models/user.types";

@Injectable({
	providedIn: "root",
})
export class UsersApi {
	private readonly http = inject(HttpClient);

	getOwnProfile(): Observable<UserDto> {
		return this.http
			.get<ApiResponse<UserDto>>("/api/users/me/profile")
			.pipe(map(response => response.data));
	}

	updateOwnProfile(payload: UpdateOwnProfileRequest): Observable<UserDto> {
		return this.http
			.patch<ApiResponse<UserDto>>("/api/users/me/profile", payload)
			.pipe(map(response => response.data));
	}

	getUsers(
		params: GetUsersParams
	): Observable<ApiResponse<UserDto[], UsersMetaDto>> {
		const httpParams = new HttpParams()
			.set("limit", params.limit)
			.set("offset", params.offset);

		return this.http.get<ApiResponse<UserDto[], UsersMetaDto>>("/api/users", {
			params: httpParams,
		});
	}

	getUserById(userId: string): Observable<UserDto> {
		return this.http
			.get<ApiResponse<UserDto>>(`/api/users/${userId}`)
			.pipe(map(response => response.data));
	}
}
