from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('regis', views.login, name = 'login'),
]