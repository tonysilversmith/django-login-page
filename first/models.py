from django.db import models
from django.forms import forms

# Create your models here.

class UserDetailslala(models.Model):
    email = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)


# class Customer(models.Model):
    # name = models.CharField(max_length=128, primary_key= True)

