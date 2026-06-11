import 'package:mechanic_mobile/domain/entities/user.dart';
import 'package:mechanic_mobile/domain/entities/vehicle.dart';

class Incident {
  final String id;
  final String clientUserId;
  final String? vehicleId;
  final String? providerId;
  final String? assignedTechnicianId;
  final String? dispatchMode;
  final String status;
  final String priority;
  final String reportedCategory;
  final String title;
  final String description;
  final String? clientContactPhoneSnapshot;
  final double? incidentLatitude;
  final double? incidentLongitude;
  final String? addressReference;
  final double? estimatedPriceMin;
  final double? estimatedPriceMax;
  final String? aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;
  final double? responderLastLatitude;
  final double? responderLastLongitude;
  final double? routeDistanceKm;
  final int? routeEtaMinutes;
  final DateTime? requestedAt;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final DateTime createdAt;
  final DateTime updatedAt;
  final Vehicle? vehicle;
  final User? clientUser;
  final ProviderInfo? provider;
  final TechnicianInfo? assignedTechnician;

  Incident({
    required this.id,
    required this.clientUserId,
    this.vehicleId,
    this.providerId,
    this.assignedTechnicianId,
    this.dispatchMode,
    required this.status,
    required this.priority,
    required this.reportedCategory,
    required this.title,
    required this.description,
    this.clientContactPhoneSnapshot,
    this.incidentLatitude,
    this.incidentLongitude,
    this.addressReference,
    this.estimatedPriceMin,
    this.estimatedPriceMax,
    this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
    this.responderLastLatitude,
    this.responderLastLongitude,
    this.routeDistanceKm,
    this.routeEtaMinutes,
    this.requestedAt,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    required this.createdAt,
    required this.updatedAt,
    this.vehicle,
    this.clientUser,
    this.provider,
    this.assignedTechnician,
  });

  String get location {
    if (incidentLatitude != null && incidentLongitude != null) {
      return '${incidentLatitude!.toStringAsFixed(4)}, ${incidentLongitude!.toStringAsFixed(4)}';
    }
    return 'Sin ubicación';
  }

  bool get isActive => status != 'COMPLETED' && status != 'CANCELLED';
  bool get canBeCancelled => status == 'PENDING' || status == 'PUBLISHED';
  bool get hasProvider => provider != null;

  String get statusIcon {
    switch (status) {
      case 'PENDING':
        return '⏳';
      case 'PUBLISHED':
        return '📢';
      case 'ASSIGNED':
        return '👨‍🔧';
      case 'EN_ROUTE':
        return '🚗';
      case 'ON_SITE':
        return '📍';
      case 'IN_PROGRESS':
        return '🔧';
      case 'COMPLETED':
        return '✅';
      case 'CANCELLED':
        return '❌';
      default:
        return '📋';
    }
  }
}

class ProviderInfo {
  final String id;
  final String providerType;
  final String businessName;
  final String? contactPhone;
  final String? city;
  final bool isAvailable;
  final double averageRating;

  ProviderInfo({
    required this.id,
    required this.providerType,
    required this.businessName,
    this.contactPhone,
    this.city,
    required this.isAvailable,
    required this.averageRating,
  });
}

class TechnicianInfo {
  final String id;
  final String providerId;
  final String firstName;
  final String lastName;
  final String? phoneNumber;
  final String? specialty;
  final bool isActive;
  final bool isAvailable;

  TechnicianInfo({
    required this.id,
    required this.providerId,
    required this.firstName,
    required this.lastName,
    this.phoneNumber,
    this.specialty,
    required this.isActive,
    required this.isAvailable,
  });

  String get fullName => '$firstName $lastName';
}
