from configurations import importer
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test-project.config')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TEST-PROJECT-WEB.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


importer.install()


app = Celery('test-project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


