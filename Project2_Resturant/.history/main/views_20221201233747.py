from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    return render(request, 'index.html')


def chefs(request):
 = Chef_One()
    return render(request, 'chefs.html')