from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if username is not None and password is not None:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already registered')
                return redirect('index')
            else:
                user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, password = password)
                user.save();
                # print("user created") VALIDATION ONLY FROM TERMINAL
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('index')
        # return redirect('/')
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')