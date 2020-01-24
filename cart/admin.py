from django.contrib import admin
from .models import cart
from store.models import product

# Register your models here.
admin.site.register(product)
admin.site.register(cart)