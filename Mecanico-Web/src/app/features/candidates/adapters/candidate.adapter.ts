import {
	AssignmentCandidate,
	AssignmentCandidateDto,
	CandidateActionResult,
	CandidateActionResultDto,
	CandidateIncident,
	CandidateIncidentDto,
	CandidateMatchedService,
	CandidateMatchedServiceDto,
	CandidateProvider,
	CandidateProviderDto,
	CandidateProviderOwnerUser,
	CandidateProviderOwnerUserDto,
} from "../models/candidate.types";

export function toCandidateProviderOwnerUser(
	dto: CandidateProviderOwnerUserDto
): CandidateProviderOwnerUser {
	return {
		id: dto.id,
		email: dto.email,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
	};
}

export function toCandidateMatchedService(
	dto: CandidateMatchedServiceDto
): CandidateMatchedService {
	return {
		code: dto.code,
		category: dto.category,
		title: dto.title,
	};
}

export function toCandidateMatchedServices(
	dtos: CandidateMatchedServiceDto[]
): CandidateMatchedService[] {
	return dtos.map(toCandidateMatchedService);
}

export function toCandidateProvider(
	dto: CandidateProviderDto
): CandidateProvider {
	return {
		id: dto.id,
		providerType: dto.provider_type,
		businessName: dto.business_name,
		city: dto.city,
		contactPhone: dto.contact_phone,
		averageRating: dto.average_rating,
		availableCapacity: dto.available_capacity,
		availableTechniciansCount: dto.available_technicians_count,
		baseLatitude: dto.base_latitude,
		baseLongitude: dto.base_longitude,
		ownerUser: toCandidateProviderOwnerUser(dto.owner_user),
		matchedServices: toCandidateMatchedServices(dto.matched_services),
	};
}

export function toCandidateIncident(
	dto: CandidateIncidentDto
): CandidateIncident {
	return {
		id: dto.id,
		status: dto.status,
		priority: dto.priority,
		reportedCategory: dto.reported_category,
		title: dto.title,
		description: dto.description,
		incidentLatitude: dto.incident_latitude,
		incidentLongitude: dto.incident_longitude,
		addressReference: dto.address_reference,
		aiSummaryStatus: dto.ai_summary_status,
		structuredSummary: dto.structured_summary,
		suggestedCategory: dto.suggested_category,
		suggestedPriority: dto.suggested_priority,
		requiresMoreInformation: dto.requires_more_information,
	};
}

export function toAssignmentCandidate(
	dto: AssignmentCandidateDto
): AssignmentCandidate {
	return {
		id: dto.id,
		incidentId: dto.incident_id,
		providerId: dto.provider_id,
		status: dto.status,
		recommendationRank: dto.recommendation_rank,
		score: dto.score,
		distanceKm: dto.distance_km,
		requiredServiceCodes: dto.required_service_codes,
		matchedServiceCodes: dto.matched_service_codes,
		rationale: dto.rationale,
		providerAverageRatingSnapshot: dto.provider_average_rating_snapshot,
		providerAvailableCapacitySnapshot: dto.provider_available_capacity_snapshot,
		availableTechniciansCountSnapshot: dto.available_technicians_count_snapshot,
		publishedAt: new Date(dto.published_at).toDateString(),
		respondedAt: dto.responded_at
			? new Date(dto.responded_at).toDateString()
			: null,
		expiresAt: dto.expires_at ? new Date(dto.expires_at).toDateString() : null,
		provider: toCandidateProvider(dto.provider),
		incident: toCandidateIncident(dto.incident),
	};
}

export function toAssignmentCandidates(
	dtos: AssignmentCandidateDto[]
): AssignmentCandidate[] {
	return dtos.map(toAssignmentCandidate);
}

export function toCandidateActionResult(
	dto: CandidateActionResultDto
): CandidateActionResult {
	return {
		candidateId: dto.candidate_id,
		candidateStatus: dto.candidate_status,
		incidentId: dto.incident_id,
		incidentStatus: dto.incident_status,
		assignedProviderId: dto.assigned_provider_id,
		assignedAt: dto.assigned_at
			? new Date(dto.assigned_at).toDateString()
			: null,
	};
}
