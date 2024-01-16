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


# Schedule periodic task to check currency values 
# TODO Not working [?] check_currency_threshold() missing 4 required positional arguments: 'user_email', 'currency_shortcut', 'currency_value', and 'threshold'
# the issue you're encountering is likely due to the asynchronous nature of Celery.
#  I can try doing: def fetch_currency_values_and_notify(user_email, currency_shortcut, currency_rates, threshold)
    # and passing kwargs like in commented chunk of code below 
app.conf.beat_schedule = {
    'check-currency-every-hour': {
        'task': 'currencycheckapp.services.notification_handler.fetch_currency_values_and_notify',
        # 'schedule': crontab(minute=0, hour='*'),
        'schedule': timedelta(minutes=2),
        # 'args': (),
        # 'kwargs': {
        #     # 'user_email_func': 'currencycheckapp.services.notification_handler.get_user_email',
        #     # 'get_currency_value': 'currencycheckapp.services.notification_handler.get_currency_value',
        #     # 'get_threshold': 'currencycheckapp.services.notification_handler.get_threshold',
        # },
    },
}

app.conf.timezone = 'UTC'