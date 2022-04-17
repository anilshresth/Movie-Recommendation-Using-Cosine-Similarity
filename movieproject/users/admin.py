from re import U
from django.contrib import admin
from .models import UserProfile, Movie

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)
