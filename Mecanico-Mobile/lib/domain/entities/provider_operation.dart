import 'package:flutter/material.dart';

import '../../domain/entities/user.dart';
import '../../domain/entities/technician.dart';

class ProviderOperation {
  final String incidentId;
  final String providerId;
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
  final String? aiSummaryStatus;
  final String? structuredSummary;
  final String? suggestedCategory;
  final String? suggestedPriority;
  final bool requiresMoreInformation;
  final DateTime? assignedAt;
  final DateTime? enRouteAt;
  final DateTime? arrivedAt;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final DateTime? cancelledAt;
  final User? clientUser;
  final Technician? assignedTechnician;

  ProviderOperation({
    required this.incidentId,
    required this.providerId,
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
    this.aiSummaryStatus,
    this.structuredSummary,
    this.suggestedCategory,
    this.suggestedPriority,
    required this.requiresMoreInformation,
    this.assignedAt,
    this.enRouteAt,
    this.arrivedAt,
    this.startedAt,
    this.completedAt,
    this.cancelledAt,
    this.clientUser,
    this.assignedTechnician,
  });

  String get location {
    if (incidentLatitude != null && incidentLongitude != null) {
      return '${incidentLatitude!.toStringAsFixed(4)}, ${incidentLongitude!.toStringAsFixed(4)}';
    }
    return 'Sin ubicación';
  }

  bool get canDispatch => status == 'ASSIGNED' && assignedTechnicianId == null;
  bool get canArrive => status == 'EN_ROUTE';
  bool get canStart => status == 'ON_SITE';
  bool get canComplete => status == 'IN_PROGRESS';
  bool get canCancel => status != 'COMPLETED' && status != 'CANCELLED';

  String get statusText {
    switch (status) {
      case 'ASSIGNED':
        return 'Asignado - Pendiente de despachar';
      case 'EN_ROUTE':
        return 'En camino';
      case 'ON_SITE':
        return 'En el lugar';
      case 'IN_PROGRESS':
        return 'En progreso';
      case 'COMPLETED':
        return 'Completado';
      case 'CANCELLED':
        return 'Cancelado';
      default:
        return status;
    }
  }

  Color get statusColor {
    switch (status) {
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

  IconData get statusIcon {
    switch (status) {
      case 'ASSIGNED':
        return Icons.person_add;
      case 'EN_ROUTE':
        return Icons.directions_car;
      case 'ON_SITE':
        return Icons.location_on;
      case 'IN_PROGRESS':
        return Icons.build;
      case 'COMPLETED':
        return Icons.check_circle;
      case 'CANCELLED':
        return Icons.cancel;
      default:
        return Icons.info;
    }
  }
}
