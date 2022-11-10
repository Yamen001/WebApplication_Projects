from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        user = User.objects.create_user(username = username,firstname = firstname, lastname = lastname, email = email, password = password, phone_number = phone_number,address = address)
        user.save();
        print("user created")
        return redirect('/')
    return render(request, 'register.html')
