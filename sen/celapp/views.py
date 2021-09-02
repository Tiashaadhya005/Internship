from django.shortcuts import redirect, render
from .tasks import *

# Create your views here.

def celtask(request):
    a=add.delay(35,5)
    a.get()
    return render(request,"index.html")

def celli(request):
    mul.delay(55,899)
    return redirect('/')
