import os

from celery import Celery
from celery.signals import setup_logging

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("cookiecutter_playground")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig

    from django.conf import settings

    dictConfig(settings.LOGGING)


"""
# /app
base_dir = os.getcwd()  # noqa: PTH109
task_folder = os.path.join(base_dir, "tasks")  # noqa: PTH118
if os.path.exists(task_folder) and os.path.isdir(task_folder):  # noqa: PTH110, PTH112
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("x") and filename.endswith(".py"):
            module_name = f"tasks.{filename[:-3]}"
            module = __import__(module_name, fromlist=["*"])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")
"""

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
