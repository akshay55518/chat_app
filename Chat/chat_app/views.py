from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# from chat_app.urls import 

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def login_register(request):
    if 'login' in request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if User.objects.filter(username=username,password=password).exists():
            return redirect(dashboard)
        else:
            messages.info(request,'Password or username incorrect')
            return redirect(login_register)
    
    if 'register' in request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        if User.objects.filter(username=username).exists() or User.objects.filter(phonenumber=phonenumber).exists() :
                messages.warning(request,"Username or phone number already exists")
                return redirect(login_register)
        else:
            User.objects.create_user(username=username,email=email,phonenumber=phonenumber,password=password)
            # login(request,user)
            messages.info(request,'User Added')
            return redirect('dashboard')
    else:
        return render(request,'login.html',locals())


def logout_view(request):
    logout(request)
    return redirect('login_register')  # Redirect to login page after logout

    
    