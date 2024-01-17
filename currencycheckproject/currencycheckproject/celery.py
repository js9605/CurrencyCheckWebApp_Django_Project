from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab
from django import setup


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currencycheckproject.settings')

app = Celery('currencycheckproject.celery')
app.config_from_object('django.conf:settings', namespace='CELERY')

setup() # Call Django setup to initialize the application
# app.autodiscover_tasks() # Instead of relying on autodiscovery, explicitly specify the task name in your Celery beat schedule

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Schedule periodic task to check currency values 
# TODO Not working [?]
app.conf.beat_schedule = {
    'check-currency-every-hour': {
        'task': 'currencycheckapp.services.notification_handler.fetch_currency_values_and_notify',
        # 'schedule': crontab(minute=0, hour='*'),
        'schedule': timedelta(minutes=2),
    },
}

app.conf.timezone = 'UTC'