from django.shortcuts import redirect, render, HttpResponse
from urllib3 import HTTPResponse
from register.models import Register
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request, "register.html")

def submit_form(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        # Phone_Number = request.POST['Phone_Number']
        # Home_Address = request.POST['Home_Address']
        # Gender = request.POST['Gender']
        Register(First_Name=First_Name, Last_Name=Last_Name)
        msg = "Form submitted successfully"
        return render(request,"main.html",{"msg" : msg}) #! if success redirect to main page
    else:
        return HttpResponse("404 - Not Found") #! debugging not started -- if user didnt fill all redirected to main.html ( WRONG )

def logout(request):
    return render(request, 'logout.html')

#!-- NOTE: logout.html does not exist yet

def login(request):
    return render(request,"Accepted.html")


def authenticated_user(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    user = authenticate(request, firstname = firstname, lastname = lastname)
    if user is not None:
        login(request, user)
        # redirect to a success page!
        return redirect(request, 'main.html')
    else:
        # return an invalid login error message
        return render(request, 'Login.html')
    
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE

