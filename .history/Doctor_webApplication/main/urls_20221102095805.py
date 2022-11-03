from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('/logout', views.Logout, name = "logout"),
]
#! mostly done here!