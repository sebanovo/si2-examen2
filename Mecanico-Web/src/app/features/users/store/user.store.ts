import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toGetUsersParams,
	toUpdateOwnProfileRequest,
	toUser,
	toUsers,
} from "../adapters/user.adapter";

import {
	UpdateOwnProfileFormValue,
	User,
	UsersMetaDto,
} from "../models/user.types";
import { UsersApi } from "../services/user.service";

@Injectable({
	providedIn: "root",
})
export class UsersStore {
	private readonly usersApi = inject(UsersApi);

	// =============================
	// LISTADO
	// =============================

	readonly users = signal<User[]>([]);
	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	// =============================
	// PAGINACIÓN
	// =============================

	readonly limit = signal(4); // <-- cambiar aqui si quieres 20
	readonly offset = signal(0);
	readonly meta = signal<UsersMetaDto | null>(null);

	readonly lastPageReached = signal(false);

	readonly canGoPrevious = computed(() => this.offset() > 0 && !this.loading());

	readonly canGoNext = computed(
		() =>
			!this.loading() &&
			!this.lastPageReached() &&
			this.users().length === this.limit()
	);

	readonly currentPageLabel = computed(() => {
		const start = this.offset() + 1;
		const end = this.offset() + this.users().length;

		return this.users().length === 0
			? "Sin resultados"
			: `Mostrando ${start} - ${end}`;
	});

	readonly isEmpty = computed(
		() => this.hasLoaded() && !this.loading() && this.users().length === 0
	);

	// DETALLE

	readonly selectedUser = signal<User | null>(null);
	readonly selectedUserLoading = signal(false);
	readonly selectedUserError = signal<AppHttpError | null>(null);
	readonly hasSelectedUserError = computed(
		() => this.selectedUserError() !== null
	);

	// PERFIL PROPIO

	readonly ownProfile = signal<User | null>(null);
	readonly ownProfileLoading = signal(false);
	readonly ownProfileError = signal<AppHttpError | null>(null);
	readonly hasOwnProfileError = computed(() => this.ownProfileError() !== null);

	readonly updatingOwnProfile = signal(false);
	readonly updateOwnProfileError = signal<AppHttpError | null>(null);
	readonly hasUpdateOwnProfileError = computed(
		() => this.updateOwnProfileError() !== null
	);

	// LOAD USERS

	async loadUsers(limit = this.limit(), offset = this.offset()): Promise<void> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const params = toGetUsersParams(limit, offset);

			const response = await firstValueFrom(this.usersApi.getUsers(params));

			const mappedUsers = toUsers(response.data);

			this.users.set(mappedUsers);
			this.meta.set(response.meta);
			this.limit.set(response.meta.limit);
			this.offset.set(response.meta.offset);

			this.lastPageReached.set(mappedUsers.length < response.meta.limit);

			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.users.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	// NEXT PAGE

	async nextPage(): Promise<void> {
		if (!this.canGoNext()) {
			return;
		}

		const currentUsers = this.users();
		const currentOffset = this.offset();
		const nextOffset = currentOffset + this.limit();

		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.usersApi.getUsers({
					limit: this.limit(),
					offset: nextOffset,
				})
			);

			const mappedUsers = toUsers(response.data);

			//  CASO IMPORTANTE: NO HAY MÁS DATOS
			if (mappedUsers.length === 0) {
				this.users.set(currentUsers);
				this.offset.set(currentOffset);
				this.lastPageReached.set(true);
				return;
			}

			this.users.set(mappedUsers);
			this.offset.set(response.meta.offset);
			this.limit.set(response.meta.limit);

			this.lastPageReached.set(mappedUsers.length < response.meta.limit);
		} catch (error) {
			this.error.set(error as AppHttpError);
		} finally {
			this.loading.set(false);
		}
	}

	// PREVIOUS PAGE

	async previousPage(): Promise<void> {
		if (!this.canGoPrevious()) {
			return;
		}

		const previousOffset = Math.max(this.offset() - this.limit(), 0);

		await this.loadUsers(this.limit(), previousOffset);
	}

	// HELPERS PAGINACIÓN

	async reloadUsers(): Promise<void> {
		this.lastPageReached.set(false);
		await this.loadUsers(this.limit(), this.offset());
	}

	async resetPagination(): Promise<void> {
		this.offset.set(0);
		this.lastPageReached.set(false);
		await this.loadUsers(this.limit(), 0);
	}

	// DETALLE

	async loadUserById(userId: string): Promise<User | null> {
		this.selectedUserLoading.set(true);
		this.selectedUserError.set(null);
		this.selectedUser.set(null);

		try {
			const userDto = await firstValueFrom(this.usersApi.getUserById(userId));

			const user = toUser(userDto);

			this.selectedUser.set(user);

			return user;
		} catch (error) {
			this.selectedUserError.set(error as AppHttpError);
			this.selectedUser.set(null);
			return null;
		} finally {
			this.selectedUserLoading.set(false);
		}
	}

	// PERFIL PROPIO

	async loadOwnProfile(): Promise<User | null> {
		this.ownProfileLoading.set(true);
		this.ownProfileError.set(null);

		try {
			const userDto = await firstValueFrom(this.usersApi.getOwnProfile());

			const user = toUser(userDto);

			this.ownProfile.set(user);

			return user;
		} catch (error) {
			this.ownProfileError.set(error as AppHttpError);
			this.ownProfile.set(null);
			return null;
		} finally {
			this.ownProfileLoading.set(false);
		}
	}

	async updateOwnProfile(
		formValue: UpdateOwnProfileFormValue
	): Promise<User | null> {
		this.updatingOwnProfile.set(true);
		this.updateOwnProfileError.set(null);

		try {
			const payload = toUpdateOwnProfileRequest(formValue);

			const userDto = await firstValueFrom(
				this.usersApi.updateOwnProfile(payload)
			);

			const user = toUser(userDto);

			this.ownProfile.set(user);

			// sincroniza con detalle
			if (this.selectedUser()?.id === user.id) {
				this.selectedUser.set(user);
			}

			// sincroniza con lista
			this.users.update(current =>
				current.map(u => (u.id === user.id ? user : u))
			);

			return user;
		} catch (error) {
			this.updateOwnProfileError.set(error as AppHttpError);
			return null;
		} finally {
			this.updatingOwnProfile.set(false);
		}
	}

	// CLEANERS

	clearError(): void {
		this.error.set(null);
	}

	clearSelectedUser(): void {
		this.selectedUser.set(null);
	}

	clearSelectedUserError(): void {
		this.selectedUserError.set(null);
	}

	clearOwnProfileError(): void {
		this.ownProfileError.set(null);
	}

	clearUpdateOwnProfileError(): void {
		this.updateOwnProfileError.set(null);
	}
}
