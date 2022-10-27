from importlib.metadata import requires
from tkinter import Widget
from turtle import title
from django.db import models

# Create your models here.
class Todo(models.Model):
    category = (
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事')
        )


    title = models.CharField(max_length=50)
    detail =models.CharField(max_length=200,null=True)
    status = models.BooleanField(default=False)
    deadline = models.DateField('期限',blank=True,null=True)
    priority = models.IntegerField(null=True)
    category = models.CharField(max_length=50,null=True,choices =(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事')
        ))
    created_at =  models.DateTimeField(help_text='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(help_text='更新日時',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'

