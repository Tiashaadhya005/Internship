from django.contrib import admin
from django.urls import path,include
from . import views
from . import views_2

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.home, name='home'),
    path("addsen",views.addsen, name='addsen'),
    path("threads", views.threadss , name="threadss"),
    path("additem",views_2.additem, name="additem"),
    path("update", views_2.updateitem, name="update"),
    path("find", views_2.finditem, name="find"),
    path("deletepost", views_2.deleteitem, name="deletepost"),
]

