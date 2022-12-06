from dataclasses import fields
from django import forms
from django.core import validators
from .models import Todo,ListTodo
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime, timedelta
from django.utils.timezone import now

today =now
# tomorrow = datetime.strftime(today, '%Y-%m-%d')

class ListForm(forms.ModelForm):
    list_name = forms.CharField(label="list_name")
    class Meta:
        model =ListTodo
        exclude= ("list_counter",)
        # widgets ={'list_name':}

class AddForm(forms.ModelForm):
    title = forms.CharField(label='title')
    detail = forms.CharField(label='detail',widget=forms.Textarea(attrs={'rows':1,'cols':20}),required=False)
    deadline = forms.DateField(label='deadline', widget=AdminDateWidget(),initial=today)
    priority  = forms.ChoiceField(label='priority', choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        ),widget=forms.Select,initial=1)

    class Meta:
        model = Todo
        exclude = ['user','status','created_at','updated_at',]
        widgets ={
            'deadline':AdminDateWidget(),
        }
    
class UpdateForm(forms.ModelForm):
    title = forms.CharField(label='title')
    detail = forms.CharField(label='detail',widget=forms.Textarea(attrs={'rows':1,'cols':20}),required=False)
    deadline = forms.DateField(label='deadline', widget=AdminDateWidget(),required=False,initial=today)
    priority  = forms.ChoiceField(label='priority', choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        ),widget=forms.Select,required=False)
    
    class Meta:
        model = Todo
        exclude = ['user','status','created_at','updated_at']
        # fields="__all__"
        widgets ={
            'deadline':AdminDateWidget(),
        }