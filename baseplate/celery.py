from __future__ import absolute_import, unicode_literals
import os
from celery import Celery,platforms

platforms.C_FORCE_ROOT = True   #允许root用户启动celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baseplate.settings')

app = Celery('baseplate')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

