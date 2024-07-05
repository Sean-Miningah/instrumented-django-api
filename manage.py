#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    DjangoInstrumentor().instrument()
    
    resource = Resource(attributes={
        SERVICE_NAME: "todo-application"
    })

    traceProvider = TracerProvider(resource=resource)
    
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317"))
    traceProvider.add_span_processor(processor)
    trace.set_tracer_provider(traceProvider)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
