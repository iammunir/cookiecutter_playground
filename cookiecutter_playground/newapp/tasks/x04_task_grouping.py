from time import sleep

from celery import group
from celery import shared_task


@shared_task(queue="default")
def resize_image(image_path):
    print("start resizing image...")  # noqa: T201
    sleep(2)  # Simulating processing time
    return f"Resized {image_path}"


@shared_task(queue="default")
def apply_watermark(image_path):
    print("start applying watermark...")  # noqa: T201
    sleep(3)  # Simulating processing time
    return f"Applied watermark to {image_path}"


@shared_task(queue="default")
def convert_to_grayscale(image_path):
    print("start converting grayscale...")  # noqa: T201
    sleep(1)  # Simulating processing time
    return f"Converted {image_path} to grayscale"


def process_image(image_path):
    job = group(
        resize_image.s(image_path),
        apply_watermark.s(image_path),
        convert_to_grayscale.s(image_path),
    )

    return job.apply_async()  # Execute all tasks in parallel
