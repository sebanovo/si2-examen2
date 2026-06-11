import 'package:flutter/material.dart';
import 'package:mechanic_mobile/core/di/injection_container.dart';
import '../viewmodels/client_tracking_viewmodel.dart';

class ClientTrackingPage extends StatefulWidget {
  final String incidentId;

  const ClientTrackingPage({super.key, required this.incidentId});

  @override
  State<ClientTrackingPage> createState() => _ClientTrackingPageState();
}

class _ClientTrackingPageState extends State<ClientTrackingPage> {
  late ClientTrackingViewModel _viewModel;

  @override
  void initState() {
    super.initState();
    _viewModel = sl<ClientTrackingViewModel>();
    _loadData();
  }

  Future<void> _loadData() async {
    await _viewModel.loadLiveTracking(widget.incidentId);
    await _viewModel.loadTrackingHistory(widget.incidentId);
  }

  // void _showSnackBar(String message, {bool isError = false}) {
  //   ScaffoldMessenger.of(context).hideCurrentSnackBar();
  //   ScaffoldMessenger.of(context).showSnackBar(
  //     SnackBar(
  //       content: Row(
  //         children: [
  //           Icon(
  //             isError ? Icons.error_outline : Icons.check_circle_outline,
  //             color: Colors.white,
  //           ),
  //           const SizedBox(width: 12),
  //           Expanded(child: Text(message)),
  //         ],
  //       ),
  //       backgroundColor: isError ? Colors.red.shade700 : Colors.green.shade700,
  //       behavior: SnackBarBehavior.floating,
  //       shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
  //       margin: const EdgeInsets.all(12),
  //       duration: const Duration(seconds: 3),
  //     ),
  //   );
  // }

