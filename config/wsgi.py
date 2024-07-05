"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os

from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
DjangoInstrumentor().instrument()

resource = Resource(attributes={
  SERVICE_NAME: 'todo-django-app'
})

traceProvider = TracerProvider(resource=resource)

processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317"))
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

application = get_wsgi_application()
