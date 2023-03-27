from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'main.html')

def logins(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'Signup.html')
        else:
            print(f'user logged in with username as {username} and password as {password}')
            return render(request, 'main.html')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already registered')
                print('user exists')
                return redirect('Signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                print('email addess is not valid')
                return redirect('Signup')
            else:
                user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, email = email, password = password1)
                user.save();
                print("user is created!")
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('login')
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def Signup(request):
    return render(request, 'index.html')