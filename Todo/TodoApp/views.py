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

# Create your views here.
ch=(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事'),
    )

#HTMLに表示
def todo_home(request):
    lists = ListTodo.objects.all()
    for list in lists:
        print(list.pk)
    return render(request,'todoapp/todo_home.html',context={
        'lists':lists,
    })

def todo_today(request):
    return render(request,'todoapp/todo_today.html')

def create_list(request):
    list_form = forms.ListForm(request.POST or None)
    if list_form.is_valid():
        list_form.save()
        return HttpResponseRedirect('/todoapp/home')
    else:
        count = ListTodo.objects.filter(list_name=request.POST.get('list_name')).count()
        list_name = str(request.POST.get('list_name')) + "("+str(count)+")"
        list_form.list_name = list_name
        
        if list_form.is_valid():
            list_form.save()
            print(list_form)
            return HttpResponseRedirect('/todoapp/home')
        else:
            print(list_form.errors)
            print(list_form.list_name)

    return render(request,'todoapp/create_list.html',context={
        'form':list_form,
    })

def todo_list(request,pk):
    pk = pk
    done = Todo.objects.filter(status=True,list_name=pk)
    not_done = Todo.objects.filter(status=False,list_name=pk)
    return render(request,'todoapp/todo_list.html',context= {
        "done_list":done,
        "not_done_list":not_done,
        "pk" :pk
    })

# Todo_list()

#新しいタスクを追加
def add_todo(request,pk):
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

def delete_list(request,pk):
    list = ListTodo.objects.filter(pk=pk).delete()
    HttpResponse('削除しました')
    return HttpResponseRedirect('/todoapp/')



def change_status(request,id,status):
    todo = Todo.objects.get(id=id)
    if status == 'True':
        todo.status =  False
    elif status == 'False':
        todo.status = True
    todo.save()
    return HttpResponseRedirect('/todoapp/')


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
        done= todos.filter(status=True)
        not_done= todos.filter(status=False)
        choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
        for todo in done:
            todo.category =choices[todo.category] 
        for todo in not_done:
            todo.category =choices[todo.category] 
        return render(request,'todoapp/todo_list.html',context={
            'done_list':done,
            'not_done_list':not_done,
        })

def priority_sort(request):
    todos = Todo.objects.order_by('priority')
    done= todos.filter(status=True)
    not_done= todos.filter(status=False)
    choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
    for todo in done:
            todo.category =choices[todo.category]
    for todo in not_done:
            todo.category =choices[todo.category]
    messages.success(request, '優先度順')
    return render(request,'todoapp/todo_list.html',context={
            # 'todo_list':todos,
            'done_list':done,
            'not_done_list':not_done,

        })

def deadline_sort(request):
    todos = Todo.objects.order_by('deadline')
    done= todos.filter(status=True)
    not_done= todos.filter(status=False)
    choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
    for todo in done:
            todo.category =choices[todo.category] 
    for todo in not_done:
            todo.category =choices[todo.category] 
    messages.success(request, '期限順')
    return render(request,'todoapp/todo_list.html',context={
            # 'todo_list':todos,
            'done_list':done,
            'not_done_list':not_done,
        })

def category_sort(request):
    todos = Todo.objects.order_by('category')
    done= todos.filter(status=True)
    not_done= todos.filter(status=False)
    choices={"1":'仕事',"2":'習慣',"3":'用事',"4":'やりたい事'}
    for todo in done:
            todo.category =choices[todo.category] 
    for todo in not_done:
            todo.category =choices[todo.category] 
    messages.success(request, 'カテゴリ順')
    return render(request,'todoapp/todo_list.html',context={
            # 'todo_list':todos,
            'done_list':done,
            'not_done_list':not_done,
        })
