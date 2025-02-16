from celery import shared_task


@shared_task()
def add_numbers(num1, num2):
    return num1 + num2
