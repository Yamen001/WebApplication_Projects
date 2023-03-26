from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length = 255, verbose_name='username', null = False , blank = False)
    first_name = models.CharField(max_length = 255, verbose_name='firstname', null = False, blank= False)
    last_name = models.CharField(max_length = 255, verbose_name='lastname', null = False, blank= False)
    email = models.EmailField()
    password = models.CharField(max_length = 8)
    
    
    def __str__(self):
        return self.username
    
    
    
class Login(models.Model):
    username = models.CharField(max_length = 255, verbose_name='username', null = False , blank = False)
    password = models.CharField(max_length = 8)


#! testing both tables for user authentications
class Authentication():
    pass