from django.urls import include, path
from django.conf.urls import patterns, include, url
from rest_framework import routers
from eboutique.views import *
from erp.views import *
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_member/', views.register, name='addrecord'),
    path('login/', views.login, name = 'login'),
]
#! mostly done here!