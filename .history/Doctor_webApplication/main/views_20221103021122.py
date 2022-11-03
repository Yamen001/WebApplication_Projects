from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import logout
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def LogOut(request):
    logout(request)
    return render(request, 'logout.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        user = User.objects.create_user(username = username, password = password,phone_number = phone_number, gender = gender)
        user.save();
        print("user created successfully")
        return redirect('/') #! if success redirect to main page
    else:
        print("404 - Not Found") #! debugging not started -- if user didnt fill all redirected to main.html ( WRONG )
    return redirect('/')