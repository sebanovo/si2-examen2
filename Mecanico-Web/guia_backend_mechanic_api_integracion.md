# Guía completa del backend `mechanic-api` para integración Flutter + Angular

**Proyecto:** Plataforma Inteligente de Atención de Emergencias Vehiculares  
**Backend revisado:** `mechanic-api` exportado el 2026-04-19  
**Fecha de esta guía:** 2026-04-25  
**Tipo de revisión:** revisión estática del código exportado en Markdown. No se ejecutó el servidor ni se probaron requests reales en Docker/Postman porque el entregable recibido es un export del código, no el proyecto ejecutándose.

---

## 1. Resumen ejecutivo

El backend está bastante avanzado para la defensa del primer parcial. Implementa la mayor parte del flujo principal del sistema solicitado:

- Registro/login con JWT Bearer.
- Roles base: `CLIENT`, `PROVIDER_ADMIN`, `TECHNICIAN`, `PLATFORM_ADMIN`.
- Registro de clientes, talleres y mecánicos independientes.
- Gestión de vehículos del cliente.
- Creación y seguimiento de incidentes.
- Carga de evidencias de texto, imagen y audio.
- Procesamiento asíncrono con Celery/Redis.
- Integraciones preparadas para:
  - transcripción de audio con `faster-whisper`,
  - análisis visual con `Ultralytics YOLO`,
  - resumen/clasificación con OpenRouter,
  - cálculo de rutas con GraphHopper o fallback Haversine,
  - almacenamiento local o S3.
- Motor de asignación de talleres basado en servicios, disponibilidad, capacidad, distancia, prioridad y puntuación.
- Flujo operativo del taller: aceptar, despachar, llegar, iniciar, completar o cancelar.
- Tracking del proveedor/técnico y consulta de ubicación/ruta para cliente, taller y plataforma.
- Historial operativo del incidente.

**Nivel de cumplimiento estimado del backend:** alto para el flujo principal técnico, aproximadamente **80% a 85%** del alcance backend.  
**Brechas principales para llegar a 100%:** módulo de pagos/comisiones, notificaciones push reales, comunicación cliente-taller, calificación posterior del servicio, módulo formal de métricas/reportes y endpoint móvil específico para técnicos autenticados.

---

## 2. Cumplimiento contra el examen

| Requisito del examen          |      Estado en backend | Evidencia técnica                                                   | Observación                                                        |
| ----------------------------- | ---------------------: | ------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Backend FastAPI               |                 Cumple | `app/main.py`, routers incluidos con prefijo `/api`                 | Correcto.                                                          |
| PostgreSQL                    |                 Cumple | SQLAlchemy + Alembic + `postgresql+psycopg`                         | Correcto.                                                          |
| Autenticación y autorización  |                 Cumple | JWT Bearer, roles, `require_roles`                                  | Falta refresh token, pero para el parcial puede defenderse.        |
| Usuarios                      |                 Cumple | `auth`, `users`                                                     | Registro, login y perfil.                                          |
| Talleres/proveedores          |                 Cumple | `providers`                                                         | Soporta taller y mecánico independiente.                           |
| Técnicos de taller            |         Cumple parcial | `providers/me/technicians`                                          | Técnicos son entidades del proveedor, pero no tienen login propio. |
| Vehículos                     |                 Cumple | `vehicles`                                                          | CRUD básico del cliente.                                           |
| Incidentes                    |                 Cumple | `incidents`                                                         | Flujo cliente/proveedor/plataforma.                                |
| Evidencias texto/audio/imagen |                 Cumple | `evidences`                                                         | Soporta texto y archivos con storage local/S3.                     |
| Procesamiento de audio        | Cumple si se configura | `faster_whisper_provider` + jobs                                    | Necesita worker Celery activo y dependencia instalada.             |
| Análisis de imágenes          | Cumple si se configura | `ultralytics_yolo_provider` + jobs                                  | Análisis básico con detecciones.                                   |
| Resumen/clasificación IA      | Cumple si se configura | `openrouter_provider` + summary job                                 | Si `LLM_PROVIDER=null`, devuelve placeholder.                      |
| Priorización                  |                 Cumple | campos `priority`, `suggested_priority`                             | Manual + sugerida por IA.                                          |
| Asignación inteligente        |                 Cumple | `assignment`                                                        | Candidatos por servicios, distancia, capacidad, prioridad, rating. |
| Geolocalización               |                 Cumple | `incident_latitude`, `base_latitude`, tracking, routing             | Correcto.                                                          |
| Ruta/ETA                      |         Cumple parcial | `tracking`, GraphHopper/fallback                                    | No hay mapa; sí datos para Flutter/Angular.                        |
| Trazabilidad/historial        |                 Cumple | `incident_operation_events`, jobs, estados                          | Correcto.                                                          |
| Notificaciones push           |                Parcial | contrato `PushNotificationProvider`, `NullPushNotificationProvider` | No hay Firebase/FCM real ni registro de device tokens.             |
| Pagos cliente                 |      No cumple todavía | No hay módulo de pagos                                              | El examen pide pagos desde app.                                    |
| Comisión 10% plataforma       |      No cumple todavía | No hay modelo de comisión/liquidación                               | Necesario si la defensa exige pagos.                               |
| Seguros/suscripciones         |        No implementado | No hay módulo                                                       | Está en apuntes como adicional.                                    |
| Comunicación cliente-taller   |        No implementado | No hay chat/mensajería                                              | El examen lo marca opcional.                                       |
| Métricas/reportes             |                Parcial | existen datos, no módulo formal                                     | Se puede defender como pendiente.                                  |

---

## 3. Arquitectura del backend

### 3.1 Stack técnico

- **Framework:** FastAPI.
- **Lenguaje:** Python 3.12.
- **Base de datos:** PostgreSQL.
- **ORM:** SQLAlchemy 2.
- **Migraciones:** Alembic.
- **Autenticación:** JWT Bearer con `PyJWT`.
- **Hash de contraseñas:** `pwdlib[argon2]`.
- **Procesamiento asíncrono:** Celery + Redis.
- **Storage:** local o S3.
- **IA / procesamiento multimodal:**
  - audio: `faster-whisper`,
  - visión: `ultralytics`,
  - LLM: OpenRouter,
  - rutas: GraphHopper o fallback Haversine.

### 3.2 Módulos principales

