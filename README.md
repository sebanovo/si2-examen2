<div align="center">
   <h1>Sistema de auxiliar mecanico</h1>
</div>

## 🏗 Estructura del proyecto

frontend `mechanic_mobile` en flutter <br>
backend `mechanic-api` desarrollado con FastAPI <br>
Frontend `mechanic-web` en Angular.

```
mechanic-system/
├── mechanic_mobile/
|   ├── assets/               # Imagenes
|   ├── lib/                  # Codigo fuente
|   ├── pubspec.yaml          # Librerias y configuración
│   └── ...
│
├── mechanic-api/              # Backend (FastAPI)
│   ├── .devcontainer/         # Configuración para entorno de desarrollo
│   │   ├── Dockerfile
│   │   └── devcontainer.json
│   ├── app/                   # Código principal de la API
│   ├── requirements.txt       # Dependencias Python
│   ├── Dockerfile.dev         # Imagen para desarrollo
│   └── ...
│
├── mechanic-web/              # Frontend (Angular)
│   ├── .devcontainer/         # Configuración para entorno de desarrollo
│   ├── src/                   # Código fuente del frontend
│   ├── Dockerfile.dev         # Imagen para desarrollo
│   └── ...
│
├── .env                       # Variables de entorno (desarrollo)
├── .env.sample                # Ejemplo de variables de entorno
├── .env.prod                  # Variables de entorno para producción
├── docker-compose.yml         # Orquestación para desarrollo
└── README.md
```

### Servicios (Docker)

|    Servicio     | Tecnología        | Puerto | Descripción   |
|-----------------|-------------------|--------|---------------|
| serv-mech-web   | Angular           | 4200   | Interfaz web  |
| serv-mech-api   | Python            | 8000   | FAST API      |
| serv-mech-db    | PostgreSQL        | 5432   | Base de datos |

---

### 🧯 Comandos Docker

En la raiz jecutar
```bash
cp .env.sample .env
```
```bash

# Iniciar servicios
docker compose up --build

# Iniciar servicios en background
docker compose up --build -d

# Ver logs
docker compose logs -f

# Detener servicios
docker compose down

# Resetear volumenes y base de datos
docker compose down -v


docker container prune
docker network prune
docker volume prune
```

## 🧯 Ejecutar DevContainer en VSCode

### ⚠️ instalar devcontainer en VSCODE

1. **En VSCode**  
   Abrir `mechanic-api` o `mechanic-web`.

2. **En otra ventana Ejecutar la base de datos (solo para mechanic-api)**  

   ```bash
   docker compose up --build serv-mech-db

3. **Abrir el Command Palette**  
- Presiona `Ctrl + Shift + P`.
- Busca y selecciona la opción `Dev Containers: Reopen in Container.`

5. **Ejecutar proyectos**
- En `mechanic-api`

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
- En `mechanic-web`
   ```bash
   npm start
   ```
- Listo !!!

<hr>

<div align="center" width="100">
  <h1>Stack</h1>
  <!-- Languages -->
  </br>
  <h3>Languages and Frameworks</h3>
	<img
  		src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
  		width="60px"
  		alt="Python">
	<img
	  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg"
	  width="60px"
	  alt="FastAPI">
	<img
	  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/angularjs/angularjs-original.svg"
	  width="60px"
	  alt="Angular">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg" width="60px" alt="Flutter"/>        
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg"
    width="60px"
    alt="PostgreSQL">
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg"
    width="60px"
    alt="HTML5">
    &nbsp;&nbsp;&nbsp;&nbsp;
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg"
    width="60px"
    alt="css3">
    &nbsp;&nbsp;&nbsp;&nbsp;
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg"
    width="60px"
    alt="Tailwind CSS">
    <!-- Frameworks -->
	
  </br>
    <!-- tools -->
  </br>
  <h3>Tools</h3>
  <img
    src="https://cdn.simpleicons.org/jira/0052CC"
    width="55px"
    alt="Jira">
  <img
    src="https://cdn.simpleicons.org/github/FFFFFF"
    width="50px"
    alt="GitHub Logo White">
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg"
    width="60px"
    alt="Docker">
    &nbsp;&nbsp;&nbsp;&nbsp;
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original-wordmark.svg"
    width="65px"
    alt="Git Wordmark">
  <img
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original-wordmark.svg"
    width="60px"
    alt="VS Code">
    &nbsp;&nbsp;&nbsp;&nbsp;
</div>
<hr>

last modified: 26/04/2026
