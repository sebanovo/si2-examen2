import 'package:get_it/get_it.dart';
import 'package:mechanic_mobile/domain/repositories/service_request_repository.dart';
import 'package:mechanic_mobile/domain/repositories/vehicle_repository.dart';
import 'package:mechanic_mobile/domain/usecases/accept_candidate_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/add_file_evidence_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/add_text_evidence_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/cancel_incident_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/cancel_service_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/complete_service_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/create_incident_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/create_provider_service_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/create_technician_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/create_vehicle_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/dispatch_incident_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_active_operations_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_all_incidents_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_available_candidates_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_candidate_details_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_catalog_services_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_incident_candidates_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_incident_details_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_live_tracking_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_my_devices_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_my_incidents_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_operation_state_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_provider_profile_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_provider_services_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_providers_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_service_requests_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_my_vehicles_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_technicians_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_tracking_history_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/get_vehicle_by_id_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/mark_arrived_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/publish_incident_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/refresh_route_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/register_device_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/reject_candidate_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/report_location_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/start_service_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/unregister_device_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/update_incident_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/update_provider_profile_usecase.dart';
import 'package:mechanic_mobile/domain/usecases/update_technician_usecase.dart';
import 'package:mechanic_mobile/infrastructure/datasources/admin_incident_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/catalog_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/evidence_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/incident_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/notification_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/provider_admin_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/provider_assignment_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/provider_operation_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/provider_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/technician_datasource.dart';
import 'package:mechanic_mobile/infrastructure/datasources/tracking_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/datasources/vehicle_remote_data_source.dart';
import 'package:mechanic_mobile/infrastructure/repositories/admin_incident_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/catalog_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/evidence_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/incident_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/notification_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/provider_admin_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/provider_assignment_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/provider_operation_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/provider_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/technician_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/tracking_repository_impl.dart';
import 'package:mechanic_mobile/infrastructure/repositories/vehicle_repository_impl.dart';
import 'package:mechanic_mobile/presentation/services/notification_service.dart';
import 'package:mechanic_mobile/presentation/viewmodels/admin_incidents_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/admin_providers_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/catalog_services_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/client_tracking_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/evidence_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/home_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/incidents_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/platform_tracking_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/provider_available_requests_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/provider_operation_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/provider_profile_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/provider_tracking_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/technicians_viewmodel.dart';
import 'package:mechanic_mobile/presentation/viewmodels/vehicle_viewmodel.dart';

// CORE
import '../../core/network/api_client.dart';

// DATA
import '../../infrastructure/datasources/auth_remote_data_source.dart';
import '../../infrastructure/repositories/auth_repository_impl.dart';

// DOMAIN
import '../../domain/repositories/auth_repository.dart';
import '../../domain/usecases/login_usecase.dart';
import '../../domain/usecases/get_me_usecase.dart';
import '../../domain/usecases/get_my_profile_usecase.dart';
import '../../domain/usecases/register_usecase.dart';
import '../../domain/usecases/update_my_profile_usecase.dart';
import '../../domain/usecases/update_vehicle_usecase.dart';

// PRESENTATION
import '../../presentation/viewmodels/auth_viewmodel.dart';

final sl = GetIt.instance;

Future<void> init() async {
  // =========================
  // 🔒 CORE
  // =========================
  sl.registerLazySingleton(() => ApiClient());

  // =========================
  // 📡 DATASOURCES (REAL API)
  // =========================
  sl.registerLazySingleton<AuthRemoteDataSource>(
    () => AuthRemoteDataSource(sl()),
  );
  sl.registerLazySingleton<VehicleRemoteDataSource>(
    () => VehicleRemoteDataSource(sl()),
  );

  // =========================
  // 🧠 REPOSITORIES
  // =========================
  sl.registerLazySingleton<AuthRepository>(
    () => AuthRepositoryImpl(sl(), sl()),
  );

  sl.registerLazySingleton<VehicleRepository>(
    () => VehicleRepositoryImpl(sl()),
  );

  // =========================
  // 🎯 USE CASES
  // =========================
  sl.registerLazySingleton(() => LoginUseCase(sl()));
  sl.registerLazySingleton(() => RegisterUseCase(sl()));
  sl.registerLazySingleton(() => GetMeUseCase(sl()));
  sl.registerLazySingleton(() => GetMyProfileUseCase(sl()));
  sl.registerLazySingleton(() => UpdateMyProfileUseCase(sl()));
  sl.registerLazySingleton(() => CreateVehicleUseCase(sl()));
  sl.registerLazySingleton(() => GetMyVehiclesUseCase(sl()));
  sl.registerLazySingleton(() => GetVehicleByIdUseCase(sl()));
  sl.registerLazySingleton(() => UpdateVehicleUseCase(sl()));

  // =========================
  // 🧩 VIEWMODELS
  // =========================
  sl.registerLazySingleton(
    () => AuthViewModel(
      sl<LoginUseCase>(),
      sl<RegisterUseCase>(),
      sl<GetMeUseCase>(),
      sl<GetMyProfileUseCase>(),
      sl<UpdateMyProfileUseCase>(),
    ),
  );

  sl.registerLazySingleton(() => GetServiceRequestsUseCase(sl()));

  sl.registerLazySingleton(
    () => HomeViewModel(
      getServiceRequestsUseCase: sl<GetServiceRequestsUseCase>(),
      getAllIncidentsUseCase: sl<GetAllIncidentsUseCase>(),
    ),
  );
  sl.registerLazySingleton(
    () => VehicleViewModel(
      createVehicleUseCase: sl(),
      getMyVehiclesUseCase: sl(),
      getVehicleByIdUseCase: sl(),
      updateVehicleUseCase: sl(),
    ),
  );
  initTechniciansModule();
  initProviderModule();
  initCatalogModule();
  initIncidentModule();
  initEvidenceModule();
  initAdminIncidentModule();
  initProviderAssignmentModule();
  initProviderOperationModule();
  initTrackingModule();
  initNotificationModule();
  initAdminProvidersModule();
}

