from django.shortcuts import redirect, render
from .tasks import *

# Create your views here.

def celtask(request):
    res1=add.delay(3467,5987)
    res1.get()
    return render(request,"index.html")

def celli(request):
    res2=mul.delay(7890,7865)
    res2.get()
    return redirect('/')