| Módulo       | Responsabilidad                                                         |
| ------------ | ----------------------------------------------------------------------- |
| `auth`       | Registro, login, perfil autenticado, emisión de token.                  |
| `users`      | Perfil propio y administración de usuarios.                             |
| `providers`  | Talleres, mecánicos independientes y técnicos.                          |
| `catalog`    | Catálogo maestro de servicios y servicios ofrecidos por cada proveedor. |
| `vehicles`   | Vehículos del cliente.                                                  |
| `incidents`  | Solicitudes de emergencia.                                              |
| `evidences`  | Evidencias de texto, imagen y audio.                                    |
| `jobs`       | Jobs asíncronos de IA y procesamiento.                                  |
| `assignment` | Publicación del incidente y generación de candidatos.                   |
| `operations` | Estados operativos del servicio.                                        |
| `tracking`   | Ubicación, ruta, ETA e historial de pings.                              |
| `system`     | Salud, readiness e info del backend.                                    |

---

## 4. Contrato general de API para Flutter y Angular

### 4.1 Base URL

En local:

```http
http://localhost:8000
```

Prefijo de API:

```http
/api
```

Ejemplo:

```http
GET http://localhost:8000/api/system/health
```

Documentación Swagger:

```http
http://localhost:8000/docs
```

OpenAPI JSON:

```http
http://localhost:8000/openapi.json
```

### 4.2 Headers comunes

Para endpoints protegidos:

```http
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

Para subida de archivos:

```http
Authorization: Bearer {{clientToken}}
Content-Type: multipart/form-data
```

### 4.3 Formato estándar de respuesta exitosa

```json
{
  "success": true,
  "message": "Mensaje descriptivo.",
  "data": {},
  "meta": null
}
```

### 4.4 Formato estándar de error

```json
{
  "success": false,
  "message": "Validation error.",
  "error": {
    "code": "validation_error",
    "details": []
  }
}
```

Códigos de error comunes:

| HTTP | Código interno          | Cuándo ocurre                                    |
| ---: | ----------------------- | ------------------------------------------------ |
|  401 | `unauthorized`          | Token ausente, inválido o expirado.              |
|  403 | `forbidden`             | Rol incorrecto o recurso ajeno.                  |
|  404 | `not_found`             | Recurso inexistente.                             |
|  409 | `conflict`              | Regla de negocio incumplida.                     |
|  422 | `validation_error`      | Body inválido.                                   |
|  503 | `service_unavailable`   | Proveedor externo/IA/ruta/storage no disponible. |
|  500 | `internal_server_error` | Error no controlado.                             |

---

## 5. Roles y responsabilidades de integración

| Rol              | Aplicación principal                       | Qué puede hacer                                                                                                          |
| ---------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `CLIENT`         | Flutter cliente                            | Registrarse, crear vehículos, crear incidentes, subir evidencias, cancelar incidente, ver tracking.                      |
| `PROVIDER_ADMIN` | Angular talleres / posible Flutter técnico | Registrar/configurar taller, servicios, técnicos, ver candidatos, aceptar/rechazar, operar servicio, reportar ubicación. |
| `PLATFORM_ADMIN` | Angular admin/backoffice                   | Administrar catálogo, proveedores, usuarios, jobs, publicación de incidentes y monitoreo.                                |
| `TECHNICIAN`     | Pendiente                                  | El rol existe, pero el flujo actual opera desde `PROVIDER_ADMIN`; no hay endpoints propios del técnico autenticado.      |

---

## 6. Variables sugeridas para Postman

Crea un Environment llamado `mechanic-local`:

| Variable               | Valor inicial                 |
| ---------------------- | ----------------------------- |
| `baseUrl`              | `http://localhost:8000/api`   |
| `rootUrl`              | `http://localhost:8000`       |
| `adminEmail`           | `admin@mechanic.local`        |
| `adminPassword`        | `Admin12345`                  |
| `adminToken`           | vacío                         |
| `clientEmail`          | `cliente.demo@mechanic.local` |
| `clientPassword`       | `Cliente12345`                |
| `clientToken`          | vacío                         |
| `providerEmail`        | `taller.demo@mechanic.local`  |
| `providerPassword`     | `Taller12345`                 |
| `providerToken`        | vacío                         |
| `clientUserId`         | vacío                         |
| `providerUserId`       | vacío                         |
| `providerId`           | vacío                         |
| `technicianId`         | vacío                         |
| `serviceCatalogItemId` | vacío                         |
| `providerServiceId`    | vacío                         |
| `vehicleId`            | vacío                         |
| `incidentId`           | vacío                         |
| `textEvidenceId`       | vacío                         |
| `imageEvidenceId`      | vacío                         |
| `audioEvidenceId`      | vacío                         |
| `jobId`                | vacío                         |
| `candidateId`          | vacío                         |

Script genérico de test para casi todos los requests JSON:

```javascript
pm.test("Status 2xx", function () {
  pm.expect(pm.response.code).to.be.within(200, 299);
});

pm.test("Respuesta success=true", function () {
  const json = pm.response.json();
  pm.expect(json.success).to.eql(true);
});
```

---

# 7. Flujo principal completo de pruebas en Postman

## Paso 0. Verificar salud del backend

### 0.1 Health

```http
GET {{baseUrl}}/system/health
```

Debe devolver `success=true`.

### 0.2 Readiness

```http
GET {{baseUrl}}/system/readiness
```

Valida conexión con PostgreSQL y Redis.

### 0.3 Info de integraciones

```http
GET {{baseUrl}}/system/info
```

Sirve para verificar si están activos `llm_provider`, `vision_provider`, `speech_to_text_provider`, `routing_provider`, `push_provider`.

---

## Paso 1. Login del administrador de plataforma

```http
POST {{baseUrl}}/auth/login
Content-Type: application/json
```

Body:

```json
{
  "email": "{{adminEmail}}",
  "password": "{{adminPassword}}"
}
```

Test para guardar token:

```javascript
const json = pm.response.json();
pm.environment.set("adminToken", json.data.access_token);
pm.environment.set("adminUserId", json.data.user.id);
```

---

## Paso 2. Registrar cliente móvil

```http
POST {{baseUrl}}/auth/register
Content-Type: application/json
```

Body:

