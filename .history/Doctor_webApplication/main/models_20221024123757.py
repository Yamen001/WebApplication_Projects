from django.db import models
from .templates import img
# Create your models here.


class logo:
    id : int
    img = 'logo.png'
    
    
class Hero:
    id : int
    title : str
    description : str
    img : ''