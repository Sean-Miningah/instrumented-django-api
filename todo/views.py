from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from opentelemetry import trace
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from todo.models import Todo

tracer = trace.get_tracer(__name__)

@tracer.start_as_current_span("get-to-do's")
def home(request: HttpRequest) -> HttpResponse:
  
  # with trace.
  todos = Todo.objects.all()
  
  return TemplateResponse(
    request,
    "todos/home.html",
    {
      "todos": todos
    },
  )
  