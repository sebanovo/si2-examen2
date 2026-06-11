import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../viewmodels/auth_viewmodel.dart';
import '../../core/di/injection_container.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late AuthViewModel _authViewModel;

  @override
  void initState() {
    super.initState();
    _authViewModel = sl<AuthViewModel>();

    if (_authViewModel.user == null) {
      _authViewModel.loadMe();
    }
  }

  void _showInfoSnackBar(String message, {bool isError = false}) {
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

  void _logout() {
    _authViewModel.logout();
    _showInfoSnackBar('Sesión cerrada correctamente');
    context.go('/login');
  }

  String? _getUserRole(List<String>? roleCodes) {
    if (roleCodes == null || roleCodes.isEmpty) return null;
    return roleCodes.first;
  }

  String _getRoleDisplayName(List<String>? roleCodes) {
    final role = _getUserRole(roleCodes);
    switch (role) {
      case 'PROVIDER_ADMIN':
        return 'Taller / Proveedor';
      case 'CLIENT':
        return 'Cliente';
      case 'PLATFORM_ADMIN':
        return 'Administrador';
      case 'TECHNICIAN':
        return 'Técnico';
      default:
        return 'Usuario';
    }
  }

  bool _hasRole(List<String>? roleCodes, String role) {
    return roleCodes?.contains(role) ?? false;
  }

  @override
  Widget build(BuildContext context) {
    final userRole = _getUserRole(_authViewModel.user?.roleCodes);
    final isClient = _hasRole(_authViewModel.user?.roleCodes, 'CLIENT');
    final isAdmin = _hasRole(_authViewModel.user?.roleCodes, 'PLATFORM_ADMIN');
    final isProvider = _hasRole(
      _authViewModel.user?.roleCodes,
      'PROVIDER_ADMIN',
    );

    return Scaffold(
      appBar: AppBar(
        title: const Text('Inicio'),
        backgroundColor: const Color(0xFF1a1a2e),
        foregroundColor: Colors.white,
        elevation: 2,
      ),
      drawer: _buildDrawer(context, userRole, isClient, isAdmin, isProvider),
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
        child: _buildCalendar(),
      ),
    );
  }

  Widget _buildCalendar() {
    final now = DateTime.now();
    final weekdays = ['LUN', 'MAR', 'MIÉ', 'JUE', 'VIE', 'SÁB', 'DOM'];
    final months = [
      'Enero',
      'Febrero',
      'Marzo',
      'Abril',
      'Mayo',
      'Junio',
      'Julio',
      'Agosto',
      'Septiembre',
      'Octubre',
      'Noviembre',
      'Diciembre',
    ];

    return Center(
      child: Card(
        elevation: 6,
        color: const Color(0xFF1e1e2f),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        margin: const EdgeInsets.all(24),
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [const Color(0xFF1e1e2f), const Color(0xFF16213e)],
            ),
            borderRadius: BorderRadius.circular(24),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(Icons.calendar_today, size: 48, color: Colors.green),
              const SizedBox(height: 16),
              Text(
                '${weekdays[now.weekday - 1]}, ${now.day} de ${months[now.month - 1]}',
                style: const TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                now.year.toString(),
                style: TextStyle(fontSize: 16, color: Colors.grey.shade400),
              ),
              const Divider(height: 32, color: Color.fromRGBO(66, 66, 66, 1)),
              Text(
                'Bienvenido a la plataforma de asistencia vehicular',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 14, color: Colors.grey.shade400),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildDrawer(
    BuildContext context,
    String? userRole,
    bool isClient,
    bool isAdmin,
    bool isProvider,
  ) {
    return Drawer(
      child: Container(
        color: const Color(0xFF1a1a2e),
        child: Column(
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [const Color(0xFF1a1a2e), const Color(0xFF0f3460)],
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  CircleAvatar(
                    radius: 24,
                    backgroundColor: Colors.white,
                    child: Icon(
                      _getRoleIcon(userRole),
                      size: 28,
                      color: const Color(0xFF1a1a2e),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Flexible(
                    child: Text(
                      _authViewModel.user?.fullName ?? 'Cargando...',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 15,
                        fontWeight: FontWeight.bold,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Flexible(
                    child: Text(
                      _authViewModel.user?.email ?? '',
                      style: TextStyle(
                        color: Colors.green.shade400,
                        fontSize: 11,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 6,
                      vertical: 2,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.green.shade900.withValues(alpha: 0.5),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      _getRoleDisplayName(_authViewModel.user?.roleCodes),
                      style: const TextStyle(
                        color: Color.fromRGBO(102, 187, 106, 1),
                        fontSize: 10,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            _buildDrawerItem(
              icon: Icons.home,
              title: 'Inicio',
              onTap: () {
                context.pop();
              },
            ),
            if (isClient)
              _buildDrawerItem(
                icon: Icons.directions_car,
                title: 'Mis vehículos',
                onTap: () {
                  context.pop();
                  context.push('/vehicles');
                },
              ),
            if (isProvider)
              _buildDrawerItem(
                icon: Icons.construction,
                title: 'Mis Técnicos',
                onTap: () {
                  context.pop();
                  context.push('/technicians');
                },
              ),
            if (isProvider)
              _buildDrawerItem(
                icon: Icons.business,
                title: 'Mi Taller',
                onTap: () {
                  context.pop();
                  context.push('/provider-profile');
                },
              ),
            if (isAdmin)
              _buildDrawerItem(
                icon: Icons.business_center,
                title: 'Proveedores',
                onTap: () {
                  context.pop();
                  context.push('/admin/providers');
                },
              ),
            if (isProvider)
              _buildDrawerItem(
                icon: Icons.miscellaneous_services,
                title: 'Servicios',
                onTap: () {
                  context.pop();
                  context.push('/catalog-services');
                },
              ),
            if (isAdmin)
              _buildDrawerItem(
                icon: Icons.admin_panel_settings,
                title: 'Panel de Control',
                onTap: () {
                  context.pop();
                  context.push('/admin/incidents');
                },
              ),
            if (isProvider)
              _buildDrawerItem(
                icon: Icons.list_alt,
                title: 'Solicitudes Disponibles',
                onTap: () {
                  context.pop();
                  context.push('/provider/available-requests');
                },
              ),
            if (isProvider)
              _buildDrawerItem(
                icon: Icons.engineering,
                title: 'Operaciones Activas',
                onTap: () {
                  context.pop();
                  context.push('/provider/active-operations');
                },
              ),
            if (isClient)
              _buildDrawerItem(
                icon: Icons.list_alt,
                title: 'Mis Solicitudes',
                onTap: () {
                  context.pop();
                  context.push('/incidents');
                },
              ),
            _buildDrawerItem(
              icon: Icons.notifications,
              title: 'Mis Dispositivos',
              onTap: () {
                context.pop();
                context.push('/devices');
              },
            ),
            _buildDrawerItem(
              icon: Icons.map,
              title: 'Mapa de prueba',
              onTap: () {
                context.pop();
                context.push('/map');
              },
            ),
            const Divider(color: Color.fromRGBO(66, 66, 66, 1)),
            _buildDrawerItem(
              icon: Icons.logout,
              title: 'Cerrar sesión',
              onTap: _logout,
              isDestructive: true,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDrawerItem({
    required IconData icon,
    required String title,
    required VoidCallback onTap,
    bool isDestructive = false,
  }) {
    return ListTile(
      leading: Icon(
        icon,
        color: isDestructive ? Colors.red.shade400 : Colors.green.shade500,
      ),
      title: Text(
        title,
        style: TextStyle(
          color: isDestructive ? Colors.red.shade400 : Colors.grey.shade300,
          fontWeight: isDestructive ? FontWeight.w500 : null,
        ),
      ),
      onTap: onTap,
      hoverColor: Colors.green.shade900.withValues(alpha: 0.3),
      splashColor: Colors.green.shade800.withValues(alpha: 0.2),
    );
  }

  IconData _getRoleIcon(String? roleCode) {
    switch (roleCode) {
      case 'PROVIDER_ADMIN':
        return Icons.build_circle;
      case 'CLIENT':
        return Icons.person;
      case 'PLATFORM_ADMIN':
        return Icons.admin_panel_settings;
      case 'TECHNICIAN':
        return Icons.handyman;
      default:
        return Icons.person;
    }
  }
}
