from django.template import loader, Context
from django.http import HttpResponse 
from django.shortcuts import render
from notes.models import Note


def index(request):
    template = loader.get_template('index.html')
    context = Context()
    response = template.render(context)
    return HttpResponse(response)

def test(request):
    template = loader.get_template('test.html')
    context = Context()
    response = template.render(context)
    return HttpResponse(response)


