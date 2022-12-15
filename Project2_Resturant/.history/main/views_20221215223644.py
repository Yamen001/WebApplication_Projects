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
    chef1.img = 'static/imgs/chef_1.jpeg'
    chef1.desc = "leorm text here"
    chef1.age = 123
    # -----------------------------
    #! CHEF_2 INFORMATION IS HERE!
    chef2 = Chef_Two()
    chef2.name = "Mansour"
    chef2.profession = "Pizza"
    chef2.img = 'static/imgs/chef_2.jpeg'
    chef2.desc = "leorm text here"
    chef2.age = 29
    # -----------------------------
    #! CHEF_3 INFORMATION IS HERE!
    chef3 = Chef_Three()
    chef3.name = "lili"
    chef3.profession = "Pizza"
    chef3.img = '/static/imgs/chef_3.jpg'
    chef3.desc = "leorm text here"
    chef3.age = 45
    #------------------------------
    #! CHEF_4 INFORMATION IS HERE!
    chef4 = Chef_Four()
    chef4.name = "Sally"
    chef4.profession = "Pizza"
    chef4.img = '/static/imgs/chef_4.jpg'
    chef4.desc = "leorm text here"
    chef4.age = 39
    #------------------------------
    #! CHEF_5 INFORMATION IS HERE!
    chef5 = Chef_Five()
    chef5.name = "mohammad"
    chef5.profession = "Pizza"
    chef5.img = '/static/imgs/chef_5.jpg'
    chef5.desc = "leorm text here"
    chef5.age = 28
    
    # chefs = [chef1, chef2,chef3,chef4,chef5]
    return render(request, 'chefs.html', {'chef1': chef1, 'chef2': chef2, 'chef3': chef3, 'chef4': chef4, 'chef5': chef5})

def contact(request):
    return render(request, 'contact.html')

def handleBlog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')