from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),    
    path('main/', views.main, name = 'main'),
    path('Logout/', views.logout, name = 'logout'),


#! debugging for url mapping
    p
]
#! mostly done here!