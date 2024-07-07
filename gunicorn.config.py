import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


TRACING_EXPORTER_ENDPOINT = os.environ.get('JAEGER_ENDPOINT', 'http://127.0.0.1:4317')

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    resource = Resource(attributes={
        SERVICE_NAME: "todo-application"
    })

    traceProvider = TracerProvider(resource=resource)
    
    # processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317"))
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=TRACING_EXPORTER_ENDPOINT))
    traceProvider.add_span_processor(processor)
    trace.set_tracer_provider(traceProvider)
