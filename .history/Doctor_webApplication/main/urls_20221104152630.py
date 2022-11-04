from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),    
    path('home/main', views.main, name = 'main'),
]
#! mostly done here!