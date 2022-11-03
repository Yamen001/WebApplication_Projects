from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
# Create your views here.
class LoginView(TemplateView):
    template_name = templates/login.html