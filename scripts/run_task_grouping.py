from tasks.x04_task_grouping import process_image


def run():
    result = process_image("user_uploads/image1.jpg")
    print(f"result: {result}")  # noqa: T201
