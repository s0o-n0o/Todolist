from django.urls import path
from . import views

app_name = 'TodoApp'

urlpatterns = [
    path('',views.Todo_list, name='todo_list'),
    path('add_todo',views.add_todo,name = 'add_todo'),
]
