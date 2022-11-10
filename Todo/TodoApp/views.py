from secrets import choice
from turtle import update
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Todo
from . import forms
from django.http import HttpResponse , HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
ch=(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事'),
    )

#HTMLに表示
def todo_list(request):
    todos = Todo.objects.all()
    choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
    for todo in todos:
        todo.category =choices[todo.category] 
    return render(request,'todoapp/todo_list.html',context= {
        "todo_list":todos,
        # "choices":todos_choice,
    })

# Todo_list()

#タスクの更新(編集)
def update_todo(request,id):
    todo = Todo.objects.get(id=id)
    if todo.user.id != request.user.id:
        raise Http404
    update = forms.UpdateForm(
        initial= {
            'user':todo.user,
            'title':todo.title, 'detail':todo.detail,
            'deadline':todo.deadline, 'priority':todo.priority,
            'category':todo.category,
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
            todo.category=request.POST.get("category")
            todo.save()
            return HttpResponseRedirect('/todoapp/')
        else:
            print("失敗したので、エラーを表示します")
            print(update.errors)
    return render(request,'todoapp/update_todo.html',context={
        'update':update,
        'todo':todo,
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
            form.instance.user=request.user
            print("成功したのでデータを保存します")
            form.save()
            return HttpResponseRedirect('/todoapp/')
        else:
            print("失敗したので、エラーを表示します")
            print(form.errors)
    return render(request,'todoapp/form_page.html',context={
        "form":form
    })

async def change_status(request):
    status = request.POST.get('todostatus')
    print(status)
    todo_id = request.POST.get('todo_id')
    # if status and todo_id:
    async for todo in Todo.objects.get(id=todo_id):
        todo.status = status
        todo.save()
    return HttpResponse({'message':'変更しました'})
    

def search(request):
    todos = Todo.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')
    print(keyword)
    choices={'仕事':'1','習慣':'2','用事':"3",'やりたい事':"4"}
    key= choices[keyword]
    if keyword:
        todos = todos.filter(
                category=key
            )
        messages.success(request, '{}'.format(keyword))
        choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
        for todo in todos:
            todo.category =choices[todo.category] 
        return render(request,'todoapp/todo_list.html',context={
            'todo_list':todos,
        })

def priority_sort(request):
    todos = Todo.objects.all()
    todos = todos.filter(priority_sort)
