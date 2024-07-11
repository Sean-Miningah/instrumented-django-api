from time import sleep
from celery import shared_task
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.baggage.propagation import W3CBaggagePropagator
from opentelemetry import trace

# from config.celery import tracer

tracer = trace.get_tracer(__name__)
@shared_task
def task_created_alert(title, headers):
  # carrier ={'traceparent': headers['Traceparent']}
  # ctx = TraceContextTextMapPropagator().extract(carrier=headers)
  ctx = TraceContextTextMapPropagator().extract(carrier=headers)
  print('Received Context', ctx)

  # b2 ={'baggage': headers['Baggage']}
  # ctx2 = W3CBaggagePropagator().extract(b2, context=ctx)
  # print(f"Received context2: {ctx2}")


  
  with tracer.start_as_current_span('tack_create_alert', context=ctx):
    span = trace.get_current_span()
    span.set_attribute("title", title)
    sleep(10)
    print('Task created', title)
    
  return True
  