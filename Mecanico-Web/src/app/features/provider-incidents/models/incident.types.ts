export type IncidentDispatchMode = "TECHNICIAN" | "PROVIDER";
export type IncidentStatus =
	| "REQUESTED"
	| "ASSIGNED"
	| "EN_ROUTE"
	| "ARRIVED"
	| "IN_PROGRESS"
	| "COMPLETED"
	| "CANCELLED";

export type IncidentPriority = "LOW" | "MEDIUM" | "HIGH" | "URGENT";

export type IncidentVehicleDto = {
	id: string;
	plate_number: string;
	vehicle_type: string;
	brand: string;
	model: string;
	year: number;
	color: string;
};

export type IncidentClientUserDto = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
};

export type IncidentProviderDto = {
	id: string;
	provider_type: string;
	business_name: string;
	contact_phone: string | null;
	city: string;
	is_available: boolean;
	average_rating: number;
};

export type IncidentTechnicianDto = {
	id: string;
	provider_id: string;
	first_name: string;
	last_name: string;
	full_name: string;
	phone_number: string | null;
	specialty: string;
	is_active: boolean;
	is_available: boolean;
};

export type ProviderIncidentDto = {
	id: string;
	client_user_id: string;
	vehicle_id: string;
	provider_id: string;
	assigned_technician_id: string | null;
	dispatch_mode: IncidentDispatchMode;
	status: IncidentStatus;
	priority: IncidentPriority;
	reported_category: string;
	title: string;
	description: string;
	client_contact_phone_snapshot: string | null;
	incident_latitude: number;
	incident_longitude: number;
	address_reference: string | null;
	estimated_price_min: number | null;
	estimated_price_max: number | null;
	ai_summary_status: string | null;
	summary_provider_name: string | null;
	structured_summary: string | null;
	suggested_category: string | null;
	suggested_priority: IncidentPriority | null;
	requires_more_information: boolean;
	summary_processed_at: string | null;
	summary_error_message: string | null;
	responder_last_latitude: number | null;
	responder_last_longitude: number | null;
	responder_last_source_type: string | null;
	responder_last_recorded_at: string | null;
	route_provider_name: string | null;
	route_distance_meters: number | null;
	route_distance_km: number | null;
	route_duration_seconds: number | null;
	route_eta_seconds: number | null;
	route_eta_minutes: number | null;
	route_polyline: string | null;
	route_last_calculated_at: string | null;
	route_error_message: string | null;
	requested_at: string;
	assigned_at: string | null;
	en_route_at: string | null;
	arrived_at: string | null;
	started_at: string | null;
	completed_at: string | null;
	cancelled_at: string | null;
	created_at: string;
	updated_at: string;
	vehicle: IncidentVehicleDto;
	client_user: IncidentClientUserDto;
	provider: IncidentProviderDto;
	assigned_technician: IncidentTechnicianDto | null;
};

export type IncidentVehicle = {
	id: string;
	plateNumber: string;
	vehicleType: string;
	brand: string;
	model: string;
	year: number;
	color: string;
};

export type IncidentClientUser = {
	id: string;
	email: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
};

export type IncidentProvider = {
	id: string;
	providerType: string;
	businessName: string;
	contactPhone: string | null;
	city: string;
	isAvailable: boolean;
	averageRating: number;
};

export type IncidentTechnician = {
	id: string;
	providerId: string;
	firstName: string;
	lastName: string;
	fullName: string;
	phoneNumber: string | null;
	specialty: string;
	isActive: boolean;
	isAvailable: boolean;
};

export type ProviderIncident = {
	id: string;
	clientUserId: string;
	vehicleId: string;
	providerId: string;
	assignedTechnicianId: string | null;
	dispatchMode: IncidentDispatchMode;
	status: IncidentStatus;
	priority: IncidentPriority;
	reportedCategory: string;
	title: string;
	description: string;
	clientContactPhoneSnapshot: string | null;
	incidentLatitude: number;
	incidentLongitude: number;
	addressReference: string | null;
	estimatedPriceMin: number | null;
	estimatedPriceMax: number | null;
	aiSummaryStatus: string | null;
	summaryProviderName: string | null;
	structuredSummary: string | null;
	suggestedCategory: string | null;
	suggestedPriority: IncidentPriority | null;
	requiresMoreInformation: boolean;
	summaryProcessedAt: string | null;
	summaryErrorMessage: string | null;
	responderLastLatitude: number | null;
	responderLastLongitude: number | null;
	responderLastSourceType: string | null;
	responderLastRecordedAt: string | null;
	routeProviderName: string | null;
	routeDistanceMeters: number | null;
	routeDistanceKm: number | null;
	routeDurationSeconds: number | null;
	routeEtaSeconds: number | null;
	routeEtaMinutes: number | null;
	routePolyline: string | null;
	routeLastCalculatedAt: string | null;
	routeErrorMessage: string | null;
	requestedAt: string;
	assignedAt: string | null;
	enRouteAt: string | null;
	arrivedAt: string | null;
	startedAt: string | null;
	completedAt: string | null;
	cancelledAt: string | null;
	createdAt: string;
	updatedAt: string;
	vehicle: IncidentVehicle;
	clientUser: IncidentClientUser;
	provider: IncidentProvider;
	assignedTechnician: IncidentTechnician | null;
};

export type ProviderIncidentsMetaDto = {
	count: number;
};

export type ApiResponse<TData, TMeta = null> = {
	success: boolean;
	message: string;
	data: TData;
	meta: TMeta;
};
