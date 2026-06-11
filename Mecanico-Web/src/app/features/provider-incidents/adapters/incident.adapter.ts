import {
	IncidentClientUser,
	IncidentClientUserDto,
	IncidentProvider,
	IncidentProviderDto,
	IncidentTechnician,
	IncidentTechnicianDto,
	IncidentVehicle,
	IncidentVehicleDto,
	ProviderIncident,
	ProviderIncidentDto,
} from "../models/incident.types";

export function toIncidentVehicle(dto: IncidentVehicleDto): IncidentVehicle {
	return {
		id: dto.id,
		plateNumber: dto.plate_number,
		vehicleType: dto.vehicle_type,
		brand: dto.brand,
		model: dto.model,
		year: dto.year,
		color: dto.color,
	};
}

export function toIncidentClientUser(
	dto: IncidentClientUserDto
): IncidentClientUser {
	return {
		id: dto.id,
		email: dto.email,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
	};
}

export function toIncidentProvider(dto: IncidentProviderDto): IncidentProvider {
	return {
		id: dto.id,
		providerType: dto.provider_type,
		businessName: dto.business_name,
		contactPhone: dto.contact_phone,
		city: dto.city,
		isAvailable: dto.is_available,
		averageRating: dto.average_rating,
	};
}

export function toIncidentTechnician(
	dto: IncidentTechnicianDto
): IncidentTechnician {
	return {
		id: dto.id,
		providerId: dto.provider_id,
		firstName: dto.first_name,
		lastName: dto.last_name,
		fullName: dto.full_name,
		phoneNumber: dto.phone_number,
		specialty: dto.specialty,
		isActive: dto.is_active,
		isAvailable: dto.is_available,
	};
}

export function toProviderIncident(dto: ProviderIncidentDto): ProviderIncident {
	return {
		id: dto.id,
		clientUserId: dto.client_user_id,
		vehicleId: dto.vehicle_id,
		providerId: dto.provider_id,
		assignedTechnicianId: dto.assigned_technician_id,
		dispatchMode: dto.dispatch_mode,
		status: dto.status,
		priority: dto.priority,
		reportedCategory: dto.reported_category,
		title: dto.title,
		description: dto.description,
		clientContactPhoneSnapshot: dto.client_contact_phone_snapshot,
		incidentLatitude: dto.incident_latitude,
		incidentLongitude: dto.incident_longitude,
		addressReference: dto.address_reference,
		estimatedPriceMin: dto.estimated_price_min,
		estimatedPriceMax: dto.estimated_price_max,
		aiSummaryStatus: dto.ai_summary_status,
		summaryProviderName: dto.summary_provider_name,
		structuredSummary: dto.structured_summary,
		suggestedCategory: dto.suggested_category,
		suggestedPriority: dto.suggested_priority,
		requiresMoreInformation: dto.requires_more_information,
		summaryProcessedAt: dto.summary_processed_at
			? new Date(dto.summary_processed_at).toDateString()
			: null,
		summaryErrorMessage: dto.summary_error_message,
		responderLastLatitude: dto.responder_last_latitude,
		responderLastLongitude: dto.responder_last_longitude,
		responderLastSourceType: dto.responder_last_source_type,
		responderLastRecordedAt: dto.responder_last_recorded_at
			? new Date(dto.responder_last_recorded_at).toDateString()
			: null,
		routeProviderName: dto.route_provider_name,
		routeDistanceMeters: dto.route_distance_meters,
		routeDistanceKm: dto.route_distance_km,
		routeDurationSeconds: dto.route_duration_seconds,
		routeEtaSeconds: dto.route_eta_seconds,
		routeEtaMinutes: dto.route_eta_minutes,
		routePolyline: dto.route_polyline,
		routeLastCalculatedAt: dto.route_last_calculated_at
			? new Date(dto.route_last_calculated_at).toDateString()
			: null,
		routeErrorMessage: dto.route_error_message,
		requestedAt: new Date(dto.requested_at).toDateString(),
		assignedAt: dto.assigned_at
			? new Date(dto.assigned_at).toDateString()
			: null,
		enRouteAt: dto.en_route_at
			? new Date(dto.en_route_at).toDateString()
			: null,
		arrivedAt: dto.arrived_at ? new Date(dto.arrived_at).toDateString() : null,
		startedAt: dto.started_at ? new Date(dto.started_at).toDateString() : null,
		completedAt: dto.completed_at
			? new Date(dto.completed_at).toDateString()
			: null,
		cancelledAt: dto.cancelled_at
			? new Date(dto.cancelled_at).toDateString()
			: null,
		createdAt: new Date(dto.created_at).toDateString(),
		updatedAt: new Date(dto.updated_at).toDateString(),
		vehicle: toIncidentVehicle(dto.vehicle),
		clientUser: toIncidentClientUser(dto.client_user),
		provider: toIncidentProvider(dto.provider),
		assignedTechnician: dto.assigned_technician
			? toIncidentTechnician(dto.assigned_technician)
			: null,
	};
}

export function toProviderIncidents(
	dtos: ProviderIncidentDto[]
): ProviderIncident[] {
	return dtos.map(toProviderIncident);
}
