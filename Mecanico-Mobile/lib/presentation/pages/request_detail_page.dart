import 'package:flutter/material.dart';
import '../../domain/entities/service_request.dart';

class RequestDetailPage extends StatelessWidget {
  final ServiceRequest request;

  const RequestDetailPage({super.key, required this.request});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Detalles de la Solicitud'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 2,
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
              _buildStatusCard(context),
              const SizedBox(height: 16),
              _buildDetailSection(
                'Descripción',
                request.description,
                Icons.info_outline,
              ),
              const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
              _buildDetailSection(
                'Vehículo',
                request.vehicleDetails,
                Icons.directions_car,
              ),
              const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
              _buildDetailSection(
                'Ubicación (Dirección)',
                request.address,
                Icons.location_on,
              ),
              const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
              _buildDetailSection(
                'Mecánico Asignado',
                '${request.mechanicName} - ${request.mechanicPhone}',
                Icons.person,
              ),
              const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
              _buildDetailSection(
                'Método de Pago',
                request.paymentMethod,
                Icons.payment,
              ),
              const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
              _buildDetailSection(
                'Costo Total',
                '\$${request.totalCost.toStringAsFixed(2)}',
                Icons.monetization_on,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildStatusCard(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.green.shade900.withValues(alpha: 0.3),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.green.shade500),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          const Text(
            'Estado actual:',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 16,
              color: Colors.white,
            ),
          ),
          Text(
            request.status,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: Colors.green.shade400,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDetailSection(String title, String content, IconData icon) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(icon, color: Colors.green.shade500, size: 28),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    fontWeight: FontWeight.w500,
                    color: Colors.grey,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  content,
                  style: const TextStyle(fontSize: 16, color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
