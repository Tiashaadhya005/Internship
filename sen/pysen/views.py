from django.shortcuts import render
from django.http import HttpResponse
from .threads import createdata, createdatatwo

# Create your views here.
def home(request):
    return render(request, "index.html")

#for checking threads in django
def threadss(request):
    firstthread=createdata() #creating an instance of the thread class
    firstthread.start() #start the thread
    secondthread=createdatatwo() #creating an instance of another thread class
    secondthread.start() #start that thread
    var=HttpResponse("It's threading page!") #will be executed in main thread
    firstthread.join()
    secondthread.join()
    return var
    

def addsen(request):
    #sentry error 1: this function is for creating an error to check sentry
    HttpResponse("Checking Error for sentry") 
