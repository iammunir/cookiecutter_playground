import datetime
import sys

from celery import shared_task
from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import PeriodicTask


@shared_task(queue="default")
def task_clocked():
    print(f"[Clocked] Task executed at {datetime.datetime.now()}")


def create_task_clocked():
    # 3. CLOCKED SCHEDULE
    # Schedule a task to run once at a specific future time.
    # For example, run 5 minutes from now.
    clocked_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    clocked_schedule, _ = ClockedSchedule.objects.get_or_create(
        clocked_time=clocked_time
    )
    PeriodicTask.objects.update_or_create(
        name="One-off Clocked Task",
        defaults={
            "clocked": clocked_schedule,
            "task": "cookiecutter_playground.newapp.task.x20_task_beat_clocked.tasks.task_clocked",
            "one_off": True,  # Mark as one-off execution.
            "args": "[]",
        },
    )
    sys.stdout.write("Created clocked schedule: One-off Clocked Task")
