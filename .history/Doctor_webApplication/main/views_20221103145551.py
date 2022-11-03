from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

from django.shortcuts import redirect
from . import views

def index_redirect(request):
    return redirect('/web/')

# def register(request):
#     username = request.POST.get['username']
#     password = request.POST.get['password']
#     phone_number = request.POST.get['phone_number']
#     gender = request.POST.get['gender']
#     Obj1 = Register(username = username, password = password,phone_number = phone_number, gender = gender)
#     Obj1.save()
#     return render(request, 'main.html',{'message': 'registered!'})