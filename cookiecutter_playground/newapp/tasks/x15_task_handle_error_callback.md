### Task Result Callback in Celery with Django

A **task result callback**  in Celery allows you to execute a function when a task completes. This is useful when you need to trigger additional actions based on the task's success or failure.

**1. Basic Task Result Callback** Celery provides a `link` option to specify a callback function that will be executed when the task finishes successfully.

```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def result_callback(result):
    print(f"Task completed with result: {result}")

# Linking the callback
task = add.apply_async((10, 20), link=result_callback.s())
```

- The `link=result_callback.s()` ensures that when `add` completes successfully, `result_callback` runs with the result as its argument.

**2. Handling Errors in Callbacks (link_error)** Celery also provides a `link_error` option to handle failures. This is useful to log errors or trigger alternative flows.

```python
from celery import shared_task

@shared_task
def failing_task():
    raise ValueError("Something went wrong!")

@shared_task
def error_callback(request, exc, traceback):
    print(f"Task failed! Exception: {exc}")

# Linking error callback
task = failing_task.apply_async(link_error=error_callback.s())
```

- `link_error=error_callback.s()` ensures that `error_callback` runs when `failing_task` encounters an error.

- The `error_callback` function receives:
  - `request`: Task request object

  - `exc`: Exception message

  - `traceback`: Error traceback for debugging

**3. Storing Results and Handling in Django** Celery stores task results in a **backend (e.g., Redis, Database, or RabbitMQ)** . You can retrieve results later and perform actions based on success or failure.

```python
from celery.result import AsyncResult

task_id = task.id  # Get the task ID
result = AsyncResult(task_id)

if result.successful():
    print("Task succeeded:", result.result)
elif result.failed():
    print("Task failed:", result.traceback)
elif result.state == 'PENDING':
    print("Task is still pending")
```

**4. Advanced: Using Callbacks in Chains** You can use **Celery chains**  to execute multiple tasks in sequence, handling errors in intermediate tasks.

```python
from celery import chain

workflow = chain(
    add.s(5, 10),
    result_callback.s()
)
workflow.apply_async()
```

- If any task in the chain fails, the remaining tasks won't execute unless handled explicitly.

---

This approach ensures that your Celery tasks properly log and handle success and failure cases efficiently.

---

The functions used in **The functions used in `link`**  and **The functions used in **The functions used in `link`**  and `link_error`**  must be **Celery tasks** , not regular Python functions.
Celery treats them as separate tasks that execute asynchronously after the main task completes (successfully or with an error).

Why Should `link` and `link_error` Be Celery Tasks?**  

1. **Celery executes them asynchronously**

- If they were regular functions, Celery wouldn't be able to schedule them as separate tasks.

2. **They can run on a worker node**

- Since Celery distributes tasks across workers, the callback should also be a task to be handled by a worker.

3. **They support serialization**

- Celery can pass data between tasks only if they are registered as Celery tasks.

---

**Example: Correct Usage (Callbacks as Celery Tasks)**

```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def result_callback(result):
    print(f"Task completed with result: {result}")

@shared_task
def error_callback(request, exc, traceback):
    print(f"Task failed! Exception: {exc}")

# Linking the success and error callbacks
task = add.apply_async((10, 20), link=result_callback.s(), link_error=error_callback.s())
```

**Example: Incorrect Usage (Callbacks as Regular Functions)**

```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

def result_callback(result):  # ❌ This is a regular function, Celery won't execute it
    print(f"Task completed with result: {result}")

def error_callback(request, exc, traceback):  # ❌ This won't work in Celery
    print(f"Task failed! Exception: {exc}")

# This will not work correctly because the callbacks are not Celery tasks
task = add.apply_async((10, 20), link=result_callback, link_error=error_callback)
```

💡 **Fix:**  Always decorate the callback functions with `@shared_task`.

---

**Conclusion**  

- ✅ `link` and `link_error` must reference **Celery tasks**  (functions decorated with `@shared_task`).

- ❌ Regular functions won’t work because Celery won’t be able to distribute them to workers.
