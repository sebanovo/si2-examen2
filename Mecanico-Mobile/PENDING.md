- implementar el add evidences para imagenes y audio
- implementar las notificaciones push en el cliente

```json
implementa esto más para el admin platform
GET {{baseUrl}}/api/operations/platform/incidents/:incident_id/history
// response:
{
    "success": true,
    "message": "Platform operation history loaded successfully.",
    "data": [
        {
            "id": "417cab64-d81d-42f3-9e34-af415f135174",
            "incident_id": "d6def64c-dc6b-46fe-a765-3872e777bf33",
            "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
            "technician_id": "3652474a-dd25-4db2-a955-534c3664e451",
            "actor_user_id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
            "event_type": "DISPATCHED",
            "from_status": "ASSIGNED",
            "to_status": "EN_ROUTE",
            "note": "Se despacha técnico disponible hacia la ubicación del cliente.",
            "payload_json": {
                "dispatch_mode": "TECHNICIAN",
                "assigned_technician_id": "3652474a-dd25-4db2-a955-534c3664e451"
            },
            "created_at": "2026-04-26T16:50:59.165248Z",
            "actor_user": {
                "id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
                "email": "usuario@gmail.com",
                "first_name": "nombre",
                "last_name": "apellido",
                "full_name": "nombre apellido"
            },
            "technician": {
                "id": "3652474a-dd25-4db2-a955-534c3664e451",
                "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
                "first_name": "Carlos",
                "last_name": "Mecánico",
                "full_name": "Carlos Mecánico",
                "phone_number": "70000024",
                "specialty": "Auxilio eléctrico y llantas",
                "is_active": true,
                "is_available": true
            }
        },
        {
            "id": "fef580b9-e278-45e2-8654-2285f71634e6",
            "incident_id": "d6def64c-dc6b-46fe-a765-3872e777bf33",
            "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
            "technician_id": "3652474a-dd25-4db2-a955-534c3664e451",
            "actor_user_id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
            "event_type": "ARRIVED_ON_SITE",
            "from_status": "EN_ROUTE",
            "to_status": "ON_SITE",
            "note": null,
            "payload_json": null,
            "created_at": "2026-04-26T16:51:41.610263Z",
            "actor_user": {
                "id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
                "email": "usuario@gmail.com",
                "first_name": "nombre",
                "last_name": "apellido",
                "full_name": "nombre apellido"
            },
            "technician": {
                "id": "3652474a-dd25-4db2-a955-534c3664e451",
                "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
                "first_name": "Carlos",
                "last_name": "Mecánico",
                "full_name": "Carlos Mecánico",
                "phone_number": "70000024",
                "specialty": "Auxilio eléctrico y llantas",
                "is_active": true,
                "is_available": true
            }
        },
        {
            "id": "98c93d08-d7f2-4864-b669-67f4b562b992",
            "incident_id": "d6def64c-dc6b-46fe-a765-3872e777bf33",
            "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
            "technician_id": "3652474a-dd25-4db2-a955-534c3664e451",
            "actor_user_id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
            "event_type": "SERVICE_STARTED",
            "from_status": "ON_SITE",
            "to_status": "IN_PROGRESS",
            "note": "Se inicia revision de vehiculo",
            "payload_json": null,
            "created_at": "2026-04-26T16:52:47.981537Z",
            "actor_user": {
                "id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
                "email": "usuario@gmail.com",
                "first_name": "nombre",
                "last_name": "apellido",
                "full_name": "nombre apellido"
            },
            "technician": {
                "id": "3652474a-dd25-4db2-a955-534c3664e451",
                "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
                "first_name": "Carlos",
                "last_name": "Mecánico",
                "full_name": "Carlos Mecánico",
                "phone_number": "70000024",
                "specialty": "Auxilio eléctrico y llantas",
                "is_active": true,
                "is_available": true
            }
        },
        {
            "id": "2524b70b-f585-4b0f-a379-8dfa5f97d5bf",
            "incident_id": "d6def64c-dc6b-46fe-a765-3872e777bf33",
            "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
            "technician_id": "3652474a-dd25-4db2-a955-534c3664e451",
            "actor_user_id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
            "event_type": "SERVICE_COMPLETED",
            "from_status": "IN_PROGRESS",
            "to_status": "COMPLETED",
            "note": "Servicio finalizado correctamente.",
            "payload_json": {
                "completion_summary": "Se realizó auxilio de batería y el vehículo encendió."
            },
            "created_at": "2026-04-26T16:54:39.849024Z",
            "actor_user": {
                "id": "9a05fed4-b127-4f42-b1c9-e85616b8e9ae",
                "email": "usuario@gmail.com",
                "first_name": "nombre",
                "last_name": "apellido",
                "full_name": "nombre apellido"
            },
            "technician": {
                "id": "3652474a-dd25-4db2-a955-534c3664e451",
                "provider_id": "79a6ba07-b0cd-44d9-8480-4ad533a768e9",
                "first_name": "Carlos",
                "last_name": "Mecánico",
                "full_name": "Carlos Mecánico",
                "phone_number": "70000024",
                "specialty": "Auxilio eléctrico y llantas",
                "is_active": true,
                "is_available": true
            }
        }
    ],
    "meta": {
        "count": 4
    }
}
```