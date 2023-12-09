import os

from celery import Celery

BROKER_URI = os.environ["BROKER_URI"]
BACKEND_URI = os.environ["BACKEND_URI"]

app = Celery(
    "celery_app", broker=BROKER_URI, backend=BACKEND_URI, include=["worker.tasks"]
)


def main():
    app.worker_main(argv=["worker", "--loglevel=info"])


if __name__ == "__main__":
    main()
