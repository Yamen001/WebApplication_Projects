from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout', views.logout)
]
#! mostly done here!