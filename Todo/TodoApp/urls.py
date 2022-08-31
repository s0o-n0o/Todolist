from django.urls import path
from . import views

app_name = 'TodoApp'

urlpatterns = [
    path('Todo_list',views.Todo_list, name='Todo_list'),
]
