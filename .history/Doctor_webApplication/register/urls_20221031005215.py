from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('submit',views.submit_form),
    # path('login/', views.signin), #! not implemented yet
    # path('logout/', views.logout), #! implemented but not been tested yet!!!
    # path('signup/', views.signup), #! not implemented yet
]

#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE