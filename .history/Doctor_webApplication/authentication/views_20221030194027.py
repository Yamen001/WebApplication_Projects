from django.shortcuts import render, redirect
from django.http import HttpResponse
from doctor import settings

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")