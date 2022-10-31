from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('submit',views.submit_form),
    
    #! login is implemented
    path('Accepted/', views.login),
     #! implemented but not been tested yet!!!
    # path('logout/', views.logout),
     #! not implemented yet
    # path('signup/', views.signup),
]
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE