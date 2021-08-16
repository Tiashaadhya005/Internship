from django.shortcuts import redirect, render
from .tasks import *

# Create your views here.

def celtask(request):
    add.delay(3,5)
    return render(request,"index.html")

def celli(request):
    return redirect('/')
