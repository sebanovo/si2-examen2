import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:image_picker/image_picker.dart';
import 'package:mechanic_mobile/core/di/injection_container.dart';
import '../viewmodels/evidence_viewmodel.dart';

class AddEvidencePage extends StatefulWidget {
  final String incidentId;

  const AddEvidencePage({super.key, required this.incidentId});

  @override
  State<AddEvidencePage> createState() => _AddEvidencePageState();
}

class _AddEvidencePageState extends State<AddEvidencePage> {
  late EvidenceViewModel _viewModel;
  final _textController = TextEditingController();
  final _descriptionController = TextEditingController();
  final _imagePicker = ImagePicker();

  String _selectedEvidenceType = 'text';
  XFile? _selectedImage;
  String? _selectedImageName;

  @override
  void initState() {
    super.initState();
    _viewModel = sl<EvidenceViewModel>();
  }

  @override
  void dispose() {
    _textController.dispose();
    _descriptionController.dispose();
    super.dispose();
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

  Future<void> _pickImage() async {
    final XFile? image = await _imagePicker.pickImage(
      source: ImageSource.gallery,
      imageQuality: 80,
    );

    if (image != null) {
      setState(() {
        _selectedImage = image;
        _selectedImageName = image.name;
      });
    }
  }

  Future<void> _takePhoto() async {
    final XFile? image = await _imagePicker.pickImage(
      source: ImageSource.camera,
      imageQuality: 80,
    );

    if (image != null) {
      setState(() {
        _selectedImage = image;
        _selectedImageName = image.name;
      });
    }
  }

  Future<void> _submitTextEvidence() async {
    if (_descriptionController.text.trim().isEmpty) {
      _showSnackBar('Ingresa una descripción', isError: true);
      return;
    }
    if (_textController.text.trim().isEmpty) {
      _showSnackBar('Ingresa el contenido del texto', isError: true);
      return;
    }

    final success = await _viewModel.addTextEvidence(
      incidentId: widget.incidentId,
      description: _descriptionController.text.trim(),
      textContent: _textController.text.trim(),
    );

    if (success && mounted) {
      _showSnackBar('Evidencia de texto agregada exitosamente');
      _descriptionController.clear();
      _textController.clear();
      context.pop(true);
    } else if (mounted) {
      _showSnackBar(
        _viewModel.errorMessage ?? 'Error al agregar evidencia',
        isError: true,
      );
    }
  }

  Future<void> _submitImageEvidence() async {
    if (_descriptionController.text.trim().isEmpty) {
      _showSnackBar('Ingresa una descripción', isError: true);
      return;
    }
    if (_selectedImage == null) {
      _showSnackBar('Selecciona una imagen', isError: true);
      return;
    }

    final success = await _viewModel.addImageEvidence(
      incidentId: widget.incidentId,
      description: _descriptionController.text.trim(),
      imageFile: _selectedImage!,
    );

    if (success && mounted) {
      _showSnackBar('Imagen agregada exitosamente');
      _descriptionController.clear();
      setState(() {
        _selectedImage = null;
        _selectedImageName = null;
      });
      context.pop(true);
    } else if (mounted) {
      _showSnackBar(
        _viewModel.errorMessage ?? 'Error al agregar imagen',
        isError: true,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Agregar Evidencia'),
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
            return SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Selector de tipo de evidencia
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 4),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Tipo de evidencia',
                          style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.w500,
                            color: Colors.white,
                          ),
                        ),
                        const SizedBox(height: 8),
                        SegmentedButton<String>(
                          segments: const [
                            ButtonSegment(
                              value: 'text',
                              label: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(Icons.description, size: 18),
                                  SizedBox(width: 4),
                                  Text('Texto'),
                                ],
                              ),
                            ),
                            ButtonSegment(
                              value: 'image',
                              label: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(Icons.image, size: 18),
                                  SizedBox(width: 4),
                                  Text('Imagen'),
                                ],
                              ),
                            ),
                          ],
                          selected: {_selectedEvidenceType},
                          onSelectionChanged: (Set<String> selection) {
                            setState(() {
                              _selectedEvidenceType = selection.first;
                              _selectedImage = null;
                              _selectedImageName = null;
                              _descriptionController.clear();
                              _textController.clear();
                            });
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
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Descripción común
                  TextField(
                    controller: _descriptionController,
                    style: const TextStyle(color: Colors.white),
                    decoration: InputDecoration(
                      labelText: 'Descripción *',
                      hintText: 'Describe esta evidencia...',
                      hintStyle: TextStyle(color: Colors.grey.shade500),
                      labelStyle: TextStyle(color: Colors.grey.shade400),
                      prefixIcon: const Icon(
                        Icons.description,
                        color: Color.fromRGBO(76, 175, 80, 1),
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: BorderSide(color: Colors.grey.shade700),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: BorderSide(color: Colors.grey.shade700),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: BorderSide(
                          color: Colors.green.shade500,
                          width: 2,
                        ),
                      ),
                    ),
                    maxLines: 2,
                  ),
                  const SizedBox(height: 16),

                  // Campos según el tipo seleccionado
                  if (_selectedEvidenceType == 'text') ...[
                    TextField(
                      controller: _textController,
                      style: const TextStyle(color: Colors.white),
                      decoration: InputDecoration(
                        labelText: 'Contenido del texto *',
                        hintText: 'Escribe aquí los detalles adicionales...',
                        hintStyle: TextStyle(color: Colors.grey.shade500),
                        labelStyle: TextStyle(color: Colors.grey.shade400),
                        prefixIcon: const Icon(
                          Icons.text_fields,
                          color: Color.fromRGBO(76, 175, 80, 1),
                        ),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: BorderSide(color: Colors.grey.shade700),
                        ),
                        enabledBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: BorderSide(color: Colors.grey.shade700),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: BorderSide(
                            color: Colors.green.shade500,
                            width: 2,
                          ),
                        ),
                      ),
                      maxLines: 5,
                    ),
                  ] else ...[
                    // Selector de imagen
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.grey.shade700),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Column(
                        children: [
                          if (_selectedImage != null) ...[
                            kIsWeb
                                ? Image.network(
                                    _selectedImage!.path,
                                    height: 200,
                                    width: double.infinity,
                                    fit: BoxFit.cover,
                                    errorBuilder: (context, error, stackTrace) {
                                      return Container(
                                        height: 200,
                                        color: Colors.grey.shade800,
                                        child: const Center(
                                          child: Column(
                                            mainAxisAlignment:
                                                MainAxisAlignment.center,
                                            children: [
                                              Icon(
                                                Icons.broken_image,
                                                size: 48,
                                                color: Colors.grey,
                                              ),
                                              SizedBox(height: 8),
                                              Text(
                                                'Vista previa no disponible',
                                                style: TextStyle(
                                                  color: Colors.grey,
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      );
                                    },
                                  )
                                : Image.file(
                                    File(_selectedImage!.path),
                                    height: 200,
                                    width: double.infinity,
                                    fit: BoxFit.cover,
                                  ),
                            const SizedBox(height: 12),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                TextButton.icon(
                                  onPressed: () {
                                    setState(() {
                                      _selectedImage = null;
                                      _selectedImageName = null;
                                    });
                                  },
                                  icon: const Icon(
                                    Icons.delete_outline,
                                    color: Colors.red,
                                  ),
                                  label: const Text(
                                    'Eliminar',
                                    style: TextStyle(color: Colors.red),
                                  ),
                                  style: TextButton.styleFrom(
                                    foregroundColor: Colors.red,
                                  ),
                                ),
                              ],
                            ),
                            if (_selectedImageName != null)
                              Padding(
                                padding: const EdgeInsets.only(top: 8),
                                child: Text(
                                  _selectedImageName!,
                                  style: TextStyle(
                                    fontSize: 12,
                                    color: Colors.grey.shade400,
                                  ),
                                ),
                              ),
                          ] else ...[
                            const Icon(
                              Icons.image_outlined,
                              size: 64,
                              color: Colors.grey,
                            ),
                            const SizedBox(height: 16),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                ElevatedButton.icon(
                                  onPressed: _pickImage,
                                  icon: const Icon(Icons.photo_library),
                                  label: const Text('Galería'),
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.green.shade600,
                                    foregroundColor: Colors.white,
                                  ),
                                ),
                                const SizedBox(width: 16),
                                ElevatedButton.icon(
                                  onPressed: _takePhoto,
                                  icon: const Icon(Icons.camera_alt),
                                  label: const Text('Cámara'),
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.green.shade600,
                                    foregroundColor: Colors.white,
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ],
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'Formatos soportados: JPG, PNG',
                      style: TextStyle(
                        fontSize: 12,
                        color: Colors.grey.shade500,
                      ),
                    ),
                  ],

                  const SizedBox(height: 32),

                  // Botón de enviar
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: _viewModel.isLoading
                          ? null
                          : (_selectedEvidenceType == 'text'
                                ? _submitTextEvidence
                                : _submitImageEvidence),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.green.shade600,
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 16),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(12),
                        ),
                        elevation: 2,
                      ),
                      child: _viewModel.isLoading
                          ? const SizedBox(
                              height: 20,
                              width: 20,
                              child: CircularProgressIndicator(
                                strokeWidth: 2,
                                valueColor: AlwaysStoppedAnimation<Color>(
                                  Colors.white,
                                ),
                              ),
                            )
                          : Text(
                              _selectedEvidenceType == 'text'
                                  ? 'Agregar Texto'
                                  : 'Subir Imagen',
                              style: const TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
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
}
