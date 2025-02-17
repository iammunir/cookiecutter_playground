import time

from celery import shared_task


@shared_task(queue="default", time_limit=5)
def long_running_task():
    time.sleep(6)
    return "task completed successfully"


def execute_long_running_task():
    result = long_running_task.delay()
    try:
        task_result = result.get(
            timeout=4,
        )  # can revoke, the task does not throw an error, this operation does
        print(task_result)
    except TimeoutError:
        print("task timed out")

    # task = long_running_task.delay()
    # task.revoke(terminate=True)
