from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        firstname = request.POST('firstname')
        lastname = request.POST('lastname')
        email = request.POST('email')
        password = request.POST('password')
        phone_number = request.POST('phone_number')
        address = request.POST('address')
        user = User.objects.create_user(firstname = firstname, lastname = lastname, email = email, password = password, phone_number = phone_number,address = address)
        user.save();
        print("user created")
    return render(request, 'login.html')
