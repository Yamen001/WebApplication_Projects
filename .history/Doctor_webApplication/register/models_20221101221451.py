from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=15)
    Home_Address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    
         = request.POST['username']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        gender = request.POST['gender']
    def __str__(self):
        return self.First_Name