from tasks.x01_task_routing import cleanup_database
from tasks.x01_task_routing import send_email


def run():
    send_email.apply_async(
        args=["user@example.com", "Welcome!", "Hello!"],
        queue="email_tasks",
    )
    cleanup_database.apply_async(queue="database_tasks")
