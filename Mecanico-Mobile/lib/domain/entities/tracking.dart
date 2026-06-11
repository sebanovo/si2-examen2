import 'package:mechanic_mobile/domain/entities/admin_incident.dart';

import '../../domain/entities/user.dart';
import '../../domain/entities/technician.dart';

class TrackingData {
  final String incidentId;
  final String status;
  final String priority;
  final String title;
  final String description;
  final String? addressReference;
  final double? incidentLatitude;
  final double? incidentLongitude;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final ProviderInfo? provider;
  final Technician? assignedTechnician;
  final User? clientUser;
  final ResponderPosition? responderPosition;
  final RouteInfo? route;

  TrackingData({
    required this.incidentId,
    required this.status,
    required this.priority,
    required this.title,
    required this.description,
    this.addressReference,
    this.incidentLatitude,
    this.incidentLongitude,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    this.provider,
    this.assignedTechnician,
    this.clientUser,
    this.responderPosition,
    this.route,
  });

  String get incidentLocation {
    if (incidentLatitude != null && incidentLongitude != null) {
      return '${incidentLatitude!.toStringAsFixed(4)}, ${incidentLongitude!.toStringAsFixed(4)}';
    }
    return 'Sin ubicación';
  }

  String get formattedDistance {
    if (route?.distanceKm != null) {
      return '${route!.distanceKm.toStringAsFixed(1)} km';
    }
    return 'N/A';
  }

  String get formattedEta {
    if (route?.etaMinutes != null) {
      final minutes = route!.etaMinutes;
      if (minutes < 60) return '$minutes min';
      final hours = minutes ~/ 60;
      final remainingMinutes = minutes % 60;
      return '$hours h $remainingMinutes min';
    }
    return 'N/A';
  }
}

class ResponderPosition {
  final double latitude;
  final double longitude;
  final String sourceType;
  final DateTime recordedAt;

  ResponderPosition({
    required this.latitude,
    required this.longitude,
    required this.sourceType,
    required this.recordedAt,
  });

  String get location =>
      '${latitude.toStringAsFixed(4)}, ${longitude.toStringAsFixed(4)}';
}

class RouteInfo {
  final String providerName;
  final double distanceMeters;
  final double distanceKm;
  final int durationSeconds;
  final int etaSeconds;
  final int etaMinutes;
  final String? polyline;
  final DateTime? lastCalculatedAt;
  final String? errorMessage;

  RouteInfo({
    required this.providerName,
    required this.distanceMeters,
    required this.distanceKm,
    required this.durationSeconds,
    required this.etaSeconds,
    required this.etaMinutes,
    this.polyline,
    this.lastCalculatedAt,
    this.errorMessage,
  });
}

class TrackingHistoryItem {
  final String id;
  final String incidentId;
  final String providerId;
  final String? technicianId;
  final String sourceType;
  final double latitude;
  final double longitude;
  final double? accuracyMeters;
  final DateTime recordedAt;
  final String? providerBusinessName;
  final String? technicianFullName;

  TrackingHistoryItem({
    required this.id,
    required this.incidentId,
    required this.providerId,
    this.technicianId,
    required this.sourceType,
    required this.latitude,
    required this.longitude,
    this.accuracyMeters,
    required this.recordedAt,
    this.providerBusinessName,
    this.technicianFullName,
  });

  String get location =>
      '${latitude.toStringAsFixed(4)}, ${longitude.toStringAsFixed(4)}';
  String get formattedTime {
    return '${recordedAt.hour.toString().padLeft(2, '0')}:${recordedAt.minute.toString().padLeft(2, '0')}';
  }
}
