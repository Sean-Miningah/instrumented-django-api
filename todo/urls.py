from django.urls import path 

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path('create-todo', views.create_todo, name="create-todo")
]