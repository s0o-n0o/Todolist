from django.urls import path
from . import views

app_name = 'TodoApp'

urlpatterns = [
    path('',views.todo_list, name='todo_list'),
    path('add_todo',views.add_todo,name = 'add_todo'),
    path('update_todo/<int:id>',views.update_todo,name = 'update_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name = 'delete_todo'),
    path('change_status/<int:id>/<str:status>',views.change_status,name = 'change_status'),
    path('search',views.search,name = 'search'),
    path('priority_sort',views.priority_sort,name = 'priority_sort'),
    path('deadline_sort',views.deadline_sort,name = 'deadline_sort'),
    path('category_sort',views.category_sort,name = 'category_sort'),
]
