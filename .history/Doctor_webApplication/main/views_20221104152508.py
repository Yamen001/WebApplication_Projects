from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from . import views
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def main(request):
    template = loader,.get_template('main.html')
    return HttpResponse(template.render())