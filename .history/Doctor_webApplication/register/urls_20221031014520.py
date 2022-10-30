from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('submit',views.submit_form),
     #! not implemented yet
    # path('login/', views.signin),
     #! implemented but not been tested yet!!!
    # path('logout/', views.logout),
    # path('signup/', views.signup), #! not implemented yet
]
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE