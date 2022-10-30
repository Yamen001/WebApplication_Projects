from django.shortcuts import render, HttpResponse
from register import Register

# Create your views here.
def home(request):
    return render(request, "Register.html")


def submit_form(request):
    if request.method == "POST":
