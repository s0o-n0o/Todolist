from django.urls import path
from . import views

app_name = 'TodoApp'

urlpatterns = [
    path('',views.todo_list, name='todo_list'),
    path('add_todo',views.add_todo,name = 'add_todo'),
    path('update_todo/<int:id>',views.update_todo,name = 'update_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name = 'delete_todo'),
    path('search',views.search,name = 'search'),
]
