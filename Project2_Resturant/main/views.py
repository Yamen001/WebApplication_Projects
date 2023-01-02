from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def handleBlog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def chefs(request):
    return render(request, 'chefs.html')


def order(request):
    return render(request, 'order.html')

def error_404_view(request,exception):
    return render(request, '404_error.html')