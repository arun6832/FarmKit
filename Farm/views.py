from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SoilDataForm
import pickle

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
        username = request.POST['username'].strip()
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

    return render(request, "register.html", context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            
            else:
                error_message = "Invalid username or password."

        else:
            error_message = "Please provide both username and password."

        return render(request,'login.html', {'error_message' : error_message})
    
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('/home')


def register(request):
    return render(request, 'register.html')


def cart(request):
    return render(request, 'cart.html')

def crop(request):
    return render(request,'crop.html')

def crop_suggestion(request):
    if request.method == 'POST':
        form = SoilDataForm(request.POST)
        if form.is_valid():
            # Load the serialized Random Forest model
            with open("rf_pkl", 'rb') as file:
                model = pickle.load(file)
            
            nitrogen_level = form.cleaned_data['nitrogen_level']
            phosphorus_level = form.cleaned_data['phosphorus_level']
            potassium_level = form.cleaned_data['potassium_level']
            temperature = form.cleaned_data['temperature']
            humidity_level = form.cleaned_data['humidity_level']
            ph_level = form.cleaned_data['ph_level']
            rainfall = form.cleaned_data['rainfall']

            # Extract soil data from form inputs
            soil_data = [form.cleaned_data[attr] for attr in [nitrogen_level, phosphorus_level, potassium_level, temperature, humidity_level, ph_level, rainfall]]
            
            # Make crop prediction using the loaded model
            predicted_crop = model.predict([soil_data])[0]
            
            # Render the result along with the template
            return render(request, 'crop_suggestion.html', {'predicted_crop': predicted_crop})
    else:
        form = SoilDataForm()
    
    return render(request, 'input_form.html', {'form': form})

def news(request):
    return render(request,'news.html')