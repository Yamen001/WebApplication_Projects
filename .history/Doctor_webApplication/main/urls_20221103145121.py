from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_member/', views.register, name='login'),
    path('login/', views.login, name = 'home'),
    
]
#! mostly done here!