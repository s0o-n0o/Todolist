from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username= forms.CharField(label='username')
    email=forms.EmailField(label='email')
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm_password',widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ('username','email','password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致しません')
    
    def save(self,commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'],user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label='名前')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())