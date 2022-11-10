from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        Email = request.POST.get('Email')
        Password = request.POST.get('password')
    return render(request, 'login.html')
