from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import logout
from .models import text
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def LogOut(request):
    logout(request)
    return render(request, 'logout.html')