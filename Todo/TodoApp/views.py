from django.shortcuts import render
from .models import Todo
# Create your views here.

def Todo_list(request):
    return render(request,'TodoApp/todo_list.html')