```json
{
  "account_type": "CLIENT",
  "email": "{{clientEmail}}",
  "password": "{{clientPassword}}",
  "first_name": "Juan",
  "last_name": "Cliente",
  "phone_number": "70000011"
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("clientToken", json.data.access_token);
pm.environment.set("clientUserId", json.data.user.id);
```

---

## Paso 3. Registrar taller o mecánico independiente

Opción recomendada para el flujo normal: registro público como proveedor.

```http
POST {{baseUrl}}/auth/register
Content-Type: application/json
```

Body taller:

```json
{
  "account_type": "WORKSHOP",
  "email": "{{providerEmail}}",
  "password": "{{providerPassword}}",
  "first_name": "Mario",
  "last_name": "Taller",
  "phone_number": "70000022",
  "provider_profile": {
    "business_name": "Taller Demo Express",
    "legal_name": "Taller Demo Express SRL",
    "description": "Taller con servicio móvil de emergencia vehicular.",
    "contact_email": "contacto@tallerdemo.local",
    "contact_phone": "70000023",
    "city": "Santa Cruz",
    "address": "Av. Demo #123",
    "base_latitude": -17.7833,
    "base_longitude": -63.1821,
    "max_concurrent_services": 3
  }
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("providerToken", json.data.access_token);
pm.environment.set("providerUserId", json.data.user.id);
```

---

## Paso 4. Obtener perfil del taller y guardar `providerId`

```http
GET {{baseUrl}}/providers/me/profile
Authorization: Bearer {{providerToken}}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("providerId", json.data.id);
```

---

## Paso 5. Crear técnico del taller

```http
POST {{baseUrl}}/providers/me/technicians
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "first_name": "Carlos",
  "last_name": "Mecánico",
  "phone_number": "70000024",
  "specialty": "Auxilio eléctrico y llantas",
  "is_available": true,
  "current_latitude": -17.782,
  "current_longitude": -63.18
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("technicianId", json.data.id);
```

---

## Paso 6. Configurar servicios que ofrece el taller

Primero listar catálogo disponible para el proveedor:

```http
GET {{baseUrl}}/catalog/me/services/catalog
Authorization: Bearer {{providerToken}}
```

Test para guardar el primer servicio del catálogo:

```javascript
const json = pm.response.json();
pm.environment.set("serviceCatalogItemId", json.data[0].catalog_item.id);
```

Luego configurar un servicio para el taller:

```http
POST {{baseUrl}}/catalog/me/services
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "service_catalog_item_id": "{{serviceCatalogItemId}}",
  "custom_title": "Auxilio mecánico móvil",
  "custom_description": "Servicio disponible para emergencias en la ciudad.",
  "price_estimate_min": 80,
  "price_estimate_max": 250,
  "estimated_duration_minutes": 45,
  "is_mobile_service_enabled": true,
  "is_emergency_service_enabled": true,
  "is_active": true
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("providerServiceId", json.data.id);
```

**Importante:** para que la asignación genere candidatos, el proveedor debe tener servicios activos compatibles con la categoría del incidente. Para accidente con grúa, conviene que el taller configure `ACCIDENT_SUPPORT` y/o `TOWING`.

---

## Paso 7. Crear vehículo del cliente

```http
POST {{baseUrl}}/vehicles
Authorization: Bearer {{clientToken}}
Content-Type: application/json
```

Body:

```json
{
  "plate_number": "ABC1234",
  "vehicle_type": "CAR",
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015,
  "color": "Blanco",
  "notes": "Vehículo de prueba para emergencia."
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("vehicleId", json.data.id);
```

---

## Paso 8. Crear incidente del cliente

```http
POST {{baseUrl}}/incidents
Authorization: Bearer {{clientToken}}
Content-Type: application/json
```

Body ejemplo problema de batería:

```json
{
  "vehicle_id": "{{vehicleId}}",
  "reported_category": "BATTERY",
  "priority": "MEDIUM",
  "title": "Mi auto no enciende",
  "description": "Estoy en un estacionamiento y el vehículo no responde al intentar arrancar.",
  "incident_latitude": -17.7863,
  "incident_longitude": -63.1812,
  "address_reference": "Estacionamiento cerca del centro"
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("incidentId", json.data.id);
```

Estados esperados inicialmente:

```text
PENDING
```

---

## Paso 9. Agregar evidencia de texto

```http
POST {{baseUrl}}/evidences/client/incidents/{{incidentId}}/text
Authorization: Bearer {{clientToken}}
Content-Type: application/json
```

Body:

```json
{
  "description": "Detalle adicional escrito por el cliente.",
  "text_content": "El vehículo no enciende, parece batería descargada. Las luces del tablero se ven débiles.",
  "evidence_type": "TEXT"
}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("textEvidenceId", json.data.id);
```

Este endpoint dispara automáticamente un job de resumen del incidente.

---

## Paso 10. Agregar evidencia de imagen

```http
POST {{baseUrl}}/evidences/client/incidents/{{incidentId}}/files
Authorization: Bearer {{clientToken}}
Content-Type: multipart/form-data
```

Form-data:

| Key             | Tipo | Valor                         |
| --------------- | ---- | ----------------------------- |
| `evidence_type` | Text | `IMAGE`                       |
| `description`   | Text | `Foto del tablero o vehículo` |
| `upload_file`   | File | seleccionar `.jpg` o `.png`   |

Test:

```javascript
const json = pm.response.json();
pm.environment.set("imageEvidenceId", json.data.id);
```

Este endpoint dispara automáticamente un job de análisis de imagen.

---

## Paso 11. Agregar evidencia de audio

```http
POST {{baseUrl}}/evidences/client/incidents/{{incidentId}}/files
Authorization: Bearer {{clientToken}}
Content-Type: multipart/form-data
```

Form-data:

| Key             | Tipo | Valor                              |
| --------------- | ---- | ---------------------------------- |
| `evidence_type` | Text | `AUDIO`                            |
| `description`   | Text | `Audio describiendo el problema`   |
| `upload_file`   | File | seleccionar `.mp3`, `.wav`, `.m4a` |

Test:

```javascript
const json = pm.response.json();
pm.environment.set("audioEvidenceId", json.data.id);
```

Este endpoint dispara automáticamente un job de transcripción de audio.

---

## Paso 12. Revisar jobs de IA como administrador

```http
GET {{baseUrl}}/jobs?limit=20&offset=0
Authorization: Bearer {{adminToken}}
```

