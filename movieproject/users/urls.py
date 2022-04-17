from unicodedata import name
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path("movie-form/", views.addmovieform, name='movie-form'),




]
