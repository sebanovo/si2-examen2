import 'package:flutter/material.dart';

import '../../../core/di/injection_container.dart';
import '../../../domain/entities/vehicle.dart';
import '../viewmodels/vehicle_viewmodel.dart';

class VehiclesPage extends StatefulWidget {
  const VehiclesPage({super.key});

  @override
  State<VehiclesPage> createState() => _VehiclesPageState();
}

class _VehiclesPageState extends State<VehiclesPage> {
  late final VehicleViewModel _viewModel;
  final List<String> _validVehicleTypes = [
    'CAR',
    'MOTORCYCLE',
    'TRUCK',
    'VAN',
    'OTHER',
  ];

  @override
  void initState() {
    super.initState();
    _viewModel = sl<VehicleViewModel>();
    _viewModel.loadVehicles();
  }

  String? _validateVehicleType(String value) {
    if (!_validVehicleTypes.contains(value.toUpperCase())) {
      return 'El tipo debe ser: ${_validVehicleTypes.join(', ')}';
    }
    return null;
  }

  String? _validateTextField(String value, String fieldName) {
    if (value.trim().length < 3) {
      return '$fieldName debe tener al menos 3 caracteres';
    }
    return null;
  }

  Future<void> _openVehicleForm({Vehicle? vehicle}) async {
    final plateController = TextEditingController(text: vehicle?.plateNumber);
    final typeController = TextEditingController(
      text: vehicle?.vehicleType ?? 'CAR',
    );
    final brandController = TextEditingController(text: vehicle?.brand);
    final modelController = TextEditingController(text: vehicle?.model);
    final yearController = TextEditingController(
      text: vehicle != null ? vehicle.year.toString() : '',
    );
    final colorController = TextEditingController(text: vehicle?.color);
    final notesController = TextEditingController(text: vehicle?.notes ?? '');

    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text(vehicle == null ? 'Nuevo vehículo' : 'Editar vehículo'),
          backgroundColor: const Color(0xFF1e1e2f),
          titleTextStyle: const TextStyle(color: Colors.white, fontSize: 18),
          contentTextStyle: TextStyle(color: Colors.grey.shade400),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(
                  controller: plateController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Placa *',
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
                ),
                const SizedBox(height: 8),
                DropdownButtonFormField<String>(
                  initialValue: typeController.text,
                  dropdownColor: const Color(0xFF1e1e2f),
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Tipo *',
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
                  items: _validVehicleTypes.map((type) {
                    return DropdownMenuItem(value: type, child: Text(type));
                  }).toList(),
                  onChanged: (value) {
                    if (value != null) typeController.text = value;
                  },
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: brandController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Marca *',
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
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: modelController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Modelo *',
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
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: yearController,
                  style: const TextStyle(color: Colors.white),
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    labelText: 'Año *',
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
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: colorController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Color *',
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
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: notesController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    labelText: 'Notas',
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
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: const Text(
                'Cancelar',
                style: TextStyle(color: Color.fromRGBO(102, 187, 106, 1)),
              ),
            ),
            ElevatedButton(
              onPressed: () => Navigator.pop(context, true),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green.shade600,
                foregroundColor: Colors.white,
              ),
              child: const Text('Guardar'),
            ),
          ],
        );
      },
    );

    if (confirmed != true) return;

    // Validaciones solo al guardar
    final errors = <String>[];

    // Validar placa
    final plateError = _validateTextField(plateController.text, 'Placa');
    if (plateError != null) errors.add(plateError);

    // Validar tipo de vehículo
    final typeError = _validateVehicleType(typeController.text);
    if (typeError != null) errors.add(typeError);

    // Validar marca
    final brandError = _validateTextField(brandController.text, 'Marca');
    if (brandError != null) errors.add(brandError);

    // Validar modelo
    final modelError = _validateTextField(modelController.text, 'Modelo');
    if (modelError != null) errors.add(modelError);

    // Validar año
    final yearText = yearController.text.trim();
    final year = int.tryParse(yearText);
    if (yearText.isEmpty) {
      errors.add('El año es obligatorio');
    } else if (year == null || year < 1900 || year > DateTime.now().year + 1) {
      errors.add(
        'Ingrese un año válido (entre 1900 y ${DateTime.now().year + 1})',
      );
    }

    // Validar color
    final colorError = _validateTextField(colorController.text, 'Color');
    if (colorError != null) errors.add(colorError);

    // Notas: opcional pero si tiene contenido debe tener al menos 3 caracteres
    final notes = notesController.text.trim();
    if (notes.isNotEmpty && notes.length < 3) {
      errors.add('Las notas deben tener al menos 3 caracteres');
    }

    if (errors.isNotEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: errors
                .map(
                  (e) =>
                      Text('• $e', style: const TextStyle(color: Colors.white)),
                )
                .toList(),
          ),
          backgroundColor: Colors.red.shade700,
          behavior: SnackBarBehavior.floating,
          duration: const Duration(seconds: 3),
        ),
      );
      return;
    }

    final body = {
      "plate_number": plateController.text.trim(),
      "vehicle_type": typeController.text.trim().toUpperCase(),
      "brand": brandController.text.trim(),
      "model": modelController.text.trim(),
      "year": year,
      "color": colorController.text.trim(),
      "notes": notesController.text.trim(),
    };

    final ok = vehicle == null
        ? await _viewModel.createVehicle(body)
        : await _viewModel.updateVehicle(vehicle.id, body);

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          ok
              ? (vehicle == null
                    ? 'Vehículo registrado'
                    : 'Vehículo actualizado')
              : (_viewModel.errorMessage ?? 'No se pudo guardar'),
          style: const TextStyle(color: Colors.white),
        ),
        backgroundColor: ok ? Colors.green.shade700 : Colors.red.shade700,
      ),
    );

    if (ok) {
      _viewModel.loadVehicles();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mis vehículos'),
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
        child: ListenableBuilder(
          listenable: _viewModel,
          builder: (context, _) {
            if (_viewModel.isLoading && _viewModel.vehicles.isEmpty) {
              return const Center(
                child: CircularProgressIndicator(
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.green),
                ),
              );
            }

            if (_viewModel.errorMessage != null &&
                _viewModel.vehicles.isEmpty) {
              return Center(
                child: Text(
                  _viewModel.errorMessage!,
                  style: const TextStyle(color: Colors.white),
                ),
              );
            }

            if (_viewModel.vehicles.isEmpty) {
              return const Center(
                child: Text(
                  'Aún no registraste vehículos.',
                  style: TextStyle(color: Colors.white),
                ),
              );
            }

            return RefreshIndicator(
              onRefresh: _viewModel.loadVehicles,
              color: Colors.green,
              child: ListView.builder(
                padding: const EdgeInsets.all(8),
                itemCount: _viewModel.vehicles.length,
                itemBuilder: (context, index) {
                  final vehicle = _viewModel.vehicles[index];
                  return Card(
                    margin: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    color: const Color(0xFF1e1e2f),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: ListTile(
                      title: Text(
                        '${vehicle.brand} ${vehicle.model}',
                        style: const TextStyle(color: Colors.white),
                      ),
                      subtitle: Text(
                        '${vehicle.plateNumber} - ${vehicle.vehicleType} (${vehicle.year})',
                        style: TextStyle(color: Colors.grey.shade400),
                      ),
                      trailing: const Icon(
                        Icons.edit,
                        color: Color.fromRGBO(76, 175, 80, 1),
                      ),
                      onTap: () => _openVehicleForm(vehicle: vehicle),
                    ),
                  );
                },
              ),
            );
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _openVehicleForm(),
        backgroundColor: Colors.green.shade600,
        foregroundColor: Colors.white,
        child: const Icon(Icons.add),
      ),
    );
  }
}
