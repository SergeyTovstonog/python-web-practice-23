from celery import shared_task
import time

@shared_task
def add(x, y):
    return x + y

@shared_task
def multiply(x, y):
    return x * y

@shared_task(bind=True)
def priority_add(self, x, y):
    return x + y

@shared_task
def long_task():
    time.sleep(10)
    return 'Long task completed'
