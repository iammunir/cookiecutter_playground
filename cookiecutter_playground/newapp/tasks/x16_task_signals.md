### Task Signals, Graceful Shutdown, and Cleanup of Failed Tasks in Celery with Django

Celery provides **Task Signals**  that allow you to hook into different stages of a task's lifecycle, which is useful for monitoring, logging, and performing cleanup operations.

1. **Task Signals in Celery**
Celery has built-in signals that can be used to track task execution. Some commonly used ones include:

- **`task_prerun`** : Triggered before a task starts.

- **`task_postrun`** : Triggered after a task completes (regardless of success or failure).

- **`task_success`** : Triggered when a task completes successfully.

- **`task_failure`** : Triggered when a task fails.

- **`task_retry`** : Triggered when a task is retried.

##### Example: Logging Task Execution

You can use these signals to log or track task execution.

```python
from celery.signals import task_prerun, task_success, task_failure
import logging

logger = logging.getLogger(__name__)

@task_prerun.connect
def before_task_run(sender=None, task_id=None, task=None, args=None, kwargs=None, **kwargs_ignored):
    logger.info(f"Task {sender.name} (ID: {task_id}) is about to run.")

@task_success.connect
def task_completed(sender=None, result=None, **kwargs):
    logger.info(f"Task {sender.name} completed successfully with result: {result}")

@task_failure.connect
def task_failed(sender=None, exception=None, traceback=None, **kwargs):
    logger.error(f"Task {sender.name} failed due to: {exception}")
```

---

2. **Graceful Shutdown in Celery** When stopping a Celery worker, it's important to do it **gracefully**  to allow running tasks to complete instead of killing them immediately.

**How to Stop Celery Gracefully**  

1. Use **Ctrl + C**  when running Celery in the terminal.

2. Send the **Send the `SIGTERM`**  signal to the worker process.

3. Use the `--graceful` flag when stopping the worker.

```sh
celery -A myapp worker --graceful
```

When a Celery worker is shutting down, it stops accepting new tasks and waits for currently running tasks to finish.
**Handling Cleanup on Shutdown** You can listen to the **worker_shutdown**  signal to perform cleanup operations like closing database connections.

```python
from celery.signals import worker_shutdown

@worker_shutdown.connect
def graceful_shutdown_handler(sender=None, **kwargs):
    print("Celery worker is shutting down gracefully.")
```

---

3. **Cleanup of Failed Tasks** When a task fails, it might leave behind temporary files, database locks, or unprocessed data. To ensure proper cleanup, you can use the **

When a task fails, it might leave behind temporary files, database locks, or unprocessed data. To ensure proper cleanup, you can use the `task_failure`**  signal or handle it within the task itself.

**Example: Cleaning Up After a Failed Task**

Imagine a task that processes a file. If it fails, we want to delete the temporary file.

```python
import os
from celery import shared_task
from celery.signals import task_failure

@shared_task(bind=True)
def process_file(self, file_path):
    try:
        with open(file_path, "r") as f:
            data = f.read()
        return len(data)
    except Exception as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)

@task_failure.connect
def cleanup_failed_task(sender=None, exception=None, args=None, kwargs=None, **extra):
    if "file_path" in kwargs:
        file_path = kwargs["file_path"]
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Cleaned up file: {file_path}")
```

This ensures that if the task fails, the temporary file does not remain on the server.

---

### Summary

✅ **Task Signals**  help in tracking task execution.
✅ **Graceful Shutdown**  prevents abrupt termination of running tasks.
✅ **Cleanup of Failed Tasks**  ensures that no unnecessary resources are left behind.
