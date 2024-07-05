#!/bin/bash

# Set environment variables
export OTEL_SERVICE_NAME=todo-app
# export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=<Environment>,service.namespace=<Namespace>,service.version=<Version>,service.instance.id=<Instance>
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318/
# export DEFAULT_TRACES_EXPORT_PATH=""

# Run the Python server without reload
# gunicorn --workers=4 --bind 0.0.0.0:8000 myapp.wsgi:application
python manage.py runserver --noreload 0.0.0.0:8000
