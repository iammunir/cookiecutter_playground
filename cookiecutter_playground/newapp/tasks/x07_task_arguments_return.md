1. **Passing Arguments to Celery Tasks** 
Celery tasks work like regular Python functions. You can pass arguments when calling a task, just like calling a function.

#### Example: 

Let's say we have a Celery task that adds two numbers:


```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
```
You can call this task asynchronously using `.delay()` or `.apply_async()`:

```python
result = add.delay(10, 20)  # This runs in the background
```
Or using `.apply_async()` with more options:

```python
result = add.apply_async(args=[10, 20])
```
2. **Returning and Retrieving Results** 
Celery stores task results in a backend (e.g., Redis, PostgreSQL, or Memcached) so you can retrieve them later.

#### Example: 


```python
from celery.result import AsyncResult

result = add.delay(10, 20)  # Returns AsyncResult object

print(result.id)  # Task ID

# Check if task is done
if result.ready():
    print(result.result)  # Output: 30
else:
    print("Task is still running")
```

You can also retrieve results later using the task ID:


```python
task_id = result.id
retrieved_result = AsyncResult(task_id)
print(retrieved_result.result)
```
3. **Handling Exceptions in Task Results** 
If a task fails, you can check for errors:


```python
if result.failed():
    print("Task failed!")
elif result.successful():
    print("Task completed successfully:", result.result)
```
4. **Example in Django View** 
If you want to trigger a task from a Django view:


```python
from django.http import JsonResponse
from .tasks import add

def add_numbers_view(request):
    task = add.delay(10, 20)
    return JsonResponse({"task_id": task.id})
```

And later, you can fetch the result:


```python
def get_result_view(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        return JsonResponse({"status": "done", "result": result.result})
    return JsonResponse({"status": "pending"})
```


---


### Summary: 
 
- **Pass arguments**  like normal function arguments.
 
- **Retrieve results**  using `AsyncResult(task_id)`.
 
- **Handle errors**  using `.failed()` or `.successful()` methods.
