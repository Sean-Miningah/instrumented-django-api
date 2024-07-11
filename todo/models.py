from django.db import models
from datetime import datetime
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.

class Todo(ExportModelOperationsMixin('todo'), models.Model):
  text: str = models.TextField(null=False)
  created_at: datetime = models.DateTimeField(auto_now_add=True, null=True)
  title: str = models.CharField(max_length=100, null=False)
  is_completed: bool = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.title
  