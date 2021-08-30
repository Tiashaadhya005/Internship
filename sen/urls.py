"""sen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from sen import celapp
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("pysen.urls")),
    path("addsen",include("pysen.urls")),
    # path("celtask",include('celapp.urls')),
    # path("cell",include('celapp.urls')),
    path("threads", include('pysen.urls')),
    path("additem",include('pysen.urls')),
    path("update", include('pysen.urls')),
    path("find", include('pysen.urls')),
    path("deletepost", include('pysen.urls')),
    path('celtask', include('celapp.urls')),
    # path('celli', include('celapp.urls')),
    path('reglog',include('flr.urls')),
    path('register',include('flr.urls')),
    path('login',include('flr.urls')),
    path('show',include('flr.urls')),
]
