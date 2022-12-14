from datetime import datetime, timedelta
from email.policy import default
from importlib.metadata import requires
from tkinter import Widget
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Todo(models.Model):
    today = datetime.today() + timedelta(days =1)
    tomorrow = datetime.strftime(today, '%Y-%m-%d')
    user = models.ForeignKey(
        'user.Users', on_delete = models.CASCADE
    )
    title = models.CharField(max_length=50)
    detail =models.CharField(max_length=200,null=True)
    status = models.BooleanField(default=False)
    deadline = models.DateField('期限',blank=True,default=tomorrow)
    priority = models.IntegerField(null=True)
    category = models.CharField(max_length=50,null=True)
    created_at =  models.DateTimeField(help_text='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(help_text='更新日時',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'

