from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import logout
from .models import Register

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         phone_number = request.POST['phone_number']
#         gender = request.POST['gender']
#         user = Register(username = username, password = password,phone_number = phone_number, gender = gender)
#         user.save()
#         print("user created successfully")
#         return redirect('/') #! if success redirect to main page
#     else:
#         print("404 - Not Found") #! debugging not started -- if user didnt fill all redirected to main.html ( WRONG )
#     return redirect('/')


def add(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
