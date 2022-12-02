from django.shortcuts import redirect, render
from .models import Chef_One,Chef_Two,Chef_Three,Chef_Four,Chef_Five
# Create your views here.
def index(request):
    return render(request, 'index.html')


def chefs(request):
    chef1 = Chef_One()
    chef.name = "Ali"
    return render(request, 'chefs.html', {'chef': Chef_One})