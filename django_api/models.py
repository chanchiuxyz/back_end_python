from django.db import models
import time
from datetime import datetime
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Users(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=35)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    role_id = models.CharField(max_length=30)
    create_time = models.IntegerField(default=time.time())
    # create_time = models.DateTimeField(auto_now_add=True)
    
class Roles(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    authname = models.CharField(max_length=15)
    auth_time = models.DateTimeField(auto_now=True)
    menus = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    parentId = models.CharField(max_length=15)

class Products(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    categoryId = models.CharField(max_length=15)
    PategoryId = models.CharField(max_length=15)
    price = models.IntegerField()
    desc = models.CharField(max_length=1000)
    status = models.IntegerField(default=1)
    images = models.TextField(blank=True)



# class User(models.Model):
#     _id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=35)
#     phone = models.CharField(max_length=12)
#     email = models.CharField(max_length=30)
#     role_id = models.CharField(max_length=30)
#     create_time = models.IntegerField(default=time.time())
    