  String _formatDateTime(DateTime? date) {
    if (date == null) return 'N/A';
    return '${date.day}/${date.month}/${date.year} ${date.hour}:${date.minute.toString().padLeft(2, '0')}';
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Seguimiento de Servicio'),
          backgroundColor: const Color(0xFF1a1a2e),
          foregroundColor: Colors.white,
          elevation: 2,
          bottom: const TabBar(
            tabs: [
              Tab(icon: Icon(Icons.pin), text: 'En Vivo'),
              Tab(icon: Icon(Icons.history), text: 'Historial'),
            ],
          ),
          actions: [
            IconButton(
              icon: const Icon(Icons.refresh, color: Colors.white),
              onPressed: _loadData,
              tooltip: 'Actualizar',
            ),
          ],
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
          child: ListenableBuilder(
            listenable: _viewModel,
            builder: (context, _) {
              if (_viewModel.isLoading && _viewModel.trackingData == null) {
                return const Center(
                  child: CircularProgressIndicator(
                    valueColor: AlwaysStoppedAnimation<Color>(Colors.green),
                  ),
                );
              }

              if (_viewModel.errorMessage != null &&
                  _viewModel.trackingData == null) {
                return Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.error_outline,
                        size: 64,
                        color: Colors.red.shade300,
                      ),
                      const SizedBox(height: 16),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 32),
                        child: Text(
                          _viewModel.errorMessage!,
                          style: TextStyle(color: Colors.grey.shade400),
                          textAlign: TextAlign.center,
                        ),
                      ),
                      const SizedBox(height: 16),
                      ElevatedButton.icon(
                        onPressed: _loadData,
                        icon: const Icon(Icons.refresh),
                        label: const Text('Reintentar'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade600,
                          foregroundColor: Colors.white,
                        ),
                      ),
                    ],
                  ),
                );
              }

              if (_viewModel.trackingData == null) {
                return const SizedBox.shrink();
              }

              final data = _viewModel.trackingData!;

              return TabBarView(
                children: [
                  // Live Tracking Tab
                  RefreshIndicator(
                    onRefresh: _loadData,
                    color: Colors.green,
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          // Estado actual
                          Card(
                            color: _getStatusColor(
                              data.status,
                            ).withValues(alpha: 0.1),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(16),
                            ),
                            child: Padding(
                              padding: const EdgeInsets.all(16),
                              child: Row(
                                children: [
                                  Icon(
                                    _getStatusIcon(data.status),
                                    color: _getStatusColor(data.status),
                                    size: 32,
                                  ),
                                  const SizedBox(width: 16),
                                  Expanded(
                                    child: Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        const Text(
                                          'Estado del Servicio',
                                          style: TextStyle(
                                            fontSize: 12,
                                            color: Colors.grey,
                                          ),
                                        ),
                                        Text(
                                          _getStatusText(data.status),
                                          style: TextStyle(
                                            fontSize: 20,
                                            fontWeight: FontWeight.bold,
                                            color: _getStatusColor(data.status),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                          const SizedBox(height: 16),

                          // Información del taller
                          if (data.provider != null)
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
                                    const Divider(
                                      color: Color.fromRGBO(66, 66, 66, 1),
                                    ),
                                    _buildInfoRow(
                                      'Nombre',
                                      data.provider!.businessName,
                                    ),
                                    if (data.provider!.contactPhone != null)
                                      _buildInfoRow(
                                        'Teléfono',
                                        data.provider!.contactPhone!,
                                      ),
                                    if (data.provider!.city != null)
                                      _buildInfoRow(
                                        'Ciudad',
                                        data.provider!.city!,
                                      ),
                                  ],
                                ),
                              ),
                            ),
                          const SizedBox(height: 16),

                          // Información del técnico
                          if (data.assignedTechnician != null)
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
                                    const Divider(
                                      color: Color.fromRGBO(66, 66, 66, 1),
                                    ),
                                    _buildInfoRow(
                                      'Nombre',
                                      data.assignedTechnician!.fullName,
                                    ),
                                    _buildInfoRow(
                                      'Especialidad',
                                      data.assignedTechnician!.specialty,
                                    ),
                                    _buildInfoRow(
                                      'Teléfono',
                                      data.assignedTechnician!.phoneNumber,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          const SizedBox(height: 16),

                          // Ubicación actual del técnico
                          if (data.responderPosition != null)
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
                                    Row(
                                      children: [
                                        Icon(
                                          Icons.location_on,
                                          color: Colors.green.shade500,
                                        ),
                                        const SizedBox(width: 8),
                                        const Text(
                                          'Ubicación del Técnico',
                                          style: TextStyle(
                                            fontSize: 18,
                                            fontWeight: FontWeight.bold,
                                            color: Colors.white,
                                          ),
                                        ),
                                      ],
                                    ),
                                    const Divider(
                                      color: Color.fromRGBO(66, 66, 66, 1),
                                    ),
                                    _buildInfoRow(
                                      'Coordenadas',
                                      data.responderPosition!.location,
                                    ),
                                    _buildInfoRow(
                                      'Actualizado',
                                      _formatDateTime(
                                        data.responderPosition!.recordedAt,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          const SizedBox(height: 16),

                          // Información de ruta
                          if (data.route != null)
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
                                    Row(
                                      children: [
                                        Icon(
                                          Icons.route,
                                          color: Colors.green.shade500,
                                        ),
                                        const SizedBox(width: 8),
                                        const Text(
                                          'Información de la Ruta',
                                          style: TextStyle(
                                            fontSize: 18,
                                            fontWeight: FontWeight.bold,
                                            color: Colors.white,
                                          ),
                                        ),
                                      ],
                                    ),
                                    const Divider(
                                      color: Color.fromRGBO(66, 66, 66, 1),
                                    ),
                                    _buildInfoRow(
                                      'Distancia',
                                      data.formattedDistance,
                                    ),
                                    _buildInfoRow(
                                      'ETA estimado',
                                      data.formattedEta,
                                    ),
                                    if (data.route!.errorMessage != null)
                                      Container(
                                        padding: const EdgeInsets.all(8),
                                        decoration: BoxDecoration(
                                          color: Colors.orange.shade900
                                              .withValues(alpha: 0.3),
                                          borderRadius: BorderRadius.circular(
                                            8,
                                          ),
                                        ),
                                        child: Row(
                                          children: [
                                            Icon(
                                              Icons.warning_amber,
                                              size: 16,
                                              color: Colors.orange.shade400,
                                            ),
                                            const SizedBox(width: 8),
                                            Expanded(
                                              child: Text(
                                                data.route!.errorMessage!,
                                                style: TextStyle(
                                                  fontSize: 12,
                                                  color: Colors.orange.shade300,
                                                ),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                  ],
                                ),
                              ),
                            ),
                        ],
                      ),
                    ),
                  ),

                  // Tracking History Tab
                  RefreshIndicator(
                    onRefresh: () =>
                        _viewModel.loadTrackingHistory(widget.incidentId),
                    color: Colors.green,
                    child: _viewModel.history.isEmpty
                        ? Center(
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(
                                  Icons.history,
                                  size: 64,
                                  color: Colors.green.shade400,
                                ),
                                const SizedBox(height: 16),
                                Text(
                                  'No hay historial de ubicaciones',
                                  style: TextStyle(
                                    fontSize: 18,
                                    color: Colors.grey.shade400,
                                    fontWeight: FontWeight.w500,
                                  ),
                                ),
                                const SizedBox(height: 8),
                                Text(
                                  'El técnico aún no ha reportado ubicaciones',
                                  style: TextStyle(color: Colors.grey.shade500),
                                ),
                              ],
                            ),
                          )
                        : ListView.builder(
                            padding: const EdgeInsets.all(12),
                            itemCount: _viewModel.history.length,
                            itemBuilder: (context, index) {
                              final item = _viewModel.history[index];
                              return Card(
                                margin: const EdgeInsets.only(bottom: 12),
                                color: const Color(0xFF1e1e2f),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(16),
                                ),
                                child: ListTile(
                                  leading: CircleAvatar(
                                    backgroundColor: Colors.green.shade900
                                        .withValues(alpha: 0.5),
                                    child: const Icon(
                                      Icons.location_on,
                                      color: Colors.green,
                                    ),
                                  ),
                                  title: Text(
                                    item.location,
                                    style: const TextStyle(
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                  ),
                                  subtitle: Column(
                                    crossAxisAlignment:
                                        CrossAxisAlignment.start,
                                    children: [
                                      if (item.technicianFullName != null)
                                        Text(
                                          '👨‍🔧 ${item.technicianFullName}',
                                          style: TextStyle(
                                            color: Colors.grey.shade400,
                                          ),
                                        ),
                                      if (item.accuracyMeters != null)
                                        Text(
                                          '🎯 Precisión: ${item.accuracyMeters!.toStringAsFixed(0)} m',
                                          style: TextStyle(
                                            color: Colors.grey.shade400,
                                          ),
                                        ),
                                    ],
                                  ),
                                  trailing: Text(
                                    _formatDateTime(item.recordedAt),
                                    style: TextStyle(
                                      color: Colors.grey.shade500,
                                      fontSize: 12,
                                    ),
                                  ),
                                ),
                              );
                            },
                          ),
                  ),
                ],
              );
            },
          ),
        ),
      ),
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 100,
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

  Color _getStatusColor(String status) {
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
        return Colors.green.shade500;
      case 'CANCELLED':
        return const Color(0xFFF44336);
      default:
        return Colors.grey;
    }
  }

  IconData _getStatusIcon(String status) {
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

  String _getStatusText(String status) {
    switch (status) {
      case 'ASSIGNED':
        return 'Asignado - En espera';
      case 'EN_ROUTE':
        return 'Técnico en camino';
      case 'ON_SITE':
        return 'Técnico en el lugar';
      case 'IN_PROGRESS':
        return 'Servicio en progreso';
      case 'COMPLETED':
        return 'Servicio completado';
      case 'CANCELLED':
        return 'Servicio cancelado';
      default:
        return status;
    }
  }
}
