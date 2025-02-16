**Task Chaining in Celery with Django**

**What is Task Chaining?**
Task chaining in Celery allows you to link multiple tasks together so that each task runs only after the previous one completes successfully. This is useful when you have a sequence of dependent tasks.

**How Does It Work?** You use the `chain()` function or the `|` (pipe) operator to create a workflow where tasks execute sequentially.

---

**Example of Task Chaining in Django with Celery**
---

**Step 1: Define Tasks in `tasks.py`**
Let's assume we want to process an order in three steps:

1. **Validate payment**

2. **Update inventory**

3. **Send confirmation email**

Here’s how we define the tasks:

```python
from celery import shared_task
from celery import chain

@shared_task
def validate_payment(order_id):
    # Simulate payment validation
    print(f"Validating payment for order {order_id}")
    return order_id  # Pass order_id to the next task

@shared_task
def update_inventory(order_id):
    # Simulate updating inventory
    print(f"Updating inventory for order {order_id}")
    return order_id  # Pass order_id to the next task

@shared_task
def send_confirmation_email(order_id):
    # Simulate sending email
    print(f"Sending confirmation email for order {order_id}")
    return f"Email sent for order {order_id}"
```

---

**Step 2: Chain the Tasks**

Now, to run the tasks sequentially, we use `chain()` or the `|` operator:

```python
from celery import chain

task_chain = chain(validate_payment.s(123), update_inventory.s(), send_confirmation_email.s())
task_chain()
```

Using `|` (Pipe Operator)**

```python
(validate_payment.s(123) | update_inventory.s() | send_confirmation_email.s())()
```

Each task receives the output of the previous task as input.

---

**Step 3: Start Celery Worker**
Run Celery in a separate terminal:

```bash
celery -A my_project worker --loglevel=info
```

Now, when you execute the chained tasks, Celery will process them in order.

---

**Conclusion**
Task chaining ensures that dependent tasks execute in a specific sequence. This is useful for workflows like:

- Payment processing

- Image processing pipelines

- Data transformation steps
