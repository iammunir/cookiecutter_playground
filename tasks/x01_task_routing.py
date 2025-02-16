"""
TASK ROUTING

- Efficient and intelligent distribution of tasks
- Process of determining the destination of tasks
- Allows you to control how tasks are dispatched to worker nodes

Benefit
- Improved Scalability
- Load Balancing
- Granular Control

Advanced Routing Techniques
    - Dynamic Routing based on Runtime Conditions
    - Routing based on Task Arguments or Context
    - Using External Routing Strategies or Plugins

"""

from celery import shared_task


@shared_task(name="tasks.task_routing.send_email")
def send_email(to, subject, message):
    print("sending email ....")  # noqa: T201
    # Code to send an email


@shared_task(name="tasks.task_routing.cleanup_database")
def cleanup_database():
    print("cleaning up database ....")  # noqa: T201
    # Code to clean up old database records
