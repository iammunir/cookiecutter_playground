from celery import shared_task


@shared_task(queue="default", rate_limit="2/m")
def fetch_latest_news():
    # Simulate API call
    print("Fetching latest news from API...")  # noqa: T201


def update_news():
    for _i in range(10):
        fetch_latest_news.apply_async()