Para ver un job específico:

```http
GET {{baseUrl}}/jobs/{{jobId}}
Authorization: Bearer {{adminToken}}
```

Estados posibles del job:

```text
PENDING
RUNNING
SUCCEEDED
FAILED
```

Si los providers están en `null`, los jobs pueden generar resultados placeholder. Si están configurados correctamente, deben guardar transcripción, análisis visual o resumen estructurado.

---

## Paso 13. Ver incidente enriquecido por IA

Cliente:

```http
GET {{baseUrl}}/incidents/me/{{incidentId}}
Authorization: Bearer {{clientToken}}
```

Admin:

```http
GET {{baseUrl}}/incidents/{{incidentId}}
Authorization: Bearer {{adminToken}}
```

Campos importantes para Flutter/Angular:

```json
{
  "status": "PENDING",
  "reported_category": "BATTERY",
  "priority": "MEDIUM",
  "ai_summary_status": "SUCCEEDED",
  "structured_summary": "...",
  "suggested_category": "BATTERY",
  "suggested_priority": "MEDIUM",
  "requires_more_information": false
}
```

---

## Paso 14. Publicar incidente para asignación

Lo hace plataforma/admin:

```http
POST {{baseUrl}}/assignment/platform/incidents/{{incidentId}}/publish
Authorization: Bearer {{adminToken}}
```

Respuesta esperada:

```json
{
  "success": true,
  "data": {
    "incident_id": "...",
    "incident_status": "PUBLISHED",
    "used_category": "BATTERY",
    "used_priority": "MEDIUM",
    "required_service_codes": ["BATTERY_JUMPSTART"],
    "published_candidates_count": 1,
    "recommended_candidate_id": null,
    "recommended_provider_id": "..."
  }
}
```

**Observación técnica:** actualmente `recommended_candidate_id` puede venir `null`; para obtener el ID real del candidato usa el siguiente paso.

---

## Paso 15. Listar candidatos desde plataforma

```http
GET {{baseUrl}}/assignment/platform/incidents/{{incidentId}}/candidates
Authorization: Bearer {{adminToken}}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("candidateId", json.data[0].id);
pm.environment.set("providerId", json.data[0].provider_id);
```

---

## Paso 16. Taller lista solicitudes disponibles

```http
GET {{baseUrl}}/assignment/provider/me/available
Authorization: Bearer {{providerToken}}
```

Test:

```javascript
const json = pm.response.json();
pm.environment.set("candidateId", json.data[0].id);
```

---

## Paso 17. Taller acepta la solicitud

```http
POST {{baseUrl}}/assignment/provider/me/available/{{candidateId}}/accept
Authorization: Bearer {{providerToken}}
```

Respuesta esperada:

```json
{
  "candidate_status": "ACCEPTED",
  "incident_status": "ASSIGNED",
  "assigned_provider_id": "...",
  "assigned_at": "..."
}
```

Si otro taller acepta primero, este endpoint debe responder conflicto.

---

## Paso 18. Taller ve operaciones activas

```http
GET {{baseUrl}}/operations/provider/me/active
Authorization: Bearer {{providerToken}}
```

---

## Paso 19. Taller despacha técnico

```http
POST {{baseUrl}}/operations/provider/incidents/{{incidentId}}/dispatch
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "technician_id": "{{technicianId}}",
  "note": "Se despacha técnico disponible hacia la ubicación del cliente."
}
```

Estado esperado:

```text
EN_ROUTE
```

---

## Paso 20. Proveedor/técnico reporta ubicación

```http
POST {{baseUrl}}/tracking/provider/incidents/{{incidentId}}/location
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "latitude": -17.784,
  "longitude": -63.1805,
  "accuracy_meters": 12,
  "technician_id": "{{technicianId}}"
}
```

Este endpoint guarda ping de ubicación y recalcula ruta/ETA si hay coordenadas suficientes.

---

## Paso 21. Cliente consulta tracking en vivo

```http
GET {{baseUrl}}/tracking/client/incidents/{{incidentId}}/live
Authorization: Bearer {{clientToken}}
```

Flutter debe usar esta respuesta para pintar:

- estado del incidente,
- ubicación del incidente,
- última ubicación del técnico/proveedor,
- ETA,
- distancia,
- polyline si GraphHopper está configurado.

---

## Paso 22. Taller marca llegada

```http
POST {{baseUrl}}/operations/provider/incidents/{{incidentId}}/arrive
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "note": "El técnico llegó al lugar."
}
```

Estado esperado:

```text
ON_SITE
```

---

## Paso 23. Taller inicia servicio

```http
POST {{baseUrl}}/operations/provider/incidents/{{incidentId}}/start
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "note": "Se inicia revisión del vehículo."
}
```

Estado esperado:

```text
IN_PROGRESS
```

---

## Paso 24. Taller completa servicio

```http
POST {{baseUrl}}/operations/provider/incidents/{{incidentId}}/complete
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "note": "Servicio finalizado correctamente.",
  "completion_summary": "Se realizó auxilio de batería y el vehículo encendió."
}
```

Estado esperado:

```text
COMPLETED
```

---

## Paso 25. Ver historial operativo

Proveedor:

```http
GET {{baseUrl}}/operations/provider/incidents/{{incidentId}}/history
Authorization: Bearer {{providerToken}}
```

Plataforma:

```http
GET {{baseUrl}}/operations/platform/incidents/{{incidentId}}/history
Authorization: Bearer {{adminToken}}
```

---

## Paso 26. Cliente verifica incidente final

```http
GET {{baseUrl}}/incidents/me/{{incidentId}}
Authorization: Bearer {{clientToken}}
```

Debe mostrar estado:

```text
COMPLETED
```

---

# 8. Flujos alternativos importantes

## 8.1 Taller rechaza solicitud

```http
POST {{baseUrl}}/assignment/provider/me/available/{{candidateId}}/reject
Authorization: Bearer {{providerToken}}
```

El candidato queda en:

```text
REJECTED
```

## 8.2 Cliente cancela incidente

```http
POST {{baseUrl}}/incidents/me/{{incidentId}}/cancel
Authorization: Bearer {{clientToken}}
```

Debe usarse antes de que el flujo esté demasiado avanzado.

## 8.3 Taller cancela servicio

