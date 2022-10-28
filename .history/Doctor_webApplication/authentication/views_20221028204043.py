from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessag, send_mail
from doctor import settings
from django.contrib.sites.shortcuts import get0
# Create your views here.
