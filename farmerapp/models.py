from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique =True ,null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null = True, default= "avatar.svg")

   
    REQUIRED_FIELDS = []

class AddFarming(models.Model):
    type = models.CharField(max_length=10, null=True)

    def __str__(self):
       return self.type

class Farmer(models.Model):

    farmer_name = models.CharField(max_length=200, null=True)
    adhaarnumber = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, null=True)
    phonenumber = models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    
    

    def __str__(self):
       return self.farmer_name
    