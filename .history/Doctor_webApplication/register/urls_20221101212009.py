from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('S',views.register),
    #! login is implemented -- NOT BEED TESTED YET!!!
    path('Accepted/', views.login),
    path('logout/', views.logout),
    #! not implemented yet
]
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE