from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import logout
from . import views
def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())



def Logout(request):
    logout(request)
    return render(request, 'logout.html')
    