```http
POST {{baseUrl}}/operations/provider/incidents/{{incidentId}}/cancel
Authorization: Bearer {{providerToken}}
Content-Type: application/json
```

Body:

```json
{
  "note": "No se pudo atender por causa justificada."
}
```

## 8.4 Admin crea proveedor manualmente

```http
POST {{baseUrl}}/providers/onboarding
Authorization: Bearer {{adminToken}}
Content-Type: application/json
```

Body:

```json
{
  "admin_user": {
    "email": "admin.taller2@mechanic.local",
    "password": "Taller12345",
    "first_name": "Admin",
    "last_name": "Taller Dos",
    "phone_number": "70000033"
  },
  "provider": {
    "provider_type": "WORKSHOP",
    "business_name": "Taller Dos",
    "legal_name": "Taller Dos SRL",
    "description": "Taller con grúa y auxilio móvil.",
    "contact_email": "contacto@tallerdos.local",
    "contact_phone": "70000034",
    "city": "Santa Cruz",
    "address": "Av. Segunda #456",
    "base_latitude": -17.79,
    "base_longitude": -63.19,
    "max_concurrent_services": 5
  }
}
```

---

# 9. Tabla completa de endpoints disponibles

### System / salud

| Método | Endpoint                | Rol       | Body/Schema | Uso         |
| ------ | ----------------------- | --------- | ----------- | ----------- |
| `GET`  | `/api/system/health`    | `Público` | `-`         | `health`    |
| `GET`  | `/api/system/readiness` | `Público` | `-`         | `readiness` |
| `GET`  | `/api/system/info`      | `Público` | `-`         | `info`      |

### Autenticación

| Método | Endpoint             | Rol           | Body/Schema       | Uso                              |
| ------ | -------------------- | ------------- | ----------------- | -------------------------------- |
| `POST` | `/api/auth/register` | `Público`     | `RegisterRequest` | `register`                       |
| `POST` | `/api/auth/login`    | `Público`     | `LoginRequest`    | `login`                          |
| `GET`  | `/api/auth/me`       | `Autenticado` | `-`               | `get_authenticated_user_profile` |

### Usuarios

| Método  | Endpoint                | Rol              | Body/Schema               | Uso                  |
| ------- | ----------------------- | ---------------- | ------------------------- | -------------------- |
| `GET`   | `/api/users/me/profile` | `Autenticado`    | `-`                       | `get_own_profile`    |
| `PATCH` | `/api/users/me/profile` | `Autenticado`    | `UpdateOwnProfileRequest` | `update_own_profile` |
| `GET`   | `/api/users`            | `PLATFORM_ADMIN` | `-`                       | `list_users`         |
| `GET`   | `/api/users/{user_id}`  | `PLATFORM_ADMIN` | `-`                       | `get_user_by_id`     |

### Talleres / mecánicos / técnicos

| Método  | Endpoint                                                   | Rol              | Body/Schema                       | Uso                          |
| ------- | ---------------------------------------------------------- | ---------------- | --------------------------------- | ---------------------------- |
| `POST`  | `/api/providers/onboarding`                                | `PLATFORM_ADMIN` | `ProviderOnboardingRequest`       | `onboard_provider`           |
| `GET`   | `/api/providers`                                           | `PLATFORM_ADMIN` | `-`                               | `list_providers`             |
| `GET`   | `/api/providers/{provider_id}`                             | `PLATFORM_ADMIN` | `-`                               | `get_provider_by_id`         |
| `PATCH` | `/api/providers/{provider_id}/operations`                  | `PLATFORM_ADMIN` | `UpdateProviderOperationsRequest` | `update_provider_operations` |
| `GET`   | `/api/providers/me/profile`                                | `PROVIDER_ADMIN` | `-`                               | `get_my_provider`            |
| `PATCH` | `/api/providers/me/profile`                                | `PROVIDER_ADMIN` | `UpdateOwnProviderRequest`        | `update_my_provider`         |
| `GET`   | `/api/providers/me/technicians`                            | `PROVIDER_ADMIN` | `-`                               | `list_my_technicians`        |
| `POST`  | `/api/providers/me/technicians`                            | `PROVIDER_ADMIN` | `CreateTechnicianRequest`         | `create_my_technician`       |
| `PATCH` | `/api/providers/me/technicians/{technician_id}`            | `PROVIDER_ADMIN` | `UpdateTechnicianRequest`         | `update_my_technician`       |
| `GET`   | `/api/providers/{provider_id}/technicians`                 | `PLATFORM_ADMIN` | `-`                               | `list_provider_technicians`  |
| `POST`  | `/api/providers/{provider_id}/technicians`                 | `PLATFORM_ADMIN` | `CreateTechnicianRequest`         | `create_provider_technician` |
| `PATCH` | `/api/providers/{provider_id}/technicians/{technician_id}` | `PLATFORM_ADMIN` | `UpdateTechnicianRequest`         | `update_provider_technician` |

### Catálogo de servicios

| Método  | Endpoint                                          | Rol              | Body/Schema                       | Uso                                   |
| ------- | ------------------------------------------------- | ---------------- | --------------------------------- | ------------------------------------- |
| `POST`  | `/api/catalog/services`                           | `PLATFORM_ADMIN` | `CreateServiceCatalogItemRequest` | `create_service_catalog_item`         |
| `GET`   | `/api/catalog/services`                           | `PLATFORM_ADMIN` | `-`                               | `list_service_catalog_items`          |
| `GET`   | `/api/catalog/services/{service_catalog_item_id}` | `PLATFORM_ADMIN` | `-`                               | `get_service_catalog_item_by_id`      |
| `PATCH` | `/api/catalog/services/{service_catalog_item_id}` | `PLATFORM_ADMIN` | `UpdateServiceCatalogItemRequest` | `update_service_catalog_item`         |
| `GET`   | `/api/catalog/providers/{provider_id}/services`   | `PLATFORM_ADMIN` | `-`                               | `list_provider_services_for_platform` |
| `GET`   | `/api/catalog/me/services/catalog`                | `PROVIDER_ADMIN` | `-`                               | `list_my_catalog_with_configuration`  |
| `GET`   | `/api/catalog/me/services`                        | `PROVIDER_ADMIN` | `-`                               | `list_my_provider_services`           |
| `POST`  | `/api/catalog/me/services`                        | `PROVIDER_ADMIN` | `UpsertProviderServiceRequest`    | `upsert_my_provider_service`          |
| `PATCH` | `/api/catalog/me/services/{provider_service_id}`  | `PROVIDER_ADMIN` | `UpdateProviderServiceRequest`    | `update_my_provider_service`          |

