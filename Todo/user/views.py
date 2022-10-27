from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import UserForm,ProfileForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
# def user_list(request):
#     return render(request,'user/user_list.html')


def index(request):
    return render(request,'user/index.html')

def register(request):
    user_form = UserForm(request.POST or None)
    if user_form.is_valid(): # validation
        user = user_form.save()
        user.set_password(user.password)
        user.save() #ユーザー保存
        return redirect('user:user_login')
    return render(request ,'user/registration.html', context={
        'user_form':user_form,
    })

def user_login(request):
    login_form  = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username= username,password=password) #userが存在するかつ情報があっているか確認
        if user: #user exist
            if user.is_active: 
                login(request,user)
                return redirect('TodoApp:todo_list')
            else:
                return HttpResponse('アカウントがアクティブではないです')
        else:
            return HttpResponse('ユーザーが存在しません')
    return render(request,'user/login.html',context={
        'login_form':login_form
    })

#logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('user:user_login')

@login_required
def info(request):
    return HttpResponse('ログインしています')