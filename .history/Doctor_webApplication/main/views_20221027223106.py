from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,logout, auth
from django.template import loader
from .models import Hero
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def main(request):
    hero = Hero()
    hero.title = "Welcome Here!"
    hero.sub_title = "We are so happy to be in your service"
    hero.description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eum fugit est omnis ut cum vel libero accusantium necessitatibus placeat, assumenda consequuntur dicta tempore iusto et"
    return render(request, 'main.html', {'hero': hero})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('main:homepage')