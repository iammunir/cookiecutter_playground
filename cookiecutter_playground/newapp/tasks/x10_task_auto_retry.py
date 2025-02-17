import logging

from celery import shared_task

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(actime)s %(levelname)s %(message)s",
)


def fetch():
    msg = "connection error occurred"
    raise ConnectionError(msg)


@shared_task(
    queue="default",
    autoretry_for=(ConnectionError,),
    default_retry_delay=5,
    retry_kwargs={"max_retries": 5},
)
def fetch_data():
    try:
        fetch()
    except ConnectionError as exc:
        logging.exception("error occurred", repr(exc))  # noqa: PLE1205, TRY401
        raise ConnectionError(repr(exc)) from exc
        # perform actual error handling
