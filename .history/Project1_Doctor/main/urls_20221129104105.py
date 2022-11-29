from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index)
]
#! mostly done here!