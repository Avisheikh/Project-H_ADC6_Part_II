from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path('', signupform, name='signup'),
    path('save/', signupform_save),
    path('signin/',signinform, name='signin'),
    path('signin/login/',signinauth),
    path('signout/',signout, name='signout'),
    
    
]