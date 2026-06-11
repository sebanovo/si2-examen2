import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mechanic_mobile/core/di/injection_container.dart';
import '../../domain/entities/admin_incident.dart';
import '../viewmodels/admin_incidents_viewmodel.dart';

class AdminIncidentsPage extends StatefulWidget {
  const AdminIncidentsPage({super.key});

  @override
  State<AdminIncidentsPage> createState() => _AdminIncidentsPageState();
}

class _AdminIncidentsPageState extends State<AdminIncidentsPage> {
  late AdminIncidentsViewModel _viewModel;

  @override
  void initState() {
    super.initState();
    _viewModel = sl<AdminIncidentsViewModel>();
    _viewModel.loadIncidents();
  }

  void _showSnackBar(String message, {bool isError = false}) {
    ScaffoldMessenger.of(context).hideCurrentSnackBar();
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            Icon(
              isError ? Icons.error_outline : Icons.check_circle_outline,
              color: Colors.white,
            ),
            const SizedBox(width: 12),
            Expanded(child: Text(message)),
          ],
        ),
        backgroundColor: isError ? Colors.red.shade700 : Colors.green.shade700,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
        margin: const EdgeInsets.all(12),
        duration: const Duration(seconds: 3),
      ),
    );
  }

  Future<void> _showPublishConfirmDialog(AdminIncident incident) async {
    return showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Publicar Incidente'),
        content: Text(
          '¿Estás seguro de que deseas publicar el incidente "${incident.title}"? Esto lo hará visible para los talleres.',
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        backgroundColor: const Color(0xFF1e1e2f),
        titleTextStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        contentTextStyle: TextStyle(color: Colors.grey.shade400),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text(
              'Cancelar',
              style: TextStyle(color: Color.fromRGBO(102, 187, 106, 1)),
            ),
          ),
          ElevatedButton(
            onPressed: () async {
              Navigator.pop(context);
              final success = await _viewModel.publishIncident(incident.id);
              if (success) {
                _showSnackBar('Incidente publicado exitosamente');
              } else {
                _showSnackBar(
                  _viewModel.errorMessage ?? 'Error al publicar',
                  isError: true,
                );
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.green.shade600,
              foregroundColor: Colors.white,
            ),
            child: const Text('Publicar'),
          ),
        ],
      ),
    );
  }

  Future<void> _showCandidatesDialog(String incidentId) async {
    await _viewModel.loadCandidates(incidentId);

    if (!mounted) return;

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Candidatos para el Incidente'),
        backgroundColor: const Color(0xFF1e1e2f),
        titleTextStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        content: _viewModel.candidates.isEmpty
            ? const SizedBox(
                height: 100,
                child: Center(
                  child: Text(
                    'No hay candidatos disponibles',
                    style: TextStyle(color: Colors.grey),
                  ),
                ),
              )
            : SizedBox(
                width: double.maxFinite,
                height: 400,
                child: ListView.builder(
                  itemCount: _viewModel.candidates.length,
                  itemBuilder: (context, index) {
                    final candidate = _viewModel.candidates[index];
                    return Card(
                      margin: const EdgeInsets.only(bottom: 8),
                      color: const Color(0xFF16213e),
                      child: ListTile(
                        leading: const CircleAvatar(
                          backgroundColor: Color.fromRGBO(56, 142, 60, 1),
                          child: Icon(Icons.business, color: Colors.white),
                        ),
                        title: Text(
                          candidate.providerName,
                          style: const TextStyle(color: Colors.white),
                        ),
                        subtitle: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Distancia: ${candidate.distanceKm.toStringAsFixed(1)} km',
                              style: TextStyle(color: Colors.grey.shade400),
                            ),
                            Text(
                              'Puntuación: ${candidate.score.toStringAsFixed(1)}',
                              style: TextStyle(color: Colors.grey.shade400),
                            ),
                            Text(
                              'Servicios: ${candidate.matchedServices.join(", ")}',
                              style: TextStyle(color: Colors.grey.shade400),
                            ),
                          ],
                        ),
                        trailing: Chip(
                          label: Text(
                            candidate.providerType,
                            style: const TextStyle(color: Colors.white),
                          ),
                          backgroundColor: Colors.green.shade800,
                        ),
                      ),
                    );
                  },
                ),
              ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text(
              'Cerrar',
              style: TextStyle(color: Color.fromRGBO(102, 187, 106, 1)),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Gestión de Incidentes'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 2,
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh, color: Colors.white),
            onPressed: () => _viewModel.loadIncidents(),
            tooltip: 'Actualizar',
          ),
        ],
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(48),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: Row(
              children: [
                Expanded(
                  child: SegmentedButton<String>(
                    segments: const [
                      ButtonSegment(value: 'all', label: Text('Todos')),
                      ButtonSegment(
                        value: 'pending',
                        label: Text('Pendientes'),
                      ),
                      ButtonSegment(
                        value: 'published',
                        label: Text('Publicados'),
                      ),
                      ButtonSegment(value: 'active', label: Text('Activos')),
                      ButtonSegment(
                        value: 'completed',
                        label: Text('Completados'),
                      ),
                    ],
                    selected: {_viewModel.selectedTab},
                    onSelectionChanged: (Set<String> selection) {
                      _viewModel.setSelectedTab(selection.first);
                    },
                    style: ButtonStyle(
                      backgroundColor: WidgetStateProperty.resolveWith((
                        states,
                      ) {
                        if (states.contains(WidgetState.selected)) {
                          return Colors.green.shade700;
                        }
                        return const Color(0xFF1e1e2f);
                      }),
                      foregroundColor: WidgetStateProperty.resolveWith((
                        states,
                      ) {
                        if (states.contains(WidgetState.selected)) {
                          return Colors.white;
                        }
                        return Colors.green.shade400;
                      }),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
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
            if (_viewModel.isLoading && _viewModel.incidents.isEmpty) {
              return const Center(
                child: CircularProgressIndicator(
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.green),
                ),
              );
            }

            if (_viewModel.errorMessage != null &&
                _viewModel.incidents.isEmpty) {
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
                      onPressed: () => _viewModel.loadIncidents(),
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

            final incidents = _viewModel.filteredIncidents;

            if (incidents.isEmpty) {
              return Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.inbox, size: 64, color: Colors.green.shade400),
                    const SizedBox(height: 16),
                    Text(
                      'No hay incidentes en esta categoría',
                      style: TextStyle(
                        fontSize: 18,
                        color: Colors.grey.shade400,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              );
            }

            return RefreshIndicator(
              onRefresh: () => _viewModel.loadIncidents(),
              color: Colors.green,
              child: ListView.builder(
                padding: const EdgeInsets.all(12),
                itemCount: incidents.length,
                itemBuilder: (context, index) {
                  final incident = incidents[index];
                  return _buildIncidentCard(incident);
                },
              ),
            );
          },
        ),
      ),
    );
  }

  Widget _buildIncidentCard(AdminIncident incident) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      elevation: 4,
      color: const Color(0xFF1e1e2f),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(
          color: incident.statusColor.withValues(alpha: 0.3),
          width: 1,
        ),
      ),
      child: InkWell(
        onTap: () {
          context.push('/admin/incident/${incident.id}');
        },
        borderRadius: BorderRadius.circular(16),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: incident.statusColor.withValues(alpha: 0.1),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      incident.statusIcon,
                      style: const TextStyle(fontSize: 20),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          incident.title,
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                        const SizedBox(height: 4),
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 2,
                          ),
                          decoration: BoxDecoration(
                            color: incident.statusColor.withValues(alpha: 0.1),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Text(
                            incident.status,
                            style: TextStyle(
                              fontSize: 12,
                              color: incident.statusColor,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  if (incident.canBePublished)
                    IconButton(
                      icon: Icon(Icons.publish, color: Colors.green.shade500),
                      onPressed: () => _showPublishConfirmDialog(incident),
                      tooltip: 'Publicar incidente',
                    ),
                  IconButton(
                    icon: Icon(
                      Icons.people_outline,
                      color: Colors.green.shade500,
                    ),
                    onPressed: () => _showCandidatesDialog(incident.id),
                    tooltip: 'Ver candidatos',
                  ),
                  Icon(Icons.chevron_right, color: Colors.grey.shade500),
                ],
              ),
              const SizedBox(height: 12),
              Row(
                children: [
                  Icon(
                    Icons.person_outline,
                    size: 14,
                    color: Colors.grey.shade500,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    incident.clientUser?.fullName ?? 'Cliente',
                    style: TextStyle(fontSize: 12, color: Colors.grey.shade400),
                  ),
                  const SizedBox(width: 16),
                  Icon(Icons.category, size: 14, color: Colors.grey.shade500),
                  const SizedBox(width: 4),
                  Text(
                    incident.reportedCategory,
                    style: TextStyle(fontSize: 12, color: Colors.grey.shade400),
                  ),
                  const SizedBox(width: 16),
                  Icon(
                    Icons.priority_high,
                    size: 14,
                    color: Colors.grey.shade500,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    incident.priority,
                    style: TextStyle(
                      fontSize: 12,
                      color:
                          incident.priority == 'HIGH' ||
                              incident.priority == 'URGENT'
                          ? Colors.red.shade400
                          : Colors.grey.shade400,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Row(
                children: [
                  Icon(
                    Icons.location_on,
                    size: 14,
                    color: Colors.grey.shade500,
                  ),
                  const SizedBox(width: 4),
                  Expanded(
                    child: Text(
                      incident.addressReference ?? 'Sin dirección especificada',
                      style: TextStyle(
                        fontSize: 12,
                        color: Colors.grey.shade400,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
              if (incident.provider != null) ...[
                const SizedBox(height: 8),
                Row(
                  children: [
                    Icon(Icons.business, size: 14, color: Colors.grey.shade500),
                    const SizedBox(width: 4),
                    Expanded(
                      child: Text(
                        incident.provider!.businessName,
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey.shade400,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
              if (incident.aiSummaryStatus == 'SUCCEEDED' &&
                  incident.structuredSummary != null) ...[
                const SizedBox(height: 8),
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.green.shade900.withValues(alpha: 0.3),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Row(
                    children: [
                      Icon(
                        Icons.auto_awesome,
                        size: 14,
                        color: Colors.green.shade400,
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(
                          incident.structuredSummary!,
                          style: TextStyle(
                            fontSize: 12,
                            color: Colors.green.shade300,
                          ),
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
