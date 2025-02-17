import logging

from celery import shared_task

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(actime)s %(levelname)s %(message)s",
)

"""
from celery import Task
from config.celery_app import app

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("connection error occurred")
        else:
            print(f"{task_id!r} failed: {exc!r}")  # noqa: T201
            # perform additional error handling

app.Task = CustomTask
"""


def get():
    msg = "connection error occurred"
    raise ConnectionError(msg)


@shared_task(queue="default")
def get_data():
    try:
        get()
    except ConnectionError as exc:
        logging.exception("error occurred", repr(exc))  # noqa: PLE1205, TRY401
        # raise ConnectionError(repr(exc)) from exc  # noqa: ERA001
        # perform actual error handling
