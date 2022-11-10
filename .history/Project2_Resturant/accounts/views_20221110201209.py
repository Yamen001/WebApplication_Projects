from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, email = email, password = password,address = address)
        user.save();
        print("user created")
        return redirect('/')
    return render(request, 'register.html')
