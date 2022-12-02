from django.shortcuts import redirect, render
from .models import Chef_One,Chef_Two,Chef_Three,Chef_Four,Chef_Five
# Create your views here.
def index(request):
    return render(request, 'index.html')

def chefs(request):
    chef1 = Chef_One()
    chef1.name = "ali"
    chef1.profession = "Pizza"
    chef1.img = 'imgs/chef1.jpeg'
    chef1.desc = "leorm text here"
    chef1.phone = 963-993-211-788
    chef1.age = 22
    return render(request, 'chefs.html', {'chef1': chef1})
    # chef1 = Chef_One()


#! CHEF_1 INFORMATION IS HERE!
#! CHEF_2 INFORMATION IS HERE!

#! CHEF_3 INFORMATION IS HERE!

#! CHEF_4 INFORMATION IS HERE!

#! CHEF_5 INFORMATION IS HERE!