
### Task Timeout and Revoking in Celery with Django

**1. Task Timeout in Celery**
Task timeout ensures that a task does not run indefinitely. If a task exceeds a specified time limit, Celery will forcefully terminate it.
**How to Set Timeout for a Task?**
You can set a timeout for individual tasks or all tasks globally.

1. **Setting Timeout for an Individual Task**

```python
from celery import shared_task

@shared_task(time_limit=10)  # Task will be forcibly terminated after 10 seconds
def long_running_task():
    import time
    time.sleep(15)  # This will exceed the timeout and be killed
    return "Task completed"
```

2. **Setting Timeout Globally (For All Tasks)**
In `celery.py`:

```python
from celery import Celery

app = Celery('myproject')

app.conf.update(
    task_time_limit=10  # Applies to all tasks
)
```

**2. Revoking a Task in Celery**
Revoking a task allows you to cancel its execution.
**How to Revoke a Task?**  

- **If the Task Has Not Started Yet:**  You can revoke it safely.

- **If the Task Is Already Running:**  Revoking won't stop it unless `terminate=True` is used.

1. **Revoke a Task Before It Starts**

```python
from celery.result import AsyncResult

task = long_running_task.delay()
task_id = task.id

# Revoke the task before it starts
AsyncResult(task_id).revoke()
```

2. **Revoke a Running Task (Force Kill)**

```python
AsyncResult(task_id).revoke(terminate=True, signal='SIGKILL')
```

- `terminate=True`: Forces the task to stop.

- `signal='SIGKILL'`: Sends a termination signal to kill the task.
**When to Use Timeout vs. Revoking?** | Feature | Purpose |
| --- | --- |
| Timeout | Prevents tasks from running indefinitely. Use when you expect tasks to complete within a fixed duration. |
| Revoking | Cancels a task manually when it's no longer needed. Use for user-initiated cancellations or system shutdowns. |
