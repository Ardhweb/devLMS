from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devlms.settings')

app = Celery('devlms')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    CELERY_POOL = 'solo',
    CELERY_BROKER_URL = f'sqla+sqlite:///{os.path.join(settings.BASE_DIR, "db.sqlite3")}',
    CELERY_RESULT_BACKEND = f'db+sqlite:///{os.path.join(settings.BASE_DIR, "db.sqlite3")}'
)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
