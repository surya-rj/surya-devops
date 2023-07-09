from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("hello World")

def index2(request):
    t=loader.get_template("index.html")
    return HttpResponse(t.render())
