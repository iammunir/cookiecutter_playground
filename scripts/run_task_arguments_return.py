import time

from celery.result import AsyncResult

from tasks.x07_task_arguments_return import add_numbers


def run():
    task = add_numbers.apply_async(args=[3, 8], kwargs={"message": "the result"})
    print(f"task_id: {task.id}")  # noqa: T201

    retrieved_result = AsyncResult(task.id)

    counter = 0
    limit = 20
    while retrieved_result.result is None and counter <= limit:
        print(retrieved_result.status)  # noqa: T201
        counter += 1
        time.sleep(1)

    print(retrieved_result.result)  # noqa: T201
