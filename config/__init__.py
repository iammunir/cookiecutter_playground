# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from tasks.x00_intro import sub_numbers
from tasks.x01_task_routing import cleanup_database
from tasks.x01_task_routing import send_email
from tasks.x04_task_grouping import apply_watermark
from tasks.x04_task_grouping import convert_to_grayscale
from tasks.x04_task_grouping import resize_image
from tasks.x05_task_chaining import send_confirmation_email
from tasks.x05_task_chaining import update_inventory
from tasks.x05_task_chaining import validate_payment
from tasks.x06_task_rate_limit import fetch_latest_news
from tasks.x07_task_arguments_return import add_numbers
from tasks.x09_task_error_handling import get_data
from tasks.x10_task_auto_retry import fetch_data
from tasks.x11_task_error_group import process_data
from tasks.x12_task_error_chain import add
from tasks.x12_task_error_chain import multiply_two
from tasks.x12_task_error_chain import result_info

from .celery_app import app as celery_app

__all__ = (
    "add",
    "add_numbers",
    "apply_watermark",
    "celery_app",
    "cleanup_database",
    "convert_to_grayscale",
    "fetch_data",
    "fetch_latest_news",
    "get_data",
    "multiply_two",
    "process_data",
    "resize_image",
    "result_info",
    "send_confirmation_email",
    "send_email",
    "sub_numbers",
    "update_inventory",
    "validate_payment",
)
