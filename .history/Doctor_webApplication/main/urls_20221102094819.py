from django.urls import include, path
from . import views
from 
urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.logout, name = "logout"),
]
#! mostly done here!