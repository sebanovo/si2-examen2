# mechanic_mobile

A new Flutter project.

### Clean Archutecture
```
└── 📁lib
    └── 📁constants
        ├── env.dart
    └── 📁core
        └── 📁di
            ├── injection_container.dart
        └── 📁error
            ├── failures.dart
        └── 📁routes
            ├── app_routes.dart
    └── 📁data
        └── 📁datasources
            ├── mock_auth_data_source.dart
        └── 📁models
            ├── service_request_model.dart
            ├── user_model.dart
        └── 📁repositories
            ├── auth_repository_impl.dart
    └── 📁domain
        └── 📁entities
            ├── service_request.dart
            ├── user.dart
        └── 📁repositories
            ├── auth_repository.dart
            ├── service_request_repository.dart
        └── 📁usecases
            ├── get_service_requests_usecase.dart
            ├── login_usecase.dart
    └── 📁presentation
        └── 📁auth
            └── 📁pages
                ├── login_page.dart
            └── 📁viewmodels
                ├── auth_viewmodel.dart
        └── 📁home
            └── 📁pages
                ├── home_page.dart
            └── 📁viewmodels
                ├── home_viewmodel.dart
        └── 📁service_request
            └── 📁pages
                ├── request_detail_page.dart
    └── main.dart
```

```bash
Clean Code Flow
domain:
(entities)vehicle 
|  |
|  |->(repositories)vehicle_repository "interface"
|  |
|--|->(usecases)get_vehicles_usecase


infrastructure:
(models)vehicle
  |
  |->(datasources)vehicle_remote_datasource "interface" + "class" -> (class implements inteface)
  |
  |->(repositories)vehicle_repository_impl (class implements interface off domain/repositories)


presentation:
(viewmodels)vehicles_viewmodel usa domain/entities y domain/usecases
  |
  |->(pages)vehicles_page usa core/di

```