from celery import shared_task


@shared_task()
def sub_numbers(num1, num2):
    return num1 - num2
