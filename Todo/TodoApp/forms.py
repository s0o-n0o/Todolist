from dataclasses import fields
from django import forms
from django.core import validators
from .models import Todo
from django.contrib.admin.widgets import AdminDateWidget

class AddForm(forms.ModelForm):
    title = forms.CharField(label='title')
    detail = forms.CharField(label='detail',widget=forms.Textarea(attrs={'rows':1,'cols':20}),required=False)
    category = forms.ChoiceField(label='category',choices=(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事'),
    ),widget=forms.SelectMultiple,required=False)
    deadline = forms.DateField(label='deadline', widget=AdminDateWidget(attrs={'placeholder':'2000-01-01'}),required=False)
    priority  = forms.ChoiceField(label='priority', choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        ),widget=forms.RadioSelect,initial=1)
    # created_at = 

    class Meta:
        model = Todo
        exclude = ['status','created_at','updated_at']
        # fields="__all__"
        widgets ={
            'deadline':AdminDateWidget(),
        }
    
class UpdateForm(forms.ModelForm):
    title = forms.CharField(label='title')
    detail = forms.CharField(label='detail',widget=forms.Textarea(attrs={'rows':1,'cols':20}),required=False)
    category = forms.ChoiceField(label='category',choices=(
        (1,'仕事'),
        (2,'習慣'),
        (3,'用事'),
        (4,'やりたい事'),
    ),widget=forms.SelectMultiple,required=False)
    deadline = forms.DateField(label='deadline', widget=AdminDateWidget(attrs={'placeholder':'2000-01-01'}),required=False)
    priority  = forms.ChoiceField(label='priority', choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        ),widget=forms.RadioSelect,required=False)
    
    class Meta:
        model = Todo
        exclude = ['status','created_at','updated_at']
        # fields="__all__"
        widgets ={
            'deadline':AdminDateWidget(),
        }