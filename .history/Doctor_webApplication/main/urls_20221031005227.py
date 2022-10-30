from django.urls import include, path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('', views.text, name = 'text'),
]
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE