from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    crop_mapping = {
        0 : 'Apple', 1 : 'Banana', 2 : 'Black Gram', 3 : 'Chickpea', 4 : 'Coconut', 5 : 'Coffee', 6 : 'Cotton', 7 : 'Grapes', 8 : 'Jute', 9 : 'Kidney Beans', 10 : 'Lentil', 11 : 'Maize', 12 : 'Mango', 13 : 'Moth Beans', 14 : 'Mung Beans', 15 : 'Muskmelon', 16 : 'Orange', 17 : 'Papaya', 18 : 'Pigeon Peas', 19 : 'Poomogranate', 20 : 'Rice', 21 : 'Watermelon'
    }

    if request.method == 'POST':
            
            nitrogen_level = float(request.POST['nitrogen_level'])
            phosphorus_level = float(request.POST['phosphorus_level'])
            potassium_level = float(request.POST['potassium_level'])
            temperature = float(request.POST['temperature'])
            humidity_level = float(request.POST['humidity_level'])
            ph_level = float(request.POST['ph_level'])
            rainfall = float(request.POST['rainfall'])

            with open("crop_pkl", 'rb') as file:
                model = pickle.load(file)

            soil_data = [nitrogen_level, phosphorus_level, potassium_level,
                     temperature, humidity_level, ph_level, rainfall]
            
            predicted_crop_index = model.predict([soil_data])[0]

            predicted_crop = crop_mapping.get(predicted_crop_index, 'Unknown Crop')
            
            return render(request, 'result.html', {'predicted_crop': predicted_crop})
    
    return render(request, 'crop.html')


import requests
from django.shortcuts import render
from datetime import datetime

def get_rain(request):
    if request.method == 'POST':
        user_api = "dd831f307390d80448eadc841767b847"
        location = request.POST.get('city_name')
        date = request.POST.get('date')
        
        # Integrate soil data with the weather API request
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        # Extract weather data
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        date_time = date

        # Render the template with weather and soil data
        return render(request, 'weather_and_soil.html', {
            'location': location,
            'date_time': date_time,
            'temp_city': temp_city,
            'weather_desc': weather_desc,
            'hmdt': hmdt,
        })
    else:
        return render(request, 'weather.html')

# def news(request):
#     return render(request, 'news.html')
    
def predict(request):
    return render(request,'predict.html')