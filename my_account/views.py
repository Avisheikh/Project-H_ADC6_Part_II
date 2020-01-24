from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
# Create your views here.

def profile(request):
    return render(request,'profile.html')

# def profile_id(request,id):
#     get_id = User.objects.get(id=id)
#     return render(request,'profile.html',{'profileid':get_id})


# def profile_update(request):
#     if request.method == "GET":
#         return render(request,'profile.html')
#     else:
#         try:
#             user = User.objects.update_user(username=request.POST['u_name'],first_name= request.POST['f_name'], last_name = request.POST['l_name'],
#             email=request.POST['c_email'],password= request.POST['u_pass'] )
#             user.save()
#             messages.info(request,"Successfully Created.You can Sign In.")
#             return redirect('signin')

#         except IntegrityError:
#             messages.error(request,"Username Already Exists.Please Try again Another One.")
#             return redirect('profile')

# def profile_update(request):


def update_profile(request):
    if request.method == "GET":
        return render(request,'profile.html')
    
    elif request.user.is_authenticated:
        users = request.user
        user = User.objects.get(pk=users.id)
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email = request.POST['c_email']
        user.username= request.POST['u_name']
        user.set_password(request.POST['c_pass']) 
        user.save()
        return redirect('/')