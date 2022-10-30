from django.shortcuts import render
from SignIn.models import Register
# Create your views here.

def index(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Phone_Number = request.POST['Phone_Number']
        Home_Address = request.POST['Home_Address']
        Gender = request.POST['Gender']
        
        
        Register(First_Name, Last_Name, Phone_Number, Home_Address).save()
        msg = "form submitted successfully"
        return render(request, "Register.html",{msg: msg})