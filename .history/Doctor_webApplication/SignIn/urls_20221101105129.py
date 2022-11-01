from django.urls import path

urlpatterns = [
    path('', views.SignIn, name = 'SignIn')
]