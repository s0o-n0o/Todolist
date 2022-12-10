from django.urls import path
from . import views

app_name = 'TodoApp'

urlpatterns = [
    path('today',views.todo_today, name='todo_today'),
    path('home',views.todo_home, name='todo_home'),
    path('todolist/<str:pk>/',views.todo_list, name='todo_list'),
    path('add_todo/<str:pk>',views.add_todo,name = 'add_todo'),
    path('create_list',views.create_list,name = 'create_list'),
    path('update_todo/<str:pk>/<int:id>',views.update_todo,name = 'update_todo'),
    path('delete_todo/<str:pk><int:id>',views.delete_todo,name = 'delete_todo'),
    path('delete_list/<str:pk>',views.delete_list,name = 'delete_list'),
    path('change_status/<str:pk>/<int:id>/<str:status>',views.change_status,name = 'change_status'),
    # path('search', views.search, name='search'),
    path('priority_sort/<str:pk>',views.priority_sort,name = 'priority_sort'),
    path('deadline_sort/<str:pk>',views.deadline_sort,name = 'deadline_sort'),
]
