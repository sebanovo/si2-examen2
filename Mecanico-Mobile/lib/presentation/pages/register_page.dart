import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../core/di/injection_container.dart';
import '../viewmodels/auth_viewmodel.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  late final AuthViewModel _authViewModel;

  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  final _firstNameController = TextEditingController();
  final _lastNameController = TextEditingController();
  final _phoneController = TextEditingController();

  final _businessNameController = TextEditingController();
  final _legalNameController = TextEditingController();
  final _descriptionController = TextEditingController();
  final _contactEmailController = TextEditingController();
  final _contactPhoneController = TextEditingController();
  final _cityController = TextEditingController();
  final _addressController = TextEditingController();

  // ✅ Variables para mostrar/ocultar contraseñas
  bool _showPassword = false;
  bool _showConfirmPassword = false;
  String _accountType = 'CLIENT';
  bool _acceptedTerms = false;

  // Estados de error
  String? _emailError;
  String? _passwordError;
  String? _confirmPasswordError;
  String? _firstNameError;
  String? _lastNameError;
  String? _phoneError;
  String? _businessNameError;
  String? _cityError;
  String? _addressError;

  @override
  void initState() {
    super.initState();
    _authViewModel = sl<AuthViewModel>();

    // Agregar listeners para validación en tiempo real
    _emailController.addListener(_validateEmail);
    _passwordController.addListener(_validatePassword);
    _confirmPasswordController.addListener(_validateConfirmPassword);
    _firstNameController.addListener(_validateFirstName);
    _lastNameController.addListener(_validateLastName);
    _phoneController.addListener(_validatePhone);
    _businessNameController.addListener(_validateBusinessName);
    _cityController.addListener(_validateCity);
    _addressController.addListener(_validateAddress);
  }

  @override
  void dispose() {
    _emailController.removeListener(_validateEmail);
    _passwordController.removeListener(_validatePassword);
    _confirmPasswordController.removeListener(_validateConfirmPassword);
    _firstNameController.removeListener(_validateFirstName);
    _lastNameController.removeListener(_validateLastName);
    _phoneController.removeListener(_validatePhone);
    _businessNameController.removeListener(_validateBusinessName);
    _cityController.removeListener(_validateCity);
    _addressController.removeListener(_validateAddress);
    _emailController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    _firstNameController.dispose();
    _lastNameController.dispose();
    _phoneController.dispose();
    _businessNameController.dispose();
    _legalNameController.dispose();
    _descriptionController.dispose();
    _contactEmailController.dispose();
    _contactPhoneController.dispose();
    _cityController.dispose();
    _addressController.dispose();
    super.dispose();
  }

  // Validaciones en tiempo real
  void _validateEmail() {
    setState(() {
      final email = _emailController.text.trim();
      if (email.isEmpty) {
        _emailError = null;
      } else if (!email.contains('@')) {
        _emailError = 'El email debe contener @';
      } else if (!email.contains('.') ||
          email.indexOf('@') == 0 ||
          email.endsWith('@')) {
        _emailError = 'Ingresa un email válido (ejemplo@dominio.com)';
      } else {
        _emailError = null;
      }
    });
  }

  // ✅ Validación de contraseña actualizada: solo 8 caracteres
  void _validatePassword() {
    setState(() {
      final password = _passwordController.text;
      if (password.isEmpty) {
        _passwordError = null;
      } else if (password.length < 8) {
        _passwordError = 'La contraseña debe tener al menos 8 caracteres';
      } else {
        _passwordError = null;
      }
      // Revalidar confirmación cuando cambia la contraseña
      _validateConfirmPassword();
    });
  }

  void _validateConfirmPassword() {
    setState(() {
      final password = _passwordController.text;
      final confirm = _confirmPasswordController.text;
      if (confirm.isEmpty) {
        _confirmPasswordError = null;
      } else if (password != confirm) {
        _confirmPasswordError = 'Las contraseñas no coinciden';
      } else {
        _confirmPasswordError = null;
      }
    });
  }

  void _validateFirstName() {
    setState(() {
      final name = _firstNameController.text.trim();
      if (name.isEmpty) {
        _firstNameError = null;
      } else if (name.length < 2) {
        _firstNameError = 'El nombre debe tener al menos 2 caracteres';
      } else {
        _firstNameError = null;
      }
    });
  }

  void _validateLastName() {
    setState(() {
      final lastName = _lastNameController.text.trim();
      if (lastName.isEmpty) {
        _lastNameError = null;
      } else if (lastName.length < 2) {
        _lastNameError = 'El apellido debe tener al menos 2 caracteres';
      } else {
        _lastNameError = null;
      }
    });
  }

  void _validatePhone() {
    setState(() {
      final phone = _phoneController.text.trim();
      if (phone.isEmpty) {
        _phoneError = null;
      } else if (phone.length < 8) {
        _phoneError = 'El teléfono debe tener al menos 8 dígitos';
      } else if (!RegExp(r'^[0-9]+$').hasMatch(phone)) {
        _phoneError = 'Solo se permiten números';
      } else {
        _phoneError = null;
      }
    });
  }

  void _validateBusinessName() {
    if (_accountType != 'WORKSHOP') return;
    setState(() {
      final name = _businessNameController.text.trim();
      if (name.isEmpty) {
        _businessNameError = null;
      } else if (name.length < 3) {
        _businessNameError =
            'El nombre del negocio debe tener al menos 3 caracteres';
      } else {
        _businessNameError = null;
      }
    });
  }

  void _validateCity() {
    if (_accountType != 'WORKSHOP') return;
    setState(() {
      final city = _cityController.text.trim();
      if (city.isEmpty) {
        _cityError = null;
      } else if (city.length < 2) {
        _cityError = 'La ciudad debe tener al menos 2 caracteres';
      } else {
        _cityError = null;
      }
    });
  }

  void _validateAddress() {
    if (_accountType != 'WORKSHOP') return;
    setState(() {
      final address = _addressController.text.trim();
      if (address.isEmpty) {
        _addressError = null;
      } else if (address.length < 5) {
        _addressError = 'La dirección debe tener al menos 5 caracteres';
      } else {
        _addressError = null;
      }
    });
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
              size: 20,
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

  bool _validateForm() {
    bool isValid = true;

    // Validar email
    final email = _emailController.text.trim();
    if (email.isEmpty) {
      _emailError = 'El email es requerido';
      isValid = false;
    } else if (!email.contains('@')) {
      _emailError = 'El email debe contener @';
      isValid = false;
    } else {
      _emailError = null;
    }

    // ✅ Validar password (solo 8 caracteres)
    final password = _passwordController.text;
    if (password.isEmpty) {
      _passwordError = 'La contraseña es requerida';
      isValid = false;
    } else if (password.length < 8) {
      _passwordError = 'La contraseña debe tener al menos 8 caracteres';
      isValid = false;
    } else {
      _passwordError = null;
    }

    // Validar confirmación
    if (_confirmPasswordController.text.isEmpty) {
      _confirmPasswordError = 'Confirma tu contraseña';
      isValid = false;
    } else if (password != _confirmPasswordController.text) {
      _confirmPasswordError = 'Las contraseñas no coinciden';
      isValid = false;
    } else {
      _confirmPasswordError = null;
    }

    // Validar nombre
    if (_firstNameController.text.trim().isEmpty) {
      _firstNameError = 'El nombre es requerido';
      isValid = false;
    } else if (_firstNameController.text.trim().length < 2) {
      _firstNameError = 'El nombre debe tener al menos 2 caracteres';
      isValid = false;
    } else {
      _firstNameError = null;
    }

    // Validar apellido
    if (_lastNameController.text.trim().isEmpty) {
      _lastNameError = 'El apellido es requerido';
      isValid = false;
    } else if (_lastNameController.text.trim().length < 2) {
      _lastNameError = 'El apellido debe tener al menos 2 caracteres';
      isValid = false;
    } else {
      _lastNameError = null;
    }

    // Validar teléfono
    final phone = _phoneController.text.trim();
    if (phone.isEmpty) {
      _phoneError = 'El teléfono es requerido';
      isValid = false;
    } else if (phone.length < 8) {
      _phoneError = 'El teléfono debe tener al menos 8 dígitos';
      isValid = false;
    } else if (!RegExp(r'^[0-9]+$').hasMatch(phone)) {
      _phoneError = 'Solo se permiten números';
      isValid = false;
    } else {
      _phoneError = null;
    }

    // Validar campos de taller si aplica
    if (_accountType == 'WORKSHOP') {
      if (_businessNameController.text.trim().isEmpty) {
        _businessNameError = 'El nombre del negocio es requerido';
        isValid = false;
      } else if (_businessNameController.text.trim().length < 3) {
        _businessNameError = 'Debe tener al menos 3 caracteres';
        isValid = false;
      } else {
        _businessNameError = null;
      }

      if (_cityController.text.trim().isEmpty) {
        _cityError = 'La ciudad es requerida';
        isValid = false;
      } else if (_cityController.text.trim().length < 2) {
        _cityError = 'Debe tener al menos 2 caracteres';
        isValid = false;
      } else {
        _cityError = null;
      }

      if (_addressController.text.trim().isEmpty) {
        _addressError = 'La dirección es requerida';
        isValid = false;
      } else if (_addressController.text.trim().length < 5) {
        _addressError = 'Debe tener al menos 5 caracteres';
        isValid = false;
      } else {
        _addressError = null;
      }
    }

    if (!_acceptedTerms) {
      _showSnackBar('Debes aceptar los términos y condiciones', isError: true);
      isValid = false;
    }

    setState(() {});
    return isValid;
  }

  Map<String, dynamic> _buildRegisterBody() {
    final body = <String, dynamic>{
      "email": _emailController.text.trim(),
      "password": _passwordController.text,
      "first_name": _firstNameController.text.trim(),
      "last_name": _lastNameController.text.trim(),
      "account_type": _accountType,
      "phone_number": _phoneController.text.trim(),
    };

    if (_accountType == 'WORKSHOP') {
      body["provider_profile"] = {
        "business_name": _businessNameController.text.trim(),
        "legal_name": _legalNameController.text.trim(),
        "description": _descriptionController.text.trim(),
        "contact_email": _contactEmailController.text.trim(),
        "contact_phone": _contactPhoneController.text.trim(),
        "city": _cityController.text.trim(),
        "address": _addressController.text.trim(),
      };
    }
    return body;
  }

  Future<void> _onRegister() async {
    if (!_validateForm()) return;

    final success = await _authViewModel.register(_buildRegisterBody());
    if (!mounted) return;

    if (success) {
      _showSnackBar('¡Registro exitoso! Ahora puedes iniciar sesión');
      Future.delayed(const Duration(seconds: 2), () {
        if (mounted) context.go('/login');
      });
    } else {
      _showSnackBar(
        _authViewModel.errorMessage ?? 'Error al registrar usuario',
        isError: true,
      );
    }
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    String? hint,
    IconData? prefixIcon,
    bool obscure = false,
    TextInputType keyboardType = TextInputType.text,
    String? errorText,
    VoidCallback? onChanged,
    Widget? suffixIcon,
  }) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextField(
            controller: controller,
            obscureText: obscure,
            keyboardType: keyboardType,
            textInputAction: TextInputAction.next,
            style: const TextStyle(color: Colors.white),
            onChanged: (_) => onChanged?.call(),
            decoration: InputDecoration(
              labelText: label,
              hintText: hint,
              hintStyle: TextStyle(color: Colors.grey.shade500),
              labelStyle: TextStyle(color: Colors.grey.shade400),
              prefixIcon: prefixIcon != null
                  ? Icon(prefixIcon, color: Colors.green.shade500)
                  : null,
              suffixIcon: suffixIcon,
              errorText: errorText,
              errorStyle: TextStyle(color: Colors.red.shade400),
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
                borderSide: BorderSide(color: Colors.green.shade500, width: 2),
              ),
              errorBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
                borderSide: BorderSide(color: Colors.red.shade400, width: 1),
              ),
              focusedErrorBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
                borderSide: BorderSide(color: Colors.red.shade400, width: 2),
              ),
              contentPadding: const EdgeInsets.symmetric(
                horizontal: 16,
                vertical: 14,
              ),
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
        title: const Text('Crear cuenta'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      body: ListenableBuilder(
        listenable: _authViewModel,
        builder: (context, _) {
          final isLoading = _authViewModel.isLoading;
          return Stack(
            children: [
              Container(
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
              ),
              SingleChildScrollView(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Step indicator
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 16,
                        vertical: 8,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.green.shade900.withValues(alpha: 0.3),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.person_add,
                            size: 18,
                            color: Colors.green.shade500,
                          ),
                          const SizedBox(width: 8),
                          Text(
                            'Datos de acceso',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                              color: Colors.green.shade400,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),

                    // Email field
                    _buildTextField(
                      controller: _emailController,
                      label: 'Correo electrónico',
                      hint: 'usuario@ejemplo.com',
                      prefixIcon: Icons.email_outlined,
                      keyboardType: TextInputType.emailAddress,
                      errorText: _emailError,
                    ),

                    // Password field with requirements indicator
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        _buildTextField(
                          controller: _passwordController,
                          label: 'Contraseña',
                          obscure: !_showPassword,
                          prefixIcon: Icons.lock_outline,
                          hint: 'Mínimo 8 caracteres',
                          errorText: _passwordError,
                          suffixIcon: IconButton(
                            icon: Icon(
                              _showPassword
                                  ? Icons.visibility_off
                                  : Icons.visibility,
                              color: Colors.grey.shade500,
                            ),
                            onPressed: () {
                              setState(() => _showPassword = !_showPassword);
                            },
                          ),
                        ),
                      ],
                    ),

                    // Confirm password field
                    _buildTextField(
                      controller: _confirmPasswordController,
                      label: 'Confirmar contraseña',
                      obscure: !_showConfirmPassword,
                      prefixIcon: Icons.lock_outline,
                      errorText: _confirmPasswordError,
                      suffixIcon: IconButton(
                        icon: Icon(
                          _showConfirmPassword
                              ? Icons.visibility_off
                              : Icons.visibility,
                          color: Colors.grey.shade500,
                        ),
                        onPressed: () {
                          setState(
                            () => _showConfirmPassword = !_showConfirmPassword,
                          );
                        },
                      ),
                    ),

                    // First name
                    _buildTextField(
                      controller: _firstNameController,
                      label: 'Nombre',
                      prefixIcon: Icons.person_outline,
                      errorText: _firstNameError,
                    ),

                    // Last name
                    _buildTextField(
                      controller: _lastNameController,
                      label: 'Apellido',
                      prefixIcon: Icons.person_outline,
                      errorText: _lastNameError,
                    ),

                    // Phone
                    _buildTextField(
                      controller: _phoneController,
                      label: 'Teléfono',
                      prefixIcon: Icons.phone_outlined,
                      keyboardType: TextInputType.phone,
                      errorText: _phoneError,
                    ),

                    const SizedBox(height: 16),

                    // Account type
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 4),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Tipo de cuenta *',
                            style: TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.w500,
                              color: Colors.grey.shade400,
                            ),
                          ),
                          const SizedBox(height: 8),
                          Container(
                            decoration: BoxDecoration(
                              border: Border.all(color: Colors.grey.shade700),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: DropdownButtonFormField<String>(
                              initialValue: _accountType,
                              dropdownColor: const Color(0xFF1e1e2f),
                              style: const TextStyle(color: Colors.white),
                              decoration: const InputDecoration(
                                border: InputBorder.none,
                                contentPadding: EdgeInsets.symmetric(
                                  horizontal: 16,
                                ),
                              ),
                              items: const [
                                DropdownMenuItem(
                                  value: 'CLIENT',
                                  child: Row(
                                    children: [
                                      Icon(
                                        Icons.person,
                                        size: 20,
                                        color: Color.fromRGBO(72, 203, 76, 1),
                                      ),
                                      SizedBox(width: 8),
                                      Text('Cliente particular'),
                                    ],
                                  ),
                                ),
                                DropdownMenuItem(
                                  value: 'WORKSHOP',
                                  child: Row(
                                    children: [
                                      Icon(
                                        Icons.build,
                                        size: 20,
                                        color: Color.fromRGBO(76, 175, 80, 1),
                                      ),
                                      SizedBox(width: 8),
                                      Text('Taller mecánico'),
                                    ],
                                  ),
                                ),
                                DropdownMenuItem(
                                  value: 'INDEPENDENT_MECHANIC',
                                  child: Row(
                                    children: [
                                      Icon(
                                        Icons.handyman,
                                        size: 20,
                                        color: Color.fromRGBO(76, 175, 80, 1),
                                      ),
                                      SizedBox(width: 8),
                                      Text('Mecánico independiente'),
                                    ],
                                  ),
                                ),
                              ],
                              onChanged: (value) {
                                if (value != null) {
                                  setState(() => _accountType = value);
                                }
                              },
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Workshop specific fields
                    if (_accountType == 'WORKSHOP') ...[
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 4),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const SizedBox(height: 8),
                            Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 16,
                                vertical: 8,
                              ),
                              decoration: BoxDecoration(
                                color: Colors.green.shade900.withValues(
                                  alpha: 0.3,
                                ),
                                borderRadius: BorderRadius.circular(20),
                              ),
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(
                                    Icons.factory,
                                    size: 18,
                                    color: Colors.green.shade500,
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    'Información del taller',
                                    style: TextStyle(
                                      fontSize: 12,
                                      fontWeight: FontWeight.w500,
                                      color: Colors.green.shade400,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 16),
                          ],
                        ),
                      ),
                      _buildTextField(
                        controller: _businessNameController,
                        label: 'Nombre del negocio',
                        prefixIcon: Icons.business,
                        errorText: _businessNameError,
                      ),
                      _buildTextField(
                        controller: _legalNameController,
                        label: 'Razón social',
                        prefixIcon: Icons.description,
                      ),
                      _buildTextField(
                        controller: _descriptionController,
                        label: 'Descripción',
                        hint: 'Describe los servicios que ofreces',
                        prefixIcon: Icons.info_outline,
                      ),
                      _buildTextField(
                        controller: _contactEmailController,
                        label: 'Email de contacto',
                        hint: 'contacto@taller.com',
                        prefixIcon: Icons.email_outlined,
                        keyboardType: TextInputType.emailAddress,
                      ),
                      _buildTextField(
                        controller: _contactPhoneController,
                        label: 'Teléfono de contacto',
                        prefixIcon: Icons.phone_outlined,
                        keyboardType: TextInputType.phone,
                      ),
                      _buildTextField(
                        controller: _cityController,
                        label: 'Ciudad',
                        prefixIcon: Icons.location_city,
                        errorText: _cityError,
                      ),
                      _buildTextField(
                        controller: _addressController,
                        label: 'Dirección',
                        prefixIcon: Icons.location_on_outlined,
                        errorText: _addressError,
                      ),
                    ],

                    const SizedBox(height: 16),

                    // Terms and conditions
                    Row(
                      children: [
                        Checkbox(
                          value: _acceptedTerms,
                          onChanged: (value) {
                            setState(() => _acceptedTerms = value ?? false);
                          },
                          activeColor: Colors.green.shade500,
                          checkColor: Colors.white,
                          side: BorderSide(color: Colors.grey.shade600),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(4),
                          ),
                        ),
                        Expanded(
                          child: GestureDetector(
                            onTap: () {
                              setState(() => _acceptedTerms = !_acceptedTerms);
                            },
                            child: RichText(
                              text: TextSpan(
                                style: TextStyle(color: Colors.grey.shade400),
                                children: [
                                  const TextSpan(text: 'Acepto los '),
                                  TextSpan(
                                    text: 'términos y condiciones',
                                    style: TextStyle(
                                      color: Colors.green.shade400,
                                      fontWeight: FontWeight.w600,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 24),

                    // Register button
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: isLoading ? null : _onRegister,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade600,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 16),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                          elevation: 2,
                        ),
                        child: isLoading
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
                            : const Text(
                                'Registrarme',
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Login link
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          '¿Ya tienes cuenta?',
                          style: TextStyle(color: Colors.grey.shade400),
                        ),
                        TextButton(
                          onPressed: () => context.go('/login'),
                          child: Text(
                            'Inicia sesión aquí',
                            style: TextStyle(
                              color: Colors.green.shade400,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 32),
                  ],
                ),
              ),

              // Loading overlay
              if (isLoading)
                Container(
                  color: Colors.black.withValues(alpha: 0.6),
                  child: const Center(
                    child: Card(
                      color: Color(0xFF1e1e2f),
                      child: Padding(
                        padding: EdgeInsets.all(20),
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            CircularProgressIndicator(),
                            SizedBox(height: 12),
                            Text('Creando cuenta...'),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
            ],
          );
        },
      ),
    );
  }
}