### Vehículos

| Método  | Endpoint                     | Rol      | Body/Schema               | Uso                  |
| ------- | ---------------------------- | -------- | ------------------------- | -------------------- |
| `POST`  | `/api/vehicles`              | `CLIENT` | `CreateVehicleRequest`    | `create_own_vehicle` |
| `GET`   | `/api/vehicles`              | `CLIENT` | `-`                       | `list_own_vehicles`  |
| `GET`   | `/api/vehicles/{vehicle_id}` | `CLIENT` | `-`                       | `get_own_vehicle`    |
| `PATCH` | `/api/vehicles/{vehicle_id}` | `CLIENT` | `UpdateOwnVehicleRequest` | `update_own_vehicle` |

### Incidentes

| Método  | Endpoint                                   | Rol              | Body/Schema                       | Uso                               |
| ------- | ------------------------------------------ | ---------------- | --------------------------------- | --------------------------------- |
| `POST`  | `/api/incidents`                           | `CLIENT`         | `CreateIncidentRequest`           | `create_own_incident`             |
| `GET`   | `/api/incidents/me`                        | `CLIENT`         | `-`                               | `list_own_incidents`              |
| `GET`   | `/api/incidents/me/{incident_id}`          | `CLIENT`         | `-`                               | `get_own_incident`                |
| `PATCH` | `/api/incidents/me/{incident_id}`          | `CLIENT`         | `UpdateOwnPendingIncidentRequest` | `update_own_pending_incident`     |
| `POST`  | `/api/incidents/me/{incident_id}/cancel`   | `CLIENT`         | `-`                               | `cancel_own_incident`             |
| `GET`   | `/api/incidents`                           | `PLATFORM_ADMIN` | `-`                               | `list_all_incidents`              |
| `GET`   | `/api/incidents/{incident_id}`             | `PLATFORM_ADMIN` | `-`                               | `get_incident_by_id_for_platform` |
| `GET`   | `/api/incidents/provider/me`               | `PROVIDER_ADMIN` | `-`                               | `list_provider_incidents`         |
| `GET`   | `/api/incidents/provider/me/{incident_id}` | `PROVIDER_ADMIN` | `-`                               | `get_provider_incident`           |

### Evidencias

| Método | Endpoint                                              | Rol              | Body/Schema                 | Uso                                       |
| ------ | ----------------------------------------------------- | ---------------- | --------------------------- | ----------------------------------------- |
| `POST` | `/api/evidences/client/incidents/{incident_id}/files` | `CLIENT`         | `-`                         | `upload_incident_file_evidence_as_client` |
| `POST` | `/api/evidences/client/incidents/{incident_id}/text`  | `CLIENT`         | `CreateTextEvidenceRequest` | `create_incident_text_evidence_as_client` |
| `GET`  | `/api/evidences/client/incidents/{incident_id}`       | `CLIENT`         | `-`                         | `list_client_incident_evidences`          |
| `GET`  | `/api/evidences/provider/incidents/{incident_id}`     | `PROVIDER_ADMIN` | `-`                         | `list_provider_incident_evidences`        |
| `GET`  | `/api/evidences/platform/incidents/{incident_id}`     | `PLATFORM_ADMIN` | `-`                         | `list_platform_incident_evidences`        |
| `GET`  | `/api/evidences/{evidence_id}/download`               | `Público`        | `-`                         | ``                                        |

### Jobs / procesamiento IA

| Método | Endpoint                                                        | Rol              | Body/Schema             | Uso                               |
| ------ | --------------------------------------------------------------- | ---------------- | ----------------------- | --------------------------------- |
| `POST` | `/api/jobs/demo/enqueue`                                        | `PLATFORM_ADMIN` | `DemoJobEnqueueRequest` | `enqueue_demo_job`                |
| `POST` | `/api/jobs/evidences/{evidence_id}/audio-transcription/enqueue` | `PLATFORM_ADMIN` | `-`                     | `enqueue_audio_transcription_job` |
| `POST` | `/api/jobs/evidences/{evidence_id}/image-analysis/enqueue`      | `PLATFORM_ADMIN` | `-`                     | `enqueue_image_analysis_job`      |
| `POST` | `/api/jobs/incidents/{incident_id}/summary/enqueue`             | `PLATFORM_ADMIN` | `-`                     | `enqueue_incident_summary_job`    |
| `GET`  | `/api/jobs`                                                     | `PLATFORM_ADMIN` | `-`                     | `list_jobs`                       |
| `GET`  | `/api/jobs/{job_id}`                                            | `PLATFORM_ADMIN` | `-`                     | `get_job_by_id`                   |

### Asignación inteligente

| Método | Endpoint                                                      | Rol              | Body/Schema | Uso                                     |
| ------ | ------------------------------------------------------------- | ---------------- | ----------- | --------------------------------------- |
| `POST` | `/api/assignment/platform/incidents/{incident_id}/publish`    | `PLATFORM_ADMIN` | `-`         | `publish_incident_for_assignment`       |
| `GET`  | `/api/assignment/platform/incidents/{incident_id}/candidates` | `PLATFORM_ADMIN` | `-`         | `list_platform_candidates_for_incident` |
| `GET`  | `/api/assignment/provider/me/available`                       | `PROVIDER_ADMIN` | `-`         | `list_my_available_candidates`          |
| `GET`  | `/api/assignment/provider/me/available/{candidate_id}`        | `PROVIDER_ADMIN` | `-`         | `get_my_available_candidate`            |
| `POST` | `/api/assignment/provider/me/available/{candidate_id}/accept` | `PROVIDER_ADMIN` | `-`         | `accept_my_candidate`                   |
| `POST` | `/api/assignment/provider/me/available/{candidate_id}/reject` | `PROVIDER_ADMIN` | `-`         | `reject_my_candidate`                   |

### Operación del servicio

