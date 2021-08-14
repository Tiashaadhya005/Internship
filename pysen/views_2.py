#from sen.utils import get_coll, get_db
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from pymongo import MongoClient
from pymongo.message import delete
from pymongo.operations import DeleteOne
import utils
import time

db_name,client=utils.get_db()  #for storing the database name and  instances 
coll_name=utils.get_coll()     #for storing the collection name

# following functions are for checking crud operation in pymongo

def additem(request):
    #for adding entries in mongodb
    if request.method =='POST':
        _id=request.POST.get('id','')
        Firstname=request.POST.get('Firstname','')
        post=request.POST.get('post','')
        #print(db_name,coll_name)
        coll_name.insert_one({'_id':_id,'Firstname':Firstname, 'post':post})
        # the above line will save user given id, firstname and post inside the key id,firstname and post respectively
        print('Saved!')
        messages.info(request,"Successfully Created")
        return redirect('/')
    else:return render(request,"addpost.html")

def finditem(request):
    #for read operation in mongodb
    if request.method == 'POST':
        key=request.POST.get('key','') #the key should be the firstname to find the particular post 
        getval=list(coll_name.find({'Firstname': key}))
        if len(getval) !=0:
            for value in getval:
                #for printing all the posts with the same firstname
                messages.info(request,value["post"])
                print(value["post"])
                time.sleep(1)
            print("Some records are there ")
        else:print("nothing there")
        return redirect('/')
    else:return render(request, "read.html")


def updateitem(request):
    #for update opertion in mongodb
    if request.method == 'POST':
        key=request.POST.get('key','')
        newpost=request.POST.get('newpost',"")
        updatedval=coll_name.find_one_and_update({'Firstname':key},{"$set":{'post':newpost}})#to find that name and update the corresponding post
        print(updatedval)
        return redirect('/')
        # updated_val={"$set":{'post':newpost}}
        # coll_name.update_one(key,updated_val)
    else:return render(request,'modify.html')
    

def deleteitem(request):
    #for delete operation in mongodb
    if request.method == 'POST':
        key=request.POST.get('key','')
        deletedvalue=coll_name.delete_one({'Firstname':key})
        print(deletedvalue)
        return redirect('/')
    else:return render(request,'delete.html')