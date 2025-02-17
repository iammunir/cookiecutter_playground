from celery import chain
from celery import shared_task
from celery.signals import task_failure

from .x12_task_error_chain import add
from .x12_task_error_chain import result_info


@shared_task(queue="default")
def multiply_two_may_error(num):
    if num == 0:
        msg = "error multiplying 0"
        raise ValueError(msg)
    return num * 2


@shared_task(queue="dead_letter")
def save_failed_task(task_info):
    print("saving failed task", task_info)


@task_failure.connect
def handle_error(sender=None, exception=None, **kwargs):
    task_info = {
        "task_name": sender.name,
        "exception": str(exception),
    }
    save_failed_task.apply_async(args=[task_info], queue="dead_letter")


def run_task_chain():
    task_chain = chain(add.s(3, -3), multiply_two_may_error.s(), result_info.s())
    result = task_chain.apply_async()
    result.get()
