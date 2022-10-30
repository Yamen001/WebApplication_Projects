from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('submit',views.submit_form),
    # path('login/', views.signin), #! not implemented yet
    # path('logout/', views.logout), #! implemented but 
    # path('signup/', views.signup), #! not implemented yet
]