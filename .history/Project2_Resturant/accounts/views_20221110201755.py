from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            
        user = User.objects.create_user(username = username,first_name = first_name, last_name = last_name, email = email, password1 = password1)
        user.save();
        print("user created")
        return redirect('/')
    return render(request, 'register.html')
