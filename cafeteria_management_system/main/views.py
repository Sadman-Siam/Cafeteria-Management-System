from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello, world. You're at the main index.<h1>")
def v1(response):
    return HttpResponse("<h1>view 1<h1>")
