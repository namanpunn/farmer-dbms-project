from django import forms
from django.forms import ModelForm
from .models import CustomUser, Farmer, AddFarming, AgroProduct
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


      

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields = ['username', 'name', 'email']

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

class AddFarmingForm(forms.ModelForm):
    class Meta: 
        model = AddFarming
        fields = '__all__'

class AgroProductForm(forms.ModelForm):
    class Meta: 
        model = AgroProduct
        fields = '__all__'

