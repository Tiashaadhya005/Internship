from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('reglog', views.index_for_reg_log, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('show', views.show, name="showdata"),


]
