import datetime
import sys

from celery import shared_task
from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import SolarSchedule


@shared_task(queue="default")
def task_solar():
    print(f"[Solar] Task executed at {datetime.datetime.now()}")


def create_task_solar():
    # 4. SOLAR SCHEDULE
    # Schedule a task based on a solar event (e.g., sunrise).
    # Replace latitude and longitude with your location.
    solar_schedule, _ = SolarSchedule.objects.get_or_create(
        event="sunrise",  # Other options: "sunset", "dawn", "dusk", etc.
        latitude=40.7128,  # Example: New York City latitude
        longitude=-74.0060,  # Example: New York City longitude
    )
    PeriodicTask.objects.update_or_create(
        name="Task at Sunrise",
        defaults={
            "solar": solar_schedule,
            "task": "your_app.tasks.task_solar",
            "args": "[]",
        },
    )
    sys.stdout.write("Created solar schedule: Task at Sunrise")
