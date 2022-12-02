from django.shortcuts import redirect, render
from .models import Chef_One,Chef_Two,Chef_Three,Chef_Four,Chef_Five
# Create your views here.
def index(request):
    return render(request, 'index.html')

def chefs(request):
    #! CHEF_1 INFORMATION IS HERE!
    chef1 = Chef_One()
    chef1.name = "ali"
    chef1.profession = "Pizza"
    chef1.img = 'imgs/chef1.jpeg'
    chef1.desc = "leorm text here"
    chef1.phone = 963-993-211-788
    chef1.age = 22
    # -----------------------------
    #! CHEF_2 INFORMATION IS HERE!
    chef2 = Chef_Two()
    chef2.name = "Mansour"
    chef2.profession = "Pizza"
    chef2.img = 'imgs/chef1.jpeg'
    chef2.desc = "leorm text here"
    chef2.phone = 963-993-211-788
    chef2.age = 22
    # -----------------------------
    #! CHEF_3 INFORMATION IS HERE!
    chef3 = Chef_Three()
    chef3.name = "lili"
    chef3.profession = "Pizza"
    chef3.img = 'imgs/chef1.jpeg'
    chef3.desc = "leorm text here"
    chef3.phone = 963-993-211-788
    chef3.age = 22
    #------------------------------
    #! CHEF_4 INFORMATION IS HERE!
    chef4 = Chef_Four()
    chef4.name = "Sally"
    chef4.profession = "Pizza"
    chef4.img = 'imgs/chef1.jpeg'
    chef4.desc = "leorm text here"
    chef4.phone = 963-993-211-788
    chef4.age = 22
    #------------------------------
    #! CHEF_5 INFORMATION IS HERE!
    chef5 = Chef_Five()
    chef5.name = "mohammad"
    chef5.profession = "Pizza"
    chef5.img = 'imgs/chef1.jpeg'
    chef5.desc = "leorm text here"
    chef5.phone = 963-993-211-788
    chef5.age = 22