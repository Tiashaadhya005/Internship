from __future__ import absolute_import , unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','sen.settings')
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379')
app = Celery('sen')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
#inside paranthesis lambda: settings.INSTALLED_APPS
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
