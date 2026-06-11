FROM python:3.12-slim

# Prevents Python from generating .pyc files inside the container.
ENV PYTHONDONTWRITEBYTECODE=1

# Ensures Python logs are printed immediately in Docker.
ENV PYTHONUNBUFFERED=1

WORKDIR /mechanic-api

# Basic tools for development:
# - build-essential: compile native dependencies if needed
# - git, curl: common developer tools
# - libpq-dev, postgresql-client: PostgreSQL support
# - netcat-openbsd: useful for connectivity checks
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    netcat-openbsd \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Keeps the container ready for VS Code remote development.
CMD ["sleep", "infinity"]