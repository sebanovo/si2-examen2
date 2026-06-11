import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../domain/entities/incident.dart';

class IncidentDetailPage extends StatefulWidget {
  final Incident? incident;

  const IncidentDetailPage({super.key, this.incident});

  @override
  State<IncidentDetailPage> createState() => _IncidentDetailPageState();
}

class _IncidentDetailPageState extends State<IncidentDetailPage> {
  late Incident _incident;

  @override
  void initState() {
    super.initState();
    if (widget.incident == null) {
      _incident = widget.incident!;
    } else {
      _incident = widget.incident!;
    }
  }

  String _formatDate(DateTime? date) {
    if (date == null) return 'N/A';
    return '${date.day}/${date.month}/${date.year} ${date.hour}:${date.minute.toString().padLeft(2, '0')}';
  }

  Color _getStatusColor(String status) {
    switch (status) {
      case 'PENDING':
        return Colors.orange;
      case 'PUBLISHED':
        return Colors.blue;
      case 'ASSIGNED':
        return Colors.purple;
      case 'EN_ROUTE':
        return Colors.cyan;
      case 'ON_SITE':
        return Colors.teal;
      case 'IN_PROGRESS':
        return Colors.indigo;
      case 'COMPLETED':
        return Colors.green.shade500;
      case 'CANCELLED':
        return Colors.red;
      default:
        return Colors.grey;
    }
  }

  Color _getPriorityColor(String priority) {
    switch (priority) {
      case 'LOW':
        return Colors.green.shade500;
      case 'MEDIUM':
        return Colors.orange;
      case 'HIGH':
        return Colors.red;
      case 'URGENT':
        return Colors.purple;
      default:
        return Colors.grey;
    }
  }

