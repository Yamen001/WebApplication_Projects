from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import text
def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# def text(request):
#     text = text()
#     text.name = ""
#     text.sub_title =
#     text.description = 
#     return render(request, 'main.html', {'text': text})