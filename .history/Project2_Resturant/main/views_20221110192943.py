from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        firstname = request.POST('firstname')
        lastname = request.POST('lastname')
        Email = request.POST('Email')
        Password = request.POST.get('Password')
    return render(request, 'login.html')
