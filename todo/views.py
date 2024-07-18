from django.shortcuts import  redirect
from django.template.response import TemplateResponse
from django.http import HttpRequest, HttpResponse
from time import sleep

from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from todo.models import Todo
from todo.task import task_created_alert

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

def create_todo(request: HttpRequest) -> HttpResponse: 
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    created_todo = Todo.objects.create(title=title, text=description)

    carrier = {}
    TraceContextTextMapPropagator().inject(carrier) 
    task_created_alert.delay(title=created_todo.title, headers=carrier)
    sleep(5)
    return redirect('home')
  
  return TemplateResponse(
    request, 
    "todos/create_todo.html"
  )

  