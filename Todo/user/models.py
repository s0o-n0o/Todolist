from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser ,BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import UserManager

# Create your models here.


class Users(AbstractBaseUser,PermissionsMixin):
    username= models.CharField(max_length = 255)
    email = models.EmailField(max_length= 255,unique=True)
    is_staff = models.BooleanField(default=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'



    