"""
https://docs.celeryq.dev/en/stable/userguide/routing.html#redis-message-priorities

app.conf.broker_transport_options = {
    'queue_order_strategy': 'priority',
}

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

['celery', 'celery:1', 'celery:2', 'celery:3', 'celery:4', 'celery:5', 'celery:6', 'celery:7', 'celery:8', 'celery:9']


"""  # noqa: E501