void initTechniciansModule() {
  sl.registerFactory<TechnicianRemoteDataSource>(
    () => TechnicianRemoteDataSourceImpl(sl<ApiClient>()),
  );

  sl.registerFactory<TechnicianRepository>(
    () => TechnicianRepository(sl<TechnicianRemoteDataSource>()),
  );

  sl.registerFactory<CreateTechnicianUseCase>(
    () => CreateTechnicianUseCaseImpl(sl<TechnicianRepository>()),
  );

  sl.registerFactory<GetTechniciansUseCase>(
    () => GetTechniciansUseCaseImpl(sl<TechnicianRepository>()),
  );

  sl.registerFactory<UpdateTechnicianUseCase>(
    () => UpdateTechnicianUseCaseImpl(sl<TechnicianRepository>()),
  );

  sl.registerFactory<TechniciansViewModel>(
    () => TechniciansViewModel(
      createTechnicianUseCase: sl<CreateTechnicianUseCase>(),
      getTechniciansUseCase: sl<GetTechniciansUseCase>(),
      updateTechnicianUseCase: sl<UpdateTechnicianUseCase>(),
    ),
  );
}

// Agregar módulo
void initProviderModule() {
  // Data Source
  sl.registerFactory<ProviderRemoteDataSource>(
    () => ProviderRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<ProviderRepository>(
    () => ProviderRepository(sl<ProviderRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetProviderProfileUseCase>(
    () => GetProviderProfileUseCaseImpl(sl<ProviderRepository>()),
  );

  sl.registerFactory<UpdateProviderProfileUseCase>(
    () => UpdateProviderProfileUseCaseImpl(sl<ProviderRepository>()),
  );

  // ViewModel
  sl.registerFactory<ProviderProfileViewModel>(
    () => ProviderProfileViewModel(
      getProviderProfileUseCase: sl<GetProviderProfileUseCase>(),
      updateProviderProfileUseCase: sl<UpdateProviderProfileUseCase>(),
    ),
  );
}

void initCatalogModule() {
  // Data Source
  sl.registerFactory<CatalogRemoteDataSource>(
    () => CatalogRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<CatalogRepository>(
    () => CatalogRepository(sl<CatalogRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetCatalogServicesUseCase>(
    () => GetCatalogServicesUseCaseImpl(sl<CatalogRepository>()),
  );

  sl.registerFactory<GetProviderServicesUseCase>(
    () => GetProviderServicesUseCaseImpl(sl<CatalogRepository>()),
  );

  sl.registerFactory<CreateProviderServiceUseCase>(
    () => CreateProviderServiceUseCaseImpl(sl<CatalogRepository>()),
  );

  // ViewModel
  sl.registerFactory<CatalogServicesViewModel>(
    () => CatalogServicesViewModel(
      getCatalogServicesUseCase: sl<GetCatalogServicesUseCase>(),
      getProviderServicesUseCase: sl<GetProviderServicesUseCase>(),
      createProviderServiceUseCase: sl<CreateProviderServiceUseCase>(),
    ),
  );
}

void initIncidentModule() {
  // Data Source
  sl.registerFactory<IncidentRemoteDataSource>(
    () => IncidentRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<IncidentRepository>(
    () => IncidentRepository(sl<IncidentRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetMyIncidentsUseCase>(
    () => GetMyIncidentsUseCaseImpl(sl<IncidentRepository>()),
  );

  sl.registerFactory<CreateIncidentUseCase>(
    () => CreateIncidentUseCaseImpl(sl<IncidentRepository>()),
  );

  sl.registerFactory<UpdateIncidentUseCase>(
    () => UpdateIncidentUseCaseImpl(sl<IncidentRepository>()),
  );

  sl.registerFactory<CancelIncidentUseCase>(
    () => CancelIncidentUseCaseImpl(sl<IncidentRepository>()),
  );

  // ViewModel
  sl.registerFactory<IncidentsViewModel>(
    () => IncidentsViewModel(
      getMyIncidentsUseCase: sl<GetMyIncidentsUseCase>(),
      createIncidentUseCase: sl<CreateIncidentUseCase>(),
      updateIncidentUseCase: sl<UpdateIncidentUseCase>(),
      cancelIncidentUseCase: sl<CancelIncidentUseCase>(),
    ),
  );
}

void initEvidenceModule() {
  // Data Source
  sl.registerFactory<EvidenceRemoteDataSource>(
    () => EvidenceRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<EvidenceRepository>(
    () => EvidenceRepository(sl<EvidenceRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<AddTextEvidenceUseCase>(
    () => AddTextEvidenceUseCaseImpl(sl<EvidenceRepository>()),
  );

  sl.registerFactory<AddFileEvidenceUseCase>(
    () => AddFileEvidenceUseCaseImpl(sl<EvidenceRepository>()),
  );

  // ViewModel
  sl.registerFactory<EvidenceViewModel>(
    () => EvidenceViewModel(
      addTextEvidenceUseCase: sl<AddTextEvidenceUseCase>(),
      addFileEvidenceUseCase: sl<AddFileEvidenceUseCase>(),
    ),
  );
}

void initAdminIncidentModule() {
  // Data Source
  sl.registerFactory<AdminIncidentRemoteDataSource>(
    () => AdminIncidentRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<AdminIncidentRepository>(
    () => AdminIncidentRepository(sl<AdminIncidentRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetAllIncidentsUseCase>(
    () => GetAllIncidentsUseCaseImpl(sl<AdminIncidentRepository>()),
  );

  sl.registerFactory<GetIncidentDetailsUseCase>(
    () => GetIncidentDetailsUseCaseImpl(sl<AdminIncidentRepository>()),
  );

  sl.registerFactory<GetIncidentCandidatesUseCase>(
    () => GetIncidentCandidatesUseCaseImpl(sl<AdminIncidentRepository>()),
  );

  sl.registerFactory<PublishIncidentUseCase>(
    () => PublishIncidentUseCaseImpl(sl<AdminIncidentRepository>()),
  );

  // ViewModel
  sl.registerFactory<AdminIncidentsViewModel>(
    () => AdminIncidentsViewModel(
      getAllIncidentsUseCase: sl<GetAllIncidentsUseCase>(),
      getIncidentDetailsUseCase: sl<GetIncidentDetailsUseCase>(),
      getIncidentCandidatesUseCase: sl<GetIncidentCandidatesUseCase>(),
      publishIncidentUseCase: sl<PublishIncidentUseCase>(),
    ),
  );
}

void initProviderAssignmentModule() {
  // Data Source
  sl.registerFactory<ProviderAssignmentRemoteDataSource>(
    () => ProviderAssignmentRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<ProviderAssignmentRepository>(
    () =>
        ProviderAssignmentRepository(sl<ProviderAssignmentRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetAvailableCandidatesUseCase>(
    () => GetAvailableCandidatesUseCaseImpl(sl<ProviderAssignmentRepository>()),
  );

  sl.registerFactory<GetCandidateDetailsUseCase>(
    () => GetCandidateDetailsUseCaseImpl(sl<ProviderAssignmentRepository>()),
  );

  sl.registerFactory<AcceptCandidateUseCase>(
    () => AcceptCandidateUseCaseImpl(sl<ProviderAssignmentRepository>()),
  );

  sl.registerFactory<RejectCandidateUseCase>(
    () => RejectCandidateUseCaseImpl(sl<ProviderAssignmentRepository>()),
  );

  // ViewModel
  sl.registerFactory<ProviderAvailableRequestsViewModel>(
    () => ProviderAvailableRequestsViewModel(
      getAvailableCandidatesUseCase: sl<GetAvailableCandidatesUseCase>(),
      getCandidateDetailsUseCase: sl<GetCandidateDetailsUseCase>(),
      acceptCandidateUseCase: sl<AcceptCandidateUseCase>(),
      rejectCandidateUseCase: sl<RejectCandidateUseCase>(),
    ),
  );
}

void initProviderOperationModule() {
  // Data Source
  sl.registerFactory<ProviderOperationRemoteDataSource>(
    () => ProviderOperationRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<ProviderOperationRepository>(
    () => ProviderOperationRepository(sl<ProviderOperationRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<GetActiveOperationsUseCase>(
    () => GetActiveOperationsUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<GetOperationStateUseCase>(
    () => GetOperationStateUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<DispatchIncidentUseCase>(
    () => DispatchIncidentUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<MarkArrivedUseCase>(
    () => MarkArrivedUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<StartServiceUseCase>(
    () => StartServiceUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<CompleteServiceUseCase>(
    () => CompleteServiceUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  sl.registerFactory<CancelServiceUseCase>(
    () => CancelServiceUseCaseImpl(sl<ProviderOperationRepository>()),
  );

  // ViewModel
  sl.registerFactory<ProviderOperationViewModel>(
    () => ProviderOperationViewModel(
      getActiveOperationsUseCase: sl<GetActiveOperationsUseCase>(),
      getOperationStateUseCase: sl<GetOperationStateUseCase>(),
      dispatchIncidentUseCase: sl<DispatchIncidentUseCase>(),
      markArrivedUseCase: sl<MarkArrivedUseCase>(),
      startServiceUseCase: sl<StartServiceUseCase>(),
      completeServiceUseCase: sl<CompleteServiceUseCase>(),
      cancelServiceUseCase: sl<CancelServiceUseCase>(),
    ),
  );
}

void initTrackingModule() {
  // Data Source
  sl.registerFactory<TrackingRemoteDataSource>(
    () => TrackingRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<TrackingRepository>(
    () => TrackingRepository(sl<TrackingRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<ReportLocationUseCase>(
    () => ReportLocationUseCaseImpl(sl<TrackingRepository>()),
  );

  sl.registerFactory<RefreshRouteUseCase>(
    () => RefreshRouteUseCaseImpl(sl<TrackingRepository>()),
  );

  sl.registerFactory<GetLiveTrackingUseCase>(
    () => GetLiveTrackingUseCaseImpl(sl<TrackingRepository>()),
  );

  sl.registerFactory<GetTrackingHistoryUseCase>(
    () => GetTrackingHistoryUseCaseImpl(sl<TrackingRepository>()),
  );

  // ViewModel
  sl.registerFactory<ProviderTrackingViewModel>(
    () => ProviderTrackingViewModel(
      reportLocationUseCase: sl<ReportLocationUseCase>(),
      refreshRouteUseCase: sl<RefreshRouteUseCase>(),
      getLiveTrackingUseCase: sl<GetLiveTrackingUseCase>(),
      getTrackingHistoryUseCase: sl<GetTrackingHistoryUseCase>(),
    ),
  );

  sl.registerFactory<ClientTrackingViewModel>(
    () => ClientTrackingViewModel(sl<TrackingRemoteDataSource>()),
  );

  sl.registerFactory<PlatformTrackingViewModel>(
    () => PlatformTrackingViewModel(sl<TrackingRemoteDataSource>()),
  );
}

// Agregar módulo
void initNotificationModule() {
  // Data Source
  sl.registerFactory<NotificationRemoteDataSource>(
    () => NotificationRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<NotificationRepository>(
    () => NotificationRepository(sl<NotificationRemoteDataSource>()),
  );

  // Use Cases
  sl.registerFactory<RegisterDeviceUseCase>(
    () => RegisterDeviceUseCaseImpl(sl<NotificationRepository>()),
  );

  sl.registerFactory<UnregisterDeviceUseCase>(
    () => UnregisterDeviceUseCaseImpl(sl<NotificationRepository>()),
  );

  sl.registerFactory<GetMyDevicesUseCase>(
    () => GetMyDevicesUseCaseImpl(sl<NotificationRepository>()),
  );

  // Service - Singleton
  sl.registerLazySingleton<NotificationService>(() => NotificationService());
}

void initAdminProvidersModule() {
  // Data Source
  sl.registerFactory<ProviderAdminRemoteDataSource>(
    () => ProviderAdminRemoteDataSourceImpl(sl<ApiClient>()),
  );

  // Repository
  sl.registerFactory<ProviderAdminRepository>(
    () => ProviderAdminRepository(sl<ProviderAdminRemoteDataSource>()),
  );

  // Use Case
  sl.registerFactory<GetProvidersUseCase>(
    () => GetProvidersUseCaseImpl(sl<ProviderAdminRepository>()),
  );

  // ViewModel
  sl.registerFactory<AdminProvidersViewModel>(
    () =>
        AdminProvidersViewModel(getProvidersUseCase: sl<GetProvidersUseCase>()),
  );
}
