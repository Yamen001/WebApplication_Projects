from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=14)
    Gender=models.CharField(max_length=10)
    
    def __str__(self):
        return self.username