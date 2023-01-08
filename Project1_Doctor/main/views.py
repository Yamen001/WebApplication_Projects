from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registeration(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'main.html')

def login(request):
    return render(request,'login.html')

def logins(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = auth.authenticate(first_name = first_name, last_name = last_name)
        if user is not None:
            auth.login(request, user)
            return render('main.html')
        else:
            messages.info(request, 'invalid password')
            return render(request, 'login.html')
    else:
        return render('index.html')
     
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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, email = email, password = password1)
                user.save();
                print("user is created!")
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('login')
        # return redirect('/')
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def main(request):
    return render(request, 'main.html')