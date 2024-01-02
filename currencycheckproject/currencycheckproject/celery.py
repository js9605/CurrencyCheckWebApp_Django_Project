from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django import setup
from django.apps import apps

print(f"DEBUG: DJANGO_SETTINGS_MODULE={os.environ['DJANGO_SETTINGS_MODULE']}")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ['DJANGO_SETTINGS_MODULE'])
app = Celery('currencycheckproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

setup()  # Call Django setup to initialize the application

def autodiscover_tasks():
    for app_config in apps.get_app_configs():
        # Look for celery_tasks.py instead of tasks.py
        app_config_path = app_config.path.replace('.', '/')
        app_tasks_module = f'{app_config_path}/tasks/celery_tasks.py'
        try:
            __import__(app_tasks_module)
        except ImportError:
            print("ImportError in celery.py")

# custom function
autodiscover_tasks()