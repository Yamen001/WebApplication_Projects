from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def handleBlog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')