| Método | Endpoint                                                    | Rol              | Body/Schema               | Uso                               |
| ------ | ----------------------------------------------------------- | ---------------- | ------------------------- | --------------------------------- |
| `GET`  | `/api/operations/provider/me/active`                        | `PROVIDER_ADMIN` | `-`                       | `list_my_active_operations`       |
| `GET`  | `/api/operations/provider/incidents/{incident_id}/state`    | `PROVIDER_ADMIN` | `-`                       | `get_my_operation_state`          |
| `POST` | `/api/operations/provider/incidents/{incident_id}/dispatch` | `PROVIDER_ADMIN` | `DispatchIncidentRequest` | `dispatch_my_incident`            |
| `POST` | `/api/operations/provider/incidents/{incident_id}/arrive`   | `PROVIDER_ADMIN` | `OperationNoteRequest`    | `mark_my_arrival`                 |
| `POST` | `/api/operations/provider/incidents/{incident_id}/start`    | `PROVIDER_ADMIN` | `OperationNoteRequest`    | `start_my_service`                |
| `POST` | `/api/operations/provider/incidents/{incident_id}/complete` | `PROVIDER_ADMIN` | `CompleteIncidentRequest` | `complete_my_service`             |
| `POST` | `/api/operations/provider/incidents/{incident_id}/cancel`   | `PROVIDER_ADMIN` | `OperationNoteRequest`    | `cancel_my_service`               |
| `GET`  | `/api/operations/provider/incidents/{incident_id}/history`  | `PROVIDER_ADMIN` | `-`                       | `list_my_operation_history`       |
| `GET`  | `/api/operations/platform/incidents/{incident_id}/history`  | `PLATFORM_ADMIN` | `-`                       | `list_platform_operation_history` |

### Tracking y rutas

| Método | Endpoint                                                       | Rol              | Body/Schema           | Uso                              |
| ------ | -------------------------------------------------------------- | ---------------- | --------------------- | -------------------------------- |
| `POST` | `/api/tracking/provider/incidents/{incident_id}/location`      | `PROVIDER_ADMIN` | `LocationPingRequest` | `report_my_location`             |
| `POST` | `/api/tracking/provider/incidents/{incident_id}/refresh-route` | `PROVIDER_ADMIN` | `-`                   | `refresh_my_route`               |
| `GET`  | `/api/tracking/provider/incidents/{incident_id}/live`          | `PROVIDER_ADMIN` | `-`                   | `get_provider_live_tracking`     |
| `GET`  | `/api/tracking/provider/incidents/{incident_id}/history`       | `PROVIDER_ADMIN` | `-`                   | `list_provider_tracking_history` |
| `GET`  | `/api/tracking/client/incidents/{incident_id}/live`            | `CLIENT`         | `-`                   | `get_client_live_tracking`       |
| `GET`  | `/api/tracking/client/incidents/{incident_id}/history`         | `CLIENT`         | `-`                   | `list_client_tracking_history`   |
| `GET`  | `/api/tracking/platform/incidents/{incident_id}/live`          | `PLATFORM_ADMIN` | `-`                   | `get_platform_live_tracking`     |
| `GET`  | `/api/tracking/platform/incidents/{incident_id}/history`       | `PLATFORM_ADMIN` | `-`                   | `list_platform_tracking_history` |

---

# 10. Recomendaciones para Flutter

## 10.1 Pantallas mínimas del cliente móvil

1. Login/registro.
2. Mis vehículos.
3. Crear vehículo.
4. Reportar emergencia.
5. Adjuntar evidencia:
   - texto,
   - foto,
   - audio,
   - ubicación.
6. Estado de solicitud.
7. Tracking en mapa.
8. Historial de solicitudes.
9. Pantalla de pago: **pendiente de backend**.
10. Calificación del servicio: **pendiente de backend**.

## 10.2 Flujo Flutter recomendado

```text
Login/Register
  -> guardar access_token seguro
  -> crear/listar vehículos
  -> crear incidente
  -> subir evidencias
  -> consultar incidente
  -> consultar tracking live cada 5-10 segundos
  -> mostrar estado PENDING/PUBLISHED/ASSIGNED/EN_ROUTE/ON_SITE/IN_PROGRESS/COMPLETED
```

## 10.3 Manejo de tokens

- Guardar `access_token` en almacenamiento seguro.
- Enviar `Authorization: Bearer <token>`.
- Si responde 401, redirigir a login.
- El backend actual no implementa refresh token; cuando expire el token, el frontend debe pedir login nuevamente.

---

# 11. Recomendaciones para Angular

## 11.1 Panel de taller

Pantallas mínimas:

1. Login del taller.
2. Perfil del proveedor.
3. Gestión de técnicos.
4. Catálogo de servicios ofrecidos.
5. Solicitudes disponibles.
6. Detalle estructurado del incidente.
7. Aceptar/rechazar.
8. Operación activa:
   - despachar,
   - llegada,
   - iniciar,
   - completar/cancelar.
9. Tracking / mapa.
10. Historial de atenciones.

## 11.2 Panel de plataforma/admin

Pantallas mínimas:

1. Login admin.
2. Dashboard de salud del sistema.
3. Usuarios.
4. Proveedores.
5. Catálogo global de servicios.
6. Incidentes.
7. Evidencias.
8. Jobs IA.
9. Publicar incidente y ver candidatos.
10. Historial operativo y tracking.

---

# 12. Datos importantes para mostrar en UI

## Incidente

Mostrar:

- `title`
- `description`
- `status`
- `priority`
- `reported_category`
- `suggested_category`
- `suggested_priority`
- `structured_summary`
- `requires_more_information`
- `vehicle`
- `provider`
- `assigned_technician`
- `incident_latitude`
- `incident_longitude`
- `address_reference`
- fechas de estado

## Taller/proveedor candidato

Mostrar:

- `business_name`
- `provider_type`
- `average_rating`
- `available_capacity`
- `available_technicians_count`
- `distance_km`
- `matched_services`
- `score`
- `rationale`

## Tracking

Mostrar:

- ubicación del incidente,
- última ubicación del técnico/proveedor,
- distancia en km,
- ETA en minutos,
- polyline si existe,
- fecha de último cálculo.

---

# 13. Configuración de proveedores externos

## 13.1 Modo demo/sin servicios externos

Usar:

```env
SPEECH_TO_TEXT_PROVIDER=null
VISION_PROVIDER=null
LLM_PROVIDER=null
ROUTING_PROVIDER=null
PUSH_PROVIDER=null
STORAGE_PROVIDER=local
```

Ventaja: corre sin claves externas.  
Desventaja: IA y push serán resultados placeholder.

