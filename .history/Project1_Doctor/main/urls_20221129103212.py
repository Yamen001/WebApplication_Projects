from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('Logout/', views.logout, name='logout'),
    path('register', views.register, name = 'register'),
    #! debugging for url mapping(''
    path('index.html', views.index, name='index'),
    path('', views.login, name='login'),
]
#! mostly done here!






if test > 10:
    print("hello") else: print ('jo'