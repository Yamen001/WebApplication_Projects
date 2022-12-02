from django.shortcuts import redirect, render
from .models import models
# Create your views here.
def index(request):
    return render(request, 'index.html')


def chefs(request):
    chef = Chef_One()
    return render(request, 'chefs.html')