## 13.2 Modo con OpenRouter

```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=tu_api_key
OPENROUTER_API_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openrouter/auto
OPENROUTER_TEMPERATURE=0.2
OPENROUTER_MAX_TOKENS=350
OPENROUTER_TIMEOUT_SECONDS=120
```

## 13.3 Modo con GraphHopper

```env
ROUTING_PROVIDER=graphhopper
GRAPHHOPPER_API_KEY=tu_api_key
GRAPHHOPPER_PROFILE=car
```

## 13.4 Modo con Whisper local

```env
SPEECH_TO_TEXT_PROVIDER=faster_whisper
FASTER_WHISPER_MODEL_SIZE=small
FASTER_WHISPER_DEVICE=cpu
FASTER_WHISPER_COMPUTE_TYPE=int8
```

## 13.5 Modo con YOLO

```env
VISION_PROVIDER=ultralytics_yolo
ULTRALYTICS_YOLO_MODEL=yolo11n.pt
ULTRALYTICS_YOLO_DEVICE=cpu
```

---

# 14. Brechas que deben resolverse antes de una versión completa

## 14.1 Pagos y comisión

El examen indica que el cliente debe pagar desde la app y que el taller debe pagar 10% de comisión a la plataforma. El backend actual no tiene:

- tabla de pagos,
- tabla de transacciones,
- comisión de plataforma,
- recibo/factura,
- estado de pago,
- integración QR/pasarela,
- endpoint de confirmación de pago.

Recomendación mínima para defensa:

```text
payments
  - Payment
  - PaymentIntent
  - PlatformCommission
  - endpoints:
    POST /payments/incidents/{incident_id}/simulate
    GET /payments/incidents/{incident_id}
    POST /payments/{payment_id}/confirm
```

Para el parcial, puedes defenderlo como **módulo pendiente del siguiente sprint**, pero si la docente lo exige como obligatorio, conviene implementarlo.

## 14.2 Push real

Actualmente existe contrato de push, pero el proveedor real retorna `accepted=false`. Falta:

- registro de device token,
- Firebase Cloud Messaging,
- envío real a cliente y taller,
- eventos de notificación al publicar/asignar/cambiar estado.

## 14.3 Tiempo real

Actualmente el tracking puede integrarse por polling HTTP. Falta:

- WebSocket,
- Server-Sent Events,
- canal en tiempo real para estados y ubicación.

Para el parcial, se puede defender como actualización periódica desde Flutter/Angular.

## 14.4 Técnicos con login propio

El rol `TECHNICIAN` existe, pero no hay endpoints propios para que un técnico inicie sesión y opere desde móvil. Ahora todo lo hace el `PROVIDER_ADMIN`.

## 14.5 Calificación del servicio

El motor usa `average_rating`, pero no se observa endpoint para que el cliente califique al taller después de completar.

## 14.6 Seguros/suscripciones

Está en los apuntes como adicional, pero no está implementado.

---

# 15. Checklist de defensa técnica

Antes de defender:

- [ ] Levantar PostgreSQL, Redis, API y worker Celery.
- [ ] Ejecutar migraciones Alembic.
- [ ] Verificar `/api/system/health`.
- [ ] Verificar `/api/system/readiness`.
- [ ] Iniciar sesión como `admin@mechanic.local`.
- [ ] Registrar un cliente.
- [ ] Registrar un taller.
- [ ] Crear técnico.
- [ ] Configurar al menos un servicio compatible.
- [ ] Crear vehículo.
- [ ] Crear incidente.
- [ ] Subir texto, imagen y audio.
- [ ] Ver jobs creados.
- [ ] Publicar incidente.
- [ ] Ver candidatos.
- [ ] Aceptar desde taller.
- [ ] Despachar técnico.
- [ ] Reportar ubicación.
- [ ] Ver tracking como cliente.
- [ ] Marcar llegada.
- [ ] Iniciar servicio.
- [ ] Completar servicio.
- [ ] Ver historial.
- [ ] Explicar brechas honestamente: pagos, push real, técnicos con login, calificaciones.

---

# 16. Errores comunes y cómo diagnosticarlos

## No aparecen candidatos

Revisar:

1. El proveedor está `is_active=true`.
2. El proveedor está `is_available=true`.
3. `current_active_services < max_concurrent_services`.
4. Si es taller, tiene técnicos activos y disponibles.
5. El proveedor configuró servicios activos en `/catalog/me/services`.
6. El servicio coincide con la categoría del incidente.
7. El incidente está en estado compatible para publicar.
8. Si requiere grúa (`TOWING`), el proveedor debe ser `WORKSHOP`.

## Job queda en PENDING

Revisar:

1. Worker Celery levantado.
2. Redis conectado.
3. Cola correcta: `default,audio,image,summary,push`.
4. Variables de proveedor configuradas.
5. Dependencias instaladas.
6. Logs del worker.

## Error 401

Revisar:

1. Header `Authorization`.
2. Token correcto.
3. Token no expirado.
4. Usuario activo.

## Error 403

Revisar:

1. Rol del usuario.
2. Recurso pertenece al usuario correcto.
3. Cliente no puede acceder a endpoints de proveedor/admin.
4. Taller no puede acceder a incidentes que no aceptó.

## Error 409

Normalmente es regla de negocio:

- email repetido,
- placa repetida,
- incidente ya asignado,
- candidato ya no disponible,
- proveedor sin capacidad,
- archivo vacío,
- evidence type inválido.

---

# 17. Conclusión para entregar al desarrollador Flutter/Angular

El backend ya ofrece un contrato REST suficientemente claro para iniciar integración frontend/mobile. Flutter puede avanzar con el flujo de cliente: autenticación, vehículos, incidentes, evidencias y tracking. Angular puede avanzar con el panel de taller y plataforma: proveedores, catálogo, candidatos, operación, jobs e historial.

Para una integración limpia, ambos equipos deben respetar:

- prefijo `/api`,
- token Bearer,
- respuesta estándar `success/message/data/meta`,
- roles separados,
- IDs guardados por flujo,
- polling temporal para tracking,
- manejo de errores 401/403/409/422.

Los módulos que deben tratarse como pendientes o siguiente sprint son: pagos, comisión, notificaciones push reales, técnicos con login propio, calificaciones y comunicación cliente-taller.
