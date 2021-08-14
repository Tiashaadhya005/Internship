from django.shortcuts import render
from django.http import HttpResponse
from .threads import createdata, createdatatwo

# Create your views here.
def home(request):
    return render(request, "index.html")

#for checking threads in django
def threadss(request):
    c=createdata()
    c.start()
    d=createdatatwo()
    d.start()
    return HttpResponse("It's threading page!")
    

def addsen(request):
    #sentry error -1: this function is for creating an error to check sentry
    HttpResponse("Checking Error for sentry") 
