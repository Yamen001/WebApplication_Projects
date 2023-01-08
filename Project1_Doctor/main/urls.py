from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name  = 'index'),
    path('index', views.index, name = 'index'),
    
    #! testing urls
    path('logins', views.index, name = 'logins'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('main', views.main, name = 'main'),
]