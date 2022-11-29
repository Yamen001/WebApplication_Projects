from django.conf.urls import url
from . import views
from django.urls import path, include
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    path('home', include('main.urls')
    
]