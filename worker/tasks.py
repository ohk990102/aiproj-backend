from celery import Task, shared_task

from worker.worker import app

@shared_task(name='generate_text_task')
def generate_text_task():
    return 'Hello World!'

