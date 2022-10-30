from django.shortcuts import render, HttpResponse
from register.models import Register
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request, "register.html")



def submit_form(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Phone_Number = request.POST['Phone_Number']
        Home_Address = request.POST['Home_Address']
        Gender = request.POST['Gender']
        Register(First_Name=First_Name, Last_Name=Last_Name)
        msg = "Form submitted successfully"
        return render(request,"register.html",{"msg" : msg})
    else:
        return HttpResponse("404 - Not Found")
    
def logout(request):
    logout(request)
    return render(request,"logout.html")

#!-- NOTE: logout.html does not exist yet

def login(request):
    firstname = request.POST['firstname']
    lastname = request.POST