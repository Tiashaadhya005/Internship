from __future__ import absolute_import , unicode_literals
from celery import shared_task
from time import sleep

@shared_task
def add(a,b):
    return a+b

@shared_task
def mul(x, y):
    return x * y
