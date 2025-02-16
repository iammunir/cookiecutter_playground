"""
https://docs.celeryq.dev/en/stable/userguide/routing.html#rabbitmq-message-priorities

from kombu import Exchange, Queue

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_queue_max_priority = 10
app.conf.task_default_priority = 5
app.conf.task_acks_late = True
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

"""
