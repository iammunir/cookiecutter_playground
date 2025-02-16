from celery import chain
from celery import shared_task


@shared_task(queue="default")
def validate_payment(order_id):
    # Simulate payment validation
    print(f"Validating payment for order {order_id}")  # noqa: T201
    return order_id  # Pass order_id to the next task


@shared_task(queue="default")
def update_inventory(order_id):
    # Simulate updating inventory
    print(f"Updating inventory for order {order_id}")  # noqa: T201
    return order_id  # Pass order_id to the next task


@shared_task(queue="default")
def send_confirmation_email(order_id):
    # Simulate sending email
    print(f"Sending confirmation email for order {order_id}")  # noqa: T201
    return f"Email sent for order {order_id}"


def process_payment(order_id):
    task_chain = chain(
        validate_payment.s(order_id),
        update_inventory.s(),
        send_confirmation_email.s(),
    )
    task_chain()
