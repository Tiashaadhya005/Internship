from .models import User_lists
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages


#from models import user_list
# Create your views here.

#it is the function which return a html template by which we can register or log 
def index_for_reg_log(request):
    return render(request, "index_reg_log.html")


def register(request):
    if request.method =='POST':
        Firstname=request.POST.get('Firstname','')
        Lastname=request.POST.get('Lastname','')
        Email=request.POST.get('email','')
        Username=request.POST.get('username','')
        password=request.POST.get('password','')
        Mobile_No=request.POST.get('mobile_no'," ")
        u=User_lists(Username=Username, Password=password, Email=Email, Firstname=Firstname, Lastname=Lastname, Mobile_No=Mobile_No)
        u.save()
        #print('Saved!')
        return redirect('/')
    else:return render(request,"register.html")



def login(request):
    if request.method=='POST':
        Username= request.POST.get("Username","")
        Password= request.POST.get("Password","")
        u=User_lists.checkss(Username,Password)
        if u==True :
            messages.info(request, 'Login Successful')
            return redirect('/')
        else:
            #return HttpResponse("invalid login")
            messages.info(request,"Invalid login")
            return render(request,'login.html')

    else:return render(request,"login.html")

def show(request):
    person_all=User_lists.get_queryset().order_by('Firstname')
    print(person_all)
    return render(request, 'show.html', {"person_all":person_all})