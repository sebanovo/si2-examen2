#!/bin/sh
set -e

echo "Waiting for PostgreSQL at ${POSTGRES_SERV}:${POSTGRES_PORT}..."
while ! nc -z "${POSTGRES_SERV}" "${POSTGRES_PORT}"; do
  sleep 1
done

echo "Waiting for Redis at ${REDIS_HOST}:${REDIS_PORT}..."
while ! nc -z "${REDIS_HOST}" "${REDIS_PORT}"; do
  sleep 1
done

echo "Starting Celery worker..."
exec celery -A app.tasks.celery_app.celery_app worker --loglevel=info -Q default,audio,image,summary,push