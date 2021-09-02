from django.core import validators
from django.core.checks import messages
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_email
from django.shortcuts import redirect, render

# Create your models here.
class User_lists(models.Model):
    id=models.IntegerField(primary_key=True)
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Email=models.EmailField(EmailValidator)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=50)
    Mobile_No=models.CharField(max_length=10,default="0000000000")
    person=models.Manager() #created custome manager


    def __str__(self):
        return self.Username+" "+self.Password

    #validating username
    def validate_Username(self,value):
        a=User_lists.person.filter(Username=value)
        if a==None:return value
        else:
            raise ValidationError(_('Username already used'), code='Username already used')
            #("Username already used.Use another")

    
    # def checkuser(self,Username):
    #     a=User_lists.person.filter(Username=Username)
    #     if a!=None:return False
    #     return True


    def isvalid(self):
        try:
            if EmailValidator(message=None, code=None, allowlist=None):
                return True
        except Exception as err:
            return "Give an valid email address"


    def checkss(username,password):
        #used filter function from the base class for checking purpose
        d=User_lists.person.filter(Username=username,Password=password)
        l=len(d)
        # print(l)
        if l==0:return False
        else:return True
        
    def get_queryset():
        '''used the parent class function and modified it for my requirement'''
        return User_lists.person.get_queryset().order_by("Firstname")


