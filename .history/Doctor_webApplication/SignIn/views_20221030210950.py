from django.http import HttpResponse
from django.shortcuts import render
from SignIn.models import Register
# Create your views here.

def index(request):
    return render(request, "register.html")