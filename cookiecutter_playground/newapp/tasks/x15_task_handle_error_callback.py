import sys

from celery import shared_task


@shared_task(queue="default")
def task_throw_error():
    msg = "something went wrong..."
    raise ValueError(msg)


@shared_task(queue="default")
def process_task_result(result):
    sys.stdout.write("process task result")
    sys.stdout.write(result)
    sys.stdout.flush()


@shared_task(queue="default")
def error_handler(task_id, exc, traceback):
    sys.stdout.write(">>>>>")
    sys.stdout.write(str(exc))
    sys.stdout.write(">>>>>")
    sys.stdout.flush()


def run_task():
    task_throw_error.apply_async(
        link=[process_task_result.s()],
        link_error=[error_handler.s()],
    )
