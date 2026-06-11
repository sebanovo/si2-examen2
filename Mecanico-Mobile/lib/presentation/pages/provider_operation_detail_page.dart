import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mechanic_mobile/core/di/injection_container.dart';
import 'package:mechanic_mobile/presentation/viewmodels/technicians_viewmodel.dart';
import '../../domain/entities/provider_operation.dart';
import '../viewmodels/provider_operation_viewmodel.dart';

class ProviderOperationDetailPage extends StatefulWidget {
  final ProviderOperation? operation;

  const ProviderOperationDetailPage({super.key, this.operation});

  @override
  State<ProviderOperationDetailPage> createState() =>
      _ProviderOperationDetailPageState();
}

class _ProviderOperationDetailPageState
    extends State<ProviderOperationDetailPage> {
  late ProviderOperationViewModel _viewModel;
  late ProviderOperation _operation;

  @override
  void initState() {
    super.initState();
    _viewModel = sl<ProviderOperationViewModel>();

    if (widget.operation != null) {
      _operation = widget.operation!;
    }
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

  Future<void> _showDispatchDialog() async {
    final technicianVM = sl<TechniciansViewModel>();
    await technicianVM.loadTechnicians();
    final availableTechnicians = technicianVM.technicians
        .where((t) => t.isAvailable)
        .toList();

    if (availableTechnicians.isEmpty) {
      _showSnackBar('No hay técnicos disponibles', isError: true);
      return;
    }

    String? selectedTechnicianId;
    final noteController = TextEditingController();

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Despachar Técnico'),
        backgroundColor: const Color(0xFF1e1e2f),
        titleTextStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            DropdownButtonFormField<String>(
              dropdownColor: const Color(0xFF1e1e2f),
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                labelText: 'Seleccionar técnico',
                labelStyle: TextStyle(color: Colors.grey.shade400),
                border: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                enabledBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.green.shade500,
                    width: 2,
                  ),
                ),
              ),
              items: availableTechnicians.map((tech) {
                return DropdownMenuItem(
                  value: tech.id,
                  child: Text('${tech.fullName} - ${tech.specialty}'),
                );
              }).toList(),
              onChanged: (value) => selectedTechnicianId = value,
              validator: (value) =>
                  value == null ? 'Seleccione un técnico' : null,
            ),
            const SizedBox(height: 12),
            TextField(
              controller: noteController,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                labelText: 'Nota (opcional)',
                labelStyle: TextStyle(color: Colors.grey.shade400),
                border: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                enabledBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.green.shade500,
                    width: 2,
                  ),
                ),
              ),
              maxLines: 2,
            ),
          ],
        ),
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
              if (selectedTechnicianId == null) {
                _showSnackBar('Seleccione un técnico', isError: true);
                return;
              }
              Navigator.pop(context);
              final result = await _viewModel.dispatchIncident(
                _operation.incidentId,
                selectedTechnicianId!,
                note: noteController.text.trim().isEmpty
                    ? null
                    : noteController.text.trim(),
              );
              if (result != null) {
                setState(() {
                  _operation = result;
                });
                _showSnackBar('Técnico despachado exitosamente');
              } else {
                _showSnackBar(
                  _viewModel.errorMessage ?? 'Error al despachar',
                  isError: true,
                );
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.green.shade600,
              foregroundColor: Colors.white,
            ),
            child: const Text('Despachar'),
          ),
        ],
      ),
    );
  }

  Future<void> _showCompleteDialog() async {
    final noteController = TextEditingController();
    final summaryController = TextEditingController();

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Completar Servicio'),
        backgroundColor: const Color(0xFF1e1e2f),
        titleTextStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              controller: summaryController,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                labelText: 'Resumen del servicio *',
                labelStyle: TextStyle(color: Colors.grey.shade400),
                hintText: 'Describe el trabajo realizado...',
                hintStyle: TextStyle(color: Colors.grey.shade500),
                border: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                enabledBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.green.shade500,
                    width: 2,
                  ),
                ),
              ),
              maxLines: 3,
            ),
            const SizedBox(height: 12),
            TextField(
              controller: noteController,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                labelText: 'Nota adicional (opcional)',
                labelStyle: TextStyle(color: Colors.grey.shade400),
                border: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                enabledBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.green.shade500,
                    width: 2,
                  ),
                ),
              ),
              maxLines: 2,
            ),
          ],
        ),
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
              if (summaryController.text.trim().isEmpty) {
                _showSnackBar('Ingrese un resumen del servicio', isError: true);
                return;
              }
              Navigator.pop(context);
              final result = await _viewModel.completeService(
                _operation.incidentId,
                summaryController.text.trim(),
                note: noteController.text.trim().isEmpty
                    ? null
                    : noteController.text.trim(),
              );
              if (result != null) {
                setState(() {
                  _operation = result;
                });
                _showSnackBar('Servicio completado exitosamente');
                Future.delayed(const Duration(seconds: 2), () {
                  context.go('/provider/active-operations');
                });
              } else {
                _showSnackBar(
                  _viewModel.errorMessage ?? 'Error al completar servicio',
                  isError: true,
                );
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.green.shade600,
              foregroundColor: Colors.white,
            ),
            child: const Text('Completar'),
          ),
        ],
      ),
    );
  }

  Future<void> _showCancelDialog() async {
    final noteController = TextEditingController();

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Cancelar Servicio'),
        backgroundColor: const Color(0xFF1e1e2f),
        titleTextStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
          fontWeight: FontWeight.bold,
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              '¿Estás seguro de que deseas cancelar este servicio?',
              style: TextStyle(color: Colors.white),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: noteController,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                labelText: 'Motivo de cancelación (opcional)',
                labelStyle: TextStyle(color: Colors.grey.shade400),
                border: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                enabledBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey.shade700),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.green.shade500,
                    width: 2,
                  ),
                ),
              ),
              maxLines: 2,
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text(
              'No',
              style: TextStyle(color: Color.fromRGBO(102, 187, 106, 1)),
            ),
          ),
          ElevatedButton(
            onPressed: () async {
              Navigator.pop(context);
              final result = await _viewModel.cancelService(
                _operation.incidentId,
                note: noteController.text.trim().isEmpty
                    ? null
                    : noteController.text.trim(),
              );
              if (result != null) {
                _showSnackBar('Servicio cancelado');
                context.go('/provider/active-operations');
              } else {
                _showSnackBar(
                  _viewModel.errorMessage ?? 'Error al cancelar servicio',
                  isError: true,
                );
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.red.shade700,
              foregroundColor: Colors.white,
            ),
            child: const Text('Sí, cancelar'),
          ),
        ],
      ),
    );
  }

  String _formatDate(DateTime? date) {
    if (date == null) return 'N/A';
    return '${date.day}/${date.month}/${date.year} ${date.hour}:${date.minute.toString().padLeft(2, '0')}';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Detalle de Operación'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 2,
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh, color: Colors.white),
            onPressed: () async {
              await _viewModel.loadOperationState(_operation.incidentId);
              if (_viewModel.selectedOperation != null) {
                setState(() {
                  _operation = _viewModel.selectedOperation!;
                });
              }
            },
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
            return SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Estado actual
                  Card(
                    color: _operation.statusColor.withValues(alpha: 0.1),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Row(
                        children: [
                          Icon(
                            _operation.statusIcon,
                            color: _operation.statusColor,
                            size: 32,
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                const Text(
                                  'Estado Actual',
                                  style: TextStyle(
                                    fontSize: 12,
                                    color: Colors.grey,
                                  ),
                                ),
                                Text(
                                  _operation.statusText,
                                  style: TextStyle(
                                    fontSize: 20,
                                    fontWeight: FontWeight.bold,
                                    color: _operation.statusColor,
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

                  // Botones de acción según estado
                  if (_operation.canDispatch)
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: _showDispatchDialog,
                        icon: const Icon(Icons.person_add),
                        label: const Text('Despachar Técnico'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade600,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                      ),
                    ),
                  if (_operation.canArrive)
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: () async {
                          final result = await _viewModel.markArrived(
                            _operation.incidentId,
                          );
                          if (result != null) {
                            setState(() {
                              _operation = result;
                            });
                            _showSnackBar('Llegada registrada');
                          } else {
                            _showSnackBar(
                              _viewModel.errorMessage ??
                                  'Error al registrar llegada',
                              isError: true,
                            );
                          }
                        },
                        icon: const Icon(Icons.location_on),
                        label: const Text('Marcar Llegada'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.teal.shade700,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                      ),
                    ),
                  if (_operation.canStart)
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: () async {
                          final result = await _viewModel.startService(
                            _operation.incidentId,
                          );
                          if (result != null) {
                            setState(() {
                              _operation = result;
                            });
                            _showSnackBar('Servicio iniciado');
                          } else {
                            _showSnackBar(
                              _viewModel.errorMessage ??
                                  'Error al iniciar servicio',
                              isError: true,
                            );
                          }
                        },
                        icon: const Icon(Icons.play_arrow),
                        label: const Text('Iniciar Servicio'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.indigo.shade700,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                      ),
                    ),
                  if (_operation.canComplete)
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: _showCompleteDialog,
                        icon: const Icon(Icons.check_circle),
                        label: const Text('Completar Servicio'),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade600,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                      ),
                    ),
                  if (_operation.canCancel && !_operation.canComplete)
                    SizedBox(
                      width: double.infinity,
                      child: OutlinedButton.icon(
                        onPressed: _showCancelDialog,
                        icon: const Icon(Icons.cancel),
                        label: const Text('Cancelar Servicio'),
                        style: OutlinedButton.styleFrom(
                          foregroundColor: Colors.red.shade400,
                          side: BorderSide(color: Colors.red.shade700),
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                      ),
                    ),

                  // Botón de Tracking
                  if (_operation.status == 'EN_ROUTE' &&
                      _operation.assignedTechnician != null)
                    Padding(
                      padding: const EdgeInsets.only(top: 8),
                      child: SizedBox(
                        width: double.infinity,
                        child: OutlinedButton.icon(
                          onPressed: () {
                            context.push(
                              '/provider/tracking/${_operation.incidentId}/${_operation.assignedTechnician!.id}',
                            );
                          },
                          icon: const Icon(Icons.location_on),
                          label: const Text('Ver Tracking en Vivo'),
                          style: OutlinedButton.styleFrom(
                            foregroundColor: Colors.green.shade400,
                            side: BorderSide(color: Colors.green.shade600),
                            padding: const EdgeInsets.symmetric(vertical: 14),
                          ),
                        ),
                      ),
                    ),

                  const SizedBox(height: 16),

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
                            'Información del Incidente',
                            style: TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: Colors.white,
                            ),
                          ),
                          const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                          _buildInfoRow('ID', _operation.incidentId),
                          _buildInfoRow('Título', _operation.title),
                          _buildInfoRow('Descripción', _operation.description),
                          _buildInfoRow('Prioridad', _operation.priority),
                          _buildInfoRow(
                            'Categoría',
                            _operation.reportedCategory,
                          ),
                          if (_operation.addressReference != null)
                            _buildInfoRow(
                              'Dirección',
                              _operation.addressReference!,
                            ),
                          if (_operation.incidentLatitude != null)
                            _buildInfoRow('Ubicación', _operation.location),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Información del cliente
                  if (_operation.clientUser != null)
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
                              'Información del Cliente',
                              style: TextStyle(
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            ),
                            const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
                            _buildInfoRow(
                              'Nombre',
                              _operation.clientUser!.fullName,
                            ),
                            _buildInfoRow(
                              'Email',
                              _operation.clientUser!.email,
                            ),
                            _buildInfoRow(
                              'Teléfono',
                              _operation.clientUser!.phoneNumber ?? 'N/A',
                            ),
                          ],
                        ),
                      ),
                    ),
                  const SizedBox(height: 16),

                  // Información del técnico
                  if (_operation.assignedTechnician != null)
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
                              _operation.assignedTechnician!.fullName,
                            ),
                            _buildInfoRow(
                              'Especialidad',
                              _operation.assignedTechnician!.specialty,
                            ),
                            _buildInfoRow(
                              'Teléfono',
                              _operation.assignedTechnician!.phoneNumber,
                            ),
                          ],
                        ),
                      ),
                    ),
                  const SizedBox(height: 16),

                  // Línea de tiempo
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
                            'Asignado',
                            _operation.assignedAt,
                            Icons.assignment_ind,
                          ),
                          _buildTimelineItem(
                            'En camino',
                            _operation.enRouteAt,
                            Icons.directions_car,
                          ),
                          _buildTimelineItem(
                            'Llegó al lugar',
                            _operation.arrivedAt,
                            Icons.location_on,
                          ),
                          _buildTimelineItem(
                            'Servicio iniciado',
                            _operation.startedAt,
                            Icons.build,
                          ),
                          _buildTimelineItem(
                            'Servicio completado',
                            _operation.completedAt,
                            Icons.check_circle,
                          ),
                          _buildTimelineItem(
                            'Cancelado',
                            _operation.cancelledAt,
                            Icons.cancel,
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            );
          },
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

  Widget _buildTimelineItem(String label, DateTime? date, IconData icon) {
    final isCompleted = date != null;
    final color = isCompleted ? Colors.green.shade500 : Colors.grey.shade500;

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
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
                    style: TextStyle(fontSize: 12, color: Colors.grey.shade500),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
