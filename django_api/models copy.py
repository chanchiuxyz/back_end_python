from django.db import models
from datetime import datetime



# Create your models here.
# class Users(models.Model):
#     _id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=35)
#     phone = models.CharField(max_length=12)
#     email = models.CharField(max_length=30)
#     role_id = models.CharField(max_length=30)
#     create_time = models.IntegerField()

class Users(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=35)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    role_id = models.CharField(max_length=30)
    create_time = models.DateTimeField.auto_now_add(auto_now_add=True)
    
