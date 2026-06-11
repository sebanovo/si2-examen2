import 'package:flutter/material.dart';
import '../../domain/entities/user.dart';
import '../../domain/entities/vehicle.dart';

class AdminIncident {
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

  AdminIncident({
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
  bool get canBePublished => status == 'PENDING';

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

  Color get statusColor {
    switch (status) {
      case 'PENDING':
        return const Color(0xFFFF9800);
      case 'PUBLISHED':
        return const Color(0xFF2196F3);
      case 'ASSIGNED':
        return const Color(0xFF9C27B0);
      case 'EN_ROUTE':
        return const Color(0xFF00BCD4);
      case 'ON_SITE':
        return const Color(0xFF00897B);
      case 'IN_PROGRESS':
        return const Color(0xFF3F51B5);
      case 'COMPLETED':
        return const Color(0xFF4CAF50);
      case 'CANCELLED':
        return const Color(0xFFF44336);
      default:
        return Colors.grey;
    }
  }
}

class Candidate {
  final String id;
  final String providerId;
  final String providerName;
  final String providerType;
  final double averageRating;
  final int availableCapacity;
  final int availableTechniciansCount;
  final double distanceKm;
  final List<String> matchedServices;
  final double score;
  final String rationale;
  final DateTime createdAt;

  Candidate({
    required this.id,
    required this.providerId,
    required this.providerName,
    required this.providerType,
    required this.averageRating,
    required this.availableCapacity,
    required this.availableTechniciansCount,
    required this.distanceKm,
    required this.matchedServices,
    required this.score,
    required this.rationale,
    required this.createdAt,
  });
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
