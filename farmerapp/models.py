from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    # Modify the groups and user_permissions fields to have unique related names
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A group represents a collection of users who have certain permissions in common.',
        related_name="customuser_set",
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
    )

    REQUIRED_FIELDS = []

class AddFarming(models.Model):
    farming_type = models.CharField(max_length=10, blank=True, null=False)

    def __str__(self):
        return self.farming_type

class Farmer(models.Model):
    farmer_name = models.CharField(max_length=200, null=True)
    adhaarnumber = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, null=True)
    phonenumber = models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    farming_type = models.ForeignKey(AddFarming, on_delete=models.CASCADE)

    def __str__(self):
        return self.farmer_name

class AgroProduct(models.Model):
    farmer_name = models.CharField(max_length=200, null=True)
    Product_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True, null=True)
    Product_description = models.TextField(null=True, blank=True)
    Price = models.IntegerField(default=0)


    def __str__(self):
        return self.Product_name
