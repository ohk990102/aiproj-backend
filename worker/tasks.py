from celery import shared_task, Task

from worker.worker import app


@shared_task(name="generate_text_task")
def generate_text_task():
    return "Hello World!"
