from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery


print(f"DEBUG: DJANGO_SETTINGS_MODULE={os.environ['DJANGO_SETTINGS_MODULE']}")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ['DJANGO_SETTINGS_MODULE'])
app = Celery('currencycheckproject')
app.config_from_object('django.conf:settings', namespace='CELERY')