from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect,get_object_or_404
from .models import CustomUser, Farmer, AddFarming, AgroProduct
from .forms import MyUserCreationForm, FarmerForm, AddFarmingForm, AgroProductForm
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'farmerapp/home.html', {})

def register(request):
    if request.method == 'POST':
        farmerform = FarmerForm(request.POST)
        if farmerform.is_valid():
            farmerform.save()
            return redirect('home')  # Redirect to login_user view after successful signup
    else:
        farmerform = FarmerForm()
    return render(request, 'farmerapp/registerfarmer.html', {'FarmerForm': farmerform})

def addagroproducts(request):
    if request.method == 'POST':
        productform = AgroProductForm(request.POST or None)
        if productform.is_valid():
            productform.save()
            return redirect('agroproducts')
    else:
        productform = AgroProductForm()
    context = {'AgroProductForm': productform, 'category': 'info', 'message': 'Add Agro Products'}
    return render(request, 'farmerapp/addagroproducts.html', context)

def addfarming(request):
    farming = AddFarming.objects.all()
    if request.method == 'POST':
        form = AddFarmingForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved to database")  # Print success message to console
            return redirect('home')  # Redirect to login_user view after successful signup
    else:
        form = AddFarmingForm()
    return render(request, 'farmerapp/addfarming.html', {'addfarmingform':form,'farming': farming})


def farmer_details(request):
    # ... your code here ...
    farmer_list = Farmer.objects.all()
    context = {'farmer_list': farmer_list, 'category': 'info', 'message': 'Farmer Details'}
    return render(request, 'farmerapp/farmingdetails.html', context)

def agroproducts(request):
    agroproduct = AgroProduct.objects.all()
    context = {'agroproduct': agroproduct, 'category': 'info', 'message': 'Farmer Details'}
    return render(request, 'farmerapp/agroproducts.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
    return render(request, 'farmerapp/login.html')

    
def auth(request):
    return render(request, 'auth.html', {})

def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login_user view after successful signup
    else:
        form = MyUserCreationForm()
    return render(request, 'farmerapp/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')



def edit(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('home', farmer_id=farmer.id)
    else:
        form = FarmerForm(instance=farmer)
    return render(request, 'farmerapp/edit.html', {'form': form})

def delete(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    farmer.delete()
    return redirect('farmingdetails')