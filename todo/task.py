from time import sleep
from celery import shared_task
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry import trace


tracer = trace.get_tracer(__name__)
@shared_task
def task_created_alert(title, headers):
  ctx = TraceContextTextMapPropagator().extract(carrier=headers)

  
  with tracer.start_as_current_span('tack_create_alert', context=ctx):
    span = trace.get_current_span()
    span.set_attribute("title", title)
    sleep(10)
    
  return True
  