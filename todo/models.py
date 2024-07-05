from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
  text: str = models.TextField(null=False)
  date: datetime = models.TextField(null=False)
  title: str = models.CharField(max_length=100, null=False)
  is_completed: bool = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.title
  