  Widget _buildInfoRow(String label, String value, {IconData? icon}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (icon != null)
            Padding(
              padding: const EdgeInsets.only(right: 12),
              child: Icon(icon, size: 20, color: Colors.green.shade500),
            ),
          SizedBox(
            width: 120,
            child: Text(
              label,
              style: const TextStyle(
                fontWeight: FontWeight.w600,
                color: Colors.grey,
              ),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: const TextStyle(fontSize: 14, color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTimelineItem(
    String label,
    DateTime? date,
    IconData icon, {
    bool isCompleted = false,
  }) {
    final color = isCompleted && date != null
        ? Colors.green.shade500
        : Colors.grey.shade500;

    return Column(
      children: [
        Row(
          children: [
            Container(
              width: 32,
              height: 32,
              decoration: BoxDecoration(
                color: color.withValues(alpha: 0.2),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, size: 18, color: color),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    label,
                    style: TextStyle(
                      fontWeight: FontWeight.w500,
                      color: isCompleted ? Colors.white : Colors.grey.shade400,
                    ),
                  ),
                  if (date != null)
                    Text(
                      _formatDate(date),
                      style: TextStyle(
                        fontSize: 12,
                        color: Colors.grey.shade500,
                      ),
                    ),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Detalle de Solicitud'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 2,
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () async {
          final result = await context.push('/add-evidence/${_incident.id}');
          if (result == true) {
            // Recargar datos si es necesario
          }
        },
        icon: const Icon(Icons.add),
        label: const Text('Agregar Evidencia'),
        backgroundColor: Colors.green.shade600,
        foregroundColor: Colors.white,
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              const Color(0xFF1a1a2e),
              const Color(0xFF16213e),
              const Color(0xFF0f3460),
            ],
          ),
        ),
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Estado y Prioridad
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    decoration: BoxDecoration(
                      color: _getStatusColor(
                        _incident.status,
                      ).withValues(alpha: 0.1),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.circle,
                          size: 10,
                          color: _getStatusColor(_incident.status),
                        ),
                        const SizedBox(width: 6),
                        Text(
                          _incident.status,
                          style: TextStyle(
                            color: _getStatusColor(_incident.status),
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 12),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    decoration: BoxDecoration(
                      color: _getPriorityColor(
                        _incident.priority,
                      ).withValues(alpha: 0.1),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.priority_high,
                          size: 14,
                          color: _getPriorityColor(_incident.priority),
                        ),
                        const SizedBox(width: 6),
                        Text(
                          _incident.priority,
                          style: TextStyle(
                            color: _getPriorityColor(_incident.priority),
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // Información del incidente
              Card(
                color: const Color(0xFF1e1e2f),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Información de la Solicitud',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                      _buildInfoRow(
                        'Título',
                        _incident.title,
                        icon: Icons.title,
                      ),
                      _buildInfoRow(
                        'Descripción',
                        _incident.description,
                        icon: Icons.description,
                      ),
                      _buildInfoRow(
                        'Categoría',
                        _incident.reportedCategory,
                        icon: Icons.category,
                      ),
                      if (_incident.addressReference != null)
                        _buildInfoRow(
                          'Dirección',
                          _incident.addressReference!,
                          icon: Icons.location_on,
                        ),
                      if (_incident.incidentLatitude != null &&
                          _incident.incidentLongitude != null)
                        _buildInfoRow(
                          'Coordenadas',
                          _incident.location,
                          icon: Icons.public,
                        ),
                      _buildInfoRow(
                        'Fecha',
                        _formatDate(_incident.createdAt),
                        icon: Icons.calendar_today,
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 16),

              // Información del vehículo
              if (_incident.vehicle != null)
                Card(
                  color: const Color(0xFF1e1e2f),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Vehículo',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                        _buildInfoRow(
                          'Marca',
                          _incident.vehicle!.brand,
                          icon: Icons.directions_car,
                        ),
                        _buildInfoRow('Modelo', _incident.vehicle!.model),
                        _buildInfoRow('Placa', _incident.vehicle!.plateNumber),
                        _buildInfoRow(
                          'Año',
                          _incident.vehicle!.year.toString(),
                        ),
                        _buildInfoRow('Color', _incident.vehicle!.color),
                      ],
                    ),
                  ),
                ),
              const SizedBox(height: 16),

              // Información del proveedor/taller
              if (_incident.provider != null)
                Card(
                  color: const Color(0xFF1e1e2f),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Taller Asignado',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                        _buildInfoRow(
                          'Nombre',
                          _incident.provider!.businessName,
                          icon: Icons.business,
                        ),
                        if (_incident.provider!.contactPhone != null)
                          _buildInfoRow(
                            'Teléfono',
                            _incident.provider!.contactPhone!,
                            icon: Icons.phone,
                          ),
                        if (_incident.provider!.city != null)
                          _buildInfoRow(
                            'Ciudad',
                            _incident.provider!.city!,
                            icon: Icons.location_city,
                          ),
                      ],
                    ),
                  ),
                ),
              const SizedBox(height: 16),

              // Información del técnico
              if (_incident.assignedTechnician != null)
                Card(
                  color: const Color(0xFF1e1e2f),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Técnico Asignado',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                        _buildInfoRow(
                          'Nombre',
                          _incident.assignedTechnician!.fullName,
                          icon: Icons.person,
                        ),
                        if (_incident.assignedTechnician!.phoneNumber != null)
                          _buildInfoRow(
                            'Teléfono',
                            _incident.assignedTechnician!.phoneNumber!,
                            icon: Icons.phone,
                          ),
                        if (_incident.assignedTechnician!.specialty != null)
                          _buildInfoRow(
                            'Especialidad',
                            _incident.assignedTechnician!.specialty!,
                            icon: Icons.build,
                          ),
                      ],
                    ),
                  ),
                ),
              const SizedBox(height: 16),

              // Ruta y ETA
              if (_incident.routeDistanceKm != null)
                Card(
                  color: const Color(0xFF1e1e2f),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Información de Ruta',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                        _buildInfoRow(
                          'Distancia',
                          '${_incident.routeDistanceKm!.toStringAsFixed(1)} km',
                          icon: Icons.route,
                        ),
                        _buildInfoRow(
                          'ETA estimado',
                          '${_incident.routeEtaMinutes} minutos',
                          icon: Icons.timer,
                        ),
                        if (_incident.responderLastLatitude != null)
                          _buildInfoRow(
                            'Ubicación del respondedor',
                            '${_incident.responderLastLatitude!.toStringAsFixed(4)}, ${_incident.responderLastLongitude!.toStringAsFixed(4)}',
                            icon: Icons.location_searching,
                          ),
                      ],
                    ),
                  ),
                ),
              const SizedBox(height: 16),

              // Timeline de estados
              Card(
                color: const Color(0xFF1e1e2f),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Línea de Tiempo',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                      _buildTimelineItem(
                        'Solicitud creada',
                        _incident.requestedAt ?? _incident.createdAt,
                        Icons.add_circle_outline,
                        isCompleted: true,
                      ),
                      if (_incident.assignedAt != null)
                        _buildTimelineItem(
                          'Asignado a taller',
                          _incident.assignedAt,
                          Icons.assignment_ind,
                          isCompleted: true,
                        ),
                      if (_incident.enRouteAt != null)
                        _buildTimelineItem(
                          'Técnico en camino',
                          _incident.enRouteAt,
                          Icons.directions_car,
                          isCompleted: true,
                        ),
                      if (_incident.arrivedAt != null)
                        _buildTimelineItem(
                          'Técnico en el lugar',
                          _incident.arrivedAt,
                          Icons.location_on,
                          isCompleted: true,
                        ),
                      if (_incident.startedAt != null)
                        _buildTimelineItem(
                          'Servicio iniciado',
                          _incident.startedAt,
                          Icons.build,
                          isCompleted: true,
                        ),
                      if (_incident.completedAt != null)
                        _buildTimelineItem(
                          'Servicio completado',
                          _incident.completedAt,
                          Icons.check_circle,
                          isCompleted: true,
                        ),
                      if (_incident.cancelledAt != null)
                        _buildTimelineItem(
                          'Solicitud cancelada',
                          _incident.cancelledAt,
                          Icons.cancel,
                          isCompleted: true,
                        ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 32),
            ],
          ),
        ),
      ),
    );
  }
}
