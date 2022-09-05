from dataclasses import fields
from django import forms
from django.core import validators
from .models import Todo
from django.contrib.admin.widgets import AdminDateWidget


class AddTodo(forms.ModelForm):
    title = forms.CharField(label='title')
    detail = forms.CharField(label='detail',widget=forms.Textarea(attrs={'rows':1,'cols':20}))
    category = forms.ChoiceField(label='category',choices=(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事'),
    ),widget=forms.RadioSelect)
    deadline = forms.DateField(label='deadline', widget=AdminDateWidget)
    priority  = forms.ChoiceField(label='priority', choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        ),widget=forms.RadioSelect)
    # created_at = 

    class Meta:
        model = Todo
        exclude = ['status','created_at','updated_at']
        # fields="__all__"
        widgets ={
            'deadline':AdminDateWidget(),
        }