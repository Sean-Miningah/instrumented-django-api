from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from todo.models import Todo

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

trace.set_tracer_provider(TracerProvider())

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

def home(request: HttpRequest) -> HttpResponse:
  
  todos = Todo.objects.all()
  
  return TemplateResponse(
    request,
    "todos/home.html",
    {
      "todos": todos
    },
  )
  