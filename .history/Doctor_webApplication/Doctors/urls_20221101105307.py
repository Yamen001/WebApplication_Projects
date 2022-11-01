from django.urls import path

urlpatters = [
    path('', views.Doctors, name = 'Doctors')
]