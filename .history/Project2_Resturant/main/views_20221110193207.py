from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        firstname = request.POST('firstname')
        lastname = request.POST('lastname')
        email = request.POST('Email')
        password = request.POST('Password')
        phone_number = request.POST('ahone_Number')
        address = request.POST('Aaddress')
        user = User.objects.create_user(firstname = firstname, lastname = lastname, email = email, password = password, phone_number = phone_number,address = address)
    return render(request, 'login.html')
