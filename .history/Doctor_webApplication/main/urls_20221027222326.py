from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('', views.main, name = 'main'),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
]