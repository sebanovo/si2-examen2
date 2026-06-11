export type CandidateStatus = "AVAILABLE" | "ACCEPTED" | "REJECTED" | "EXPIRED";

export type CandidateIncidentStatus =
	| "PUBLISHED"
	| "ASSIGNED"
	| "EN_ROUTE"
	| "ARRIVED"
	| "IN_PROGRESS"
	| "COMPLETED"
	| "CANCELLED";

export type CandidatePriority = "LOW" | "MEDIUM" | "HIGH" | "URGENT";

export type CandidateRationaleDto = Record<string, string>;

export type CandidateProviderOwnerUserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
};

export type CandidateMatchedServiceDto = {
	code: string;
	category: string;
	title: string;
};

export type CandidateProviderDto = {
	id: string;
	provider_type: string;
	business_name: string;
	city: string;
	contact_phone: string | null;
	average_rating: number;
	available_capacity: number;
	available_technicians_count: number;
	base_latitude: number;
	base_longitude: number;
	owner_user: CandidateProviderOwnerUserDto;
	matched_services: CandidateMatchedServiceDto[];
};

export type CandidateIncidentDto = {
	id: string;
	status: CandidateIncidentStatus;
	priority: CandidatePriority;
	reported_category: string;
	title: string;
	description: string;
	incident_latitude: number;
	incident_longitude: number;
	address_reference: string | null;
	ai_summary_status: string | null;
	structured_summary: string | null;
	suggested_category: string | null;
	suggested_priority: CandidatePriority | null;
	requires_more_information: boolean;
};

export type AssignmentCandidateDto = {
	id: string;
	incident_id: string;
	provider_id: string;
	status: CandidateStatus;
	recommendation_rank: number;
	score: number;
	distance_km: number;
	required_service_codes: string[];
	matched_service_codes: string[];
	rationale: CandidateRationaleDto;
	provider_average_rating_snapshot: number;
	provider_available_capacity_snapshot: number;
	available_technicians_count_snapshot: number;
	published_at: string;
	responded_at: string | null;
	expires_at: string | null;
	provider: CandidateProviderDto;
	incident: CandidateIncidentDto;
};

export type CandidateProviderOwnerUser = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
};

export type CandidateMatchedService = {
	code: string;
	category: string;
	title: string;
};

export type CandidateProvider = {
	id: string;
	providerType: string;
	businessName: string;
	city: string;
	contactPhone: string | null;
	averageRating: number;
	availableCapacity: number;
	availableTechniciansCount: number;
	baseLatitude: number;
	baseLongitude: number;
	ownerUser: CandidateProviderOwnerUser;
	matchedServices: CandidateMatchedService[];
};

export type CandidateIncident = {
	id: string;
	status: CandidateIncidentStatus;
	priority: CandidatePriority;
	reportedCategory: string;
	title: string;
	description: string;
	incidentLatitude: number;
	incidentLongitude: number;
	addressReference: string | null;
	aiSummaryStatus: string | null;
	structuredSummary: string | null;
	suggestedCategory: string | null;
	suggestedPriority: CandidatePriority | null;
	requiresMoreInformation: boolean;
};

export type AssignmentCandidate = {
	id: string;
	incidentId: string;
	providerId: string;
	status: CandidateStatus;
	recommendationRank: number;
	score: number;
	distanceKm: number;
	requiredServiceCodes: string[];
	matchedServiceCodes: string[];
	rationale: Record<string, string>;
	providerAverageRatingSnapshot: number;
	providerAvailableCapacitySnapshot: number;
	availableTechniciansCountSnapshot: number;
	publishedAt: string;
	respondedAt: string | null;
	expiresAt: string | null;
	provider: CandidateProvider;
	incident: CandidateIncident;
};

export type CandidateActionResultDto = {
	candidate_id: string;
	candidate_status: CandidateStatus;
	incident_id: string;
	incident_status: CandidateIncidentStatus;
	assigned_provider_id: string | null;
	assigned_at: string | null;
};

export type CandidateActionResult = {
	candidateId: string;
	candidateStatus: CandidateStatus;
	incidentId: string;
	incidentStatus: CandidateIncidentStatus;
	assignedProviderId: string | null;
	assignedAt: string | null;
};

export type CandidatesMetaDto = {
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
