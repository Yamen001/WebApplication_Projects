from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=14)
    email=models.CharField(max_length=255)
    Gender=models.CharField(max_length=10)
    
         = request.POST['email']
        gender = request.POST['gender']
    def __str__(self):
        return self.First_Name