from django.shortcuts import redirect, render, HttpResponse
from .models import Register
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, "register.html")

# def logout(request):
#     return render(request, 'logout.html')

#!-- NOTE: logout.html does not exist yet

# def login(request):
#     return render(request,"Accepted.html")


# def authenticated_user(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username = username, password = password)
#     if user is not None:
#         login(request, user)
#         # redirect to a success page!
#         return redirect(request, 'main.html')
#     else:
#         # return an invalid login error message
#         return render(request, 'Login.html')