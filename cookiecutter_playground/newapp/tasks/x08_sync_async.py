from .x07_task_arguments_return import add_numbers


def execute_sync():
    task = add_numbers.apply_async(args=[3, 8], kwargs={"message": "the result"})
    task_result = task.get()
    print("Task is running synchronously")  # noqa: T201
    print(task_result)  # noqa: T201


def execute_async():
    task = add_numbers.apply_async(args=[3, 8], kwargs={"message": "the result"})
    task_result = task.result
    print("Task is running asynchronously")  # noqa: T201
    print(task_result)  # noqa: T201
