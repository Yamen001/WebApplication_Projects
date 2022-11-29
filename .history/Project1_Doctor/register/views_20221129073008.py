from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.

def index(request):
    if request.method == 'POST':
        # member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user = auth.authenticate(username = username, password = password, firstname = firstname, lastname = lastname )
        
        if user is not None:
            auth.login(request,user)
            return redirect('')
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)

