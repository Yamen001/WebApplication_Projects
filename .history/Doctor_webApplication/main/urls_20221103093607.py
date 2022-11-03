from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_member/', views.register, name='addrecord'),
    path('login/', views.login, name = 'login'),
    url(r'^/login/' , login_view, name='logout_view')
]
#! mostly done here!