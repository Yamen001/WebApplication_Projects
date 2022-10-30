from django.shortcuts import render, HttpResponse
from register import Register

# Create your views here.
def home(request):
    return render(request, "Register.html")


def submit_form(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Phone_Number = request.POST['Phone_Number']
        Home_Address = request.POST['Home_Address']
        Gender = request.POST['Gender']
