from django.db import models

# Create your models here.
class Register(models.Model):
    First_Name = models.CharField(max_length = 50)
    Last_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=15)