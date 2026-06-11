class ProviderCandidate {
  final String id;
  final String incidentId;
  final String providerId;
  final String status;
  final int recommendationRank;
  final double score;
  final double distanceKm;
  final List<String> requiredServiceCodes;
  final List<String> matchedServiceCodes;
  final Map<String, dynamic> rationale;
  final double providerAverageRatingSnapshot;
  final int providerAvailableCapacitySnapshot;
  final int availableTechniciansCountSnapshot;
  final DateTime publishedAt;
  final DateTime? respondedAt;
  final DateTime? expiresAt;
  final CandidateProvider provider;
  final CandidateIncident incident;

  ProviderCandidate({
    required this.id,
    required this.incidentId,
    required this.providerId,
    required this.status,
    required this.recommendationRank,
    required this.score,
    required this.distanceKm,
    required this.requiredServiceCodes,
    required this.matchedServiceCodes,
    required this.rationale,
    required this.providerAverageRatingSnapshot,
    required this.providerAvailableCapacitySnapshot,
    required this.availableTechniciansCountSnapshot,
    required this.publishedAt,
    this.respondedAt,
    this.expiresAt,
    required this.provider,
    required this.incident,
  });

  String get formattedDistance => '${distanceKm.toStringAsFixed(1)} km';
  String get formattedScore => '${score.toStringAsFixed(1)} pts';
  String get priority => incident.priority;
  String get category => incident.reportedCategory;
}

class CandidateProvider {
  final String id;
  final String providerType;
  final String businessName;
  final String city;
  final String? contactPhone;
  final double averageRating;
  final int availableCapacity;
  final int availableTechniciansCount;
  final double baseLatitude;
  final double baseLongitude;
  final CandidateProviderOwnerUser ownerUser;
  final List<CandidateMatchedService> matchedServices;

  CandidateProvider({
    required this.id,
    required this.providerType,
    required this.businessName,
    required this.city,
    this.contactPhone,
    required this.averageRating,
    required this.availableCapacity,
    required this.availableTechniciansCount,
    required this.baseLatitude,
    required this.baseLongitude,
    required this.ownerUser,
    required this.matchedServices,
  });
}

class CandidateProviderOwnerUser {
  final String id;
  final String email;
  final String firstName;
  final String lastName;
  final String fullName;
  final String phoneNumber;

  CandidateProviderOwnerUser({
    required this.id,
    required this.email,
    required this.firstName,
    required this.lastName,
    required this.fullName,
    required this.phoneNumber,
  });
}

class CandidateMatchedService {
  final String code;
  final String category;
  final String title;

  CandidateMatchedService({
    required this.code,
    required this.category,
    required this.title,
  });
}

class CandidateIncident {
  final String id;
  final String status;
  final String priority;
  final String reportedCategory;
  final String title;
  final String description;
  final double incidentLatitude;
  final double incidentLongitude;
  final String addressReference;
  final String aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;

  CandidateIncident({
    required this.id,
    required this.status,
    required this.priority,
    required this.reportedCategory,
    required this.title,
    required this.description,
    required this.incidentLatitude,
    required this.incidentLongitude,
    required this.addressReference,
    required this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
  });

  String get location {
    return '${incidentLatitude.toStringAsFixed(4)}, ${incidentLongitude.toStringAsFixed(4)}';
  }
}