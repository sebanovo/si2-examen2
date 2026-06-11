import 'package:go_router/go_router.dart';
import 'package:mechanic_mobile/domain/entities/incident.dart';
import 'package:mechanic_mobile/domain/entities/provider_operation.dart';
import 'package:mechanic_mobile/presentation/pages/add_evidence_page.dart';
import 'package:mechanic_mobile/presentation/pages/admin_incident_detail_page.dart';
import 'package:mechanic_mobile/presentation/pages/admin_incidents_page.dart';
import 'package:mechanic_mobile/presentation/pages/admin_providers_page.dart';
import 'package:mechanic_mobile/presentation/pages/catalog_services_page.dart';
import 'package:mechanic_mobile/presentation/pages/client_tracking_page.dart';
import 'package:mechanic_mobile/presentation/pages/create_incident_page.dart';
import 'package:mechanic_mobile/presentation/pages/devices_page.dart';
import 'package:mechanic_mobile/presentation/pages/incident_detail_page.dart';
import 'package:mechanic_mobile/presentation/pages/incidents_page.dart';
import 'package:mechanic_mobile/presentation/pages/map_page.dart';
import 'package:mechanic_mobile/presentation/pages/platform_tracking_page.dart';
import 'package:mechanic_mobile/presentation/pages/provider_active_operations_page.dart';
import 'package:mechanic_mobile/presentation/pages/provider_available_requests_page.dart';
import 'package:mechanic_mobile/presentation/pages/provider_operation_detail_page.dart';
import 'package:mechanic_mobile/presentation/pages/provider_profile_page.dart';
import 'package:mechanic_mobile/presentation/pages/provider_tracking_page.dart';
import 'package:mechanic_mobile/presentation/pages/technicians_page.dart';
import '../../domain/entities/service_request.dart';
import '../../presentation/pages/login_page.dart';
import '../../presentation/pages/register_page.dart';
import '../../presentation/pages/home_page.dart';
import '../../presentation/pages/request_detail_page.dart';
import '../../presentation/pages/vehicles_page.dart';

final appRouter = GoRouter(
  initialLocation: '/login',
  routes: [
    GoRoute(path: '/login', builder: (context, state) => const LoginPage()),
    GoRoute(
      path: '/register',
      builder: (context, state) => const RegisterPage(),
    ),
    GoRoute(path: '/', builder: (context, state) => const HomePage()),
    GoRoute(
      path: '/vehicles',
      builder: (context, state) => const VehiclesPage(),
    ),
    GoRoute(
      path: '/technicians',
      builder: (context, state) => const TechniciansPage(),
    ),
    GoRoute(
      path: '/provider-profile',
      builder: (context, state) => const ProviderProfilePage(),
    ),
    GoRoute(
      path: '/catalog-services',
      builder: (context, state) => const CatalogServicesPage(),
    ),
    GoRoute(
      path: '/incidents',
      name: 'incidents',
      builder: (context, state) => const IncidentsPage(),
    ),
    GoRoute(
      path: '/create-incident',
      name: 'create-incident',
      builder: (context, state) => const CreateIncidentPage(),
    ),
    GoRoute(
      path: '/incident-detail/:id',
      name: 'incident-detail',
      builder: (context, state) {
        final incident = state.extra as Incident?;
        return IncidentDetailPage(incident: incident);
      },
    ),
    GoRoute(
      path: '/add-evidence/:incidentId',
      name: 'add-evidence',
      builder: (context, state) {
        final incidentId = state.pathParameters['incidentId']!;
        return AddEvidencePage(incidentId: incidentId);
      },
    ),
    GoRoute(
      path: '/admin/incidents',
      name: 'admin-incidents',
      builder: (context, state) => const AdminIncidentsPage(),
    ),
    GoRoute(
      path: '/admin/incident/:id',
      name: 'admin-incident-detail',
      builder: (context, state) {
        final id = state.pathParameters['id']!;
        return AdminIncidentDetailPage(incidentId: id);
      },
    ),

    GoRoute(
      path: '/provider/active-operations',
      name: 'provider-active-operations',
      builder: (context, state) => const ProviderActiveOperationsPage(),
    ),
    GoRoute(
      path: '/provider/operation/:id',
      name: 'provider-operation-detail',
      builder: (context, state) {
        final operation = state.extra as ProviderOperation?;
        return ProviderOperationDetailPage(operation: operation);
      },
    ),

    GoRoute(
      path: '/provider/tracking/:incidentId/:technicianId',
      name: 'provider-tracking',
      builder: (context, state) {
        final incidentId = state.pathParameters['incidentId']!;
        final technicianId = state.pathParameters['technicianId']!;
        return ProviderTrackingPage(
          incidentId: incidentId,
          technicianId: technicianId,
        );
      },
    ),

    GoRoute(
      path: '/client/tracking/:incidentId',
      name: 'client-tracking',
      builder: (context, state) {
        final incidentId = state.pathParameters['incidentId']!;
        return ClientTrackingPage(incidentId: incidentId);
      },
    ),
    GoRoute(
      path: '/platform/tracking/:incidentId',
      name: 'platform-tracking',
      builder: (context, state) {
        final incidentId = state.pathParameters['incidentId']!;
        return PlatformTrackingPage(incidentId: incidentId);
      },
    ),

    GoRoute(
      path: '/provider/available-requests',
      name: 'provider-available-requests',
      builder: (context, state) => const ProviderAvailableRequestsPage(),
    ),

    GoRoute(
      path: '/devices',
      name: 'devices',
      builder: (context, state) => const DevicesPage(),
    ),

    GoRoute(
      path: '/admin/providers',
      name: 'admin-providers',
      builder: (context, state) => const AdminProvidersPage(),
    ),

    GoRoute(
      path: '/map',
      name: 'map',
      builder: (context, state) => const MapPage(),
    ),

    GoRoute(
      path: '/request/:id',
      builder: (context, state) {
        // We pass the ServiceRequest as an extra object to avoid fetching it again just for the detail view
        // in this simple static data approach.
        final request = state.extra as ServiceRequest;
        return RequestDetailPage(request: request);
      },
    ),
  ],
);
