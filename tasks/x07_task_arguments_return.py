import time

from celery import shared_task


@shared_task(queue="default")
def add_numbers(num1, num2, message=None):
    time.sleep(5)
    if message is None:
        return f"{num1 + num2}"
    return f"{message}: {num1 + num2}"
