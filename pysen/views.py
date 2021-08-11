from django.shortcuts import render
from django.http import HttpResponse
from .threads import createdata, createdatatwo

# Create your views here.
def home(request):
    return HttpResponse("HEY USERS!!")

def threadss(request):
    c=createdata()
    c.start()
    d=createdatatwo()
    d.start()
    return HttpResponse("It's threading page!")
    

def addsen(request):
    HttpResponse("Checking Error for sentry")
