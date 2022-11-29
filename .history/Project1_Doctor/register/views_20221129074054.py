from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Member
# Create your views here.

def index(request):
    if request.method == 'POST':
        # member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user = auth.authenticate(username = username, password = password, firstname = firstname, lastname = lastname )
        
        if user is not None:
            auth.login(request,user)
            return redirect('register.html')
        else:
            messages.info(request, 'invalid password')
            return redirect('login')
    else:
        return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if username is not None and password is not None:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already registered')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('index')
            else:
                user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, email = email, password = password1)
                user.save();
                # print("user created") VALIDATION ONLY FROM TERMINAL
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('register')
        # return redirect('/')
    else:
        return render(request, 'index.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')