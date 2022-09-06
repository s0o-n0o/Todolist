from turtle import update
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Todo
from . import forms
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

#HTMLに表示
def Todo_list(request):
    todos = Todo.objects.all()
    choices=['仕事', '習慣','用事','やりたい事']
    return render(request,'todoapp/todo_list.html',context= {
        "todo_list":todos,
        "choices":choices,
    })

#タスクの更新(編集)
def update_todo(request,id):
    todo = Todo.objects.get(id=id)
    update = forms.UpdateForm(
        initial= {
            'title':todo.title, 'detail':todo.detail,
            'deadline':todo.deadline, 'priority':todo.priority,
            'category':todo.category,
            }
    )
    if request.method == 'POST':
        update = forms.UpdateForm(request.POST)
        if update.is_valid():
            todo.title=request.POST.get("title")
            todo.detail=request.POST.get("detail")
            todo.deadline=request.POST.get("deadline")
            todo.priority=request.POST.get("priority")
            todo.category=request.POST.get("category")
            todo.save()
            return HttpResponseRedirect('/todoapp/')
        else:
            print("失敗したので、エラーを表示します")
            print(update.errors)
    return render(request,'todoapp/update_todo.html',context={
        'update':update,
        'todo':todo
    })

#タスクの削除
def delete_todo(request,id):
    todo = Todo.objects.filter(id=id).delete()
    HttpResponse('削除しました')
    return HttpResponseRedirect('/todoapp/')



#新しいタスクを追加
def add_todo(request):
    form=forms.AddForm()
    if request.method == "POST":
        form = forms.AddForm(request.POST) 
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