from celery import group
from celery import shared_task


@shared_task(queue="default")
def process_data(num):
    if num == 3:  # noqa: PLR2004
        raise ValueError("error number")  # noqa: EM101, TRY003


def handle_result(result):
    if result.successful():
        print(f"task completed: {result.get()}")
    elif result.failed() and isinstance(result.result, ValueError):
        print(f"task failed: {result.result}")
    elif result.status == "REVOKED":
        print(f"task was revoked: {result.id}")


def run_process_data():
    task_group = group(process_data.s(i) for i in range(5))
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)

    for result in result_group:
        handle_result(result)
