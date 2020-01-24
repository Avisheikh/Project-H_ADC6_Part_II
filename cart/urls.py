from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path('cart/<int:id>/', add_to_cart, name='cart'),
    path('show_cart/',cart_details, name = 'carts'),
    path('show_cart/delete/<int:id>/', delete_from_cart, name='delete_item'),
  
    
    
]