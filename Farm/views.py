from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def products(request):
    return render(request,'products.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'home.html')

        else:
            error_message = "Invalid username or password."
            return render(request, 'register.html', {'error_message': error_message})
    
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('index.html')

def register(request):
    return render(request, 'register.html')