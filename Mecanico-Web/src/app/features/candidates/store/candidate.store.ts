import { computed, inject, Injectable, signal } from "@angular/core";
import { firstValueFrom } from "rxjs";

import { AppHttpError } from "../../../core/http/models/app-http-error.model";
import {
	toAssignmentCandidate,
	toAssignmentCandidates,
	toCandidateActionResult,
} from "../adapters/candidate.adapter";
import {
	AssignmentCandidate,
	CandidateActionResult,
	CandidatesMetaDto,
} from "../models/candidate.types";
import { CandidatesApi } from "../services/candidate.service";

@Injectable({
	providedIn: "root",
})
export class CandidatesStore {
	private readonly candidatesApi = inject(CandidatesApi);

	readonly candidates = signal<AssignmentCandidate[]>([]);
	readonly meta = signal<CandidatesMetaDto | null>(null);

	readonly loading = signal(false);
	readonly hasLoaded = signal(false);
	readonly error = signal<AppHttpError | null>(null);
	readonly hasError = computed(() => this.error() !== null);

	readonly count = computed(
		() => this.meta()?.count ?? this.candidates().length
	);

	readonly isEmpty = computed(
		() => this.hasLoaded() && !this.loading() && this.candidates().length === 0
	);

	readonly selectedCandidate = signal<AssignmentCandidate | null>(null);
	readonly selectedCandidateLoading = signal(false);
	readonly selectedCandidateError = signal<AppHttpError | null>(null);
	readonly hasSelectedCandidateError = computed(
		() => this.selectedCandidateError() !== null
	);

	readonly acceptingCandidateIds = signal<string[]>([]);
	readonly acceptingCandidateError = signal<AppHttpError | null>(null);

	readonly rejectingCandidateIds = signal<string[]>([]);
	readonly rejectingCandidateError = signal<AppHttpError | null>(null);

	readonly actingCandidateIds = computed(() => [
		...this.acceptingCandidateIds(),
		...this.rejectingCandidateIds(),
	]);

	async loadAvailableCandidates(): Promise<void> {
		this.loading.set(true);
		this.error.set(null);

		try {
			const response = await firstValueFrom(
				this.candidatesApi.getAvailableCandidates()
			);

			this.candidates.set(toAssignmentCandidates(response.data));
			this.meta.set(response.meta);
			this.hasLoaded.set(true);
		} catch (error) {
			this.error.set(error as AppHttpError);
			this.candidates.set([]);
			this.meta.set(null);
			this.hasLoaded.set(true);
		} finally {
			this.loading.set(false);
		}
	}

	async loadAvailableCandidateById(
		candidateId: string
	): Promise<AssignmentCandidate | null> {
		this.selectedCandidateLoading.set(true);
		this.selectedCandidateError.set(null);
		this.selectedCandidate.set(null);

		try {
			const dto = await firstValueFrom(
				this.candidatesApi.getAvailableCandidateById(candidateId)
			);

			const candidate = toAssignmentCandidate(dto);

			this.selectedCandidate.set(candidate);

			return candidate;
		} catch (error) {
			this.selectedCandidateError.set(error as AppHttpError);
			this.selectedCandidate.set(null);
			return null;
		} finally {
			this.selectedCandidateLoading.set(false);
		}
	}

	async acceptCandidate(
		candidateId: string
	): Promise<CandidateActionResult | null> {
		this.acceptingCandidateError.set(null);
		this.acceptingCandidateIds.update(current => [...current, candidateId]);

		try {
			const dto = await firstValueFrom(
				this.candidatesApi.acceptCandidate(candidateId)
			);

			const result = toCandidateActionResult(dto);

			this.applyCandidateActionResult(result);

			return result;
		} catch (error) {
			this.acceptingCandidateError.set(error as AppHttpError);
			return null;
		} finally {
			this.acceptingCandidateIds.update(current =>
				current.filter(id => id !== candidateId)
			);
		}
	}

	async rejectCandidate(
		candidateId: string
	): Promise<CandidateActionResult | null> {
		this.rejectingCandidateError.set(null);
		this.rejectingCandidateIds.update(current => [...current, candidateId]);

		try {
			const dto = await firstValueFrom(
				this.candidatesApi.rejectCandidate(candidateId)
			);

			const result = toCandidateActionResult(dto);

			this.applyCandidateActionResult(result);

			return result;
		} catch (error) {
			this.rejectingCandidateError.set(error as AppHttpError);
			return null;
		} finally {
			this.rejectingCandidateIds.update(current =>
				current.filter(id => id !== candidateId)
			);
		}
	}

	isCandidateActing(candidateId: string): boolean {
		return this.actingCandidateIds().includes(candidateId);
	}

	private applyCandidateActionResult(result: CandidateActionResult): void {
		this.candidates.update(current =>
			current.map(candidate =>
				candidate.id === result.candidateId
					? {
							...candidate,
							status: result.candidateStatus,
							respondedAt: result.assignedAt,
							incident: {
								...candidate.incident,
								status: result.incidentStatus,
							},
						}
					: candidate
			)
		);

		const selected = this.selectedCandidate();

		if (selected?.id === result.candidateId) {
			this.selectedCandidate.set({
				...selected,
				status: result.candidateStatus,
				respondedAt: result.assignedAt,
				incident: {
					...selected.incident,
					status: result.incidentStatus,
				},
			});
		}
	}

	clearError(): void {
		this.error.set(null);
	}

	clearSelectedCandidate(): void {
		this.selectedCandidate.set(null);
	}

	clearSelectedCandidateError(): void {
		this.selectedCandidateError.set(null);
	}

	clearAcceptingCandidateError(): void {
		this.acceptingCandidateError.set(null);
	}

	clearRejectingCandidateError(): void {
		this.rejectingCandidateError.set(null);
	}
}
