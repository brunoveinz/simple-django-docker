from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('<h1>MI APP DE DJANGO DOCKERIZADA</h1>')
