from secrets import choice
from turtle import update
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Todo,ListTodo
from . import forms
from django.http import HttpResponse , HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import datetime

# Create your views here.
#HTMLに表示
def todo_home(request):
    lists = ListTodo.objects.all()
    return render(request,'todoapp/todo_home.html',context={
        'lists':lists,
    })


def todo_today(request):
    now = datetime.datetime.now()
    print(now)
    done = Todo.objects.filter(status=True,deadline=now)
    not_done = Todo.objects.filter(status=False,deadline=now)
    return render(request,'todoapp/todo_today.html',context= {
        "done_list":done,
        "not_done_list":not_done,
    })


def create_list(request):
    list_form = forms.ListForm()
    if request.method == 'POST':
        list_form = forms.ListForm(request.POST)
        list_todo = list(ListTodo.objects.filter(list_name=request.POST.get('list_name')))
        if list_form.is_valid() :
            list_form.save()
            return HttpResponseRedirect('/todoapp/home')
        else:
            for i in range(1,1000):
                list_name = str(request.POST.get('list_name')) + "("+str(i)+")"
                if ListTodo.objects.filter(list_name=list_name).exists() == False:
                    break
                print(list_name)
                i = i+1
            new_list_todo = ListTodo(list_name=list_name)
            new_list_todo.save()
            return HttpResponseRedirect('/todoapp/home')
    return render(request,'todoapp/create_list.html',context={
        'form':list_form,
    })


def todo_list(request,pk):
    pk = pk
    list_name = ListTodo.objects.get(pk=pk)
    done = Todo.objects.filter(status=True,list_name=pk)
    not_done = Todo.objects.filter(status=False,list_name=pk)
    return render(request,'todoapp/todo_list.html',context= {
        "done_list":done,
        "not_done_list":not_done,
        "pk" :pk,
        'list_name':list_name,
    })

# Todo_list()

#新しいタスクを追加
def add_todo(request,pk):
    today = ""
    if pk == "None":
        today = pk
        pk = "1"
    list_todo = ListTodo.objects.get(pk=pk)
    form=forms.AddForm(initial={'list_name':list_todo})
    if request.method == "POST":
        form = forms.AddForm(request.POST) 
        if form.is_valid():
            form.instance.user=request.user
            print("成功したのでデータを保存します")
            form.save()
            if today == "None":
                return HttpResponseRedirect('/todoapp/today')
            return HttpResponseRedirect('/todoapp/todolist/'+ pk)
        else:
            print("失敗したので、エラーを表示します")
            print(form.errors)
    return render(request,'todoapp/form_page.html',context={
        "form":form,
        "pk" : pk,
    })

#タスクの更新(編集)
def update_todo(request,pk,id):
    todo = Todo.objects.get(id=id)
    if todo.user.id != request.user.id:
        raise Http404
    update = forms.UpdateForm(
        initial= {
            'user':todo.user,
            'title':todo.title, 'detail':todo.detail,
            'deadline':todo.deadline, 'priority':todo.priority,
            'list_name':todo.list_name
            }
    )
    if request.method == 'POST':
        update = forms.UpdateForm(request.POST)
        if update.is_valid():
            todo.user=request.user
            todo.title=request.POST.get("title")
            todo.detail=request.POST.get("detail")
            todo.deadline=request.POST.get("deadline")
            todo.priority=request.POST.get("priority")
            todo.list_name.list_name=request.POST.get("list_name")
            todo.save()
            return HttpResponseRedirect('/todoapp/todolist/'+pk)
        else:
            print("失敗したので、エラーを表示します")
            print(update.errors)
    return render(request,'todoapp/update_todo.html',context={
        'update':update,
        'todo':todo,
        'pk':pk,
    })

#タスクの削除
def delete_todo(request,pk,id):
    todo = Todo.objects.filter(id=id).delete()

    HttpResponse('削除しました')
    return HttpResponseRedirect('/todoapp/todolist/'+pk)

def delete_list(request,pk):
    list = ListTodo.objects.filter(pk=pk).delete()
    HttpResponse('削除しました')
    return HttpResponseRedirect('/todoapp/home')



def change_status(request,pk,id,status):
    todo = Todo.objects.get(id=id)
    if status == 'True':
        todo.status =  False
    elif status == 'False':
        todo.status = True
    todo.save()
    if pk == 'None':
        return HttpResponseRedirect('/todoapp/today')

    return HttpResponseRedirect('/todoapp/todolist/'+pk)


def priority_sort(request,pk):
    todos = Todo.objects.filter(list_name=pk).order_by('priority')
    done= todos.filter(status=True)
    not_done= todos.filter(status=False)
    messages.success(request, '優先度順')
    return render(request,'todoapp/todo_list.html',context={
            # 'todo_list':todos,
            'done_list':done,
            'not_done_list':not_done,
            'pk':pk
        })

def deadline_sort(request,pk):
    todos = Todo.objects.filter(list_name=pk).order_by('deadline')
    done= todos.filter(status=True)
    not_done= todos.filter(status=False)
    messages.success(request, '期限順')
    return render(request,'todoapp/todo_list.html',context={
            # 'todo_list':todos,
            'done_list':done,
            'not_done_list':not_done,
            'pk':pk,
                    })
