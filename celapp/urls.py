from django.urls import path,include
from .views import celli,celtask

urlpatterns = [
    path('/celtask', celtask, name='celtask'),
    path('celli', celli, name='celli')
]
