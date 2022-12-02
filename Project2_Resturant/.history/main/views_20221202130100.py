from django.shortcuts import redirect, render
from .models import Chef_One,Chef_Two,Chef_Three,Chef_Four,Chef_Five
# Create your views here.
def index(request):
    return render(request, 'index.html')


def chefs(request):
    chef1 = Chef_One()
    chef1.name = "Ali"
    return render(request, 'chefs.html', {'chef1': chef1})  # type: ignore)