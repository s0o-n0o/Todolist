from turtle import title
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    detail =models.CharField(max_length=200)
    status = models.Choices
    created_at =  models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    priority = models.IntegerField()

    class Meta:
        db_table = 'todo'
        
