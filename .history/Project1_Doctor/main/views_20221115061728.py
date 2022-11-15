from django.http import HttpResponse, render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import logout
from . import views
def index(request): 
    return render(request, 'index.html')
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())



def Logout(request):
    logout(request)
    return render(request, 'logout.html')
    