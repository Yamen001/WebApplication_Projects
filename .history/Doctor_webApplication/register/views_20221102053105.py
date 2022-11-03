from django.shortcuts import redirect, render, HttpResponse
from register.models import Register
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, "register.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        user = Register.objects.create_user(username = username, password = password,phone_number = phone_number, gender = gender)
        user.save();
        print("user created successfully")
        return redirect(request,"main.html") #! if success redirect to main page
    else:
        return HttpResponse("404 - Not Found") #! debugging not started -- if user didnt fill all redirected to main.html ( WRONG )

def logout(request):
    return render(request, 'logout.html')

#!-- NOTE: logout.html does not exist yet

def login(request):
    return render(request,"Accepted.html")


def authenticated_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        # redirect to a success page!
        return redirect(request, 'main.html')
    else:
        # return an invalid login error message
        return render(request, 'Login.html')
    
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE


#!----------------------------------------------------------------
#! DONT TOUCH THESE ATTRIBUTES
