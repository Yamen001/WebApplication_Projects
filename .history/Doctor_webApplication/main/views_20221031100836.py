from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Hero
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def text(request):
    text = text()
    hero.title = "Welcome Here!"
    hero.sub_title = "We are so happy to be in your service"
    hero.description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eum fugit est omnis ut cum vel libero accusantium necessitatibus placeat, assumenda consequuntur dicta tempore iusto et"
    return render(request, 'main.html', {'text': text})