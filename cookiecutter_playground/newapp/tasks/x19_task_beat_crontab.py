import datetime
import sys

from celery import shared_task
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import PeriodicTask


@shared_task(queue="default")
def task_crontab():
    print(f"[Crontab] Task executed at {datetime.datetime.now()}")


def create_task_crontab():
    # 2. CRONTAB SCHEDULE
    # Run a task daily at 3:00 AM.
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="3",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
    )
    PeriodicTask.objects.update_or_create(
        name="Daily Task at 3 AM",
        defaults={
            "crontab": crontab_schedule,
            "task": "cookiecutter_playground.newapp.tasks.x19_task_beat_crontab.task_crontab",
            "args": "[]",
        },
    )
    sys.stdout.write("Created crontab schedule: Daily Task at 3 AM")
