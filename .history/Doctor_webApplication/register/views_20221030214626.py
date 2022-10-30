from django.shortcuts import render, HttpResponse
from register.models import Register

# Create your views here.
def index(request):
    return render(request, "templates/SignIn.html")


def submit_form(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Phone_Number = request.POST['Phone_Number']
        Home_Address = request.POST['Home_Address']
        Gender = request.POST['Gender']
        Register(First_Name=First_Name, Last_Name=Last_Name)
        msg = "Form submitted successfully"
        return render(request,"SignIn.html",{"msg" : msg})
    else:
        return HttpResponse("404 - Not Found")