from django.shortcuts import render
from .models import order, cart
from store.models import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages


# Create your views here.
# Create your views here.
# def show_cart(request,id):
#     get_product = product.objects.get(id=id)
#     try: 
#         get_cart = cart()
#         get_cart.products.add(get_product)
#     except ValueError:
#         get_cart.save()
#         get_cart.products.add(get_product)

#     get_all = get_cart.products.all()
#     context = {
#         "get_product":get_all
#     }
#     return render(request,'cart.html',context)


def get_user_pending_order(request):
    user_profile = get_object_or_404(User, username=request.user)
    order = cart.objects.filter(user=user_profile)
    if order.exists():
        return order[0]

    return 0


def add_to_cart(request,id):
    user_profile = get_object_or_404(User, username=request.user)
    products = product.objects.get(id=id)
    order_item, status = order.objects.get_or_create(products=products)
    user_order, status = cart.objects.get_or_create(user=user_profile)
    user_order.items.add(order_item)
    
    if status:
        user_order.save()
    
    return redirect(reverse('carts'))


def delete_from_cart(request,id):
    item_to_delete = order.objects.filter(pk=id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('carts'))


def cart_details(request):
    show_order = get_user_pending_order(request)
    context = {
        'order':show_order
    }
    return render(request,'cart.html',context)




