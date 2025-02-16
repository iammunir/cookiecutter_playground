from tasks.x10_task_auto_retry import fetch_data


def run():
    fetch_data.apply_async()
