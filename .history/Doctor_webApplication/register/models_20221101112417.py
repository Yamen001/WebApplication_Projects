from django.db import models

# Create your models here.
clas=models.CharField(max_length=50)
    Last_Nas Register(models.Model):
    First_Nameme=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=15)
    Home_Address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.First_Name