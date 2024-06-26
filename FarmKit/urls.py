"""
URL configuration for FarmKit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Farm.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('home', index, name='index'),
    path('about',about,name='about'),
    path('blog',blog,name='blog'),
    path('contact',contact,name='contact'),
    path('products',products,name='products'),
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('register',user_register,name='register'),
    path('crop',crop,name='crop'),
    path('crop_suggestion', crop_suggestion, name='suggest'),
    path('predict', predict, name='predict'),
    
    path('cart',cart,name='cart'),


]
