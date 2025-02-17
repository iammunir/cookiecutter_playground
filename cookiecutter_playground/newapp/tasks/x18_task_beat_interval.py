import datetime
import sys

from celery import shared_task
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask


@shared_task(queue="default")
def task_interval():
    print(f"[Interval] Task executed at {datetime.datetime.now()}")


def create_task_interval():
    # INTERVAL SCHEDULE
    # Run a task every 10 seconds.
    interval_schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )
    PeriodicTask.objects.update_or_create(
        name="Task Every 10 Seconds",
        defaults={
            "interval": interval_schedule,
            "task": "cookiecutter_playground.newapp.tasks.x18_task_beat_interval.task_interval",
            "args": "[]",  # Optional: pass args as JSON string.
        },
    )
    sys.stdout.write("Created interval schedule: Task Every 10 Seconds\n")
