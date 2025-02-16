from celery import chain
from celery import shared_task


@shared_task(queue="default")
def add(num1, num2):
    return num1 + num2


@shared_task(queue="default")
def multiply_two(num):
    if num == 0:
        msg = "error multiplying 0"
        # raise ValueError(msg)  # noqa: ERA001
        return {"error": msg}
    return num * 2


@shared_task(queue="default")
def result_info(result):
    if "error" in result:
        return f"error detected: {result['error']}"
    return f"this is the result: {result}"


def run_task_chain():
    task_chain = chain(add.s(3, -3), multiply_two.s(), result_info.s())
    result = task_chain.apply_async()
    result.get()
