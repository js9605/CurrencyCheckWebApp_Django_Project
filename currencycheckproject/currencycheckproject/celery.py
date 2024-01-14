from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab
from django import setup


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currencycheckproject.settings')

app = Celery('currencycheckproject.celery')
app.config_from_object('django.conf:settings', namespace='CELERY')

setup()  # Call Django setup to initialize the application
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Schedule periodic task to check currency values #TODO Not working [?] set up Celery Beat to schedule periodic tasks 
# Ive put it in func last time to check if  @app.task(bind=True) will trigger beat_schedule
# @app.task(bind=True)
# def main_celery():
#     app.conf.beat_schedule = {
#         'check-currency-every-hour': {
#             'task': 'currencycheckapp.services.notification_handler.fetch_currency_values_and_notify',
#             # 'schedule': crontab(minute=0, hour='*'),
#             'schedule': timedelta(minutes=2),
#             'args': (),
#             'kwargs': {
#                 'user_email_func': 'currencycheckapp.services.notification_handler.get_user_email',
#                 'currency_value_func': 'currencycheckapp.services.notification_handler.get_currency_value',
#                 'threshold_func': 'currencycheckapp.services.notification_handler.get_threshold',
#             },
#         },
#     }

#     app.conf.timezone = 'UTC'
    
app.conf.beat_schedule = {
    'check-currency-every-hour': {
        'task': 'currencycheckapp.services.notification_handler.fetch_currency_values_and_notify',
        # 'schedule': crontab(minute=0, hour='*'),
        'schedule': timedelta(minutes=2),
        'args': (),
        'kwargs': {
            'user_email_func': 'currencycheckapp.services.notification_handler.get_user_email',
            'currency_value_func': 'currencycheckapp.services.notification_handler.get_currency_value',
            'threshold_func': 'currencycheckapp.services.notification_handler.get_threshold',
        },
    },
}

app.conf.timezone = 'UTC'