from django.shortcuts import redirect, render
from .models import Chef_One,Chef_Two,Chef_Three,Chef_Four,Chef_Five
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def handleBlog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')