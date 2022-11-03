from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_member/', views.register, name='addrecord'),

]
#! mostly done here!