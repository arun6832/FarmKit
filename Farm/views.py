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

def user_register(request):
    errors = {}
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        phone = request.POST['phone'].strip()
        username = request.POST['register_number'].strip()
        password = request.POST['password'].strip()

        if not username:
            errors['username'] = 'Username field is required.'
        else:
            is_used = User.objects.filter(username='username').exists()
            if is_used:
                errors['username'] = 'This username is already taken.'

        if not phone:
            errors['phone'] = 'Phone number is required.'
        else:
            is_used = User.objects.filter(username='phone').exists()
            if is_used:
                errors['phone'] = 'Phone number already exits.'

        if not password:
            errors['password'] = 'Password is required.'

        is_valid = len(errors.keys()) == 0

        if is_valid:

            ## Creating an user

            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password
            )
            
            user.save()
            login(request,user)
            return redirect("/home")
        
    context = {
        'errors' : errors
    }

    return render (request, "register.html", context)


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