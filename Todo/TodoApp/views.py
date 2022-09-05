from unicodedata import category
from django.shortcuts import render,redirect
from .models import Todo
from . import forms
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

#HTMLに表示
def Todo_list(request):
    todos = Todo.objects.all()
    return render(request,'TodoApp/todo_list.html',context= {
        "todo_list":todos,
    })

#新しいタスクが
def add_todo(request):
    form=forms.AddTodo()
    if request.method == "POST":
        form = forms.AddTodo(request.POST) 
        if form.is_valid():
            print("成功したのでデータを保存します")
            form.save()
            return HttpResponseRedirect('/todoapp/')
        else:
            print("失敗したので、エラーを表示します")
            print(form.errors)
    return render(request,'todoapp/form_page.html',context={
        "form":form
    })