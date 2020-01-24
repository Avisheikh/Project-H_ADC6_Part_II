
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('update/',update_profile)

]


