from re import template
from django.http import HttpResponse
from django.template import loader
from .models import Hero
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def main(request):
    hero = Hero()
    hero.title = "Welcome Here!"
    hero.description = Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eum fugit est omnis ut cum vel libero accusantium necessitatibus placeat, assumenda consequuntur dicta tempore iusto et?""