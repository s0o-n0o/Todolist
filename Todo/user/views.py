from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages



def index(request):
    return render(request,'user/index.html')

def register(request):
    user_form = forms.RegistForm(request.POST or None)
    if user_form.is_valid(): # validation
        try:
            user_form.save()
            return redirect('user:user_login')
        except ValidationError as e:
            user_form.add_error('password',e)
    return render(request ,'user/registration.html', context={
        'user_form':user_form,
    })

def user_login(request):
    login_form  = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email =email, password=password) #userが存在するかつ情報があっているか確認
        print(password)
        if user: #user exist
            login(request,user)
            return redirect('TodoApp:todo_list')
        else:
            messages.warning(request,'ユーザかパスワードが間違っています')
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